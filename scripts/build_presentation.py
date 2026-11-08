"""Create twelve editable slides with authentic app evidence and speaker notes."""

from pathlib import Path

from performance.benchmark import ROOT
from scripts.build_report import report_values


def run() -> None:
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.util import Inches, Pt
    from PIL import Image

    values = report_values()
    deck = Presentation()
    deck.slide_width, deck.slide_height = Inches(13.333), Inches(7.5)
    navy, teal, ink, muted = '152F43', '087F7B', '203B4A', '526674'
    outline, walkthrough = ['# AlgoNexis — final presentation\n'], ['# Presentation walkthrough\n']

    def text(slide, x, y, w, h, content, size=22, color=ink, bold=False):
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        frame = box.text_frame
        frame.word_wrap = True
        frame.margin_left = frame.margin_right = 0
        frame.margin_top = frame.margin_bottom = 0
        for index, line in enumerate(content.split('\n')):
            paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
            paragraph.text = line
            paragraph.space_after = Pt(15)
            paragraph.font.name = 'Arial'
            paragraph.font.size = Pt(size)
            paragraph.font.bold = bold
            paragraph.font.color.rgb = RGBColor.from_string(color)
        return box

    def panel(slide, x, y, w, h, color):
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor.from_string(color)
        shape.line.fill.background()

    def picture(slide, relative, x=5.45, y=1.8, w=7.2, h=4.8):
        path = ROOT / relative
        width, height = Image.open(path).size
        scale = min(w/width, h/height)
        width, height = width*scale, height*scale
        slide.shapes.add_picture(str(path), Inches(x+(w-width)/2), Inches(y+(h-height)/2),
                                 width=Inches(width), height=Inches(height))

    def slide(title, lines, notes, image=None, kicker='IMPLEMENTATION → EVIDENCE → LEARNING', citation='Source: AlgoNexis implementation and recorded measurements'):
        current = deck.slides.add_slide(deck.slide_layouts[6])
        current.background.fill.solid()
        current.background.fill.fore_color.rgb = RGBColor.from_string('F5F8FA')
        panel(current, 0, 0, 13.333, .12, teal)
        text(current, .6, .38, 12, .35, kicker, 12, teal, True)
        text(current, .6, .95, 12.1, .75, title, 30, navy, True)
        if image:
            text(current, .65, 1.95, 4.4, 4.75, '\n'.join(lines), 22)
            picture(current, image)
        else:
            text(current, .8, 2.1, 11.7, 4.45, '\n'.join(lines), 25)
        panel(current, .6, 6.94, 12.1, .015, 'C9D8DE')
        text(current, .65, 7.08, 11.4, .25, citation, 10, muted)
        text(current, 12.2, 7.06, .5, .25, f'{len(deck.slides):02}', 12, teal, True)
        current.notes_slide.notes_text_frame.text = notes
        number = len(deck.slides)
        outline.append(f'## {number}. {title}\n\n' + '\n'.join(f'- {line}' for line in lines) +
                       (f'\n\nEvidence image: `{image}`' if image else '') + f'\n\n{citation}\n')
        walkthrough.append(f'## Slide {number}: {title}\n\n{notes}\n')
        return current

    slide('AlgoNexis', ['An interactive algorithms & data structures portfolio',
          'Shreyash · CSU Global · CSC506', 'November 7, 2026 · Portfolio v1.0.0'],
          'Introduce the portfolio as one application connecting implementation, explanation, and measured evidence. '
          'State the scope: two algorithms, sorting visualization, a custom set, five other structures, an interactive interface, '
          'and reproducible performance analysis. Explain that the presentation uses the actual working application and its saved data. '
          'The report provides eight substantive body pages plus a cover and references. The walkthrough follows the same requirements '
          'as the implementation plan and closes with the limits of the conclusions.', image='documentation/screenshots/dashboard.png')
    slide('One portfolio, four ways to explore', ['Dashboard: scope and guide', 'Algorithms: sort, select, inspect steps',
          'Data Structures: six persistent models', 'Performance: measurements and CSV'],
          'Open the local app with python -m streamlit run app.py. Begin on Dashboard, then use the sidebar to visit Algorithms, '
          'Data Structures, and Performance Analysis. Describe the learner journey: enter a dataset, inspect a computed result, '
          'change a structure, and examine evidence. State survives navigation because model data is separate from widget state. '
          'The browser walkthrough exercised these navigation and reset paths; the screenshots are captures of that real session.',
          image='documentation/screenshots/dashboard-mobile.png')
    architecture = slide('Architecture keeps the core independently testable', [],
          'Trace the arrows from the Streamlit views to plain Python APIs. Algorithms produce immutable results and sorting frames. '
          'The manager dispatches only explicitly registered structure methods. The benchmark calls the core directly, outside rendering. '
          'Fixtures, expectations, and validation are prepared outside each measurement. This separation allows tests and command line '
          'experiments to reuse exactly the same implementations. No core import starts the user interface. The source digests identify '
          'the measured core even after later documentation commits.')
    for x, y, w, title, detail in [(0.8,2.0,11.7,'Streamlit views + session state','Bounded input · explicit errors · independent model state'),
                                 (0.8,3.55,5.6,'Algorithms → immutable frames','Bubble Sort · Quickselect · step retrieval'),
                                 (6.9,3.55,5.6,'Manager → six structures','Explicit registry · persistent instances'),
                                 (0.8,5.1,11.7,'Performance → CSV → figures → report / slides','Fresh fixtures · correctness checks · separate time and allocation trials')]:
        panel(architecture,x,y,w,1.1,'E2EEEF')
        text(architecture,x+.2,y+.12,w-.4,.4,title,21,teal,True)
        text(architecture,x+.2,y+.61,w-.4,.35,detail,16)
    outline[-1] = outline[-1].replace('Source:',
        '- Streamlit views and session state call plain Python APIs.\n'
        '- Algorithms emit immutable frames; the manager owns six structures.\n'
        '- Direct core benchmarks produce CSV, figures, report, and slides.\n\nSource:')
    slide('Bubble Sort: make every comparison inspectable', ['Adjacent compare and swap', 'Early exit: O(n) best case',
          'O(n²) average / worst, untraced', 'Immutable snapshots; trace limit 50'],
          'In Algorithms, enter 3, 1, 2 and run Bubble Sort. Show the output 1, 2, 3. Step through initial, comparison, swap, '
          'and final events; use Previous and Reset to demonstrate replay without recomputation. There are three comparisons and '
          'two swaps for this example. The caller list is preserved. Explain that complete snapshots can cost O(n³) time and storage, '
          'so the interface bounds traced input and benchmarks disable tracing. Cite the report for the conventional adjacent-pass '
          'algorithm and the project-specific early-exit analysis.', image='documentation/screenshots/sorting-steps.png',
          citation='Algorithm background: OpenDSA, Bubble sort; project early-exit and trace contracts')
    slide('Quickselect: ask for one rank', ['One-based k; duplicates retain ranks', 'Randomized three-way partition',
          'Expected O(n); worst O(n²)', 'Copy preserves the caller’s input'],
          'Use the list 7, 2, 7, -1, 4 and choose k=3. The selected result is 4, matching the third entry of the sorted reference. '
          'Show the invalid rank message for k beyond the list length, then restore a valid value. Explain the smaller, equal, '
          'and larger pivot regions. Only the region containing the requested rank remains active. The plotted workload selects '
          'one middle rank, while Bubble Sort returns every item ordered; their times do not represent interchangeable tasks. '
          'An injected Random instance fixes pivot seeds without changing global random state.', image='results/figures/quickselect.png',
          citation='Selection background: Sedgewick & Wayne, Quick.java; means/min–max from final CSV')
    slide('Custom Set: membership defines equality', ['Dictionary-backed membership', 'Explicit union / intersection loops',
          'Difference and symmetric difference', 'Derived results preserve both operands'],
          'Select Custom Set and add 1 and 2. Use a second operand containing 2 and 3. Demonstrate union [1,2,3], '
          'intersection [2], difference [1], and symmetric difference [1,3]. Explain that the displayed order follows insertion '
          'for predictability while set equality remains unordered membership. Derived operations return new sets and do not mutate '
          'the inputs. The implementation writes the algebra explicitly rather than delegating to built-in set operators. '
          'Keys must be hashable, and expected membership costs depend on the dictionary hashing behavior.')
    slide('Stack and Queue: order determines representation', ['Stack: list end → LIFO, amortized O(1) push',
          'Queue: deque ends → FIFO, O(1) removal', 'Empty removal raises a clear IndexError',
          'Draining n elements is an O(n) batch'],
          'Push 10 then 20 on the Stack; peek and pop return 20. Enqueue 10 then 20 on the Queue; front and dequeue return 10. '
          'Drain both and demonstrate a graceful empty-state error. Explain the concrete representation choice: Python lists '
          'support efficient end operations, whereas repeatedly removing index zero shifts later elements. Deque avoids that '
          'front-shifting cost. The performance workload drains a preloaded fixture and constructs a returned list, so its '
          'operation allocation includes output storage and excludes the original structure.',
          citation='Python Software Foundation, collections — deque end operations and list front-removal costs')
    slide('Tree, Graph, Hash Table: expose the trade-offs', ['BST: ordered keys; shape controls search',
          'Graph: undirected adjacency; BFS / DFS',
          'Hash Table: fixed separate chains',
          f'One bucket / 2n lookup means: {values["hash_ratio"]}'],
          'Insert tree values 2,1,3 and show inorder [1,2,3]; describe how monotone insertion can instead form a chain. '
          'Create graph edges 0–1 and 1–2, then traverse from 0 using both BFS and DFS. Query an absent starting vertex to '
          'show the validation behavior. Insert, update, find, and delete an integer hash key with a text value. Explain that '
          'the importable core API also supports None payloads, distinct from missing keys; the UI deliberately uses text values. '
          'The chart holds queries constant while changing bucket capacity. One bucket forces a chain, while these keys occupy '
          'separate buckets at 2n capacity. It measures successful lookup batches, excluding construction.', image='results/figures/hash_collisions.png',
          citation='Sedgewick & Wayne: BST.java, BreadthFirstPaths.java, SeparateChainingHashST.java; controlled CSV')
    slide('The interface is part of correctness', ['Strict integer parsing; no eval', 'Separate model and widget state',
          'Explicit growth and trace limits', 'Navigation, failures, resets checked in Edge'],
          'Show the Algorithms screenshot, then switch sections and return to demonstrate persistence. Enter 1.5 to trigger '
          'the integer-input error and disabled action. In Data Structures, operate on a model, navigate away, and return. '
          'Reset all structures and confirm their empty state. Explain the limits: 50 traced sort items, 1,000 untraced sort '
          'items, general input at most 5,000 integers, and 200-item structure growth guards. Updates that do not grow a '
          'structure remain possible. These boundaries preserve a responsive local teaching application.',
          image='documentation/screenshots/algorithms.png')
    slide('Measure the work that the label describes', ['1,080 observed rows + 8 guarded skips', 'Five timing + five allocation repeats per case',
          'Setup / checking excluded; output included', 'Separate 60-row controlled collision profile'],
          'Open Performance Analysis and explain its pattern filter, timing and allocation charts, summary table, and full CSV '
          'download. Use the saved run instead of replacing the evidence during this presentation. Inputs are seeded with 506, '
          'and Quickselect pivots use seed plus trial. Point out that skips are blank observations rather than zeros. '
          'The CSV has environment and core source provenance; the analysis manifest hashes data and figures. The graph chart '
          'workload is a path, while the default hash profile has max(8,2n) capacity. Confidence intervals were not estimated.',
          image='results/figures/bubble_sort.png', citation='Final run c6f11506577d47dc87eddb2fc4391644 · mean with observed min–max')
    slide('Findings need boundaries', [f'BST sorted / random means: {values["bst_ratio"]}',
          'Repeated keys reduce effective fixture size', 'Tracked operation allocation ≠ total RAM',
          'One machine, five repeats, selected workloads'],
          'Explain the measured BST order effect using the actual prebuilt-tree search workload. Duplicates reduce stored '
          'node count and therefore change the fixture, not merely its query order. On this chart, output lists and protective '
          'copies explain much of the incremental allocation. Prebuilt structures are excluded, so these values cannot rank '
          'total representation memory. tracemalloc observes Python-tracked allocations, not resident memory. The shapes '
          'are consistent with implementation analysis but do not prove complexity or statistical significance. Distinguish '
          'all observed ratios from portable performance guarantees.', image='results/figures/allocations.png',
          citation='Python Software Foundation, tracemalloc; final measured summaries; prebuilt fixtures excluded')
    slide('Learning outcomes and release', ['Contracts connect algorithms, UI, tests, and evidence',
          '195 automated tests + real browser walkthrough', 'Report: 8 substantive pages; slides: 12',
          'Next: balanced tree, resizing hash, broader datasets'],
          'Close by mapping the eight deliverables: Bubble Sort and visualization, Quickselect, Custom Set, integrated '
          'portfolio, working interface, substantive performance report, presentation, and technical documentation. '
          'Describe learning about nonmutation, event immutability, insertion-order sensitivity, collision cost, '
          'and honest measurement boundaries. The clean install exposed a pandas wheel compatibility issue; the tested '
          'maintenance version resolved it without changing system policy. The retrospective records that challenge. '
          'The release checklist and verification record provide commands and evidence. Future work should follow '
          'the observed limitations: balancing, resizing, and independent datasets rather than unmeasured feature claims.')
    path = ROOT / 'documentation/portfolio_presentation.pptx'
    deck.save(path)
    (ROOT / 'documentation/portfolio_presentation.md').write_text('\n'.join(outline), encoding='utf-8')
    introduction = ('Suggested delivery: approximately 8–10 minutes, with the app launched beforehand. '
                    'The script below supplies speaker notes; actual oral delivery has not been performed by a human. '
                    'The browser walkthrough separately exercises navigation, algorithm events, failures, all six structures, '
                    'reset, charts, and exact CSV download. Do not rerun benchmarks during delivery because the report refers '
                    'to the saved final run.\n\n')
    (ROOT / 'documentation/presentation_walkthrough.md').write_text(introduction + '\n'.join(walkthrough), encoding='utf-8')
    print(f'Saved {len(deck.slides)} editable slides with authentic screenshots, figures, and speaker notes.')


if __name__ == '__main__':
    run()
