# Graph Report - AlgoNexis Day 2  (2026-11-05)

## Corpus Check
- Corpus is ~20,947 words - fits in a single context window. You may not need a graph.

## Summary
- 335 nodes · 729 edges · 20 communities detected
- Extraction: 65% EXTRACTED · 13% INFERRED · 22% AMBIGUOUS · INFERRED: 94 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Sorting Trace and Playback
- Chained Hash Table Tests
- Selection and Integer Validation
- Custom Set Algebra Tests
- Verified Day Two Contracts
- Deterministic Graph Traversal
- Core Modules and Imports
- Verified Day One Contracts
- Unbalanced Tree Traversals
- Future UI and Submission
- Manager Dispatch and Integration
- FIFO Queue and Checks
- LIFO Stack and Checks
- Algorithm Package Boundary
- Structures Package Boundary
- Performance Package Boundary
- Test Package Boundary
- Visualization Package Boundary
- Evidence Integrity Rationale
- Historical Day One Planning

## God Nodes (most connected - your core abstractions)
1. `CustomSet` - 29 edges
2. `Graph` - 26 edges
3. `HashTable` - 26 edges
4. `DataStructureManager` - 22 edges
5. `BinarySearchTree` - 22 edges
6. `bubble_sort()` - 19 edges
7. `quickselect()` - 18 edges
8. `Queue` - 18 edges
9. `Stack` - 18 edges
10. `SortingVisualizer` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Prepare immutable Bubble Sort frames without a Streamlit dependency.  Example:` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py
- `UI-ready metadata; values reuse the algorithm's immutable snapshot.` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py
- `Read-only, index-based view of a traced BubbleSortResult.      Indices are zero-` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py
- `Number of available frames, including initial and final states.` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py
- `Return the requested frame without altering playback or result state.` --uses--> `BubbleSortResult`  [AMBIGUOUS]
  visualization\sorting_visualizer.py → algorithms\bubble_sort.py

## Hyperedges (group relationships)
- **Day 1 Verified Algorithm and Playback Evidence** — readme_bubble, readme_quickselect, readme_visualizer, readme_tests, arch_imports [EXTRACTED 1.00]
- **Six Structures Behind One Persistent Manager** — readme_manager, readme_set, readme_stack, readme_queue, readme_bst, readme_graph, readme_hash [EXTRACTED 1.00]
- **G2 Acceptance Through Regression and All Manager Routes** — readme_g2, day2_tests, manager_routes, day2_record, arch_imports [EXTRACTED 1.00]

## Communities

### Community 0 - "Sorting Trace and Playback"
Cohesion: 0.1
Nodes (33): Frozen SortingStep, bubble_sort(), BubbleSortResult, Adjacent-element Bubble Sort with an optional complete, immutable trace.  The ca, One observed event; counters are cumulative as of this snapshot.      A compare, Sorted values, exact operation totals, and an optional event sequence., Return a nonmutating sort result; duplicates keep their relative order.      ``t, SortingStep (+25 more)

### Community 1 - "Chained Hash Table Tests"
Cohesion: 0.1
Nodes (17): Remove a member, raising KeyError if absent., HashTable, Insert/update; True for a new key, False for an update., Return the stored value, including None; raise KeyError if missing., Remove/return the value; raise KeyError if missing., Detached key/value pairs in bucket order, then chain insertion order., Detached bucket and chain containers for collision inspection., test_mutations_membership_and_missing_values() (+9 more)

### Community 2 - "Selection and Integer Validation"
Cohesion: 0.12
Nodes (26): quickselect(), Iterative randomized Quickselect with one-based ranks and duplicate support.  Un, Return the kth-smallest integer without sorting or changing caller data.      Ra, Random, assert_replay(), Independently replay the emitted actions rather than another sort loop., test_exhaustive_short_lists_replay_every_event(), test_seeded_random_traces_match_oracle_and_inversion_count() (+18 more)

