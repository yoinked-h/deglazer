import cv2
import numpy as np
try:
    from cv2.ximgproc import guidedFilter # type: ignore
except ImportError:
    raise ImportError('Please install opencv-contrib-python package with: pip install opencv-contrib-python')

def clean(image: np.ndarray):
    y = image.copy()
    for _ in range(64):
        y = cv2.bilateralFilter(y, 5, 8, 8)
    for _ in range(4):
        y = guidedFilter(image, y, 4, 16)
    return y
