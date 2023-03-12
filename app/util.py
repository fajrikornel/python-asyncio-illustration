import cv2
import numpy as np
from . import app


def convert_to_opencv_image(img):
    img_np = np.fromstring(img, np.uint8)
    return cv2.imdecode(img_np, -1)


def concatenate_image(image_list):
    min_width = min(img.shape[1] for img in image_list)

    resized_image_list = [cv2.resize(
        img,
        (min_width, int(img.shape[0] * min_width / img.shape[1]))) for img in image_list]

    concat_img = cv2.vconcat(resized_image_list)
    return concat_img


def concatenate_and_save_image(image_filename, image_list):
    image_list = list(map(convert_to_opencv_image, image_list))
    image_concatenated = concatenate_image(image_list)

    app.logger.info(f"Saving image to {image_filename}")
    cv2.imwrite(image_filename, image_concatenated)