### Community 3 - "Custom Set Algebra Tests"
Cohesion: 0.11
Nodes (15): CustomSet, Mutable membership with nonmutating, new-set derived operations., Insert a hashable value; return True only when membership changes., Remove if present; return whether membership changed., Return a detached member list in insertion order., New set of both operands, left members followed by new right members., _require_set(), itertools (external import) (+7 more)

### Community 4 - "Verified Day Two Contracts"
Cohesion: 0.12
Nodes (31): Independent Core and Future UI, Ignore Duplicate Integers and Avoid Recursion, Day 2 Acceptance Evidence, 143 Passing Day 1 and Day 2 Tests, IndexError for Empty Stack and Queue Operations, Validated Auto Endpoints and Idempotent Self-Loop Edges, Deterministic Reachable-Component BFS and Iterator DFS, Fixed Positive Hash Capacity and Load-Dependent Costs (+23 more)

### Community 5 - "Deterministic Graph Traversal"
Cohesion: 0.18
Nodes (14): Graph, Add if missing; return whether the vertex is new., Validate both endpoints before mutating, then add an undirected edge., Match recursive preorder using neighbor iterators, without recursion., Copy the adjacency mapping and each neighbor container, in order., test_seeded_graph_traversals_match_independent_small_reference(), example_graph(), Deterministic component traversals, cycles, and adjacency isolation. (+6 more)

### Community 6 - "Core Modules and Imports"
Cohesion: 0.12
Nodes (14): collections (external import), collections.abc (external import), Insertion-ordered custom set with explicitly implemented set algebra.  A dict st, functools (external import), Undirected, unweighted graph with insertion-ordered adjacency lists.  Hashable v, Custom fixed-capacity hash buckets with separate chaining.  Keys are hashable an, inspect (external import), Persistent structure instances behind an explicit operation allowlist.  No eval, (+6 more)

### Community 7 - "Verified Day One Contracts"
Cohesion: 0.15
Nodes (23): Caller Input Preservation, Frozen SortingFrame, Standard-Library-Only Core Imports, Iterative Randomized Three-Way Partition, Repeat Pivots Without Global RNG Mutation, Frozen BubbleSortResult, Full Snapshot Time and Storage Costs, Integer Validation and Explicit Errors (+15 more)

### Community 8 - "Unbalanced Tree Traversals"
Cohesion: 0.24
Nodes (11): Traversal, uniqueness, skew, and integer-domain checks., test_empty_and_singleton(), test_invalid_values_leave_tree_unchanged(), test_known_traversals_duplicate_policy_and_search(), test_seeded_insertions_match_sorted_unique_reference(), test_skewed_tree_beyond_recursion_depth(), BinarySearchTree, _Node (+3 more)

### Community 9 - "Future UI and Submission"
Cohesion: 0.13
Nodes (19): Avoid Snapshot Costs in Large Execution Trials, Explicit Trace-Disabled Benchmark Mode, Six Persistent Isolated Manager Instances, Next D3.1 Streamlit Shell Work Package, Planned Day 3 UI and Measurements, Planned Day 4 Submission Preparation, Planned Reproducible Measurement Protocol, Preexecution UI Workload Validation (+11 more)

### Community 10 - "Manager Dispatch and Integration"
Cohesion: 0.28
Nodes (13): DataStructureManager, Detached registry metadata for UI choices; exposes no bound methods., Dispatch a named operation with keyword arguments and preserve state.          U, test_common_size_routes_bind_to_each_independent_structure(), test_every_registered_operation_has_an_exercised_integration_route(), Allowlisted dispatch, state persistence, and safe result ownership., test_argument_errors_are_clear_and_do_not_mutate(), test_managers_registry_metadata_and_display_results_are_isolated() (+5 more)

### Community 11 - "FIFO Queue and Checks"
Cohesion: 0.24
Nodes (7): pytest (external import), Queue, Shallow copy in front-to-rear order., FIFO, error, and detached-inspection contracts., test_empty_operations_raise_index_error(), test_fifo_front_size_and_detached_input_display(), test_seeded_mixed_workload_matches_fifo_list_model()

