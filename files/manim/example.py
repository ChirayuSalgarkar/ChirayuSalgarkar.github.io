# from manim import *  # or: from manimlib import *
# from manim_slides import Slide

# class BasicExample(Slide):
#     def construct(self):
#         circle = Circle(radius=3, color=BLUE)
#         dot = Dot()

#         self.play(GrowFromCenter(circle))
#         self.next_slide()  # Waits user to press continue to go to the next slide

#         self.next_slide(loop=True)  # Start loop
#         self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
#         self.next_slide()  # This will start a new non-looping slide

#         self.play(dot.animate.move_to(ORIGIN))

from manim import *
from manim_slides import Slide
from datetime import date

class FooterText(Text):
    def __init__(self, text, **kwargs):
        super().__init__(
            text,
            font_size=16,
            color=WHITE,
            **kwargs
        )
        self.to_edge(DOWN, buff=0.2)

class PageNumber(Text):
    def __init__(self, num=1):
        super().__init__(
            f"Page {num}",
            font_size=16,
            color=WHITE
        )
        self.to_edge(DOWN, buff=0.2).to_edge(RIGHT, buff=0.5)

class BasicExample(Slide):
    def construct(self):
        # Footer setup
        footer_group = VGroup(
            FooterText("Mathematical Animations"),
            FooterText("Chirayu Salgarkar"),
            FooterText(date.today().strftime("%B %d, %Y")),
        ).arrange(RIGHT, buff=1).to_edge(DOWN, buff=0.2)
        
        footer_line = Line(
            start=np.array([-6.5, -3.5, 0]),
            end=np.array([6.5, -3.5, 0]),
            color=WHITE,
            stroke_width=1
        )

        # Initialize page number
        page_num = PageNumber(1)
        self.add(footer_group, footer_line, page_num)
        
        # Title Slide
        title = Text("Safe Reinforcement Learning using Black-box Reachability Analysis", font_size=25)
        subtitle = Text("Selim, M., Alanwar, A., Kousik, S., Gao, G., Pavone, M., & Johansson, K. H. (2022)", font_size=20)
        author = Text("Presented by Chirayu Salgarkar", font_size=20)
        
        title_group = VGroup(title, subtitle, author).arrange(DOWN, buff=0.5)
        
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.play(FadeIn(author, shift=UP), run_time=1)
        self.wait()
        self.next_slide()

        # Fade out title slide
        self.play(FadeOut(title_group))


    #-----------------------------------------------------------------------------------    
        # Basic Text Slide Example
        page_num.become(PageNumber(2))
        
        # Slide Title
        slide_title = Text("Key Concepts", font_size=48).to_edge(UP, buff=0.5)
        
        # Bullet points
        bullets = VGroup(
            Text("• First point: Introduction to animations", font_size=36),
            Text("• Second point: Understanding transforms", font_size=36),
            Text("• Third point: Working with shapes", font_size=36),
            Text("• Fourth point: Creating custom scenes", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(slide_title, DOWN, buff=0.5)

        # Show title
        self.play(Write(slide_title))
        
        # Show bullets one by one
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT * 0.5))
            self.wait(0.5)
            
        self.wait()
        self.next_slide()

        # Clean up before next slide
        self.play(FadeOut(slide_title), FadeOut(bullets))
     #-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------    
        # Basic Text Slide Example
        page_num.become(PageNumber(2))
        
        # Slide Title
        slide_title = Text("What is safe RL?", font_size=20).to_edge(UP, buff=0.5)
        
        # Bullet points
        bullets = VGroup(
            Text("• RL: perceive, react to environmental change", font_size=15),
            Text("Goal: maximise some long-term cumulative expected reward", font_size=15),
            Text("• What if you don't know the system dynamics?", font_size=15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(slide_title, DOWN, buff=0.5)

        # Show title
        self.play(Write(slide_title))
        
        # Show bullets one by one
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT * 0.5))
            self.wait(0.5)
            
        self.wait()
        self.next_slide()

        # Clean up before next slide
        self.play(FadeOut(slide_title), FadeOut(bullets))
     #-----------------------------------------------------------------------------------------








        # Continue with your circle animation...
        page_num.become(PageNumber(3))
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide()
        
        page_num.become(PageNumber(4))
        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()
        
        page_num.become(PageNumber(5))
        self.play(dot.animate.move_to(ORIGIN))