import cv2
import numpy as np
import os

caminho_diretorio = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(caminho_diretorio, "rosto.jpg")
output_img = os.path.join(caminho_diretorio, "rosto_output.jpg")


def pencil_sketch(image_path, output_path):
    # Check if the image was loaded successfully
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return  # Exit the function if image loading failed

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted_gray_image = cv2.bitwise_not(gray_image)

    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    cv2.imwrite(output_path, pencil_sketch_image)

    cv2.imshow("Pencil Sketch", pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


input_image_path = arquivo
output_image_path = output_img
pencil_sketch(input_image_path, output_image_path)
