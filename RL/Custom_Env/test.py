try:
    import sys
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    print('okay')

from helper_functions import *
import neural_thread

main_thread = neural_thread.Thread(150)

left_squares = order_files_by_date(
    "/home/andrew/Github/neuralink-bot/Image_Segmentation/segmented_images/square_segmentation_crops/left_crop/", 
    ".jpg")
VESSEL_IMG = get_example_image(left_squares, 0)

distance_dict = neural_thread.Distances()

print(f"X {main_thread.x} y {main_thread.y}")
print(main_thread.distance(VESSEL_IMG, distance_dict))
show = True
COLLISION = True
while show:
    center_coordinates = (main_thread.x, main_thread.y)
    radius = 5
    color = (0, 0, 255)
    thickness = -1

    image = cv2.circle(VESSEL_IMG, center_coordinates, radius, color, thickness)
    cv2.imshow("Render", image)
    if COLLISION == True or COLLISION == False:
        # crummy code to hang at the end if we reach abrupt end for good reasons or not.
        if cv2.waitKey(500) & 0xFF == ord('q'):
            print('YES')
    else:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("NO")
