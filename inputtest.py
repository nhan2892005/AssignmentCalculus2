import csv

def generate_data_from_input(num_points):
    data = []
    for _ in range(num_points):
        x = float(input("Nhập giá trị của x: "))
        y = float(input("Nhập giá trị của y: "))
        f_xy = float(input("Nhập giá trị của f(x,y): "))
        data.append([x, y, f_xy])
    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'f(x,y)'])
        writer.writerows(data)
    print(f"Đã lưu dữ liệu vào {filename}")

def get_user_input():
    while True:
        try:
            num_points = int(input("Nhập số điểm dữ liệu cần tạo: "))
            if num_points > 0:
                return num_points
            else:
                print("Số điểm dữ liệu phải lớn hơn 0. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    num_points = get_user_input()
    data = generate_data_from_input(num_points)
    save_to_csv(data, './data.csv')
