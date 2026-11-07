# Graph Report - AlgoNexis Day 3  (2026-11-06)

## Corpus Check
- Corpus is ~29,457 words - fits in a single context window. You may not need a graph.

## Summary
- 501 nodes · 1123 edges · 23 communities detected
- Extraction: 65% EXTRACTED · 14% INFERRED · 20% AMBIGUOUS · INFERRED: 162 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Benchmark Execution and Evidence
- Verified Day Three Contracts
- Sorting Playback and Charts
- Session State and App Integration
- Stack and Queue Workloads
- Application Modules and Imports
- Selection and Dataset Invalidation
- Structure and Measurement Contracts
- Custom Set Operations
- Chained Hash Table Operations
- Deterministic Graph Traversal
- Strict Integer Input Validation
- Algorithm Package Boundary
- Structures Package Boundary
- Performance Package Boundary
- Test Package Boundary
- UI Package Boundary
- Visualization Package Boundary
- Evidence Integrity Rationale
- Historical Day One Planning
- Historical Day Two Gate
- Altair Chart Dependency
- Pandas Table Dependency

## God Nodes (most connected - your core abstractions)
1. `CustomSet` - 33 edges
2. `Graph` - 30 edges
3. `HashTable` - 30 edges
4. `DataStructureManager` - 26 edges
5. `BinarySearchTree` - 26 edges
6. `Queue` - 22 edges
7. `Stack` - 22 edges
8. `_prepare()` - 22 edges
9. `bubble_sort()` - 21 edges
10. `quickselect()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Session model independent of Streamlit, with explicit reset boundaries.` --uses--> `DataStructureManager`  [AMBIGUOUS]
  ui\state.py → data_structures\manager.py
- `perf_counter_ns Timing in Milliseconds` --implements--> `measure_time()`  [INFERRED]
  documentation/benchmark_methodology.md → performance\metrics.py
- `test_day1_and_all_day2_structures_run_without_installed_site_packages()` --calls--> `run()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py → tests\browser_smoke.py
- `test_core_imports_and_playback_need_only_the_standard_library()` --calls--> `run()`  [AMBIGUOUS]
  tests\test_sorting_visualizer.py → tests\browser_smoke.py
- `Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py

## Hyperedges (group relationships)
- **Day 1 Verified Algorithm and Playback Evidence** — readme_bubble, readme_quickselect, readme_visualizer, readme_tests, arch_imports [EXTRACTED 1.00]
- **G2 Acceptance Through Regression and All Manager Routes** — readme_g2, day2_tests, manager_routes, day2_record, arch_imports [EXTRACTED 1.00]
- **G3 Combines Regression Browser and Measurement Evidence** — day3_g3, day3_tests191, day3_browser, day3_observations, day3_csv_match [EXTRACTED 1.00]
- **Reproducible Run Connects Methods Values and Provenance** — day3_rows, day3_patterns, day3_pivot_trials, day3_environment, day3_digest [EXTRACTED 1.00]

## Communities

### Community 0 - "Benchmark Execution and Evidence"
Cohesion: 0.06
Nodes (60): argparse (external import), _atomic_write(), BenchmarkConfig, BenchmarkRun, dataset(), _environment(), load_rows(), main() (+52 more)

### Community 1 - "Verified Day Three Contracts"
Cohesion: 0.05
Nodes (66): Nonmutating Integer Algorithm Inputs, Frozen Sorting Frames With Explicit Event Metadata, Standard-Library-Only Core Imports, Explicit Type and Rank Errors, Core Algorithm Outputs and Readable Input Errors, Fresh Headless Edge End-to-End Walkthrough, Optional Reproducible Browser Smoke Command, Development Module Caching Resolved by Fresh Launch (+58 more)

### Community 2 - "Sorting Playback and Charts"
Cohesion: 0.08
Nodes (37): altair (external import), bubble_sort(), BubbleSortResult, Adjacent-element Bubble Sort with an optional complete, immutable trace.  The ca, One observed event; counters are cumulative as of this snapshot.      A compare, Sorted values, exact operation totals, and an optional event sequence., Return a nonmutating sort result; duplicates keep their relative order.      ``t, SortingStep (+29 more)

