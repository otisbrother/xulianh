# sobel_edge.py
"""
Sobel Edge Detection: X, Y, combined, kernel size comparison.
"""
import cv2
import numpy as np

def sobel_edges(img, ksize=3):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    return sobelx, sobely, combined

def compare_kernels(img, kernels=[3, 5, 7]):
    results = {}
    for k in kernels:
        _, _, combined = sobel_edges(img, ksize=k)
        results[k] = combined
    return results

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "images/sample.jpg"
    img = cv2.imread(path)
    sobelx, sobely, combined = sobel_edges(img)
    kernels = compare_kernels(img)
    cv2.imshow("Sobel X", sobelx)
    cv2.imshow("Sobel Y", sobely)
    cv2.imshow("Sobel Combined", combined)
    for k, res in kernels.items():
        cv2.imshow(f"Sobel Combined k={k}", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
