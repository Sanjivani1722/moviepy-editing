import os
from moviepy.editor import *
import time

currentDirectory = os.getcwd()
subDirectories =  os.listdir(currentDirectory)
subDirectories = [i for i in subDirectories if i == "DBMS" or i == "OS"]

for i in subDirectories[:]: #AltIntro, DBMS, Nhce_Logo.png, OS, sem3.py
    for j in os.listdir(i):
        mp4Split = j.split('.mp4')
        LabVidSplitList = mp4Split[0].split('_')
        LabVidString = '\n'.join(map(str, LabVidSplitList))   

        #Have found the lab prgm path here
        video_path = os.path.join(currentDirectory, i, j)

        #Passing each prgm path to generate labClip
        labClip = VideoFileClip(video_path)
        lw, lh = labClip.size
        #sample is our subclip for 
        labSubClip = labClip.subclip(0,10)
        NhceLogo = ImageClip('Nhce_Logo.png')
        NhceLogo = NhceLogo.resize(0.2)
        NhceLogo = NhceLogo.set_opacity(0.5)
        NhceLogo = NhceLogo.set_duration(10)

        # Set the position of logo on the video
        NhceLogo = NhceLogo.set_position("right", "center")

        #Clipping logo on the video
        sampleSubCLipWithLogo = CompositeVideoClip([labSubClip, NhceLogo])

        #Text Clip Generated
        txt_clip = TextClip(LabVidString, fontsize=35, color='white', font='Perpetua-Titling-MT-Light', interline = 10)
        txt_clip = txt_clip.set_position('center')

        #Path of Inro Clip
        introClip = VideoFileClip("AltIntro.mp4")

        #Deriving text-clip size
        w, h = txt_clip.size
        #Genereating our background color clip, and having its size larger than text clio
        color_clip = ColorClip(size=(w + 300, h + 50), color=(0, 100, 150)) #some Bluish-Green shade
        #Reducing only background opacity
        color_clip = color_clip.set_opacity(0.5)

        #Pasting txt_clip on our color_clip
        mask_clip = CompositeVideoClip([color_clip, txt_clip])
        mask_clip = mask_clip.set_position('center').set_duration(introClip.duration)
        mask_clip = mask_clip.crossfadein(0.9).crossfadeout(0.9)

        #Pasting our mask_Clip on our introClip
        introVideo = CompositeVideoClip([introClip, mask_clip])
        introVideo = introVideo.set_duration(introClip.duration)
        final_clip = concatenate_videoclips([introVideo, sampleSubCLipWithLogo])

        #Saving the file as the lab vid name we derived
        final_clip.write_videofile(j)




