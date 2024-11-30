# MiniProj_FloodPrediction_ML_SpHuongGraduationProj_2024


### **Class ModelAnalysis - Summary**

**Mục đích**: Hỗ trợ phân tích và đánh giá các mô hình hồi quy (regression) bằng cách:
1. **Đánh giá hiệu suất** của mô hình trên tập train và test.
2. **Trực quan hóa dự đoán**: So sánh giá trị thực tế và giá trị dự đoán.
3. **Trực quan hóa hệ số (coefficients)**: Hiển thị mức độ ảnh hưởng của các biến đầu vào.

---

### **Các Chức Năng Chính**

1. **`evaluate_metrics(y_train, y_pred_train)`**:
   - Đánh giá hiệu suất mô hình trên tập train và test.
   - Sử dụng các chỉ số phổ biến:
     - **R²**: Mức độ giải thích của mô hình với dữ liệu.
     - **MSE, RMSE**: Đo độ chênh lệch bình phương (và căn bậc 2).
     - **MAE**: Sai số trung bình tuyệt đối.
     - **MAPE**: Sai số phần trăm trung bình.
   - **Đầu ra**: Bảng chỉ số hiệu suất cho cả tập train và test.

2. **`visualize_predictions(num_samples=50)`**:
   - So sánh giá trị dự đoán và thực tế.
   - **Biểu đồ scatter**: Hiển thị mối quan hệ giữa giá trị thực và giá trị dự đoán.
   - **Biểu đồ line**: So sánh trực tiếp từng mẫu (số mẫu được chọn qua `num_samples`).

3. **`visualize_coefficients(feature_names, top_n=10)`**:
   - Trực quan hóa các hệ số của mô hình (áp dụng với các mô hình có thuộc tính `coef_` như Lasso, Ridge, Linear Regression).
   - **Biểu đồ cột**: Hiển thị mức độ ảnh hưởng của các biến đầu vào (sắp xếp theo giá trị tuyệt đối của hệ số).
   - **Đầu vào**: 
     - `feature_names`: Tên các biến đầu vào.
     - `top_n`: Số lượng biến ảnh hưởng lớn nhất.