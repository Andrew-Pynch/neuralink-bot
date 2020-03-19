import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import cv2
vidcap = cv2.VideoCapture('neuralink3.mp4')
success,image = vidcap.read()
count = 0

while success:
  cv2.imwrite("jpg_extraction/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

