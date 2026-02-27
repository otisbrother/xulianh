# basic_processing.py
"""
Basic image processing: load, resize, grayscale, display multiple windows.
"""
import cv2
import numpy as np

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")
    return img

def resize_image(img, width=None, height=None):
    h, w = img.shape[:2]
    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

def to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def show_images(images, titles=None):
    for i, img in enumerate(images):
        title = titles[i] if titles and i < len(titles) else f"Image {i+1}"
        cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "images/sample.jpg"
    img = load_image(path)
    img_resized = resize_image(img, width=400)
    img_gray = to_grayscale(img_resized)
    show_images([img_resized, img_gray], ["Resized", "Grayscale"])