### Community 3 - "Session State and App Integration"
Cohesion: 0.09
Nodes (39): main(), run(), DataStructureManager, Detached registry metadata for UI choices; exposes no bound methods., Dispatch a named operation with keyword arguments and preserve state.          U, pathlib (external import), execute_structure(), initialize() (+31 more)

### Community 4 - "Stack and Queue Workloads"
Cohesion: 0.1
Nodes (21): _prepare(), Return operation, external correctness checker, and prebuilt fixture size., Queue, Shallow copy in front-to-rear order., Shallow copy in bottom-to-top order., Stack, FIFO, error, and detached-inspection contracts., test_empty_operations_raise_index_error() (+13 more)

### Community 5 - "Application Modules and Imports"
Cohesion: 0.08
Nodes (24): Local AlgoNexis portfolio. Launch with python -m streamlit run app.py., collections (external import), collections.abc (external import), Insertion-ordered custom set with explicitly implemented set algebra.  A dict st, functools (external import), Undirected, unweighted graph with insertion-ordered adjacency lists.  Hashable v, Custom fixed-capacity hash buckets with separate chaining.  Keys are hashable an, inspect (external import) (+16 more)

### Community 6 - "Selection and Dataset Invalidation"
Cohesion: 0.1
Nodes (30): _load_sample(), Algorithm controls call core APIs and retain independent result state., render(), quickselect(), Iterative randomized Quickselect with one-based ranks and duplicate support.  Un, Return the kth-smallest integer without sorting or changing caller data.      Ra, Random, update_dataset() (+22 more)

### Community 7 - "Structure and Measurement Contracts"
Cohesion: 0.1
Nodes (35): UI-Independent Core and Measurement Boundaries, Ignore Duplicate Integers and Avoid Recursion, Day 2 Acceptance Evidence, 143 Passing Day 1 and Day 2 Tests, Implemented Core UI and Measurement Architecture, BFS Once Per Size Over an n-Vertex Path, Measured Hash Capacity max(8,2n) Versus UI Capacity 8, Operation Boundaries and Evidence Interpretation Method (+27 more)

### Community 8 - "Custom Set Operations"
Cohesion: 0.1
Nodes (17): CustomSet, Mutable membership with nonmutating, new-set derived operations., Insert a hashable value; return True only when membership changes., Remove a member, raising KeyError if absent., Remove if present; return whether membership changed., Return a detached member list in insertion order., New set of both operands, left members followed by new right members., _require_set() (+9 more)

### Community 9 - "Chained Hash Table Operations"
Cohesion: 0.12
Nodes (16): HashTable, Insert/update; True for a new key, False for an update., Return the stored value, including None; raise KeyError if missing., Remove/return the value; raise KeyError if missing., Detached key/value pairs in bucket order, then chain insertion order., Detached bucket and chain containers for collision inspection., CollidingKey, Collision chains, missing keys, updates, and mapping-model workloads. (+8 more)

### Community 10 - "Deterministic Graph Traversal"
Cohesion: 0.18
Nodes (14): Graph, Add if missing; return whether the vertex is new., Validate both endpoints before mutating, then add an undirected edge., Match recursive preorder using neighbor iterators, without recursion., Copy the adjacency mapping and each neighbor container, in order., test_seeded_graph_traversals_match_independent_small_reference(), example_graph(), Deterministic component traversals, cycles, and adjacency isolation. (+6 more)

### Community 11 - "Strict Integer Input Validation"
Cohesion: 0.23
Nodes (11): parse_integer(), parse_integer_list(), Strict, bounded integer input parsing without eval or permissive coercion., Accept comma/whitespace-separated ASCII integers within +/- 1e9., pytest (external import), re (external import), _arguments(), Reject partial numeric coercion and unsafe or oversized datasets. (+3 more)

### Community 12 - "Algorithm Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent algorithms for AlgoNexis.

### Community 13 - "Structures Package Boundary"
Cohesion: 1.0
Nodes (1): Standalone custom sets, data structures, and allowlisted stateful dispatch.

### Community 14 - "Performance Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent correctness-checked timing and Python allocation tools.

