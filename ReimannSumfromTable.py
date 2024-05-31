import csv

def checkDelta(arr):
  delta = arr[1] - arr[0]
  for i in range(len(arr) - 2):
    if arr[i + 2] - arr[i + 1] != delta:
      print("Không thể dùng tổng Reimann trung tâm")
      return None
  return delta

def checkRectangle(start_x, start_y, del_x, del_y, f_val, num_x, num_y):
  sum = 0
  for i in range(num_x):
      for j in range(num_y):
        x = start_x + i * del_x * 2
        y = start_y + j * del_y * 2
        if x not in f_val or y not in f_val[x]:
          print("Không thể dùng tổng Reimann trung tâm")
          return False
  start_x = start_x + del_x
  start_y = start_y + del_y
  for i in range(num_x - 1):
     for j in range(num_y - 1):
        x = start_x + i * del_x * 2
        y = start_y + j * del_y * 2
        if x not in f_val or y not in f_val[x]:
          print("Không thể dùng tổng Reimann trung tâm")
          return False
        else:
          sum = sum + f_val[x][y]

  return sum

def read_data_from_csv():
    data = []
    func_val = {}
    # Read data
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            x, y, value = float(row[0].strip()), float(row[1].strip()), float(row[2].strip())
            data.append((x, y, value))

            if x not in func_val:
                func_val[x] = {}
            func_val[x][y] = value
    return data, func_val