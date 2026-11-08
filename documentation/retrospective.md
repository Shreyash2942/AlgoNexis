# AlgoNexis retrospective

## Delivered against scope

The four-day scope produced two tested algorithms, immutable sorting events and
step retrieval, a Custom Set and five additional structures, a unified manager,
four working Streamlit sections, reproducible measurements, a substantive report,
and a twelve-slide presentation. Each daily gate built on verified prior work.
The final default study has 1,080 observed rows and eight guarded skips; a separate
60-row capacity experiment supplies actual evidence about hash collisions. The
report has eight substantive body pages, with title and reference pages separate.

## Challenges and resolutions

Input preservation required a public contract rather than relying on the usual
in-place textbook descriptions. Both algorithms copy inputs. Immutable snapshots
prevented later swaps from rewriting earlier frames, while explicit counters and
reconstruction tests kept the visualizer consistent. Recognizing the cubic trace
cost led to a small traced-input limit and an untraced benchmark path.

Structure integration required preserving different semantics behind a consistent
manager. Empty-state exceptions, missing keys versus stored None, ignored tree
duplicates, reachable graph traversal, and explicit set algebra remain visible.
Deque replaced front removal from a list in the reviewed Queue adaptation.
Explicit dispatch and signature checking kept user operation names bounded.

The UI work exposed integration details beyond algorithm correctness: AppTest
paths needed to resolve from the repository root, real benchmark interactions
needed a suitable timeout, model state needed independence from widget cleanup,
and development servers needed restarting when imported modules stayed cached.
Real Edge checks caught presentation details such as chart legend clipping. Those
issues were resolved and covered by the documented UI checks.

Final fresh-environment QA discovered a Windows Application Control block on a
newly installed pandas 3.1.1 binary. The previously working file had identical
bytes, but a new installation still failed. The maintained 3.0.6 wheel imported
successfully and passed all 195 tests; the dependency files now select that tested
series. System security policy was left intact. Fresh installation therefore
provided evidence that reusing a long-lived environment alone would have missed.

Measurement interpretation was another central challenge. Setup had to stay
outside both timing and tracing, while output construction remained included.
Prebuilt-fixture exclusion makes incremental allocation different from total
structure memory. Guard skips retain blank values. Controlled capacity variation
was measured separately because the default low-load profile could not establish
collision effects. Byte-preserving evidence attributes protect provenance across
Git checkouts with different newline settings.

## What worked and what follows

Small verified commits, plain Python contracts, shared core APIs, seeded input,
actual browser captures, and artifact builders kept the portfolio reviewable.
The report and slides consume the same saved summaries, avoiding hand-entered
timing claims. Native PowerPoint export and PDF content checks exposed layout
issues before release. Speaker notes provide a concise presentation route; the
automated UI walkthrough does not claim a human oral rehearsal.

Three realistic improvements follow from current limits:

1. Add a balanced BST variant and measure height, construction, and unsuccessful
   queries independently from successful searches.
2. Add hash resizing with load-factor thresholds, then compare total fixture
   storage and construction cost alongside the existing operation-only profile.
3. Expand independent dataset seeds and graph topologies, reporting distributions
   across inputs rather than only repeat timings for one sample per pattern.

The current release is a local educational portfolio. It intentionally omits
weighted/directed graph algorithms, persistent storage, and production deployment.
