import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Đọc dữ liệu
flood_data = pd.read_csv('/path/to/your/flood.csv')

# 1. Phân tích tổng quan về dữ liệu
def overview_analysis(df):
    print("1. TỔNG QUAN VỀ DỮ LIỆU")
    print("\nThông tin cơ bản:")
    print(df.info())
    
    print("\nXem 5 dòng đầu tiên:")
    print(df.head())
    
    print("\nThống kê mô tả:")
    print(df.describe())
    
    # Kiểm tra giá trị null
    null_counts = df.isnull().sum()
    print("\nSố lượng giá trị null trong mỗi cột:")
    print(null_counts)

# 2. Phân tích phân phối của các biến
def distribution_analysis(df):
    print("\n2. PHÂN TÍCH PHÂN PHỐI")
    
    # Histogram cho biến mục tiêu
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='FloodProbability', bins=30, kde=True)
    plt.title('Phân phối của xác suất lũ lụt')
    plt.xlabel('Xác suất lũ lụt')
    plt.ylabel('Số lượng')
    plt.show()
    
    # Box plot cho tất cả các biến số
    plt.figure(figsize=(15, 8))
    df.boxplot()
    plt.xticks(rotation=90)
    plt.title('Boxplot của tất cả các biến')
    plt.tight_layout()
    plt.show()
    
    # Kiểm tra độ nghiêng và độ nhọn
    skewness = df.skew()
    kurtosis = df.kurtosis()
    print("\nĐộ nghiêng của các biến:")
    print(skewness)
    print("\nĐộ nhọn của các biến:")
    print(kurtosis)

# 3. Phân tích tương quan
def correlation_analysis(df):
    print("\n3. PHÂN TÍCH TƯƠNG QUAN")
    
    # Ma trận tương quan
    correlation_matrix = df.corr()
    
    # Vẽ heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Ma trận tương quan giữa các biến')
    plt.tight_layout()
    plt.show()
    
    # Top 5 biến có tương quan mạnh nhất với FloodProbability
    flood_corr = correlation_matrix['FloodProbability'].abs().sort_values(ascending=False)
    print("\nTop 5 biến có tương quan mạnh nhất với FloodProbability:")
    print(flood_corr.head())

# 4. Phân tích mối quan hệ giữa các biến
def relationship_analysis(df):
    print("\n4. PHÂN TÍCH MỐI QUAN HỆ")
    
    # Scatter plots cho top 5 biến có tương quan cao nhất với FloodProbability
    correlation_matrix = df.corr()
    top_5_features = correlation_matrix['FloodProbability'].abs().sort_values(ascending=False)[1:6].index
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()
    
    for idx, feature in enumerate(top_5_features):
        sns.scatterplot(data=df, x=feature, y='FloodProbability', ax=axes[idx])
        axes[idx].set_title(f'{feature} vs FloodProbability')
    
    plt.tight_layout()
    plt.show()
    
    # Pair plot cho các biến quan trọng
    sns.pairplot(df[list(top_5_features) + ['FloodProbability']])
    plt.show()

# 5. Phân tích thống kê nâng cao
def advanced_statistics(df):
    print("\n5. PHÂN TÍCH THỐNG KÊ NÂNG CAO")
    
    # Kiểm tra tính chuẩn của biến mục tiêu
    statistic, p_value = stats.normaltest(df['FloodProbability'])
    print("\nKiểm định tính chuẩn cho FloodProbability:")
    print(f"Statistic: {statistic}")
    print(f"P-value: {p_value}")
    
    # Tính IQR và xác định outliers
    Q1 = df['FloodProbability'].quantile(0.25)
    Q3 = df['FloodProbability'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df['FloodProbability'] < (Q1 - 1.5 * IQR)) | 
                  (df['FloodProbability'] > (Q3 + 1.5 * IQR))]
    
    print(f"\nSố lượng outliers trong FloodProbability: {len(outliers)}")

# Thực hiện tất cả các phân tích
def run_full_eda(df):
    overview_analysis(df)
    distribution_analysis(df)
    correlation_analysis(df)
    relationship_analysis(df)
    advanced_statistics(df)

# Chạy phân tích EDA
if __name__ == "__main__":
    run_full_eda(flood_data)