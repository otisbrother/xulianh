# preprocessing.py
"""
Image preprocessing: Gaussian Blur, Median Blur, Bilateral Filter, Histogram Equalization.
"""
import cv2
import numpy as np

def gaussian_blur(img, ksize=5):
    return cv2.GaussianBlur(img, (ksize, ksize), 0)

def median_blur(img, ksize=5):
    return cv2.medianBlur(img, ksize)

def bilateral_filter(img, d=9, sigmaColor=75, sigmaSpace=75):
    return cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)

def hist_equalization(img):
    if len(img.shape) == 2:
        return cv2.equalizeHist(img)
    else:
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "images/sample.jpg"
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = gaussian_blur(img_gray)
    median = median_blur(img_gray)
    bilateral = bilateral_filter(img_gray)
    hist_eq = hist_equalization(img_gray)
    cv2.imshow("Original", img_gray)
    cv2.imshow("Gaussian Blur", blur)
    cv2.imshow("Median Blur", median)
    cv2.imshow("Bilateral Filter", bilateral)
    cv2.imshow("Histogram Equalization", hist_eq)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
