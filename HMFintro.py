# manim -ql -p HMFintro.py Introduction
from manim import *

class FontDisplay(Scene):
    def construct(self):
        import manimpango
        for f in manimpango.list_fonts():
            fonttext = Text(f, font_size=48, color=PURPLE, font=f)
            self.play(Create(fonttext))
            self.wait(0.5)
            self.play(FadeOut(fonttext))
            self.wait(0.1)

class DMTitleScreen(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsmath}")
        import manimpango
        title1 = Text("Discrete Math", font_size=84, color=BLUE, font="Palatino Linotype")
        title2 = Text("Converting decimal to binary", font_size=28, color=GREEN, font="Gill Sans MT")
        title3 = Text("Video 2.4.10", font_size=20, color=ORANGE, font="Tahoma")
        title4 = Text("Jason Lee, Ph.D.", font_size=12, color=PURPLE, font="Gill Sans MT")
        VGroup(title1).set_x(0).arrange(buff=0).set_y(1)
        VGroup(title2).set_x(0).arrange(buff=0).set_y(0)
        VGroup(title3).set_x(0).arrange(buff=0).set_y(-1)
        VGroup(title4).set_x(6.3).set_y(-3.7)
        self.add(title1, title2, title3, title4)

class DMIntroduction(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsmath}")
        import manimpango
        title1 = Text("Discrete Math", font_size=72, color=BLUE, font="Garamond")
        title2 = Text("Jason Lee, Ph.D.", font_size=24, color=PURPLE, font="Gill Sans MT")
        title3 = Text("Hello Math Fans!", font_size=12, color=GREEN, font="Georgia", slant=ITALIC)
        title4 = MathTex(r"(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}")
        VGroup(title1).set_x(0).arrange(buff=0).set_y(1)
        VGroup(title2).set_x(0).arrange(buff=0).set_y(0)
        VGroup(title3).set_x(0).arrange(buff=0).set_y(-0.5)
        VGroup(title4).set_x(0).arrange(buff=0).set_y(-2)
        self.play(GrowFromPoint(title1, ORIGIN))
        self.play(GrowFromCenter(title2))
        self.play(SpinInFromNothing(title3))
        self.play(Create(title4))
        self.wait(1)
        self.play(FadeOut(title1, title2, title3, title4))


        