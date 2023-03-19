import os
import cv2
import numpy as np
import pywt

def resize_image(img, max_size):
    h, w = img.shape[:2]
    if h <= max_size and w <= max_size:
        return img
    scale = max_size / max(h, w)
    new_h, new_w = int(h * scale), int(w * scale)
    return cv2.resize(img, (new_w, new_h))

def compress_image(img, wavelet='haar', level=1, ratio=0.5):
    coeffs = pywt.wavedec2(img, wavelet, level=level)
    threshold = ratio * max([np.max(np.abs(c)) for c in coeffs])
    thresholded_coeffs = [pywt.threshold(c, threshold) for c in coeffs]
    return pywt.waverec2(thresholded_coeffs, wavelet)

def process_image_file(input_path, output_path, max_size=1024, wavelet='haar', level=1, ratio=0.5):
    img = cv2.imread(input_path)
    resized_img = resize_image(img, max_size)
    compressed_img = compress_image(resized_img, wavelet=wavelet, level=level, ratio=ratio)
    cv2.imwrite(output_path, compressed_img)

def process_image_directory(input_dir, output_dir, max_size=1024, wavelet='haar', level=1, ratio=0.5):
    for root, _, files in os.walk(input_dir):
        for file in files:
            input_path = os.path.join(root, file)
            rel_path = os.path.relpath(input_path, input_dir)
            output_path = os.path.join(output_dir, rel_path)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            process_image_file(input_path, output_path, max_size=max_size, wavelet=wavelet, level=level, ratio=ratio)