### Community 15 - "Test Package Boundary"
Cohesion: 1.0
Nodes (1): Automated AlgoNexis correctness and integration checks.

### Community 16 - "UI Package Boundary"
Cohesion: 1.0
Nodes (1): Streamlit views and independently testable input/session helpers.

### Community 17 - "Visualization Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent visualization data for AlgoNexis.

### Community 18 - "Evidence Integrity Rationale"
Cohesion: 1.0
Nodes (1): Verified Evidence and No Placeholder Results

### Community 19 - "Historical Day One Planning"
Cohesion: 1.0
Nodes (1): Historical Day 1 Plan for CustomSet

### Community 20 - "Historical Day Two Gate"
Cohesion: 1.0
Nodes (1): Historical Day 2 G3 Pending Status

### Community 21 - "Altair Chart Dependency"
Cohesion: 1.0
Nodes (1): Altair Direct Dependency Range 6.3 to Below 7

### Community 22 - "Pandas Table Dependency"
Cohesion: 1.0
Nodes (1): Pandas Direct Dependency Range 3.1 to Below 4

## Ambiguous Edges - Review These
- `BubbleSortResult` → `SortingFrame`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `UI-ready metadata; values reuse the algorithm's immutable snapshot.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Read-only, index-based view of a traced BubbleSortResult.      Indices are zero-`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Number of available frames, including initial and final states.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Return the requested frame without altering playback or result state.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Yield every frame in execution order, without keeping a cursor.`  [AMBIGUOUS]
  visualization\sorting_visualizer.py · relation: uses
- `quickselect()` → `.randrange()`  [AMBIGUOUS]
  algorithms\quickselect.py · relation: calls
- `CustomSet` → `Persistent structure instances behind an explicit operation allowlist.  No eval,`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `CustomSet` → `Detached registry metadata for UI choices; exposes no bound methods.`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `CustomSet` → `Dispatch a named operation with keyword arguments and preserve state.          U`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `CustomSet` → `BenchmarkConfig`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `CustomSet` → `BenchmarkRun`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `CustomSet` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `CustomSet` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `CustomSet` → `Mathematical reference checks and mutation contracts for CustomSet.`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: uses
- `.add()` → `.bfs()`  [AMBIGUOUS]
  data_structures\graph.py · relation: calls
- `.add()` → `.dfs()`  [AMBIGUOUS]
  data_structures\graph.py · relation: calls
- `.add()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.add()` → `test_all_subset_pairs_match_builtin_oracle_and_preserve_operands()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.add()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.remove()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.discard()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.union()` → `.__init__()`  [AMBIGUOUS]
  data_structures\manager.py · relation: calls
- `.intersection()` → `.__init__()`  [AMBIGUOUS]
  data_structures\manager.py · relation: calls
- `.difference()` → `.__init__()`  [AMBIGUOUS]
  data_structures\manager.py · relation: calls
- `.symmetric_difference()` → `.__init__()`  [AMBIGUOUS]
  data_structures\manager.py · relation: calls
- `Graph` → `Persistent structure instances behind an explicit operation allowlist.  No eval,`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Graph` → `Detached registry metadata for UI choices; exposes no bound methods.`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Graph` → `Dispatch a named operation with keyword arguments and preserve state.          U`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Graph` → `BenchmarkConfig`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Graph` → `BenchmarkRun`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Graph` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Graph` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Graph` → `Complete manager-route coverage and standard-library-only Day 2 integration.`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: uses
- `Graph` → `Deterministic component traversals, cycles, and adjacency isolation.`  [AMBIGUOUS]
  tests\test_graph.py · relation: uses
- `.add_vertex()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.add_vertex()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.add_vertex()` → `example_graph()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_vertex()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_vertex()` → `test_invalid_second_endpoint_does_not_add_first_endpoint()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_edge()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.add_edge()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.add_edge()` → `example_graph()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_edge()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_edge()` → `test_invalid_second_endpoint_does_not_add_first_endpoint()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_edge()` → `test_none_and_mixed_hashable_vertices_need_no_sorting()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_edge()` → `test_long_path_needs_no_recursive_stack()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.bfs()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.bfs()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.bfs()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.bfs()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.bfs()` → `test_none_and_mixed_hashable_vertices_need_no_sorting()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.bfs()` → `test_long_path_needs_no_recursive_stack()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.dfs()` → `.pop()`  [AMBIGUOUS]
  data_structures\graph.py · relation: calls
