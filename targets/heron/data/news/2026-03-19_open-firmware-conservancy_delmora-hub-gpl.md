> **FICTIONAL ARTICLE.** Invented for a training exercise. The outlet, people, companies and events do not exist.

# Delmora Hub firmware ships GPL code without source: our demand letter

**Open Firmware Conservancy (non-profit blog)** | March 19, 2026

The Open Firmware Conservancy (OFC) enforces free software licenses on behalf of developers. Today we are publishing the demand letter we sent to Delmora Home Systems on February 4, 2026.

Our engineers examined Delmora Hub firmware version 4.2. We found:

1. The firmware includes the Linux kernel and BusyBox, both licensed under the GNU General Public License version 2 (GPLv2). Delmora does not provide the corresponding source code or a written offer to provide it, as GPLv2 requires.
2. A proprietary module called `ac-runtime`, which runs the AdaptiveComfort algorithm on the hub, is **statically linked to a modified version of libthermctl**, a GPLv2 library written by OFC contributors. In our view this makes `ac-runtime` a work based on libthermctl, which must be distributed under GPLv2 with its source code.

We asked Delmora to publish the source code for the hub firmware, including `ac-runtime`, within 60 days. Delmora's outside counsel replied on March 2 that the company "takes open source compliance seriously" and is "reviewing the matter". We have heard nothing since.

We prefer to resolve compliance issues without going to court, but we will enforce the license if needed.
