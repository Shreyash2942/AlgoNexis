# Graph Report - APA Report and User Guide (2026-11-08)

## Corpus Check
- Corpus is ~44,807 words - fits in a single context window. You may not need a graph.

## Summary
- 593 nodes · 1332 edges · 26 communities detected
- Extraction: 69% EXTRACTED · 14% INFERRED · 17% AMBIGUOUS · INFERRED: 185 edges (avg confidence: 0.9)
- Token usage/cost: unavailable; zero serialization fields are placeholders, not measured usage.

## Community Hubs (Navigation)
- Measurement and Evidence Validation
- Release Evidence and References
- APA Style and Core Contracts
- Manager and UI Integration
- Sorting Frames and Replay
- Stack and Tree Algorithms
- Selection and Dataset State
- Explicit Custom Set Algebra
- Separate Chaining Hash Table
- Graph Traversal and Fixtures
- APA Build and Reproducibility
- Deque Queue Operations
- Integer Bounds and Trace Costs
- Algorithms Package Boundary
- Structures Package Boundary
- Performance Package Boundary
- Artifact Scripts Package
- Test Package Boundary
- UI Package Boundary
- Visualization Package Boundary
- Native PowerPoint Rendering
- Optional Browser QA
- Historical Evidence Integrity Rule
- Historical Custom Set Plan
- Historical G3 Pending
- Historical G4 Pending

## God Nodes (most connected - your core abstractions)
1. `CustomSet` - 33 edges
2. `HashTable` - 31 edges
3. `Graph` - 30 edges

## Surprising Connections (you probably didn't know these)
- `Preserve Saved CSVs or Rebuild All Artifacts After New Measurements` --references--> `run_benchmarks()`  [EXTRACTED]
  guide.md → performance/benchmark.py
- `perf_counter_ns Elapsed Milliseconds` --references--> `measure_time()`  [EXTRACTED]
  documentation/benchmark_methodology.md → performance/metrics.py

## Hyperedges (group relationships)
- **Reusable Core Preserves Inputs Frames and Allowed Dispatch** — arch_separation, arch_copy, arch_frame, arch_allowlist [EXTRACTED 1.00]
- **Operation Measurements Exclude Setup Check Results and Separate Units** — method_fixture, day3_correctness, method_time, day3_allocations, method_different_tasks [EXTRACTED 1.00]
- **Day 1 Verified Algorithm and Playback Evidence** — readme_bubble, readme_quickselect, readme_visualizer, readme_tests, arch_imports [EXTRACTED 1.00]
- **G2 Acceptance Through Regression and All Manager Routes** — readme_g2, day2_tests, manager_routes, day2_record, arch_imports [EXTRACTED 1.00]
- **G3 Combines Regression Browser and Measurement Evidence** — day3_g3, day3_tests191, day3_browser, day3_observations, day3_csv_match [EXTRACTED 1.00]
- **Measured Evidence Feeds Verified Report and Presentation** — method_matrix, method_collision, method_summary, method_manifest, day4_report_pages, day4_powerpoint [EXTRACTED 1.00]
- **APA Edition Combines Layout References Metadata and Figures** — apa_word_edition, apa_format_contract, apa_reference_format, apa_title_metadata, apa_five_figures [EXTRACTED 1.00]
- **Saved Observations Support Rebuilt Analysis Report Slides and APA Edition** — guide_preserve_evidence, readme_rebuild, apa_shared_values, method_manifest [EXTRACTED 1.00]

## Communities

### Community 0 - "Measurement and Evidence Validation"
Cohesion: 0.04
Nodes (82): altair (external import), Generate exportable scientific figures and summaries from recorded CSVs only., argparse (external import), _atomic_write(), BenchmarkConfig, BenchmarkRun, dataset(), _environment() (+74 more)

### Community 1 - "Release Evidence and References"
Cohesion: 0.04
Nodes (75): Alphabetized References with Hanging Indents and Italic Work Titles, BreadthFirstPaths Before BST Determines Matched Undated Suffixes, APA Edition Reuses Verified Original Analysis and Measured Summaries, APA Webpage Reference Examples, Report and Slides Resolve Shared Measured Values, Keep Controlled Capacity Profile Separate, LF Sources and Byte-Preserved Evidence Protect Hashes, Independent Core UI Measurement and Artifact Layers (+67 more)

