# Implementation Plan Analysis

Historical preimplementation review. Days 1 and 2 have since been implemented and verified;
see `../documentation/day2_verification.md` for current status. The observations
below describe the planning documents before implementation.

Scope: `AlgoNexis_4_Day_Implementation_Plan.md`, compared with the root `README.md`. This is document analysis; no application code, source-document edits, commits, application performance benchmarks, or completed gates are claimed.

## Overall assessment

The plan is coherent and sufficiently detailed to begin the first work package. It turns the README's product scope into ordered tasks, concrete outputs, acceptance checks, and four daily transition gates. Its emphasis on independently importable core modules, tested stateful structures, UI integration, and measured evidence matches the README. The plan is authoritative for task order and planned commits; the README explicitly identifies that authority. Course-specific rubric compliance remains unverified because the actual rubric and official PSEPF level definitions are unavailable. (Plan:38, 55, 232; README.md:324-329.)

Here and below, 'Plan' refers to `AlgoNexis_4_Day_Implementation_Plan.md`; line numbers identify the inspected source.

## Four-day execution map

| Day | Work and main outputs | Estimated hours | Exit gate |
|---|---|---:|---|
| 1 | Repository/environment; Bubble Sort with steps; UI-independent visualizer data layer; Quickselect; algorithm tests and API notes | 5-7 | G1: both algorithms and recorded actions pass checks; integration contracts fixed |
| 2 | CustomSet, Stack, Queue, BST, Graph, HashTable; stateful manager; regression tests and structure documentation | 6-8 | G2: required operations and manager dispatch pass tests before broad UI integration |
| 3 | Streamlit shell and state spike; algorithm/structure controls; step navigation; reproducible benchmarks, charts, CSV; end-to-end validation | 6-8 | G3: every component works through UI and measured evidence is available |
| 4 | Final QA; verified benchmark evidence; five-plus-page report; slides or video; guides, release verification, retrospective | 7-9 | G4: all eight deliverables are present, usable, and verified |

Sources: Plan:222-237, 327-335, 428-436, 543-552, 668-677. Planned commit distribution is 5/6/7/4, totaling 22. The document repeatedly makes these targets conditional on real completed work; it permits a different split when justified and prohibits artificial history. (Plan:8, 11, 683-736.)

## Dependency chain

The critical path is **environment and contracts -> correct algorithms and step data -> correct structures and manager -> integrated UI and benchmark tools -> verified observations -> academic artifacts and release**. G1, G2, and G3 are explicit prerequisites for the following day. The Day 1 visualization engine is a data layer that works without Streamlit, so later UI work can consume an already-tested record format. Manager operations must likewise work without UI. (Plan:279, 313, 343, 404, 444, 560.)

Benchmark evidence is a separate dependency: performance code calls implementation APIs directly; CSV, chart values, report conclusions, and presentation figures must agree. Rendering and input generation stay outside execution timings unless intentionally measured. A report outline can start early, but numerical conclusions depend on verified observations. (Plan:147, 552, 575-607, 761-768, 842.)

## Decisions clarified beyond the README summary

The plan supplies useful implementation detail:

- Sorting records contain snapshots, compared indices, swap metadata, and counters; captured snapshots are immutable, initial/final states are explicit, and recorded events cannot be silently dropped. Steps are optional at the algorithm contract level. (Plan:203, 263, 274-277.)
- Quickselect uses one-based ranks including duplicate positions; partitioning, error cases, pivot policy, and caller-input behavior must be tested. Copying input and randomized pivots are recommendations rather than immutable decisions. (Plan:204, 284-291.)
- CustomSet supports hashable values with integer UI examples; required algebra lives in the custom class. Day 2 explicitly requires derived operations to return new sets and preserve operands. (Plan:205, 347-352.)
- Graph traversal ordering is deterministic; the manager restricts dispatch and preserves instances. Queue representation should avoid repeated front deletion from a list. (Plan:209-212, 363, 376, 397-404.)
- UI controls include previous/next/reset, dataset-aware state, and a suggested visualization limit of 50 values. Benchmarks specify patterns, proposed sizes, repeated trials, environment metadata, correctness checks, and honest allocation labels. (Plan:472-478, 499-506, 761-770.)

Several choices remain deliberately open: exact Python return types and record class, final exception taxonomy, BST duplicate policy, hash key/capacity/resizing rules, and input limits. These are ordinary implementation decisions, not missing project scope. The README authorizes simple recommended defaults recorded in architecture notes. (Plan:201-212, 388; README.md:353.)

## Minor wording and estimate issues

Two small inconsistencies merit clarification when those parts are implemented:

1. The heading estimates **26-31 hours**, while the roadmap estimates **24-33 hours**. Adding the detailed work packages yields **27 hours 35 minutes**: Day 1 5h45, Day 2 7h30, Day 3 7h, Day 4 7h20. That total fits both ranges; this is differing estimate presentation rather than a schedule contradiction. (Plan:5, 222-230, 244, 342, 443, 559.)
2. Slides **or video** are allowed, and slides are the stated default, but D4.4 acceptance specifically requires a `.pptx` to open. If video is selected, adapt that acceptance wording and file checks to the chosen artifact. The traceability and final checklist already allow either medium. (Plan:614-621, 794, 865; README.md:142.)

No substantive conflict with the README's algorithms, structures, daily order, or benchmark principles was found.

## Execution risks and practical decisions

**Inferred risk: sorting trace storage:** full snapshots for quadratic comparisons can require cubic element storage. The plan recognizes bounded visualization and optional steps; make the benchmark policy explicit: large execution measurements should use a documented trace-disabled mode, while small visualization runs retain every required event. Do not silently truncate a trace. (Plan:203, 263, 477, 502.)

**Inferred risk: reproducibility:** seeding dataset generation alone does not control randomized pivot choices. Define how Quickselect receives controlled randomness and record the policy. Also document the rank being measured and how separate timing/allocation trials map into CSV rows. (Plan:285, 501, 504-506, 762-770.)

**Inferred risk: compressed schedule:** the estimate assumes reusable prior-module code. A two-hour analytical report and a late UI integration day leave limited rework margin if earlier gates slip. Inventory reuse first, keep a report outline and decision notes during development, and retain required deliverables ahead of cosmetic work. These responses follow the plan's own contingency priorities. (Plan:230, 254, 588, 836-845.)

## First implementation unit and current status

The appropriate first unit is **D1.1 - Repository and environment** after inspecting actual Git history, available files, Python/dependencies, and reusable coursework. Preserve the existing `.git`, comprehensive README, and plan; their creation tasks are satisfied only to the extent inspection confirms them. Create only missing foundation artifacts, verify dependency installation and intended file changes, then report actual acceptance evidence. Do not overwrite the README with a shorter starter or reinitialize established history. (Plan:247-257; README.md:327, 333-339.)

Before D1.2, settle and document sorting result/step contracts so D1.3 and Day 3 share a stable API. Continue one verified work package at a time. All development gates remain unverified by this analysis; no source implementation was performed.
