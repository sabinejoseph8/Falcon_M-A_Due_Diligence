#!/usr/bin/env python3
"""Run every Project Falcon check. Standard library only.

  python3 tests/run_all.py                          build checks for every target (a run is checked only if one exists)
  python3 tests/run_all.py --run examples/sample-run  also check a saved run folder
  python3 tests/run_all.py --phase 2                 only the Phase 2 checks
  python3 tests/run_all.py --write-manifest          record each target's source data as its unchanged baseline
  python3 tests/run_all.py --write-manifest --target falcon   only one target
"""
import argparse
import os
import pathlib
import sys
import unittest

TESTS = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--run", default=".", help="folder containing memory/ and output/ for a diligence run")
parser.add_argument("--phase", help="run only one phase's checks: 1, 2, 3, 4 or style")
parser.add_argument("--write-manifest", action="store_true", help="save checksums of each target's data/ and answer key")
parser.add_argument("--target", help="with --write-manifest: only this target (a folder name in targets/)")
args = parser.parse_args()

os.environ["FALCON_RUN_DIR"] = args.run
if args.write_manifest:
    from _common import ROOT, TARGETS, write_manifest
    folders = [TARGETS / args.target] if args.target else sorted(p for p in TARGETS.iterdir() if (p / "data").is_dir())
    for folder in folders:
        if not (folder / "data").is_dir():
            sys.exit(f"No data/ folder in {folder.relative_to(ROOT)}")
        print(f"Manifest written: {write_manifest(folder).relative_to(ROOT)}")
    sys.exit(0)

pattern = "test_*.py" if not args.phase else (f"test_phase{args.phase}_*.py" if args.phase.isdigit() else f"test_{args.phase}.py")
suite = unittest.defaultTestLoader.discover(str(TESTS), pattern=pattern, top_level_dir=str(TESTS))
result = unittest.TextTestRunner(verbosity=2).run(suite)
print(f"\nSUMMARY: {result.testsRun} checks, {len(result.failures) + len(result.errors)} failed, {len(result.skipped)} skipped")
sys.exit(0 if result.wasSuccessful() else 1)