### Community 2 - "APA Style and Core Contracts"
Cohesion: 0.05
Nodes (72): Letter One-Inch Margins TNR12 Double Spacing and Indents, Word PDF Preview Requires Separate Native Export, Portable DOCX Builder Checks Measured Source Provenance, Regeneration Overwrites Direct Word Edits, Student Title Page Page Numbers and Unnumbered Introduction, APA Student Paper Setup Guide, APA Title Page Setup, Personalize Author Affiliation Instructor and Actual Due Date (+64 more)

### Community 3 - "Manager and UI Integration"
Cohesion: 0.07
Nodes (48): main(), Local AlgoNexis portfolio. Launch with python -m streamlit run app.py., run(), DataStructureManager, Detached registry metadata for UI choices; exposes no bound methods., Dispatch a named operation with keyword arguments and preserve state.          U, execute_structure(), initialize() (+40 more)

### Community 4 - "Sorting Frames and Replay"
Cohesion: 0.09
Nodes (34): bubble_sort(), BubbleSortResult, One observed event; counters are cumulative as of this snapshot.      A compare, Sorted values, exact operation totals, and an optional event sequence., Return a nonmutating sort result; duplicates keep their relative order.      ``t, SortingStep, render(), UI-ready metadata; values reuse the algorithm's immutable snapshot. (+26 more)

### Community 5 - "Stack and Tree Algorithms"
Cohesion: 0.13
Nodes (17): Shallow copy in bottom-to-top order., Stack, LIFO, error, and detached-inspection contracts., test_empty_operations_raise_index_error(), test_lifo_peek_size_and_detached_input_display(), test_seeded_mixed_workload_matches_list_model(), Traversal, uniqueness, skew, and integer-domain checks., test_empty_and_singleton() (+9 more)

### Community 6 - "Selection and Dataset State"
Cohesion: 0.11
Nodes (28): _load_sample(), Algorithm controls call core APIs and retain independent result state., render(), quickselect(), Iterative randomized Quickselect with one-based ranks and duplicate support.  Un, Return the kth-smallest integer without sorting or changing caller data.      Ra, Random, update_dataset() (+20 more)

### Community 7 - "Explicit Custom Set Algebra"
Cohesion: 0.1
Nodes (17): Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim, CustomSet, Mutable membership with nonmutating, new-set derived operations., Insert a hashable value; return True only when membership changes., Remove a member, raising KeyError if absent., Remove if present; return whether membership changed., Return a detached member list in insertion order., New set of both operands, left members followed by new right members. (+9 more)

### Community 8 - "Separate Chaining Hash Table"
Cohesion: 0.12
Nodes (15): HashTable, Insert/update; True for a new key, False for an update., Return the stored value, including None; raise KeyError if missing., Remove/return the value; raise KeyError if missing., Detached key/value pairs in bucket order, then chain insertion order., Detached bucket and chain containers for collision inspection., Persistent structure instances behind an explicit operation allowlist.  No eval,, CollidingKey (+7 more)

### Community 9 - "Graph Traversal and Fixtures"
Cohesion: 0.17
Nodes (16): _prepare(), Return operation, external correctness checker, and prebuilt fixture size., Graph, Add if missing; return whether the vertex is new., Validate both endpoints before mutating, then add an undirected edge., Match recursive preorder using neighbor iterators, without recursion., Copy the adjacency mapping and each neighbor container, in order., test_seeded_graph_traversals_match_independent_small_reference() (+8 more)

### Community 10 - "APA Build and Reproducibility"
Cohesion: 0.12
Nodes (27): run(), Five Sequential Measured Figures on Pages After References, APA Figure Setup and Placement Options, APA Structure and Optional Native Preview Validation Commands, load_rows(), body_sections(), build(), report_values() (+19 more)

