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


### Results 
Linear Regression: 
```
Evaluating Model:
EVALUATE METRICS ON THE TRAIN SET
Coefficient of determination R2: 0.8448974319194739
Mean Squared Error MSE: 0.00040409012928374974
Root Mean Squared Error RMSE: 0.020101993166941175
Mean Absolute Error MAE: 0.01582127813960289
Mean Absolute Percentage Error MAPE% 3.19% 

EVALUATE METRICS ON THE TEST SET
Coefficient of determination R2: 0.8450696030886053
Mean Squared Error MSE: 0.00040278964955467927
Root Mean Squared Error RMSE: 0.02006962006503061
Mean Absolute Error MAE: 0.015787927418085844
Mean Absolute Percentage Error MAPE% 3.19%
```


KNN
```
Train RMSE: 1.2518130869377174e-09
Test RMSE: 0.031842760655068955
Train R² Score: 0.9999999999999994
Test R² Score: 0.6099863954320361
```


Bảng đã được cập nhật để chỉ hiển thị 4 chữ số sau dấu phẩy:

### Bảng so sánh hiệu suất các mô hình:

| **Mô hình**           | **R² (Train)** | **R² (Test)** | **RMSE (Train)** | **RMSE (Test)** | **MAE (Test)** | **MAPE (Test)** | **Time Training (s)** |
|------------------------|----------------|---------------|------------------|-----------------|----------------|-----------------|------------------------|
| Linear Regression      | 0.8449         | 0.8451        | 0.0201           | 0.0201          | 0.0158         | 3.19%           | 60.00                  |
| Ridge Regression       | 0.8449         | 0.8451        | 0.0201           | 0.0201          | 0.0158         | 3.19%           | 60.00                  |
| Lasso Regression       | 0.0000         | -0.0000       | 0.0510           | 0.0510          | 0.0409         | 8.26%           | 60.00                  |
| KNN                    | 0.9999         | 0.6100        | 0.0000           | 0.0318          | -              | -               | 1800.00                |

---
