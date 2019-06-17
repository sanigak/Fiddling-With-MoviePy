from moviepy.editor import *
import numpy as np

list = ["white.png"]

list = np.repeat(list, 50)

clip1 = TextClip("Hello !", font="Amiri-Bold", fontsize=70, color="white")
clip2 = TextClip("Hi !", font="Amiri-Bold", fontsize=70, color="white")
clip3 = TextClip("Hey !", font="Amiri-Bold", fontsize=70, color="white")
clip1 = clip1.set_duration(1)
clip2 = clip2.set_duration(1)
clip3 = clip3.set_duration(1)
final_clip = concatenate_videoclips([clip1,clip2,clip3])

final_clip.write_gif("circle.gif",fps=15)