### Community 11 - "Deque Queue Operations"
Cohesion: 0.24
Nodes (7): pytest (external import), Queue, Shallow copy in front-to-rear order., FIFO, error, and detached-inspection contracts., test_empty_operations_raise_index_error(), test_fifo_front_size_and_detached_input_display(), test_seeded_mixed_workload_matches_fifo_list_model()

### Community 12 - "Integer Bounds and Trace Costs"
Cohesion: 0.2
Nodes (13): Complete Snapshots Can Cost Cubic Time and Storage, Strict Integer and Explicit Operation Validation, Strict Integer Dataset and One-Based Rank Examples, Trace Limit 50 Reflects Cubic Snapshot Cost, UI Bounds 50 Traced 1000 Sort 5000 Select and 200 Structure Items, parse_integer(), parse_integer_list(), Strict, bounded integer input parsing without eval or permissive coercion. (+5 more)

### Community 13 - "Algorithms Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent algorithms for AlgoNexis.

### Community 14 - "Structures Package Boundary"
Cohesion: 1.0
Nodes (1): Standalone custom sets, data structures, and allowlisted stateful dispatch.

### Community 15 - "Performance Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent correctness-checked timing and Python allocation tools.

### Community 16 - "Artifact Scripts Package"
Cohesion: 1.0
Nodes (1): Optional, reproducible portfolio evidence and document utilities.

### Community 17 - "Test Package Boundary"
Cohesion: 1.0
Nodes (1): Automated AlgoNexis correctness and integration checks.

### Community 18 - "UI Package Boundary"
Cohesion: 1.0
Nodes (1): Streamlit views and independently testable input/session helpers.

### Community 19 - "Visualization Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent visualization data for AlgoNexis.

### Community 20 - "Native PowerPoint Rendering"
Cohesion: 1.0
Source-file-only community: render_powerpoint.ps1 (1 node).

### Community 21 - "Optional Browser QA"
Cohesion: 1.0
Nodes (1): Optional Playwright Browser QA Dependency

### Community 22 - "Historical Evidence Integrity Rule"
Cohesion: 1.0
Nodes (1): Verified Evidence and No Placeholder Results

### Community 23 - "Historical Custom Set Plan"
Cohesion: 1.0
Nodes (1): Historical Day 1 Plan for CustomSet

### Community 24 - "Historical G3 Pending"
Cohesion: 1.0
Nodes (1): Historical Day 2 G3 Pending Status

### Community 25 - "Historical G4 Pending"
Cohesion: 1.0
Nodes (1): Historical Day 1 Unverified G4 Release Gate

## Ambiguous Edges - Review These
- `BubbleSortResult` → `SortingFrame`  [AMBIGUOUS]
  visualization/sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:`  [AMBIGUOUS]
  visualization/sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `UI-ready metadata; values reuse the algorithm's immutable snapshot.`  [AMBIGUOUS]
  visualization/sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Read-only, index-based view of a traced BubbleSortResult.      Indices are zero-`  [AMBIGUOUS]
  visualization/sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Number of available frames, including initial and final states.`  [AMBIGUOUS]
  visualization/sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Return the requested frame without altering playback or result state.`  [AMBIGUOUS]
  visualization/sorting_visualizer.py · relation: uses
- `BubbleSortResult` → `Yield every frame in execution order, without keeping a cursor.`  [AMBIGUOUS]
  visualization/sorting_visualizer.py · relation: uses
- `quickselect()` → `.randrange()`  [AMBIGUOUS]
  algorithms/quickselect.py · relation: calls
- `CustomSet` → `Persistent structure instances behind an explicit operation allowlist.  No eval,`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `CustomSet` → `Detached registry metadata for UI choices; exposes no bound methods.`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `CustomSet` → `Dispatch a named operation with keyword arguments and preserve state.          U`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `CustomSet` → `BenchmarkConfig`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `CustomSet` → `BenchmarkRun`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `CustomSet` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `CustomSet` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `CustomSet` → `Mathematical reference checks and mutation contracts for CustomSet.`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: uses
- `.add()` → `.bfs()`  [AMBIGUOUS]
  data_structures/graph.py · relation: calls
- `.add()` → `.dfs()`  [AMBIGUOUS]
  data_structures/graph.py · relation: calls
- `.add()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.add()` → `test_all_subset_pairs_match_builtin_oracle_and_preserve_operands()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.add()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.remove()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.discard()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.union()` → `.__init__()`  [AMBIGUOUS]
  data_structures/manager.py · relation: calls
- `.intersection()` → `.__init__()`  [AMBIGUOUS]
  data_structures/manager.py · relation: calls
- `.difference()` → `.__init__()`  [AMBIGUOUS]
  data_structures/manager.py · relation: calls
- `.symmetric_difference()` → `.__init__()`  [AMBIGUOUS]
  data_structures/manager.py · relation: calls
- `Graph` → `Persistent structure instances behind an explicit operation allowlist.  No eval,`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Graph` → `Detached registry metadata for UI choices; exposes no bound methods.`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Graph` → `Dispatch a named operation with keyword arguments and preserve state.          U`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Graph` → `BenchmarkConfig`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Graph` → `BenchmarkRun`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Graph` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Graph` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Graph` → `Complete manager-route coverage and standard-library-only Day 2 integration.`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: uses
- `Graph` → `Deterministic component traversals, cycles, and adjacency isolation.`  [AMBIGUOUS]
  tests/test_graph.py · relation: uses
