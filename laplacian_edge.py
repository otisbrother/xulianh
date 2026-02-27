# laplacian_edge.py
"""
Laplacian Edge Detection: 3x3, noise sensitivity comparison.
"""
import cv2
import numpy as np

def laplacian_edge(img, ksize=3):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
    lap = cv2.convertScaleAbs(lap)
    return lap

def compare_noise(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = laplacian_edge(img)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    lap_blur = cv2.Laplacian(blur, cv2.CV_64F, ksize=3)
    lap_blur = cv2.convertScaleAbs(lap_blur)
    return lap, lap_blur

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "images/sample.jpg"
    img = cv2.imread(path)
    lap = laplacian_edge(img)
    lap, lap_blur = compare_noise(img)
    cv2.imshow("Laplacian 3x3", lap)
    cv2.imshow("Laplacian after Blur", lap_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
