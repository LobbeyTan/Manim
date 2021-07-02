from manim import *


class PythagorasTheorem(Scene):
    def construct(self):
        pythagoras_equation = MathTex(r"\text{Pythagoras Theorem: } a^2 + b^2 = c^2")

        parameters = MathTex(r"a = 3, b = 4")

        parameters.next_to(pythagoras_equation, DOWN)
        parameters.align_to(pythagoras_equation, LEFT)

        c = MathTex(r"c &= {\sqrt { {a}^{2}+{b}^{2}} }"
                    r"\\ &= {\sqrt { {3}^{2}+{4}^{2}} }"
                    r"\\ &= {\sqrt { {9}+{16}} }"
                    r"\\ &= {\sqrt {25} }"
                    r"\\ &= 5")

        self.play(FadeIn(pythagoras_equation), run_time=3)

        self.play(FadeIn(parameters), run_time=3)

        self.wait(3)

        self.play(FadeOut(pythagoras_equation, parameters))

        self.play(FadeIn(c), run_time=3)

        self.wait(3)


class MatrixSum(Scene):
    def construct(self):
        rule = MathTex(r"Matrix A + Matrix B = Matrix B + Matrix A")

        A = MathTex(r"\begin{bmatrix}"
                    r"a_{1}&  a_{2}&  a_{3}\\"
                    r"a_{4}&  a_{5}&  a_{6}\\"
                    r"a_{7}&  a_{8}&  a_{9}"
                    r"\end{bmatrix}")

        plus = MathTex(r" + ")

        B = MathTex(r"\begin{bmatrix}"
                    r"b_{1}&  b_{2}&  b_{3}\\"
                    r"b_{4}&  a_{5}&  b_{6}\\"
                    r"b_{7}&  a_{8}&  b_{9}"
                    r"\end{bmatrix}")

        equal = MathTex(r" = ")

        C = MathTex(r"\begin{bmatrix}"
                    r"a_{1} + b_{1}&  a_{2} + b_{2}&  a_{3} + b_{3}\\"
                    r"a_{4} + b_{4}&  a_{5} + b_{5}&  a_{6} + b_{6}\\"
                    r"a_{7} + b_{7}&  a_{8} + b_{8}&  a_{9} + b_{9}"
                    r"\end{bmatrix}")

        self.play(FadeIn(rule), run_time=3)

        self.wait(3)

        self.play(FadeOut(rule))

        self.play(FadeIn(A))

        self.play(ApplyMethod(A.move_to, LEFT * 5))

        self.play(FadeIn(plus))

        self.play(ApplyMethod(plus.next_to, A))

        self.play(FadeIn(B))

        self.play(ApplyMethod(B.next_to, plus))

        self.play(FadeIn(equal))

        self.play(ApplyMethod(equal.next_to, B))

        self.play(FadeIn(C))

        self.play(ApplyMethod(C.next_to, equal))

        self.wait(1)