- `.add_vertex()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.add_vertex()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `.add_vertex()` → `example_graph()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.add_vertex()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.add_vertex()` → `test_invalid_second_endpoint_does_not_add_first_endpoint()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.add_edge()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.add_edge()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `.add_edge()` → `example_graph()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.add_edge()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.add_edge()` → `test_invalid_second_endpoint_does_not_add_first_endpoint()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.add_edge()` → `test_none_and_mixed_hashable_vertices_need_no_sorting()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.add_edge()` → `test_long_path_needs_no_recursive_stack()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.bfs()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.bfs()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `.bfs()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.bfs()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.bfs()` → `test_none_and_mixed_hashable_vertices_need_no_sorting()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.bfs()` → `test_long_path_needs_no_recursive_stack()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.dfs()` → `.pop()`  [AMBIGUOUS]
  data_structures/graph.py · relation: calls
- `.dfs()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `.dfs()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.dfs()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.dfs()` → `test_none_and_mixed_hashable_vertices_need_no_sorting()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.dfs()` → `test_long_path_needs_no_recursive_stack()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.vertices()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `HashTable` → `Persistent structure instances behind an explicit operation allowlist.  No eval,`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `HashTable` → `Detached registry metadata for UI choices; exposes no bound methods.`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `HashTable` → `Dispatch a named operation with keyword arguments and preserve state.          U`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `HashTable` → `BenchmarkConfig`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `HashTable` → `BenchmarkRun`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `HashTable` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `HashTable` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `HashTable` → `Controlled supplemental hash experiment: one bucket versus 2n buckets.  Unique n`  [AMBIGUOUS]
  scripts/measure_hash_collisions.py · relation: uses
- `HashTable` → `CollidingKey`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: uses
- `HashTable` → `Collision chains, missing keys, updates, and mapping-model workloads.`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: uses
- `.find()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.find()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.find()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.find()` → `test_supported_hashable_keys_and_identity_equality_semantics()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.delete()` → `.pop()`  [AMBIGUOUS]
  data_structures/hash_table.py · relation: calls
- `.delete()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.delete()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.delete()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.contains()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.contains()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.contains()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `DataStructureManager` → `Complete manager-route coverage and standard-library-only Day 2 integration.`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: uses
- `DataStructureManager` → `Allowlisted dispatch, state persistence, and safe result ownership.`  [AMBIGUOUS]
  tests/test_manager.py · relation: uses
- `DataStructureManager` → `Session model independent of Streamlit, with explicit reset boundaries.`  [AMBIGUOUS]
  ui/state.py · relation: uses
- `DataStructureManager` → `Apply UI growth limits before invoking the manager's domain validation.`  [AMBIGUOUS]
  ui/state.py · relation: uses
