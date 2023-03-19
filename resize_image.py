import numpy as np
import cv2
from skimage.transform import seam_carve

def resize_image(image, resolution):
  """
  Seam Carving é um algoritmo que permite redimensionar uma imagem de forma não uniforme, 
  ou seja, sem distorções. Ele funciona encontrando caminhos de pixels menos relevantes 
  na imagem e removendo-os, o que permite reduzir ou aumentar o tamanho da imagem sem 
  perder informações importantes.
  """
    # Encontra a diferença de tamanho entre a imagem original e a resolução desejada
    height, width = image.shape[:2]
    new_height, new_width = resolution
    delta_height, delta_width = height - new_height, width - new_width

    # Redimensiona a imagem usando Seam Carving
    if delta_height < 0:
        image = cv2.copyMakeBorder(image, 0, abs(delta_height), 0, 0, cv2.BORDER_REPLICATE)
    elif delta_height > 0:
        image = seam_carve(image, np.ones((delta_height, delta_width), dtype=bool), "vertical")

    if delta_width < 0:
        image = cv2.copyMakeBorder(image, 0, 0, 0, abs(delta_width), cv2.BORDER_REPLICATE)
    elif delta_width > 0:
        image = seam_carve(image, np.ones((delta_height, delta_width), dtype=bool), "horizontal")

    return image
