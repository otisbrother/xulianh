# realtime_edge.py
"""
Realtime Canny Edge Detection on webcam with trackbar and FPS display.
"""
import cv2
import time

def nothing(x):
    pass

def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Realtime Canny')
    cv2.createTrackbar('Low', 'Realtime Canny', 50, 500, nothing)
    cv2.createTrackbar('High', 'Realtime Canny', 150, 500, nothing)
    prev_time = time.perf_counter()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        low = cv2.getTrackbarPos('Low', 'Realtime Canny')
        high = cv2.getTrackbarPos('High', 'Realtime Canny')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(blur, low, high)
        curr_time = time.perf_counter()
        fps = 1.0 / (curr_time - prev_time)
        prev_time = curr_time
        cv2.putText(edges, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
        cv2.imshow('Realtime Canny', edges)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