- `.available_operations()` → `test_every_registered_operation_has_an_exercised_integration_route()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `.available_operations()` → `test_common_size_routes_bind_to_each_independent_structure()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `.available_operations()` → `test_managers_registry_metadata_and_display_results_are_isolated()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.available_operations()` → `render()`  [AMBIGUOUS]
  ui/structures_view.py · relation: calls
- `.execute()` → `.display()`  [AMBIGUOUS]
  data_structures/manager.py · relation: calls
- `.execute()` → `test_samples_rank_invalidation_and_independent_structure_state()`  [AMBIGUOUS]
  tests/test_app_integration.py · relation: calls
- `.execute()` → `test_all_sections_render_and_manager_survives_reruns()`  [AMBIGUOUS]
  tests/test_app_shell.py · relation: calls
- `.execute()` → `test_common_size_routes_bind_to_each_independent_structure()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `.execute()` → `test_stateful_sequences_and_derived_sets_return_plain_values()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.execute()` → `test_managers_registry_metadata_and_display_results_are_isolated()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.execute()` → `test_unsupported_requests_fail_without_mutation()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.execute()` → `test_names_must_be_strings()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.execute()` → `test_argument_errors_are_clear_and_do_not_mutate()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.execute()` → `test_structure_domain_errors_preserve_exception_type()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.execute()` → `test_size_operation_cannot_override_its_bound_instance()`  [AMBIGUOUS]
  tests/test_manager.py · relation: calls
- `.execute()` → `test_integer_structure_mutations_persist_and_reset()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `.execute()` → `test_set_algebra_through_controls_preserves_operand()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `.execute()` → `test_graph_and_hash_table_controls_and_errors()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `.execute()` → `test_empty_pop_invalid_integer_and_unknown_operation_are_readable()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `.execute()` → `test_ui_growth_guard_is_atomic_and_allows_existing_key_updates()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `.execute()` → `execute_structure()`  [AMBIGUOUS]
  ui/state.py · relation: calls
- `.execute()` → `render()`  [AMBIGUOUS]
  ui/structures_view.py · relation: calls
- `Persistent structure instances behind an explicit operation allowlist.  No eval,` → `Queue`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Persistent structure instances behind an explicit operation allowlist.  No eval,` → `Stack`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Persistent structure instances behind an explicit operation allowlist.  No eval,` → `BinarySearchTree`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Detached registry metadata for UI choices; exposes no bound methods.` → `Queue`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Detached registry metadata for UI choices; exposes no bound methods.` → `Stack`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Detached registry metadata for UI choices; exposes no bound methods.` → `BinarySearchTree`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Dispatch a named operation with keyword arguments and preserve state.          U` → `Queue`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Dispatch a named operation with keyword arguments and preserve state.          U` → `Stack`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Dispatch a named operation with keyword arguments and preserve state.          U` → `BinarySearchTree`  [AMBIGUOUS]
  data_structures/manager.py · relation: uses
- `Queue` → `BenchmarkConfig`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Queue` → `BenchmarkRun`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Queue` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Queue` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Queue` → `FIFO, error, and detached-inspection contracts.`  [AMBIGUOUS]
  tests/test_queue.py · relation: uses
- `.enqueue()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.enqueue()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.dequeue()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.dequeue()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.dequeue()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.front()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.front()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `Stack` → `BenchmarkConfig`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Stack` → `BenchmarkRun`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Stack` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Stack` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `Stack` → `LIFO, error, and detached-inspection contracts.`  [AMBIGUOUS]
  tests/test_stack.py · relation: uses
- `.push()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.push()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.pop()` → `.inorder()`  [AMBIGUOUS]
  data_structures/tree.py · relation: calls
- `.pop()` → `.preorder()`  [AMBIGUOUS]
  data_structures/tree.py · relation: calls
- `.pop()` → `.postorder()`  [AMBIGUOUS]
  data_structures/tree.py · relation: calls
