from tkinter import simpledialog

def riemann_sum(f, a, b, c, d, m, n):
    dx = (b - a) / m
    dy = (d - c) / n
    riemann_sum = 0
    for i in range(m):
        for j in range(n):
            x = a + (i + 0.5) * dx
            y = c + (j + 0.5) * dy
            x = round(x, 10)
            y = round(y, 10)
            riemann_sum += f(x, y) * dx * dy
            riemann_sum = round(riemann_sum, 12)
    return riemann_sum

def prepare_data(f, a, b, c, d, m, n):
    f_v = {}
    table_data = []
    dx = (b - a) / m
    dy = (d - c) / n
    for i in range(m):
        for j in range(n):
            x = a + i * dx
            y = c + j * dy
            x = round(x, 10)
            y = round(y, 10)
            table_data.append((x, y, f(x,y)))
            f_v[x] = f_v.get(x, {})
            f_v[x][y] = f(x,y)

            x = a + (i + 0.5) * dx
            y = c + (j + 0.5) * dy
            x = round(x, 10)
            y = round(y, 10)
            table_data.append((x, y, f(x,y)))
            f_v[x] = f_v.get(x, {})
            f_v[x][y] = f(x,y)

            x = a + (i + 1) * dx
            y = c + (j + 1) * dy
            x = round(x, 10)
            y = round(y, 10)
            table_data.append((x, y, f(x,y)))
            f_v[x] = f_v.get(x, {})
            f_v[x][y] = f(x,y)

    table_data.append((a, d, f(a,d)))
    table_data.append((b, c, f(b,c)))
    f_v[a] = f_v.get(a, {})
    f_v[a][d] = f(a,d)
    f_v[b] = f_v.get(b, {})
    f_v[b][c] = f(b,c)
    return table_data, dx, dy, f_v

# Function to get user input for function
def input_function():
    expression = simpledialog.askstring("Input", "Nhập hàm số f(x, y):")
    if not expression:
        raise ValueError("Hàm số không được để trống.")
    return lambda x, y: eval(expression)

# Function to get user input for partition
def input_partition():
    m = simpledialog.askinteger("Input", "Nhập số lượng hình chữ nhật con theo trục x:")
    n = simpledialog.askinteger("Input", "Nhập số lượng hình chữ nhật con theo trục y:")
    if m is None or n is None:
        raise ValueError("Số lượng hình chữ nhật không được để trống.")
    return m, n

# Function to get user input for intervals
def input_intervals():
    interval_x = simpledialog.askstring("Input", "Nhập khoảng [a, b] trên trục x (ví dụ: 0 1):")
    interval_y = simpledialog.askstring("Input", "Nhập khoảng [c, d] trên trục y (ví dụ: 0 1):")
    
    if not interval_x or not interval_y:
        raise ValueError("Khoảng không được để trống.")
    
    a, b = map(float, interval_x.split())
    c, d = map(float, interval_y.split())
    
    return a, b, c, d