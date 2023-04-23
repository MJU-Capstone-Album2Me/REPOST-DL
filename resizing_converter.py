import cv2
import os
import pyheif
from PIL import Image
import numpy as np

### image resizing and preserving resolution on designated directory
directory_path = '/home/jeongseok/capstone/datasets/myalbum'

if not os.path.exists(directory_path+"_resize"):
    os.makedirs(directory_path+"_resize")

file_names = os.listdir(directory_path)

# resizing and save as ~
for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    file_name_exceptformat = file_name.split(".")[0]
    print(file_name_exceptformat)
    print(file_path)
    
    # check if the file is a heic file
    if file_name.endswith('.heic') or file_name.endswith('.HEIC'):
        # read the heic file using pyheif
        heif_file = pyheif.read(file_path)
        # convert the heic file to a PIL image
        pil_image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
        )
        # convert the PIL image to a cv2 image
        image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    else:
        # read the image using cv2
        image = cv2.imread(file_path)
    
    height, width, channels = image.shape
    print("file_name, height, width:", file_name, height, width)
    aspect_ratio = int(height / width)

    new_width, new_height = 256, 256
    resized_image = cv2.resize(image, (new_width, new_height))

    # save the resized image
    new_file_path = os.path.join(directory_path+"_resize", f"resize_{file_name_exceptformat}.png")
    cv2.imwrite(new_file_path, resized_image)

