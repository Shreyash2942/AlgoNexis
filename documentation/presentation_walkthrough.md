Suggested delivery: approximately 8–10 minutes, with the app launched beforehand. The script below supplies speaker notes; actual oral delivery has not been performed by a human. The browser walkthrough separately exercises navigation, algorithm events, failures, all six structures, reset, charts, and exact CSV download. Do not rerun benchmarks during delivery because the report refers to the saved final run.

# Presentation walkthrough

## Slide 1: AlgoNexis

Introduce the portfolio as one application connecting implementation, explanation, and measured evidence. State the scope: two algorithms, sorting visualization, a custom set, five other structures, an interactive interface, and reproducible performance analysis. Explain that the presentation uses the actual working application and its saved data. The report provides eight substantive body pages plus a cover and references. The walkthrough follows the same requirements as the implementation plan and closes with the limits of the conclusions.

## Slide 2: One portfolio, four ways to explore

Open the local app with python -m streamlit run app.py. Begin on Dashboard, then use the sidebar to visit Algorithms, Data Structures, and Performance Analysis. Describe the learner journey: enter a dataset, inspect a computed result, change a structure, and examine evidence. State survives navigation because model data is separate from widget state. The browser walkthrough exercised these navigation and reset paths; the screenshots are captures of that real session.

## Slide 3: Architecture keeps the core independently testable

Trace the arrows from the Streamlit views to plain Python APIs. Algorithms produce immutable results and sorting frames. The manager dispatches only explicitly registered structure methods. The benchmark calls the core directly, outside rendering. Fixtures, expectations, and validation are prepared outside each measurement. This separation allows tests and command line experiments to reuse exactly the same implementations. No core import starts the user interface. The source digests identify the measured core even after later documentation commits.

## Slide 4: Bubble Sort: make every comparison inspectable

In Algorithms, enter 3, 1, 2 and run Bubble Sort. Show the output 1, 2, 3. Step through initial, comparison, swap, and final events; use Previous and Reset to demonstrate replay without recomputation. There are three comparisons and two swaps for this example. The caller list is preserved. Explain that complete snapshots can cost O(n³) time and storage, so the interface bounds traced input and benchmarks disable tracing. Cite the report for the conventional adjacent-pass algorithm and the project-specific early-exit analysis.

## Slide 5: Quickselect: ask for one rank

Use the list 7, 2, 7, -1, 4 and choose k=3. The selected result is 4, matching the third entry of the sorted reference. Show the invalid rank message for k beyond the list length, then restore a valid value. Explain the smaller, equal, and larger pivot regions. Only the region containing the requested rank remains active. The plotted workload selects one middle rank, while Bubble Sort returns every item ordered; their times do not represent interchangeable tasks. An injected Random instance fixes pivot seeds without changing global random state.

## Slide 6: Custom Set: membership defines equality

Select Custom Set and add 1 and 2. Use a second operand containing 2 and 3. Demonstrate union [1,2,3], intersection [2], difference [1], and symmetric difference [1,3]. Explain that the displayed order follows insertion for predictability while set equality remains unordered membership. Derived operations return new sets and do not mutate the inputs. The implementation writes the algebra explicitly rather than delegating to built-in set operators. Keys must be hashable, and expected membership costs depend on the dictionary hashing behavior.

## Slide 7: Stack and Queue: order determines representation

Push 10 then 20 on the Stack; peek and pop return 20. Enqueue 10 then 20 on the Queue; front and dequeue return 10. Drain both and demonstrate a graceful empty-state error. Explain the concrete representation choice: Python lists support efficient end operations, whereas repeatedly removing index zero shifts later elements. Deque avoids that front-shifting cost. The performance workload drains a preloaded fixture and constructs a returned list, so its operation allocation includes output storage and excludes the original structure.

## Slide 8: Tree, Graph, Hash Table: expose the trade-offs

Insert tree values 2,1,3 and show inorder [1,2,3]; describe how monotone insertion can instead form a chain. Create graph edges 0–1 and 1–2, then traverse from 0 using both BFS and DFS. Query an absent starting vertex to show the validation behavior. Insert, update, find, and delete an integer hash key with a text value. Explain that the importable core API also supports None payloads, distinct from missing keys; the UI deliberately uses text values. The chart holds queries constant while changing bucket capacity. One bucket forces a chain, while these keys occupy separate buckets at 2n capacity. It measures successful lookup batches, excluding construction.

## Slide 9: The interface is part of correctness

Show the Algorithms screenshot, then switch sections and return to demonstrate persistence. Enter 1.5 to trigger the integer-input error and disabled action. In Data Structures, operate on a model, navigate away, and return. Reset all structures and confirm their empty state. Explain the limits: 50 traced sort items, 1,000 untraced sort items, general input at most 5,000 integers, and 200-item structure growth guards. Updates that do not grow a structure remain possible. These boundaries preserve a responsive local teaching application.

## Slide 10: Measure the work that the label describes

Open Performance Analysis and explain its pattern filter, timing and allocation charts, summary table, and full CSV download. Use the saved run instead of replacing the evidence during this presentation. Inputs are seeded with 506, and Quickselect pivots use seed plus trial. Point out that skips are blank observations rather than zeros. The CSV has environment and core source provenance; the analysis manifest hashes data and figures. The graph chart workload is a path, while the default hash profile has max(8,2n) capacity. Confidence intervals were not estimated.

## Slide 11: Findings need boundaries

Explain the measured BST order effect using the actual prebuilt-tree search workload. Duplicates reduce stored node count and therefore change the fixture, not merely its query order. On this chart, output lists and protective copies explain much of the incremental allocation. Prebuilt structures are excluded, so these values cannot rank total representation memory. tracemalloc observes Python-tracked allocations, not resident memory. The shapes are consistent with implementation analysis but do not prove complexity or statistical significance. Distinguish all observed ratios from portable performance guarantees.

## Slide 12: Learning outcomes and release

Close by mapping the eight deliverables: Bubble Sort and visualization, Quickselect, Custom Set, integrated portfolio, working interface, substantive performance report, presentation, and technical documentation. Describe learning about nonmutation, event immutability, insertion-order sensitivity, collision cost, and honest measurement boundaries. The clean install exposed a pandas wheel compatibility issue; the tested maintenance version resolved it without changing system policy. The retrospective records that challenge. The release checklist and verification record provide commands and evidence. Future work should follow the observed limitations: balancing, resizing, and independent datasets rather than unmeasured feature claims.
