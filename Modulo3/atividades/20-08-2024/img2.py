import cv2
import numpy as np
import os

caminho_diretorio = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(caminho_diretorio, "Foto_Original.jpg")
output_img = os.path.join(caminho_diretorio, "Foto_Original_output_2.jpg")


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

    # Increase the scale for darker lines
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=128.0)

    # Apply a sharpening filter to enhance the edges
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(pencil_sketch_image, -1, kernel)

    cv2.imwrite(output_path, sharpened_image)

    cv2.imshow("Pencil Sketch", sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


input_image_path = arquivo
output_image_path = output_img
pencil_sketch(input_image_path, output_image_path)
