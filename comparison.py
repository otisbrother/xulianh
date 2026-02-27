# comparison.py
"""
Compare Sobel, Laplacian, and Canny edge detection algorithms.
Measure processing time and noise sensitivity.
"""
import cv2
import numpy as np
import time
from sobel_edge import sobel_edges
from laplacian_edge import laplacian_edge
from canny_edge import canny_edge

def measure_time(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start

def compare_algorithms(img):
    results = {}
    results['Sobel'], t_sobel = measure_time(lambda x: sobel_edges(x)[2], img)
    results['Laplacian'], t_lap = measure_time(laplacian_edge, img)
    results['Canny'], t_canny = measure_time(canny_edge, img)
    times = {'Sobel': t_sobel, 'Laplacian': t_lap, 'Canny': t_canny}
    return results, times

def compare_noise(img):
    noisy = img + np.random.normal(0, 25, img.shape).astype(np.uint8)
    results, _ = compare_algorithms(noisy)
    return results

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "images/sample.jpg"
    img = cv2.imread(path)
    results, times = compare_algorithms(img)
    print("Processing times (seconds):", times)
    for name, res in results.items():
        cv2.imshow(f"{name} Edge", res)
    noisy_results = compare_noise(img)
    for name, res in noisy_results.items():
        cv2.imshow(f"{name} Edge (Noisy)", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
