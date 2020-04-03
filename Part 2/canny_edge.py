import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_img(image):
    original_image = image 
    # grayscale that image yo!
    processed_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Canny edge detection 
    processed_img = cv2.Canny(processed_img, threshold1 = 75, threshold2=200)
    processed_img = processed_img.astype(np.float32)
    processed_img /= 255.0
    # confirm the normalization
    # print('Min: %.3f, Max: %.3f' % (processed_img.min(), processed_img.max()))
    return processed_img


def main():
    last_time = time.time()
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0,40,750,250)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