- `.pop()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.pop()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.pop()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.pop()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.pop()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.peek()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.peek()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `BinarySearchTree` → `BenchmarkConfig`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `BinarySearchTree` → `BenchmarkRun`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `BinarySearchTree` → `Reproducible, correctness-checked microbenchmarks independent of Streamlit.  Tim`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `BinarySearchTree` → `Return operation, external correctness checker, and prebuilt fixture size.`  [AMBIGUOUS]
  performance/benchmark.py · relation: uses
- `BinarySearchTree` → `Traversal, uniqueness, skew, and integer-domain checks.`  [AMBIGUOUS]
  tests/test_tree.py · relation: uses
- `.insert()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.insert()` → `body_sections()`  [AMBIGUOUS]
  scripts/build_apa_report.py · relation: calls
- `.insert()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.insert()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.insert()` → `test_supported_hashable_keys_and_identity_equality_semantics()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.insert()` → `test_unhashable_keys_fail_without_mutation()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.insert()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.insert()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.insert()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.insert()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.search()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.search()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.search()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.search()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.search()` → `parse_integer_list()`  [AMBIGUOUS]
  ui/inputs.py · relation: calls
- `.inorder()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.inorder()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.inorder()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.inorder()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.preorder()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.preorder()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.preorder()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.postorder()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.postorder()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.postorder()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.display()` → `test_uniqueness_display_and_order_independent_equality()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.display()` → `test_all_subset_pairs_match_builtin_oracle_and_preserve_operands()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.display()` → `test_hashable_values_follow_python_equality_and_inspection_is_detached()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.display()` → `test_unhashable_values_fail_without_changing_members()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.display()` → `test_known_bfs_dfs_order_with_cycles_and_disconnected_vertex()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.display()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.display()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.display()` → `test_seeded_mutations_match_dict_reference_with_fixed_capacity()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.display()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.display()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.display()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.display()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.display()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.display()` → `test_invalid_values_leave_tree_unchanged()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `.is_empty()` → `_prepare()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `.is_empty()` → `test_uniqueness_display_and_order_independent_equality()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.is_empty()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests/test_custom_set.py · relation: calls
- `.is_empty()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.is_empty()` → `test_invalid_second_endpoint_does_not_add_first_endpoint()`  [AMBIGUOUS]
  tests/test_graph.py · relation: calls
- `.is_empty()` → `test_colliding_keys_update_find_and_delete_independently()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.is_empty()` → `test_unhashable_keys_fail_without_mutation()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `.is_empty()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.is_empty()` → `test_lifo_peek_size_and_detached_input_display()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.is_empty()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `BenchmarkConfig` → `Real small measurements, reproducibility metadata, guards, and CSV integrity.`  [AMBIGUOUS]
  tests/test_benchmark.py · relation: uses
- `BenchmarkConfig` → `Tables use the same observations as CSV; UI measurements save to test storage.`  [AMBIGUOUS]
  tests/test_performance_dashboard.py · relation: uses
- `BenchmarkConfig` → `Measured tables, separate-unit charts, and full-run CSV export.`  [AMBIGUOUS]
  ui/performance_view.py · relation: uses
- `BenchmarkRun` → `Controlled supplemental hash experiment: one bucket versus 2n buckets.  Unique n`  [AMBIGUOUS]
  scripts/measure_hash_collisions.py · relation: uses
- `_environment()` → `run()`  [AMBIGUOUS]
  performance/benchmark.py · relation: calls
- `build()` → `run()`  [AMBIGUOUS]
  scripts/build_report.py · relation: calls
- `run()` → `algorithms()`  [AMBIGUOUS]
  tests/test_algorithm_ui.py · relation: calls
- `run()` → `test_both_algorithms_and_dataset_change_clear_stale_results()`  [AMBIGUOUS]
  tests/test_algorithm_ui.py · relation: calls
- `run()` → `test_rank_changes_invalid_input_empty_lists_and_trace_limit()`  [AMBIGUOUS]
  tests/test_algorithm_ui.py · relation: calls
- `run()` → `test_samples_rank_invalidation_and_independent_structure_state()`  [AMBIGUOUS]
  tests/test_app_integration.py · relation: calls
