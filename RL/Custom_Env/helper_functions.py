import os
import sys
import glob
import math

import cv2
import numpy as np


###################
# HELPER FUNCTIONS
###################
def order_files_by_date(path_to_folder, file_type):
    files = glob.glob("%s*%s" % (path_to_folder, file_type))
    files.sort(key=os.path.getmtime)
    return files


def get_example_image(image_files, index):
    """Extract an image from a list of file names by index
    
    Arguments:
        image_files {[list]} -- [list of image files]
        index {[int]} -- [image in the list of files we would like to access]
    """
    img = cv2.imread(image_files[index])
    # Threshold all pixels to be entirelly white or black (for some reason some of the pixels were 244 / 1)
    img[img > 150] = 255
    img[img < 150] = 0
    print(f"Shape: {img.shape}, Size: {img.size}, Unique: {np.unique(img)}")
    return img


def euc_dist(p1, p2):
    """Return the euclidean distance between two poitns
    
    Arguments:
        p1 {[x, y]} -- [point containing [x, y] coordinates in a list]
        p2 {[x, y]} -- [point containing [x, y] coordinates in a list]
    
    Returns:
        [int] -- [The euclidean distance between two points]
    """
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def black_pixel_bool(vessel_img, i, j):
    """Return boolean indicating if a pixel in vessel_img at the ith row and jth column is black

    Arguments:
        vessel_img {[nparray]} -- [input image of segmented vasculature]
        i {[type]} -- [row]
        j {[type]} -- [column]
    
    Returns:
        [bool] -- [black = true, white = false]
    """
    if (
        vessel_img[i][j][0] == 0
        and vessel_img[i][j][1] == 0
        and vessel_img[i][j][2] == 0
    ):
        return True
    else:
        return False
