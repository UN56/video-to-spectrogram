from moviepy.editor import *

clip = VideoFileClip('sample.mp4')
clip = clip.set_fps(15)
clip.write_images_sequence(f"frames/frame%d.bmp", fps=15)



# import cv2
# vidcap = cv2.VideoCapture('testingResized.mp4')
# success,image = vidcap.read()
# count = 0
# while success:
#   cv2.imwrite("frames/frame%d.bmp" % count, image)     # save frame as JPEG file      
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1