"""
Template for new videos
Copy this folder to videos/your-video-name/ and customize
"""

from manim import *

# ============ COLOR PALETTE ============
BG = "#1C1C1C"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FFFF00"
TEXT = "#EAEAEA"
MONO = "Menlo"


class Scene1_Introduction(Scene):
    """Opening scene — title and hook"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Your Title Here", font_size=48, color=PRIMARY, weight=BOLD, font=MONO)
        self.play(Write(title), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(title), run_time=0.5)


class Scene2_MainConcept(Scene):
    """Core concept explanation"""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Your animation here
        text = Text("Main concept", font_size=36, color=SECONDARY, font=MONO)
        self.play(Write(text), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(text), run_time=0.5)


class Scene3_Conclusion(Scene):
    """Closing scene"""
    
    def construct(self):
        self.camera.background_color = BG
        
        final = Text("Conclusion", font_size=42, color=ACCENT, weight=BOLD, font=MONO)
        self.play(Write(final), run_time=1.5)
        self.wait(3.0)
        self.play(FadeOut(final), run_time=0.5)
