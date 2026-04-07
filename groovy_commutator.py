"""
Groovy Commutator Explainer — Manim Animation

8 scenes, ~3 minutes total
"""

from manim import *
import numpy as np

# ============ COLOR PALETTE ============
BG = "#1C1C1C"
PRIMARY = "#58C4DD"      # Blue (linear/affine)
SECONDARY = "#83C167"    # Green (nonlinear/carries)
ACCENT = "#FFFF00"       # Yellow (Class IV/critical)
ALERT = "#FF6B6B"        # Red (frozen/warning)
TEXT = "#EAEAEA"         # Light gray (text)
GRID_DIM = "#444444"     # Dark gray (grid)
MONO = "Menlo"


def eca_step(state, rule):
    """Single step of elementary CA."""
    n = len(state)
    new_state = np.zeros(n, dtype=int)
    for i in range(n):
        left = state[(i - 1) % n]
        center = state[i]
        right = state[(i + 1) % n]
        idx = (left << 2) | (center << 1) | right
        new_state[i] = (rule >> idx) & 1
    return new_state


def generate_eca(rule, width=64, steps=32):
    """Generate ECA spacetime diagram."""
    grid = np.zeros((steps, width), dtype=int)
    grid[0, width // 2] = 1
    for t in range(1, steps):
        grid[t] = eca_step(grid[t - 1], rule)
    return grid


class Scene1_Mystery(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("The Mystery", font_size=48, color=PRIMARY, weight=BOLD, font=MONO)
        title.to_edge(UP, buff=0.8)
        
        subtitle = Text("Simple rules. Complex behavior. Why?", font_size=24, color=TEXT, font=MONO)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1.0)
        self.wait(1.0)
        
        # Four CA grids
        rules = [0, 90, 30, 110]
        rule_names = ["Rule 0\n(Uniform)", "Rule 90\n(Periodic)", "Rule 30\n(Chaotic)", "Rule 110\n(Complex)"]
        colors = [PRIMARY, PRIMARY, SECONDARY, ACCENT]
        
        grids = VGroup()
        labels = VGroup()
        
        for i, (rule, name, color) in enumerate(zip(rules, rule_names, colors)):
            grid_data = generate_eca(rule, width=32, steps=24)
            pixels = VGroup()
            for row in range(24):
                for col in range(32):
                    if grid_data[row, col] == 1:
                        sq = Square(side_length=0.12, fill_color=color, fill_opacity=1, stroke_width=0)
                        sq.move_to([col * 0.12 - 1.9, row * 0.12 - 1.4, 0])
                        pixels.add(sq)
            
            x_pos = -4.5 + i * 3.0
            pixels.move_to([x_pos, 0, 0])
            
            label = Text(name, font_size=16, color=TEXT, font=MONO)
            label.next_to(pixels, DOWN, buff=0.3)
            
            grids.add(pixels)
            labels.add(label)
        
        for grid, label in zip(grids, labels):
            self.play(FadeIn(grid), Write(label), run_time=0.8)
        
        self.wait(2.0)
        
        question = Text("?", font_size=72, color=ACCENT, weight=BOLD, font=MONO)
        question.move_to(ORIGIN)
        question.set_opacity(0)
        
        self.play(FadeOut(grids), FadeOut(labels), FadeOut(subtitle),
                  question.animate.set_opacity(1).scale(1.2), run_time=1.0)
        self.play(question.animate.scale(1/1.2), run_time=0.5)
        self.wait(1.0)
        
        self.play(FadeOut(title), FadeOut(question), run_time=0.5)


class Scene2_ClassificationProblem(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("The Classification Problem", font_size=42, color=PRIMARY, weight=BOLD, font=MONO)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        
        classes = ["Class I\nUniform", "Class II\nPeriodic", "Class III\nChaotic", "Class IV\nComplex"]
        positions = [(-2.5, 1.5), (2.5, 1.5), (-2.5, -1.5), (2.5, -1.5)]
        
        quadrants = VGroup()
        for cls, (x, y) in zip(classes, positions):
            box = Rectangle(width=4, height=2.5, stroke_color=GRID_DIM, stroke_width=2)
            box.move_to([x, y, 0])
            label = Text(cls, font_size=20, color=TEXT, font=MONO)
            label.move_to([x, y + 0.8, 0])
            quadrants.add(VGroup(box, label))
        
        self.play(Create(quadrants), run_time=1.5)
        self.wait(1.0)
        
        critique = Text("Observation ≠ Explanation", font_size=28, color=ALERT, font=MONO)
        critique.to_edge(DOWN, buff=0.8)
        self.play(Write(critique), run_time=1.5)
        self.wait(1.5)
        
        self.play(FadeOut(quadrants), FadeOut(critique), run_time=0.5)
        
        # Rule 30 vs 90 contrast
        grid30 = generate_eca(30, width=40, steps=20)
        pixels30 = VGroup()
        for row in range(20):
            for col in range(40):
                if grid30[row, col] == 1:
                    sq = Square(side_length=0.1, fill_color=SECONDARY, fill_opacity=1, stroke_width=0)
                    sq.move_to([col * 0.1 - 2, row * 0.1, 0])
                    pixels30.add(sq)
        pixels30.move_to([-3, -1.5, 0])
        label30 = Text("Rule 30\n(degree 2)", font_size=14, color=SECONDARY, font=MONO)
        label30.next_to(pixels30, DOWN, buff=0.2)
        
        grid90 = generate_eca(90, width=40, steps=20)
        pixels90 = VGroup()
        for row in range(20):
            for col in range(40):
                if grid90[row, col] == 1:
                    sq = Square(side_length=0.1, fill_color=PRIMARY, fill_opacity=1, stroke_width=0)
                    sq.move_to([col * 0.1 - 2, row * 0.1, 0])
                    pixels90.add(sq)
        pixels90.move_to([3, -1.5, 0])
        label90 = Text("Rule 90\n(degree 1, affine)", font_size=14, color=PRIMARY, font=MONO)
        label90.next_to(pixels90, DOWN, buff=0.2)
        
        self.play(FadeIn(pixels30), Write(label30), FadeIn(pixels90), Write(label90), run_time=1.5)
        
        note = Text("Both chaotic — but algebraically different", font_size=20, color=ACCENT, font=MONO)
        note.to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=1.0)
        self.wait(2.0)
        
        self.play(FadeOut(title), FadeOut(pixels30), FadeOut(label30),
                  FadeOut(pixels90), FadeOut(label90), FadeOut(note), run_time=0.5)


class Scene3_Operators(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("The Operators", font_size=42, color=PRIMARY, weight=BOLD, font=MONO)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        
        # State S
        state_s = VGroup()
        bits = [1, 0, 1, 0, 0, 1, 0, 1]
        for i, b in enumerate(bits):
            color = SECONDARY if b else GRID_DIM
            sq = Square(side_length=0.4, fill_color=color, fill_opacity=1, stroke_color=TEXT, stroke_width=1)
            sq.move_to([i * 0.5 - 1.75, 1.5, 0])
            state_s.add(sq)
        
        label_s = Text("S (current state)", font_size=20, color=TEXT, font=MONO)
        label_s.next_to(state_s, UP, buff=0.3)
        
        self.play(Create(state_s), Write(label_s), run_time=1.5)
        self.wait(0.5)
        
        # D operator
        d_def = MathTex(r"D(S) = S \oplus E(S)", font_size=28, color=PRIMARY)
        d_def.move_to([-3, -0.5, 0])
        d_label = Text("D = dynamics", font_size=18, color=PRIMARY, font=MONO)
        d_label.next_to(d_def, DOWN, buff=0.2)
        d_desc = Text("which cells are about to flip", font_size=14, color=TEXT, font=MONO)
        d_desc.next_to(d_label, DOWN, buff=0.1)
        
        self.play(Write(d_def), run_time=1.5)
        self.play(FadeIn(d_label), FadeIn(d_desc), run_time=0.8)
        
        # E operator
        e_def = MathTex(r"E(S) = \text{rule}(S)", font_size=28, color=SECONDARY)
        e_def.move_to([3, -0.5, 0])
        e_label = Text("E = evolution", font_size=18, color=SECONDARY, font=MONO)
        e_label.next_to(e_def, DOWN, buff=0.2)
        e_desc = Text("what the rule computes", font_size=14, color=TEXT, font=MONO)
        e_desc.next_to(e_label, DOWN, buff=0.1)
        
        self.play(Write(e_def), run_time=1.5)
        self.play(FadeIn(e_label), FadeIn(e_desc), run_time=0.8)
        self.wait(2.0)
        
        self.play(FadeOut(d_def), FadeOut(d_label), FadeOut(d_desc),
                  FadeOut(e_def), FadeOut(e_label), FadeOut(e_desc),
                  FadeOut(label_s), run_time=0.5)
        
        # Composition diagram
        s_node = Circle(radius=0.3, fill_color=TEXT, fill_opacity=0.3, stroke_color=TEXT, stroke_width=2)
        s_node.move_to([-4, 0, 0])
        s_text = Text("S", font_size=24, color=TEXT, font=MONO)
        s_text.move_to(s_node.get_center())
        
        de_node = Circle(radius=0.3, fill_color=PRIMARY, fill_opacity=0.3, stroke_color=PRIMARY, stroke_width=2)
        de_node.move_to([0, 2, 0])
        de_text = Text("DE", font_size=20, color=PRIMARY, font=MONO)
        de_text.move_to(de_node.get_center())
        
        ed_node = Circle(radius=0.3, fill_color=SECONDARY, fill_opacity=0.3, stroke_color=SECONDARY, stroke_width=2)
        ed_node.move_to([0, -2, 0])
        ed_text = Text("ED", font_size=20, color=SECONDARY, font=MONO)
        ed_text.move_to(ed_node.get_center())
        
        arrow1 = Arrow(s_node.get_right(), de_node.get_left(), buff=0.1, color=PRIMARY)
        arrow2 = Arrow(s_node.get_right(), ed_node.get_left(), buff=0.1, color=SECONDARY)
        
        self.play(Create(s_node), Write(s_text), run_time=0.8)
        self.play(Create(de_node), Write(de_text), Create(ed_node), Write(ed_text),
                  Create(arrow1), Create(arrow2), run_time=1.5)
        
        note = Text("Two paths: D→E vs E→D", font_size=20, color=ACCENT, font=MONO)
        note.to_edge(DOWN, buff=0.8)
        self.play(Write(note), run_time=1.0)
        self.wait(2.0)
        
        self.play(FadeOut(title), FadeOut(s_node), FadeOut(s_text),
                  FadeOut(de_node), FadeOut(de_text), FadeOut(ed_node), FadeOut(ed_text),
                  FadeOut(arrow1), FadeOut(arrow2), FadeOut(note), FadeOut(state_s), run_time=0.5)


class Scene4_Commutator(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("The Groovy Commutator", font_size=42, color=ACCENT, weight=BOLD, font=MONO)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        
        equation = MathTex(r"G(S) = D(E(S)) \oplus E(D(S))", font_size=36, color=ACCENT)
        equation.move_to([0, 1, 0])
        
        self.play(Write(equation), run_time=2.0)
        self.wait(2.0)
        
        subtitle = Text("Measures non-commutativity of D and E", font_size=24, color=TEXT, font=MONO)
        subtitle.next_to(equation, DOWN, buff=0.5)
        self.play(FadeIn(subtitle), run_time=1.0)
        self.wait(1.0)
        
        self.play(FadeOut(subtitle), run_time=0.3)
        
        # Affine case
        case1_title = Text("Affine Rule (G ≡ 0)", font_size=22, color=PRIMARY, font=MONO)
        case1_title.move_to([-3, -0.5, 0])
        case1_desc = Text("Linear + constant\nOperators commute", font_size=16, color=TEXT, font=MONO)
        case1_desc.next_to(case1_title, DOWN, buff=0.3)
        
        path1a = Line([-4, -2, 0], [-2, -1, 0], color=PRIMARY, stroke_width=3)
        path1b = Line([-4, -2, 0], [-2, -3, 0], color=SECONDARY, stroke_width=3)
        converge1 = Dot([-2, -2, 0], color=PRIMARY, radius=0.15)
        
        self.play(Write(case1_title), Write(case1_desc), Create(path1a), Create(path1b), run_time=1.5)
        self.play(FadeIn(converge1), run_time=0.5)
        self.wait(0.5)
        
        # Nonlinear case
        case2_title = Text("Nonlinear Rule (G > 0)", font_size=22, color=SECONDARY, font=MONO)
        case2_title.move_to([3, -0.5, 0])
        case2_desc = Text("Carries propagate\nOperators don't commute", font_size=16, color=TEXT, font=MONO)
        case2_desc.next_to(case2_title, DOWN, buff=0.3)
        
        path2a = Line([2, -2, 0], [4, -1, 0], color=PRIMARY, stroke_width=3)
        path2b = Line([2, -2, 0], [4, -3, 0], color=SECONDARY, stroke_width=3)
        diverge2a = Dot([4, -1, 0], color=PRIMARY, radius=0.15)
        diverge2b = Dot([4, -3, 0], color=SECONDARY, radius=0.15)
        
        carries = VGroup()
        for i in range(3):
            c = Dot([3 + i*0.3, -2 + np.sin(i)*0.3, 0], color=ACCENT, radius=0.1)
            carries.add(c)
        
        self.play(Write(case2_title), Write(case2_desc), Create(path2a), Create(path2b), run_time=1.5)
        self.play(FadeIn(diverge2a), FadeIn(diverge2b), *[FadeIn(c) for c in carries], run_time=0.8)
        self.wait(2.0)
        
        insight = Text("Nonzero G = nonlinear carries = computational seeds", font_size=22, color=ACCENT, font=MONO)
        insight.to_edge(DOWN, buff=0.6)
        self.play(Write(insight), run_time=1.5)
        self.wait(3.0)
        
        self.play(FadeOut(title), FadeOut(equation), FadeOut(case1_title), FadeOut(case1_desc),
                  FadeOut(path1a), FadeOut(path1b), FadeOut(converge1), FadeOut(case2_title),
                  FadeOut(case2_desc), FadeOut(path2a), FadeOut(path2b), FadeOut(diverge2a),
                  FadeOut(diverge2b), FadeOut(carries), FadeOut(insight), run_time=0.5)


class Scene5_MonomialSupport(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Monomial Support", font_size=42, color=PRIMARY, weight=BOLD, font=MONO)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        
        anf_intro = Text("Algebraic Normal Form (over GF(2))", font_size=24, color=TEXT, font=MONO)
        anf_intro.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(anf_intro), run_time=1.0)
        self.wait(0.5)
        
        rules = [
            ("Rule 90", r"x_0 \oplus x_1", "(0, 2, 0, 0)", PRIMARY),
            ("Rule 150", r"x_0 \oplus x_1 \oplus x_2", "(0, 3, 0, 0)", PRIMARY),
            ("Rule 30", r"x_0 \oplus x_1 \oplus x_2 \oplus x_1 x_2", "(0, 3, 1, 0)", SECONDARY),
            ("Rule 110", r"x_0 \oplus x_1 \oplus x_2 \oplus x_1 x_2 \oplus x_2 x_3", "(0, 2, 1, 1)", ACCENT),
        ]
        
        current_y = 1.5
        for name, formula, profile, color in rules:
            name_text = Text(name, font_size=20, color=color, font=MONO, weight=BOLD)
            name_text.move_to([-4, current_y, 0])
            
            formula_tex = MathTex(formula, font_size=24, color=color)
            formula_tex.next_to(name_text, RIGHT, buff=0.5)
            
            profile_text = Text(profile, font_size=18, color=TEXT, font=MONO)
            profile_text.next_to(formula_tex, RIGHT, buff=0.8)
            
            self.play(Write(name_text), run_time=0.6)
            self.play(Write(formula_tex), run_time=1.0)
            self.play(FadeIn(profile_text), run_time=0.5)
            
            current_y -= 1.0
            self.wait(0.3)
        
        self.wait(1.0)
        
        insight_box = Rectangle(width=8, height=1.5, stroke_color=ACCENT, stroke_width=3, 
                               fill_color=ACCENT, fill_opacity=0.1)
        insight_box.to_edge(DOWN, buff=0.8)
        
        insight_text = Text("All Class IV rules have exactly ONE degree-2 monomial", 
                           font_size=22, color=ACCENT, font=MONO)
        insight_text.move_to(insight_box.get_center())
        
        self.play(Create(insight_box), Write(insight_text), run_time=2.0)
        self.wait(3.0)
        
        self.play(FadeOut(title), FadeOut(anf_intro), FadeOut(insight_box), FadeOut(insight_text), run_time=0.5)


class Scene6_ExperimentalResults(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Experimental Results", font_size=42, color=PRIMARY, weight=BOLD, font=MONO)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        
        # Stats boxes
        stat1_box = Rectangle(width=3.5, height=2, stroke_color=SECONDARY, stroke_width=2, 
                             fill_color=SECONDARY, fill_opacity=0.1)
        stat1_box.move_to([-3, 1, 0])
        
        stat1_value = Text("43%", font_size=48, color=SECONDARY, font=MONO, weight=BOLD)
        stat1_value.move_to([-3, 1.2, 0])
        stat1_label = Text("G variance explained\nby degree profile", font_size=16, color=TEXT, font=MONO)
        stat1_label.move_to([-3, 0.3, 0])
        
        stat2_box = Rectangle(width=3.5, height=2, stroke_color=ACCENT, stroke_width=2,
                             fill_color=ACCENT, fill_opacity=0.1)
        stat2_box.move_to([3, 1, 0])
        
        stat2_value = Text("88.6%", font_size=48, color=ACCENT, font=MONO, weight=BOLD)
        stat2_value.move_to([3, 1.2, 0])
        stat2_label = Text("Wolfram class\nprediction accuracy", font_size=16, color=TEXT, font=MONO)
        stat2_label.move_to([3, 0.3, 0])
        
        self.play(Create(stat1_box), Write(stat1_value), Write(stat1_label),
                  Create(stat2_box), Write(stat2_value), Write(stat2_label), run_time=2.0)
        self.wait(2.0)
        
        scatter_title = Text("All 256 ECA rules", font_size=20, color=TEXT, font=MONO)
        scatter_title.move_to([0, -1, 0])
        self.play(FadeIn(scatter_title), run_time=0.8)
        
        np.random.seed(42)
        points = VGroup()
        
        for _ in range(50):
            x = np.random.uniform(-4, -2)
            y = np.random.uniform(-3, -1.5)
            p = Dot([x, y, 0], color=PRIMARY, radius=0.06)
            points.add(p)
        
        for _ in range(100):
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(-3, -1.5)
            p = Dot([x, y, 0], color=SECONDARY, radius=0.06)
            points.add(p)
        
        for _ in range(20):
            x = np.random.uniform(2, 4)
            y = np.random.uniform(-2.5, -1.5)
            p = Dot([x, y, 0], color=ACCENT, radius=0.08)
            points.add(p)
        
        self.play(*[FadeIn(p) for p in points], run_time=1.5)
        
        legend = VGroup()
        leg1 = Dot([-5, -3.2, 0], color=PRIMARY, radius=0.06)
        leg1_text = Text("Affine (G≡0)", font_size=14, color=PRIMARY, font=MONO)
        leg1_text.next_to(leg1, RIGHT, buff=0.2)
        
        leg2 = Dot([-1.5, -3.2, 0], color=SECONDARY, radius=0.06)
        leg2_text = Text("Nonlinear", font_size=14, color=SECONDARY, font=MONO)
        leg2_text.next_to(leg2, RIGHT, buff=0.2)
        
        leg3 = Dot([2, -3.2, 0], color=ACCENT, radius=0.08)
        leg3_text = Text("Class IV", font_size=14, color=ACCENT, font=MONO)
        leg3_text.next_to(leg3, RIGHT, buff=0.2)
        
        legend.add(leg1, leg1_text, leg2, leg2_text, leg3, leg3_text)
        self.play(*[FadeIn(x) for x in legend], run_time=1.0)
        self.wait(3.0)
        
        self.play(FadeOut(title), FadeOut(stat1_box), FadeOut(stat1_value), FadeOut(stat1_label),
                  FadeOut(stat2_box), FadeOut(stat2_value), FadeOut(stat2_label),
                  FadeOut(scatter_title), FadeOut(points), FadeOut(legend), run_time=0.5)


class Scene7_Universality(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Universality Across Topologies", font_size=40, color=PRIMARY, weight=BOLD, font=MONO)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        
        topologies = [
            ("1D Elementary", [-4, 0, 0]),
            ("2D von Neumann", [-1.3, 0, 0]),
            ("2D Moore", [1.3, 0, 0]),
            ("Margolus Block", [4, 0, 0]),
        ]
        
        topo_group = VGroup()
        for name, pos in topologies:
            box = Rectangle(width=2.2, height=1.8, stroke_color=GRID_DIM, stroke_width=2)
            box.move_to(pos)
            label = Text(name, font_size=16, color=TEXT, font=MONO)
            label.next_to(box, DOWN, buff=0.2)
            topo_group.add(box, label)
        
        self.play(*[Create(x) if isinstance(x, Rectangle) else FadeIn(x) for x in topo_group], run_time=2.0)
        self.wait(1.0)
        
        g_formula = MathTex(r"G(S) = D(E(S)) \oplus E(D(S))", font_size=32, color=ACCENT)
        g_formula.to_edge(DOWN, buff=1)
        
        connections = VGroup()
        for _, pos in topologies:
            line = Line(pos, g_formula.get_top(), color=ACCENT, stroke_width=1, opacity=0.5)
            connections.add(line)
        
        self.play(*[Create(c) for c in connections], run_time=1.5)
        self.play(Write(g_formula), run_time=2.0)
        self.wait(2.0)
        
        tagline = Text("Same measure. Any topology.", font_size=28, color=SECONDARY, font=MONO)
        tagline.next_to(g_formula, UP, buff=0.8)
        self.play(Write(tagline), run_time=1.5)
        self.wait(3.0)
        
        self.play(FadeOut(title), FadeOut(topo_group), FadeOut(connections),
                  FadeOut(g_formula), FadeOut(tagline), run_time=0.5)


class Scene8_Implication(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        line1 = Text("Algebra", font_size=48, color=PRIMARY, font=MONO, weight=BOLD)
        line1.move_to([0, 1.5, 0])
        
        arrow = Text("→", font_size=48, color=TEXT, font=MONO)
        arrow.move_to([0, 0.5, 0])
        
        line2 = Text("Computation", font_size=48, color=ACCENT, font=MONO, weight=BOLD)
        line2.move_to([0, -0.5, 0])
        
        self.play(Write(line1), run_time=1.5)
        self.play(Write(arrow), run_time=1.0)
        self.play(Write(line2), run_time=1.5)
        self.wait(2.0)
        
        subtitle = Text("The Groovy Commutator identifies computational structure", 
                       font_size=22, color=TEXT, font=MONO)
        subtitle.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(subtitle), run_time=1.0)
        self.wait(2.0)
        
        final = Text("before simulation", font_size=28, color=SECONDARY, font=MONO, weight=BOLD)
        final.next_to(subtitle, DOWN, buff=0.5)
        self.play(Write(final), run_time=1.5)
        self.wait(3.0)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.0)
        
        logo = Text("Groovy Commutator", font_size=36, color=ACCENT, font=MONO, weight=BOLD)
        logo.move_to([0, 0.5, 0])
        
        tag = Text("Algebraic invariants for computational prediction", 
                  font_size=18, color=TEXT, font=MONO)
        tag.move_to([0, -0.3, 0])
        
        self.play(Write(logo), run_time=1.5)
        self.play(FadeIn(tag), run_time=1.0)
        self.wait(4.0)
        
        self.play(FadeOut(logo), FadeOut(tag), run_time=1.0)
