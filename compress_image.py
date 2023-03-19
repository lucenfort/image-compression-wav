import numpy as np
import pywt
import cv2
import zlib

def compress_image(image, wavelet='haar', compression_ratio=0.5, level=3):
    # Aplica a transformada wavelet à imagem
    coeffs = pywt.wavedec2(image, wavelet, level=level)

    # Redimensiona os coeficientes de acordo com a taxa de compressão
    new_coeffs = []
    for i, c in enumerate(coeffs):
        if i == 0:
            new_c = c
        else:
            new_c = []
            for j in range(len(c)):
                new_c.append(cv2.resize(c[j], (int(c[j].shape[1] * compression_ratio), int(c[j].shape[0] * compression_ratio))))
        new_coeffs.append(new_c)

    # Reconstroi os coeficientes e a imagem comprimida
    compressed_image = pywt.waverec2(new_coeffs, wavelet)

    # Comprime a imagem usando zlib
    compressed_bytes = zlib.compress(np.uint8(compressed_image))

    return compressed_bytes
