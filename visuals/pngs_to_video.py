# Turn directory of pngs into a mp4 video file.
import os
import sys
import cv2

directory = './frames/'
images = os.listdir(directory)

video_dir = './video/'
video_name = video_dir+'video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video = cv2.VideoWriter(video_name, fourcc, 21.0, (1280, 720))

frameCount = 1
for i in range(len(images)):
    name = directory+'{num:0{width}}'.format(num=frameCount, width=6)+'.png'
    if (os.path.isfile(name)):
        video.write(cv2.imread(name))
        frameCount += 1
        if (frameCount % 100 == 0):
            print('Frame: ', frameCount)

        # clean up: remove pngs
        os.remove(name)

cv2.destroyAllWindows()
video.release()