- `run()` → `test_all_sections_render_and_manager_survives_reruns()`  [AMBIGUOUS]
  tests/test_app_shell.py · relation: calls
- `run()` → `test_day1_and_all_day2_structures_run_without_installed_site_packages()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `run()` → `test_performance_ui_saves_actual_rows_and_renders_download_and_charts()`  [AMBIGUOUS]
  tests/test_performance_dashboard.py · relation: calls
- `run()` → `test_all_steps_final_values_previous_reset_and_navigation()`  [AMBIGUOUS]
  tests/test_sorting_ui.py · relation: calls
- `run()` → `test_slider_and_untraced_mode_do_not_discard_or_invent_steps()`  [AMBIGUOUS]
  tests/test_sorting_ui.py · relation: calls
- `run()` → `test_core_imports_and_playback_need_only_the_standard_library()`  [AMBIGUOUS]
  tests/test_sorting_visualizer.py · relation: calls
- `run()` → `structures()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `run()` → `test_integer_structure_mutations_persist_and_reset()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `run()` → `test_set_algebra_through_controls_preserves_operand()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `run()` → `test_graph_and_hash_table_controls_and_errors()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `run()` → `test_empty_pop_invalid_integer_and_unknown_operation_are_readable()`  [AMBIGUOUS]
  tests/test_structures_ui.py · relation: calls
- `test_seeded_random_traces_match_oracle_and_inversion_count()` → `.randrange()`  [AMBIGUOUS]
  tests/test_bubble_sort.py · relation: calls
- `test_seeded_graph_traversals_match_independent_small_reference()` → `.randrange()`  [AMBIGUOUS]
  tests/test_data_structure_integration.py · relation: calls
- `test_seeded_mutations_match_dict_reference_with_fixed_capacity()` → `.randrange()`  [AMBIGUOUS]
  tests/test_hash_table.py · relation: calls
- `test_seeded_mixed_workload_matches_fifo_list_model()` → `.randrange()`  [AMBIGUOUS]
  tests/test_queue.py · relation: calls
- `.randrange()` → `test_seeded_mixed_workload_matches_list_model()`  [AMBIGUOUS]
  tests/test_stack.py · relation: calls
- `.randrange()` → `test_seeded_insertions_match_sorted_unique_reference()`  [AMBIGUOUS]
  tests/test_tree.py · relation: calls
- `test_highlight_and_description_metadata_match_observed_events()` → `.get_step()`  [AMBIGUOUS]
  tests/test_sorting_visualizer.py · relation: calls
- `test_indices_outside_trace_are_rejected()` → `.get_step()`  [AMBIGUOUS]
  tests/test_sorting_visualizer.py · relation: calls
- `test_noninteger_indices_are_rejected()` → `.get_step()`  [AMBIGUOUS]
  tests/test_sorting_visualizer.py · relation: calls
- `Day 3's data-only playback contract and core import isolation.` → `SortingVisualizer`  [AMBIGUOUS]
  tests/test_sorting_visualizer.py · relation: uses
- `render()` → `.get_step()`  [AMBIGUOUS]
  ui/sorting_view.py · relation: calls
- `Display complete immutable traces with a persistent model playback index.` → `SortingVisualizer`  [AMBIGUOUS]
  ui/sorting_view.py · relation: uses

