


Báo cáo buổi 1: 
Chọn chủ đề và viết đề cương nộp các thầy cô duyệt . 
Ứng dụng các mô hình học máy cho bài toán dự báo lũ lụt

Tìm kiếm dataset bão lũ Việt Nam
Link dataset dự kiến: 
https://github.com/Mandolaro/flood-data/blob/main/Datasets.zip
Lưu dataset về để trên Drive: Datasets

<thầy hỏi dataset kiếm ở đâu thì em bảo em tìm các bài báo về Machine Learning dự đoán bão lũ. Tìm được bài báo này: - https://www.mdpi.com/2071-1050/14/19/11861  , trong bài báo này có giới thiệu bộ dataset>

Mô tả Dataset: 
….
Dataset Descriptions
1. Flood damages in Vietnam 1990 - 2022.xlsx
Nội dung: Ghi nhận thông tin về thiệt hại do lũ lụt tại Việt Nam từ năm 1990 đến 2022. Bao gồm các thông tin về số người bị ảnh hưởng, thiệt hại tài sản và các dữ liệu liên quan khác.
Định dạng: Tệp Excel.
2. Land use.csv
Nội dung: Thống kê về diện tích sử dụng đất ở Việt Nam, bao gồm các loại đất như đất nông nghiệp, đất lâm nghiệp, đất ở và đất đặc biệt. Số liệu được ghi nhận theo tỉnh/thành phố tính đến cuối năm 2018.
Định dạng: CSV.
3. Monthly humidity 15 provinces.csv
Nội dung: Dữ liệu về độ ẩm trung bình hàng tháng tại 15 tỉnh của Việt Nam, với số liệu phân chia theo năm và các tháng.
Định dạng: CSV.
4. Monthly rainfall in 15 provinces.csv
Nội dung: Thống kê lượng mưa hàng tháng tại 15 tỉnh của Việt Nam, được chia theo năm và tháng.
Định dạng: CSV.
5. Monthly temperature.csv
Nội dung: Nhiệt độ không khí trung bình hàng tháng tại 15 tỉnh của Việt Nam, có dữ liệu cho từng tháng trong các năm.
Định dạng: CSV.
6. More damages.xls
Nội dung: Chứa các thông tin bổ sung về thiệt hại do thiên tai. Tệp này có thể gặp lỗi định dạng và cần cài thêm thư viện xlrd để mở.
Định dạng: Tệp Excel.
7. Number of people divided into rural and urban region.csv
Nội dung: Thống kê dân số ở khu vực nông thôn và thành thị của các tỉnh Việt Nam từ năm 1995 đến 2020. Dữ liệu bao gồm cả tổng dân số, dân số thành thị và dân số nông thôn.
Định dạng: CSV.
8. Population density.csv
Nội dung: Mật độ dân số của các tỉnh, thành phố tại Việt Nam từ năm 2011 đến 2020. Tệp này cung cấp số liệu diện tích, dân số trung bình và mật độ dân số theo năm.
Định dạng: CSV.
9. Precipitation Monthly 1901 - 2020.csv
Nội dung: Dữ liệu về lượng mưa trung bình hàng tháng từ năm 1901 đến 2020. Tệp này gặp lỗi định dạng và có thể cần điều chỉnh để đọc được chính xác.
Định dạng: CSV.
10. Water flow in major river in Vietnam.csv
Nội dung: Dữ liệu về lưu lượng nước tại các con sông lớn ở Việt Nam từ năm 2010 đến 2020, bao gồm các giá trị cao nhất và thấp nhất theo từng năm.
Định dạng: CSV.
11. Water velocity in river.csv
Nội dung: Thống kê về vận tốc nước tại các con sông lớn ở Việt Nam. Dữ liệu bao gồm vận tốc lớn nhất và nhỏ nhất qua các năm từ 2002 đến 2020.
Định dạng: CSV.


—-----------


Dự kiến tuần sau: Tìm hiểu về Tiền xử lý data
Các file đang ở định dạng khác nhau, cần tiền xử lý đưa về 1 file chung, lọc bỏ các cột không cần thiết, …
1. Khám phá dữ liệu ban đầu
Xem qua từng tệp dữ liệu để hiểu rõ cấu trúc và nội dung.
Kiểm tra các giá trị bị thiếu (missing values) và xem xét cách xử lý: loại bỏ, thay thế hoặc dự đoán.
Xác định các cột không cần thiết hoặc không liên quan đến mục tiêu phân tích và có thể loại bỏ.
2. Xử lý dữ liệu thiếu
Loại bỏ hàng hoặc cột: Nếu cột/hàng có quá nhiều dữ liệu bị thiếu, cân nhắc loại bỏ.
Điền giá trị thiếu: Điền giá trị trung bình, trung vị hoặc giá trị phổ biến nhất, hoặc có thể sử dụng giá trị dự đoán từ các mô hình nếu dữ liệu có tính dự đoán cao.
3. Chuyển đổi dữ liệu
Chuyển đổi loại dữ liệu: Đảm bảo tất cả các cột có loại dữ liệu phù hợp. Ví dụ, các cột ngày tháng cần được chuyển về định dạng datetime, các cột số cần được chuyển về dạng numeric.
Mã hóa dữ liệu phân loại: Nếu có các biến phân loại, bạn có thể mã hóa chúng thành các giá trị số (sử dụng One-Hot Encoding hoặc Label Encoding).
…
