# OpenCV Edge Detection Project

## Giới thiệu
Dự án này trình bày các kỹ thuật xử lý ảnh cơ bản và phát hiện cạnh (Edge Detection) bằng OpenCV, gồm các thuật toán Sobel, Laplacian, Canny. Dự án phù hợp để học nền tảng Computer Vision, làm portfolio, không cần GPU, không cần train model.

## Cấu trúc thư mục
```
opencv-edge-detection/
├── images/
├── basic_processing.py
├── preprocessing.py
├── sobel_edge.py
├── laplacian_edge.py
├── canny_edge.py
├── realtime_edge.py
├── comparison.py
└── README.md
```

## Nội dung chính
- **Xử lý ảnh cơ bản:** Đọc, resize, chuyển grayscale, hiển thị nhiều cửa sổ.
- **Tiền xử lý:** Gaussian Blur, Median Blur, Bilateral Filter, Histogram Equalization.
- **Phát hiện cạnh:**
  - Sobel (X, Y, combined, so sánh kernel)
  - Laplacian (3x3, so sánh noise)
  - Canny (trackbar realtime, so sánh blur)
- **Realtime webcam:** Canny với trackbar, hiển thị FPS.
- **So sánh & phân tích:** Đo thời gian, so sánh độ nhiễu, phân tích ưu/nhược điểm.

## So sánh thuật toán
| Thuật toán  | Ưu điểm                | Nhược điểm                | Khi nào dùng?           |
|------------|------------------------|---------------------------|-------------------------|
| Sobel      | Đơn giản, nhanh        | Nhạy với nhiễu            | Phát hiện cạnh cơ bản   |
| Laplacian  | Nhạy cạnh mạnh         | Rất nhạy với nhiễu        | Khi cần phát hiện cạnh rõ|
| Canny      | Hiệu quả, ít nhiễu     | Tham số cần tinh chỉnh    | Ứng dụng thực tế, robust|

## Kết luận
- Nên dùng **Canny** cho ứng dụng thực tế.
- **Sobel/Laplacian** phù hợp minh họa lý thuyết, tiền xử lý.

## Yêu cầu phần cứng
- Chỉ cần CPU, không cần GPU.
- Không train model, không tốn ổ cứng.


