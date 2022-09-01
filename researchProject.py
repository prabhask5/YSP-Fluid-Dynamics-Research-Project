#import needed modules
import numpy as np
import matplotlib.pyplot as plt
from videoreader import VideoReader
import plotly.express as px
import cv2
import pandas as pd
from progressbar import ProgressBar
import plotly.io as pio

pio.renderers.default='browser'





#import video files
files = []
# files.append("1Bldg_0p1mpers.MP4")
# files.append("1Bldg_0p04mpers.MP4")
# files.append("1Bldg_0p15mpers.MP4")
# files.append("NoObs_0p1mpers.MP4")
# files.append("NoObs_0p04mpers.MP4")
# files.append("NoObs_0p15mpers.MP4")
files.append("1Bldg_0p1mpers_short.MP4")
files.append("1Bldg_0p04mpers_short.MP4")
files.append("1Bldg_0p15mpers_short.MP4")
files.append("NoObs_0p1mpers_short.MP4")
files.append("NoObs_0p04mpers_short.MP4")
files.append("NoObs_0p15mpers_short.MP4")
vf1b0p1 = VideoReader(files[0])
vf1b0p04 = VideoReader(files[1])
vf1b0p15 = VideoReader(files[2])
vf0b0p1 = VideoReader(files[3])
vf0b0p04 = VideoReader(files[4])
vf0b0p15 = VideoReader(files[5])





#getting frames
file_count = len(files)
start = 1 #debug change
end = 3 #debug change
imgs = [[] for i in range(len(files))]
for i in range(len(files)):
    frame_count = 1
    cap2 = cv2.VideoCapture(files[i])
    while (cap2.isOpened):
        success, image = cap2.read()
        if frame_count >= start and frame_count < (end + 1):
            if success == False:
                continue
            newImage = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            newImage = newImage[100:700,0:1072,:]
            imgs[i].append(newImage)
            print(f"Read frame: {frame_count} from {files[i]}: {success}")
        frame_count += 1
        if frame_count == (end + 1):
            break
    cap2.release()
# for img in imgs:
#     print(len(img))
# for i in range(file_count):
#     fig = px.imshow(imgs[i][0])
#     fig.show()





#getting light, dark, and medium pixels
lights = []
meds = []
darks = []

for i in range(len(imgs)):
    img = imgs[i]
    





#calculating average number of light, med, and dark pixels and visualizing data
for i in range(file_count):
    file = files[i]
    light = lights[i]
    med = meds[i]
    dark = darks[i]
    avLight = 0
    avMed = 0
    avDark = 0
    for j in range(len(light)):
        lightCount = 0
        medCount = 0
        darkCount = 0
        for k in range(np.size(light, 1)):
            for l in range(np.size(light, 2)):
                if light[j, k, l] == 1:
                    lightCount += 1
                if med[j, k, l] == 1:
                    medCount += 1
                if dark[j, k, l] == 1:
                    darkCount += 1
        avLight += lightCount
        avMed += medCount
        avDark += darkCount
    avLight /= len(light)
    avMed /= len(med)
    avDark /= len(dark)
    totRows = np.size(light, 1)
    totCols = np.size(light, 2)
    numPixels = totRows * totCols
    plt.bar(["Light", "Medium", "Dark"], [avLight/numPixels, avMed/numPixels, avDark/numPixels], color = "blue", width = 0.4)
    plt.xlabel("Darkness of Red Pixels")
    plt.ylabel("Average Proportion of Pixels Per Frame")
    plt.title(f"Comparing Average Proportion of Light, Medium, and Dark Pixels Per Frame in {file}")
    plt.show()
    print(f"plot {i+1} finished!")