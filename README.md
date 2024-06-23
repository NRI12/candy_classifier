
# Candy Classifier Using YOLO

## Giới Thiệu
Candy Classifier là một hệ thống được thiết kế để phân loại tự động bốn loại kẹo khác nhau sử dụng mô hình YOLO (You Only Look Once). Mục đích của hệ thống là để nâng cao hiệu quả sàng lọc và phân loại sản phẩm trong dây chuyền sản xuất kẹo, giúp doanh nghiệp giảm thiểu lỗi sản phẩm và cải thiện chất lượng tổng thể.

## Các Loại Kẹo
- **Kẹo Loại 1**: Kẹo loại1 đạt tiêu chuẩn chất lượng cao.
    ![Kẹo Loại 1]
- **Kẹo Loại 2**: Kẹo loại 2 đạt tiêu chuẩn chất lượng cao.
    ![Kẹo Loại 2]
- **Kẹo Xấu Loại 1**: Kẹo loại 1 có vấn đề về hình thức nhưng vẫn có thể ăn được.
    ![Kẹo Xấu Loại 1]
- **Kẹo Xấu Loại 2**: Kẹo loại 2 có vấn đề về hình thức nhưng vẫn có thể ăn được.
    ![Kẹo Xấu Loại 2]
## Yêu Cầu Hệ Thống
- Python 3.8+
- PyTorch 1.7+
- OpenCV 4.5+
- YOLOv5 (có thể tải về từ [đây](https://github.com/ultralytics/yolov5))
- Data và demo có thể download ở [đây]: (https://drive.google.com/file/d/1W0mn00MG2UeS7qfwKEmS9N__MU9Io2xA/view?usp=sharing)
## Cài Đặt
Để cài đặt các thư viện cần thiết, chạy lệnh sau trong terminal:
```bash
pip install -r requirements.txt
```

## Cách Sử Dụng
1. **Chuẩn Bị Dữ Liệu**: Đảm bảo rằng bạn có thư mục `data` chứa các hình ảnh kẹo được gán nhãn.
2. **Huấn Luyện Mô Hình**: Tham khảo link colab https://colab.research.google.com/drive/1HEMoX1lYk3WRWEmVy_1cgiXFY6r6Luyn?usp=sharing
3. **Đánh Giá Mô Hình**: 
    ![Đánh Giá Mô Hình](/images/results.png)
4. **Dự Đoán**: Để thực hiện dự đoán trên những hình ảnh mới với tùy biến của bạn, sử dụng `code_tuybien.py`.
    ```bash
    python code_tuybien.py
    ```
    
## Liên Hệ
Để biết thêm thông tin, vui lòng liên hệ ctv55345@gmail.com.