- `.dfs()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.dfs()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.dfs()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.dfs()` → `test_none_and_mixed_hashable_vertices_need_no_sorting()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.dfs()` → `test_long_path_needs_no_recursive_stack()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.vertices()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `HashTable` → `Persistent structure instances behind an explicit operation allowlist.  No eval,`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `HashTable` → `Detached registry metadata for UI choices; exposes no bound methods.`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `HashTable` → `Dispatch a named operation with keyword arguments and preserve state.          U`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `HashTable` → `BenchmarkConfig`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `HashTable` → `BenchmarkRun`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `HashTable` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `HashTable` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `HashTable` → `CollidingKey`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: uses
- `HashTable` → `Collision chains, missing keys, updates, and mapping-model workloads.`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: uses
- `.find()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.find()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.find()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.find()` → `test_supported_hashable_keys_and_identity_equality_semantics()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.delete()` → `.pop()`  [AMBIGUOUS]
  data_structures\hash_table.py · relation: calls
- `.delete()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.delete()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.delete()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.contains()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.contains()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.contains()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `DataStructureManager` → `Complete manager-route coverage and standard-library-only Day 2 integration.`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: uses
- `DataStructureManager` → `Allowlisted dispatch, state persistence, and safe result ownership.`  [AMBIGUOUS]
  tests\test_manager.py · relation: uses
- `DataStructureManager` → `Session model independent of Streamlit, with explicit reset boundaries.`  [AMBIGUOUS]
  ui\state.py · relation: uses
- `DataStructureManager` → `Apply UI growth limits before invoking the manager's domain validation.`  [AMBIGUOUS]
  ui\state.py · relation: uses
- `.available_operations()` → `test_every_registered_operation_has_an_exercised_integration_route()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.available_operations()` → `test_common_size_routes_bind_to_each_independent_structure()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.available_operations()` → `test_managers_registry_metadata_and_display_results_are_isolated()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.available_operations()` → `render()`  [AMBIGUOUS]
  ui\structures_view.py · relation: calls
- `.execute()` → `.display()`  [AMBIGUOUS]
  data_structures\manager.py · relation: calls
- `.execute()` → `test_samples_rank_invalidation_and_independent_structure_state()`  [AMBIGUOUS]
  tests\test_app_integration.py · relation: calls
- `.execute()` → `test_all_sections_render_and_manager_survives_reruns()`  [AMBIGUOUS]
  tests\test_app_shell.py · relation: calls
- `.execute()` → `test_common_size_routes_bind_to_each_independent_structure()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.execute()` → `test_stateful_sequences_and_derived_sets_return_plain_values()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `test_managers_registry_metadata_and_display_results_are_isolated()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `test_unsupported_requests_fail_without_mutation()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `test_names_must_be_strings()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `test_argument_errors_are_clear_and_do_not_mutate()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `test_structure_domain_errors_preserve_exception_type()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `test_size_operation_cannot_override_its_bound_instance()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `test_integer_structure_mutations_persist_and_reset()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `.execute()` → `test_set_algebra_through_controls_preserves_operand()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `.execute()` → `test_graph_and_hash_table_controls_and_errors()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `.execute()` → `test_empty_pop_invalid_integer_and_unknown_operation_are_readable()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `.execute()` → `test_ui_growth_guard_is_atomic_and_allows_existing_key_updates()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `.execute()` → `execute_structure()`  [AMBIGUOUS]
  ui\state.py · relation: calls
- `.execute()` → `render()`  [AMBIGUOUS]
  ui\structures_view.py · relation: calls