### Community 12 - "LIFO Stack and Checks"
Cohesion: 0.26
Nodes (6): Shallow copy in bottom-to-top order., Stack, LIFO, error, and detached-inspection contracts., test_empty_operations_raise_index_error(), test_lifo_peek_size_and_detached_input_display(), test_seeded_mixed_workload_matches_list_model()

### Community 13 - "Algorithm Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent algorithms for AlgoNexis.

### Community 14 - "Structures Package Boundary"
Cohesion: 1.0
Nodes (1): Standalone custom sets, data structures, and allowlisted stateful dispatch.

### Community 15 - "Performance Package Boundary"
Cohesion: 1.0
Nodes (1): Package reserved for the Day 3 performance measurement tools.

### Community 16 - "Test Package Boundary"
Cohesion: 1.0
Nodes (1): Automated AlgoNexis correctness and integration checks.

### Community 17 - "Visualization Package Boundary"
Cohesion: 1.0
Nodes (1): UI-independent visualization data for AlgoNexis.

### Community 18 - "Evidence Integrity Rationale"
Cohesion: 1.0
Nodes (1): Verified Evidence and No Placeholder Results

### Community 19 - "Historical Day One Planning"
Cohesion: 1.0
Nodes (1): Historical Day 1 Plan for CustomSet

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
- `Graph` → `Complete manager-route coverage and standard-library-only Day 2 integration.`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: uses
- `Graph` → `Deterministic component traversals, cycles, and adjacency isolation.`  [AMBIGUOUS]
  tests\test_graph.py · relation: uses
