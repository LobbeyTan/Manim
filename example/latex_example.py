from manim import *


class ExampleLaTeX(Scene):
    def construct(self):
        tex = Tex(r'\LaTeX').scale(3)
        self.add(tex)
        self.wait(1)


class Example1LaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\xrightarrow{Hello}$ \LaTeX').scale(3)
        self.add(tex)
        self.wait(1)


class Example1bLaTeX(Scene):
    def construct(self):
        tex = MathTex(r'\xrightarrow{Hello}\text{ \LaTeX}').scale(3)
        self.add(tex)
        self.wait(1)


class Example2LaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{Hello}$ \LaTeX').scale(3)
        self.add(tex)
        self.wait(1)


class Example2bLaTeX(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE).scale(3)
        self.add(tex)
        self.wait(1)


class Example3LaTeX(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(r'$\mathscr{H} \rightarrow \mathbb{H}$}', tex_template=myTemplate).scale(3)
        self.add(tex)
        self.wait(1)


class Example4LaTeX(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX').scale(3)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)
        self.wait(1)


class Example5LaTeX(Scene):
    def construct(self):
        tex = Tex(r'$f: A \rightarrow B$', tex_template=TexFontTemplates.french_cursive).scale(3)
        self.add(tex)
        self.wait(1)


class Example6LaTeX(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex).scale(3)
        self.add(tex)
        self.wait(1)


class Example7LaTeX(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6').scale(2)
        self.add(tex)
        self.wait(1)


if __name__ == '__main__':
    Example7LaTeX().construct()
