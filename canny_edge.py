# canny_edge.py
"""
Canny Edge Detection: threshold tuning, blur comparison, realtime trackbar.
"""
import cv2
import numpy as np

def canny_edge(img, low=100, high=200, blur_first=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if blur_first:
        gray = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(gray, low, high)
    return edges

def canny_trackbar(img):
    def nothing(x):
        pass
    cv2.namedWindow('Canny Trackbar')
    cv2.createTrackbar('Low', 'Canny Trackbar', 50, 500, nothing)
    cv2.createTrackbar('High', 'Canny Trackbar', 150, 500, nothing)
    while True:
        low = cv2.getTrackbarPos('Low', 'Canny Trackbar')
        high = cv2.getTrackbarPos('High', 'Canny Trackbar')
        edges = canny_edge(img, low, high)
        cv2.imshow('Canny Trackbar', edges)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

def compare_blur(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges_no_blur = cv2.Canny(gray, 100, 200)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges_blur = cv2.Canny(blur, 100, 200)
    return edges_no_blur, edges_blur

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "images/sample.jpg"
    img = cv2.imread(path)
    edges = canny_edge(img)
    edges_no_blur, edges_blur = compare_blur(img)
    cv2.imshow("Canny Default", edges)
    cv2.imshow("Canny No Blur", edges_no_blur)
    cv2.imshow("Canny With Blur", edges_blur)
    print("Press any key for trackbar demo...")
    cv2.waitKey(0)
    canny_trackbar(img)
