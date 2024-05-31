import random
import csv

def generate_rectangle_data(start_x, start_y, d_x, d_y, num_x, num_y):
    data = []
    for i in range(num_x):
      for j in range(num_y):
        x = start_x + i * d_x
        y = start_y + j * d_y
        f_xy = round(random.uniform(0, 100), 1)
        data.append([x, y, f_xy])
        
    s_x = start_x + d_x/2
    s_y = start_y + d_y/2
    for i in range(num_x - 1):
      for j in range(num_y - 1):
        x = s_x + i * d_x
        y = s_y + j * d_y
        f_xy = round(random.uniform(0, 100), 1)
        data.append([x, y, f_xy])
    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'f(x,y)'])
        writer.writerows(data)
    print(f"Đã lưu dữ liệu vào {filename}")