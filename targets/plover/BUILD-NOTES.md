# Plover target: build notes

**Fictional.** Quillmark Trail Co. and everything in `targets/plover/` is invented.

## What this is

A fourth diligence target, built to test whether the system handles kinds of problems its instructions were not written around. Same shape as the other targets so scores are comparable.

- **Codename:** Plover. **Target:** Quillmark Trail Co. (Nasdaq: QTRL), an outdoor apparel and footwear brand in Ashgrove, Oregon.
- **Industry:** branded consumer apparel and footwear sold through a dominant online marketplace, wholesale dealers and own stores, with a licensed heritage brand.
- **Deal type:** a private equity **topping bid during a go-shop**. A strategic buyer has already signed a US$24.00 cash tender offer; the investment committee (Westbrook Lane Capital) is deciding whether to bid US$25.50 before the go-shop ends. The target has dual-class shares and a controlling founder.

## Files

- `data/deal-brief.md` (six IC questions), `data/README.md`
- `data/sec-filings/`: 10-K FY2025, 10-Q Q2 2026, 8-K 2026-07-22, 8-K 2026-09-14, DEF 14A 2026 (all excerpts)
- `data/news/`: 13 dated articles, November 2025 to October 2026, including noise and an unrelated same-name company
- `data/litigation/`: `docket_index.csv` (7 matters, the same 11 column headers as Falcon's) and 4 case files `LIT-001` to `LIT-004`
- `data/financials/`: `README.md` and the 7 CSV files, with the same file names and column headers as Falcon's
- `evaluation/answer-key.md`: P01 to P18, a P19 planted-positives row, and distractors D1 to D4
- `checks.json`: expected counts for the answer key (19 P rows, 4 D rows)
- `data_manifest.json`: written with `python3 tests/run_all.py --write-manifest --target plover`

## How it was built

- Built blind to the system's prompts: the builder read only `tests/test_phase2_data.py`, `tests/_common.py`, `tests/run_all.py`, the header lines of Falcon's financial CSVs and docket index, and the layout hand-over note in the shared notes folder. One caveat: the desktop app loads the repository's `CLAUDE.md` into every session's context automatically, so the builder did see it without opening it. Issue types were chosen from the brief's list of untried diligence areas rather than from that file.
- Issue areas used (none from the excluded list): marketplace channel economics, licence key-person and royalty terms, inventory valuation and a reserve change in estimate, misleading environmental claims, bribery and corruption through a customs broker, an operating permit, chemical restrictions making inventory obsolete, unclaimed property, dealer termination law, controlling-founder deal litigation, lease-heavy store fleet, customer acquisition economics.
- The financial statements were generated from one script so every figure is derived, not typed twice. Adjusted EBITDA, LTM figures, segment contribution, channel and customer splits, share counts, voting power and the percentages quoted in the filings were recomputed by hand against the CSVs.
- Rows from net income to EBITDA have no "Add:" prefix; only the EBITDA to Adjusted EBITDA adjustments do. "Detail:" rows sum to the "other non-recurring items" add-back in every column.
- Balance sheets have no subtotal rows above "Total assets" or between "Total assets" and "Total liabilities", so the column sums used by the checks are exact.
- No em dashes in any file.

## How it was checked

`python3 tests/run_all.py --phase 2` after merging `main`: balance sheets balance, income statements add up, cash flows tie to the change in cash, Adjusted EBITDA reconciles (including the detail rows), quarters sum to FY and H1 totals, every document is labeled fictional, docket detail files exist, the answer key IDs run without gaps, and the manifest matches. All Phase 2 checks pass for every target.