## Knowledge Gaps
- **111 isolated node(s):** `Local AlgoNexis portfolio. Launch with python -m streamlit run app.py.`, `Adjacent-element Bubble Sort with an optional complete, immutable trace.  The ca`, `One observed event; counters are cumulative as of this snapshot.      A compare`, `Sorted values, exact operation totals, and an optional event sequence.`, `Return a nonmutating sort result; duplicates keep their relative order.      ``t` (+106 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Algorithms Package Boundary`** (2 nodes): `UI-independent algorithms for AlgoNexis.`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Structures Package Boundary`** (2 nodes): `Standalone custom sets, data structures, and allowlisted stateful dispatch.`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Performance Package Boundary`** (2 nodes): `UI-independent correctness-checked timing and Python allocation tools.`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Artifact Scripts Package`** (2 nodes): `Optional, reproducible portfolio evidence and document utilities.`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Test Package Boundary`** (2 nodes): `Automated AlgoNexis correctness and integration checks.`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `UI Package Boundary`** (2 nodes): `Streamlit views and independently testable input/session helpers.`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Visualization Package Boundary`** (2 nodes): `UI-independent visualization data for AlgoNexis.`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Native PowerPoint Rendering`** (1 nodes): `render_powerpoint.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Optional Browser QA`** (1 nodes): `Optional Playwright Browser QA Dependency`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Historical Evidence Integrity Rule`** (1 nodes): `Verified Evidence and No Placeholder Results`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Historical Custom Set Plan`** (1 nodes): `Historical Day 1 Plan for CustomSet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Historical G3 Pending`** (1 nodes): `Historical Day 2 G3 Pending Status`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Historical G4 Pending`** (1 nodes): `Historical Day 1 Unverified G4 Release Gate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `_prepare()` connect `Graph Traversal and Fixtures` to `Measurement and Evidence Validation`, `Sorting Frames and Replay`, `Stack and Tree Algorithms`, `Selection and Dataset State`, `Explicit Custom Set Algebra`, `Separate Chaining Hash Table`, `Deque Queue Operations`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._
- **Why does `DataStructureManager` connect `Manager and UI Integration` to `Measurement and Evidence Validation`, `APA Style and Core Contracts`, `Stack and Tree Algorithms`, `Explicit Custom Set Algebra`, `Separate Chaining Hash Table`, `Graph Traversal and Fixtures`, `Deque Queue Operations`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
## APA report and guide outcome

The root `guide.md` covers installation on Windows and POSIX, a first-use tour,
all algorithms/structures, persistence and resets, bounded input, measured-data
interpretation, benchmark preservation/rebuilding, tests, core API examples,
troubleshooting, artifact locations, and the historical v1.0.0 release snapshot.
The guide's executable Python example passed; its local links were checked.

`documentation/performance_analysis_report.docx` is an editable APA 7 student
paper using the verified original analysis and observed summaries. A native
Microsoft Word export, `performance_analysis_report_apa.pdf`, has 18 pages:
title, eleven text pages (ten meet the >=150-word substantive-page check), one
reference page, and five figure pages. Its five figures and eight references
are complete. Validation checks page size/margins, TNR12, double spacing, paragraph
and reference indents, page fields, figure order, citation suffixes, current data
values, and rendered fonts. Title/body/reference/figure pages were inspected.
Fresh APA styles remove the stock template's theme font and decorative title rule.
Instructor and actual due date remain explicit prompts because they were not
supplied; edit `documentation/apa_title_page.json` or the Word document.

All 195 existing tests passed after the initial documentation additions; the core
measured source and original Day 4 artifacts continue to pass provenance checks.
The optional python-docx dependency is confined to document building. The original
v1.0.0 tag identifies the completed Day 4 snapshot; these additions follow on main.

## Extraction audit

The final corpus contains 77 files: 57 code and 20 documentation files, about
44,807 words. Sixteen documents came from semantic cache; one mandatory semantic
agent extracted four changed/new documents into 50 nodes, 100 edges, two
hyperedges, and ten exact doc-to-AST references. Generated Word/PDF files are
excluded via `.graphifyignore`; existing report prose plus APA setup notes carry
their narrative and formatting sources. Images/results and environment locks
are also excluded to avoid duplicate generated evidence.

Six colliding rationale IDs are namespaced. Local references resolve to actual
nodes; 36 external modules are explicitly labeled imports. Unsupported AST
co-occurrence uses (233 candidates) are marked AMBIGUOUS with score 0.2, while
scoped name use only supports INFERRED relationships. This is not a full call
graph. Every ID and endpoint is checked. Community cohesion is a raw structural
score, not a software-quality grade; community lists omit source-file anchors.
Token cost counters are unavailable. Retrieval/context sizes are heuristic
estimates, not measured model usage, proven savings, or answer-quality scores.

Change since the prior graph: 42 new nodes, 116 new edges, 1 node removed, 27 edges removed.
