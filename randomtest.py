import random
import csv

def generate_random_data(num_points):
    data = []
    for _ in range(num_points):
        x = round(random.uniform(1, 5), 1)
        y = round(random.uniform(0.5, 5.0), 1)
        f_xy = round(random.uniform(4.0, 12.5), 1)
        data.append([x, y, f_xy])
    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'f(x,y)'])
        writer.writerows(data)
    print(f"Đã lưu dữ liệu vào {filename}")

if __name__ == "__main__":
    num_points = 16  # Số điểm dữ liệu cần tạo
    data = generate_random_data(num_points)
    save_to_csv(data, './data.csv')