- `Persistent structure instances behind an explicit operation allowlist.  No eval,` → `Queue`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Persistent structure instances behind an explicit operation allowlist.  No eval,` → `Stack`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Persistent structure instances behind an explicit operation allowlist.  No eval,` → `BinarySearchTree`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Detached registry metadata for UI choices; exposes no bound methods.` → `Queue`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Detached registry metadata for UI choices; exposes no bound methods.` → `Stack`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Detached registry metadata for UI choices; exposes no bound methods.` → `BinarySearchTree`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Dispatch a named operation with keyword arguments and preserve state.          U` → `Queue`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Dispatch a named operation with keyword arguments and preserve state.          U` → `Stack`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Dispatch a named operation with keyword arguments and preserve state.          U` → `BinarySearchTree`  [AMBIGUOUS]
  data_structures\manager.py · relation: uses
- `Queue` → `BenchmarkConfig`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Queue` → `BenchmarkRun`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Queue` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Queue` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Queue` → `FIFO, error, and detached-inspection contracts.`  [AMBIGUOUS]
  tests\test_queue.py · relation: uses
- `.enqueue()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.enqueue()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.dequeue()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.dequeue()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.dequeue()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.front()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.front()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `Stack` → `BenchmarkConfig`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Stack` → `BenchmarkRun`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Stack` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Stack` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `Stack` → `LIFO, error, and detached-inspection contracts.`  [AMBIGUOUS]
  tests\test_stack.py · relation: uses
- `.push()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.push()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.pop()` → `.inorder()`  [AMBIGUOUS]
  data_structures\tree.py · relation: calls
- `.pop()` → `.preorder()`  [AMBIGUOUS]
  data_structures\tree.py · relation: calls
- `.pop()` → `.postorder()`  [AMBIGUOUS]
  data_structures\tree.py · relation: calls
- `.pop()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.pop()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.pop()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.pop()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.pop()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.peek()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.peek()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `BinarySearchTree` → `BenchmarkConfig`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `BinarySearchTree` → `BenchmarkRun`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `BinarySearchTree` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `BinarySearchTree` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance\benchmark.py · relation: uses
- `BinarySearchTree` → `Traversal, uniqueness, skew, and integer-domain checks.`  [AMBIGUOUS]
  tests\test_tree.py · relation: uses
- `.insert()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.insert()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.insert()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.insert()` → `test_supported_hashable_keys_and_identity_equality_semantics()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.insert()` → `test_unhashable_keys_fail_without_mutation()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.insert()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.insert()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.insert()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.insert()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.search()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.search()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.search()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.search()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.search()` → `parse_integer_list()`  [AMBIGUOUS]
  ui\inputs.py · relation: calls
- `.inorder()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.inorder()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.inorder()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.inorder()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.preorder()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.preorder()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.preorder()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.postorder()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.postorder()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.postorder()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.display()` → `test_uniqueness_display_and_order_independent_equality()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.display()` → `test_all_subset_pairs_match_builtin_oracle_and_preserve_operands()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.display()` → `test_hashable_values_follow_python_equality_and_inspection_is_detached()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.display()` → `test_unhashable_values_fail_without_changing_members()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.display()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.display()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.display()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.display()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.display()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.display()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.display()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.display()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.display()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.display()` → `test_invalid_values_leave_tree_unchanged()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.is_empty()` → `_prepare()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `.is_empty()` → `test_uniqueness_display_and_order_independent_equality()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.is_empty()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.is_empty()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.is_empty()` → `test_invalid_second_endpoint_does_not_add_first_endpoint()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.is_empty()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.is_empty()` → `test_unhashable_keys_fail_without_mutation()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `.is_empty()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.is_empty()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.is_empty()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `BenchmarkConfig` → `Real small measurements, reproducibility metadata, guards, and CSV integrity.`  [AMBIGUOUS]
  tests\test_benchmark.py · relation: uses
- `BenchmarkConfig` → `Tables use the same observations as CSV; UI measurements save to test storage.`  [AMBIGUOUS]
  tests\test_performance_dashboard.py · relation: uses
- `BenchmarkConfig` → `Measured tables, separate-unit charts, and full-run CSV export.`  [AMBIGUOUS]
  ui\performance_view.py · relation: uses
- `_environment()` → `run()`  [AMBIGUOUS]
  performance\benchmark.py · relation: calls
- `run()` → `algorithms()`  [AMBIGUOUS]
  tests\test_algorithm_ui.py · relation: calls