- `.add_vertex()` → `test_seeded_graph_traversals_match_independent_small_reference()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.add_vertex()` → `example_graph()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_vertex()` → `test_undirected_duplicate_edges_self_loops_and_detached_display()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
- `.add_vertex()` → `test_invalid_second_endpoint_does_not_add_first_endpoint()`  [AMBIGUOUS]
  tests\test_graph.py · relation: calls
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
- `HashTable` → `CollidingKey`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: uses
- `HashTable` → `Collision chains, missing keys, updates, and mapping-model workloads.`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: uses
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
- `.contains()` → `test_mutations_membership_and_missing_values()`  [AMBIGUOUS]
  tests\test_custom_set.py · relation: calls
- `.contains()` → `test_none_values_missing_keys_and_detached_buckets()`  [AMBIGUOUS]
  tests\test_hash_table.py · relation: calls
- `DataStructureManager` → `Complete manager-route coverage and standard-library-only Day 2 integration.`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: uses
- `DataStructureManager` → `Allowlisted dispatch, state persistence, and safe result ownership.`  [AMBIGUOUS]
  tests\test_manager.py · relation: uses
- `.available_operations()` → `test_every_registered_operation_has_an_exercised_integration_route()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.available_operations()` → `test_common_size_routes_bind_to_each_independent_structure()`  [AMBIGUOUS]
  tests\test_data_structure_integration.py · relation: calls
- `.available_operations()` → `test_managers_registry_metadata_and_display_results_are_isolated()`  [AMBIGUOUS]
  tests\test_manager.py · relation: calls
- `.execute()` → `.display()`  [AMBIGUOUS]
  data_structures\manager.py · relation: calls
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
- `Queue` → `FIFO, error, and detached-inspection contracts.`  [AMBIGUOUS]
  tests\test_queue.py · relation: uses
- `.enqueue()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.enqueue()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.dequeue()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.dequeue()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.front()` → `test_fifo_front_size_and_detached_input_display()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
- `.front()` → `test_seeded_mixed_workload_matches_fifo_list_model()`  [AMBIGUOUS]
  tests\test_queue.py · relation: calls
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
- `BinarySearchTree` → `Traversal, uniqueness, skew, and integer-domain checks.`  [AMBIGUOUS]
  tests\test_tree.py · relation: uses
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
- `.search()` → `test_known_traversals_duplicate_policy_and_search()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.search()` → `test_empty_and_singleton()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
- `.search()` → `test_skewed_tree_beyond_recursion_depth()`  [AMBIGUOUS]
  tests\test_tree.py · relation: calls
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

## Knowledge Gaps
- **65 isolated node(s):** `Adjacent-element Bubble Sort with an optional complete, immutable trace.  The ca`, `One observed event; counters are cumulative as of this snapshot.      A compare`, `Sorted values, exact operation totals, and an optional event sequence.`, `Return a nonmutating sort result; duplicates keep their relative order.      ``t`, `Iterative randomized Quickselect with one-based ranks and duplicate support.  Un` (+60 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Algorithm Package Boundary`** (2 nodes): `__init__.py`, `UI-independent algorithms for AlgoNexis.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Structures Package Boundary`** (2 nodes): `__init__.py`, `Standalone custom sets, data structures, and allowlisted stateful dispatch.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Performance Package Boundary`** (2 nodes): `__init__.py`, `Package reserved for the Day 3 performance measurement tools.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Test Package Boundary`** (2 nodes): `__init__.py`, `Automated AlgoNexis correctness and integration checks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Visualization Package Boundary`** (2 nodes): `__init__.py`, `UI-independent visualization data for AlgoNexis.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Evidence Integrity Rationale`** (1 nodes): `Verified Evidence and No Placeholder Results`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Historical Day One Planning`** (1 nodes): `Historical Day 1 Plan for CustomSet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **High ambiguity: 22% of edges are AMBIGUOUS.** Review the Ambiguous Edges section above.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `HashTable` connect `Chained Hash Table Tests` to `Manager Dispatch and Integration`, `Custom Set Algebra Tests`, `Verified Day Two Contracts`, `Core Modules and Imports`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Why does `CustomSet` connect `Custom Set Algebra Tests` to `Chained Hash Table Tests`, `Manager Dispatch and Integration`, `Verified Day Two Contracts`, `Core Modules and Imports`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Why does `Graph` connect `Deterministic Graph Traversal` to `Manager Dispatch and Integration`, `Custom Set Algebra Tests`, `Verified Day Two Contracts`, `Core Modules and Imports`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `CustomSet` (e.g. with `DataStructureManager` and `.__init__()`) actually correct?**
  _`CustomSet` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Graph` (e.g. with `DataStructureManager` and `.__init__()`) actually correct?**
  _`Graph` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `HashTable` (e.g. with `DataStructureManager` and `.__init__()`) actually correct?**
  _`HashTable` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `DataStructureManager` (e.g. with `CustomSet` and `Graph`) actually correct?**
  _`DataStructureManager` has 15 INFERRED edges - model-reasoned connections that need verification._

## Verified Day 2 Outcome

All six structures and the fixed-registry manager are implemented. The full regression passed 143 tests (71 Day 1 plus 72 Day 2), including every one of the 49 registered manager routes. Compile/grammar checks, documented examples, pip dependency checks, and standard-library-only integration passed.

See [Day 2 evidence](../documentation/day2_verification.md), [operation contracts](../documentation/data_structures.md), and [architecture](../documentation/architecture.md). The tree is intentionally unbalanced and the table has fixed capacity, with documented load-dependent costs. Inspection snapshots copy containers, not arbitrary payload objects.

G1/G2 are verified; G3/G4, UI, measured application benchmarks, and final academic artifacts remain planned. Dated Day 1 evidence and its historical next-step record are retained as history. Existing user edits outside the plan Day 2 section were preserved.

## Graph Extraction Audit

The graph combines 27 Python sources, five refreshed documents, and two cached documents. Exact public API references connect contracts to AST declarations. Local import/property references were resolved to known declarations; external module nodes cite their import sites, not external source code. Duplicate package docstring IDs were namespaced by source.

AST uses candidates were checked against Name references in the actual declaration scope: matching code references retain INFERRED confidence 0.9; other module-co-occurrence candidates are AMBIGUOUS 0.2. They are not verified calls. Explicit source relationships have confidence 1.0. Suggested questions prioritize cross-community bridge nodes over heuristic ambiguity. Cohesion numbers are shown without hiding their values.


## Estimated Retrieval Benchmark

Heuristic context-size estimates only; not measured model usage, monetary savings, or an answer-quality comparison.

- Corpus estimate: 27929 tokens
- Average graph-query estimate: 9028 tokens
- Estimated reduction: 3.1x
