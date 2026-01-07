import cv2
import os
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import numpy as np
import webcolors


def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]


# Path to the folder containing images
image_folder_path = r'C:\Users\Lenovo\Desktop\M\p'

# Get a list of all PNG images
image_files = [f for f in os.listdir(image_folder_path) if f.endswith('.png')]

# Loop through each image
for image_file in image_files:
    # Construct full image path
    image_path = os.path.join(image_folder_path, image_file)

    # Read the image
    img = cv2.imread(image_path)

    # Calculate average color (BGR)
    avg_color = np.mean(img, axis=(0, 1)).astype(int)

    # Convert BGR to RGB
    avg_color_rgb = avg_color[::-1]

    # Get closest CSS3 color name
    color_name = closest_color(avg_color_rgb)

    # Display the image
    cv2.imshow('Image', img)

    # Print result
    print(
        f"Average color of {image_file}: "
        f"{to_hex(avg_color_rgb * (1/255))} "
        f"closest: {color_name}"
    )

    # Wait before next image
    cv2.waitKey(600)

# Close all OpenCV windows
cv2.destroyAllWindows()