- `run()` → `test_both_algorithms_and_dataset_change_clear_stale_results()`  [AMBIGUOUS]
  tests\test_algorithm_ui.py · relation: calls
- `run()` → `test_rank_changes_invalid_input_empty_lists_and_trace_limit()`  [AMBIGUOUS]
  tests\test_algorithm_ui.py · relation: calls
- `run()` → `test_samples_rank_invalidation_and_independent_structure_state()`  [AMBIGUOUS]
  tests\test_app_integration.py · relation: calls
- `run()` → `test_all_sections_render_and_manager_survives_reruns()`  [AMBIGUOUS]
  tests\test_app_shell.py · relation: calls
- `run()` → `test_day1_and_all_day2_structures_run_without_installed_site_packages()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `run()` → `test_performance_ui_saves_actual_rows_and_renders_download_and_charts()`  [AMBIGUOUS]
  tests\test_performance_dashboard.py · relation: calls
- `run()` → `test_all_steps_final_values_previous_reset_and_navigation()`  [AMBIGUOUS]
  tests\test_sorting_ui.py · relation: calls
- `run()` → `test_slider_and_untraced_mode_do_not_discard_or_invent_steps()`  [AMBIGUOUS]
  tests\test_sorting_ui.py · relation: calls
- `run()` → `test_core_imports_and_playback_need_only_the_standard_library()`  [AMBIGUOUS]
  tests\test_sorting_visualizer.py · relation: calls
- `run()` → `structures()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `run()` → `test_integer_structure_mutations_persist_and_reset()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `run()` → `test_set_algebra_through_controls_preserves_operand()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `run()` → `test_graph_and_hash_table_controls_and_errors()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `run()` → `test_empty_pop_invalid_integer_and_unknown_operation_are_readable()`  [AMBIGUOUS]
  tests\test_structures_ui.py · relation: calls
- `test_seeded_random_traces_match_oracle_and_inversion_count()` → `.randrange()`  [AMBIGUOUS]
  tests\test_bubble_sort.py · relation: calls
- `test_seeded_graph_traversals_match_independent_small_reference()` → `.randrange()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `test_seeded_mutations_match_dict_reference_with_fixed_capacity()` → `.randrange()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `test_seeded_mixed_workload_matches_fifo_list_model()` → `.randrange()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.randrange()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests\test_stack.py · relation: calls
- `.randrange()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `test_highlight_and_description_metadata_match_observed_events()` → `.get_step()`  [AMBIGUOUS]
  tests\test_sorting_visualizer.py · relation: calls
- `test_indices_outside_trace_are_rejected()` → `.get_step()`  [AMBIGUOUS]
  tests\test_sorting_visualizer.py · relation: calls
- `test_noninteger_indices_are_rejected()` → `.get_step()`  [AMBIGUOUS]
  tests\test_sorting_visualizer.py · relation: calls
- `Day 3's data-only playback contract and core import isolation.` → `SortingVisualizer`  [AMBIGUOUS]
  tests\test_sorting_visualizer.py · relation: uses
- `render()` → `.get_step()`  [AMBIGUOUS]
  ui\sorting_view.py · relation: calls
- `Display complete immutable traces with a persistent model playback index.` → `SortingVisualizer`  [AMBIGUOUS]
  ui\sorting_view.py · relation: uses

## Knowledge Gaps
- **101 isolated node(s):** `Local AlgoNexis portfolio. Launch with python -m streamlit run app.py.`, `Adjacent-element Bubble Sort with an optional complete, immutable trace.  The ca`, `One observed event; counters are cumulative as of this snapshot.      A compare`, `Sorted values, exact operation totals, and an optional event sequence.`, `Return a nonmutating sort result; duplicates keep their relative order.      ``t` (+96 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Algorithm Package Boundary`** (2 nodes): `__init__.py`, `UI-independent algorithms for AlgoNexis.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Structures Package Boundary`** (2 nodes): `__init__.py`, `Standalone custom sets, data structures, and allowlisted stateful dispatch.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Performance Package Boundary`** (2 nodes): `__init__.py`, `UI-independent correctness-checked timing and Python allocation tools.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Test Package Boundary`** (2 nodes): `__init__.py`, `Automated AlgoNexis correctness and integration checks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `UI Package Boundary`** (2 nodes): `__init__.py`, `Streamlit views and independently testable input/session helpers.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Visualization Package Boundary`** (2 nodes): `__init__.py`, `UI-independent visualization data for AlgoNexis.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Evidence Integrity Rationale`** (1 nodes): `Verified Evidence and No Placeholder Results`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Historical Day One Planning`** (1 nodes): `Historical Day 1 Plan for CustomSet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Historical Day Two Gate`** (1 nodes): `Historical Day 2 G3 Pending Status`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Altair Chart Dependency`** (1 nodes): `Altair Direct Dependency Range 6.3 to Below 7`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Pandas Table Dependency`** (1 nodes): `Pandas Direct Dependency Range 3.1 to Below 4`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `_prepare()` connect `Stack and Queue Workloads` to `Benchmark Execution and Evidence`, `Sorting Playback and Charts`, `Selection and Dataset Invalidation`, `Custom Set Operations`, `Chained Hash Table Operations`, `Deterministic Graph Traversal`?**
  _High betweenness centrality (0.163) - this node is a cross-community bridge._
- **Why does `DataStructureManager` connect `Session State and App Integration` to `Stack and Queue Workloads`, `Application Modules and Imports`, `Structure and Measurement Contracts`, `Custom Set Operations`, `Chained Hash Table Operations`, `Deterministic Graph Traversal`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Why does `bubble_sort()` connect `Sorting Playback and Charts` to `Verified Day Three Contracts`, `Stack and Queue Workloads`, `Selection and Dataset Invalidation`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `CustomSet` (e.g. with `DataStructureManager` and `.__init__()`) actually correct?**
  _`CustomSet` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `Graph` (e.g. with `DataStructureManager` and `.__init__()`) actually correct?**
  _`Graph` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `HashTable` (e.g. with `DataStructureManager` and `.__init__()`) actually correct?**
  _`HashTable` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `DataStructureManager` (e.g. with `CustomSet` and `Graph`) actually correct?**
  _`DataStructureManager` has 17 INFERRED edges - model-reasoned connections that need verification._

## Verified Day 3 Outcome

The complete local Streamlit portfolio is implemented: four sections, strict bounded integer input, actual algorithm outputs, complete highlighted sorting playback, persistent structure controls, and measured performance tables/charts/export. G1-G3 passed. The final full regression passed 191 tests; a fresh-launch Edge walkthrough exercised the real UI, measured benchmarks, and an exact CSV download.

The evidence includes 1,080 correctness-checked observations, eight explicit guarded cases, and 216 repeat-summary groups. Timing and allocation trials are separate; prebuilt fixtures are excluded from tracing, outputs are included, and the metric is not total RAM. Different-purpose operations and UI/benchmark hash capacity profiles are explicitly distinguished. G4 report/presentation/release work remains planned.

See [G3 verification](../documentation/day3_verification.md), [user guide](../documentation/user_guide.md), [measurement method](../documentation/benchmark_methodology.md), and [actual curves](../documentation/screenshots/performance.png).

## Extraction Audit

The source/document graph covers 47 Python files and 11 documents. Eight changed/new documents were re-extracted and three cached documents reused. Generated bulk observations and screenshots are intentionally excluded by .graphifyignore and referenced through methodology/evidence documents; no image extraction is claimed. Dated Day 1/2 pending or next-step records are labeled historical, separate from current G3 verification.

AST package-docstring IDs were namespaced and local import/property targets resolved to known declarations. External module nodes cite their import sites. AST uses candidates match actual Name references (including import aliases) at INFERRED 0.9, otherwise remain AMBIGUOUS 0.2; they are not verified calls. Explicit source relations have confidence 1.0. Community cohesion values are shown directly; suggested questions prioritize bridge nodes.


## Estimated Retrieval Benchmark

Heuristic context estimates only; not measured model tokens, monetary savings, or answer-quality evaluation.

- Full corpus estimate: 39276 tokens
- Average graph-query estimate: 5495 tokens
- Estimated reduction: 7.1x
