import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sys, os

from simulate import simulate2D, simulate3D
from ReimannSumofF import riemann_sum, input_function, input_intervals, input_partition, prepare_data
from ReimannSumfromTable import checkRectangle, read_data_from_csv
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def exit_tkinter():
    root.destroy()
def calculate_riemann_sum():
    global canvas, canvas_widget
    try:
        f = input_function()
        a, b, c, d = input_intervals()
        m, n = input_partition()
        
        result = riemann_sum(f, a, b, c, d, m, n)
        messagebox.showinfo("Result", f"Tổng Riemann của hàm số f trên hình chữ nhật R là: {result}")
        
        t_data, dx, dy, f_val = prepare_data(f,a,b,c,d,m,n)

        fig1 = simulate2D(t_data)
        simulate3D(a, c, dx/2, dy/2, f_val, m, n, fig1)

        canvas = FigureCanvasTkAgg(fig1, master=tab1)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    except Exception as e:
        messagebox.showerror("Error", f"Đã xảy ra lỗi: {e}")

def calculate_riemann_sum_from_table():
    try:
        data, func_val = read_data_from_csv()
        arr_x = sorted(set(np.array([x for x, _, _ in data])))
        arr_y = sorted(set(np.array([y for _, y, _ in data])))
        d_x = np.diff(arr_x).min()
        d_y = np.diff(arr_y).min()
        ReimannSum = False
        if d_x and d_y:
            ReimannSum = checkRectangle(arr_x[0], arr_y[0], d_x, d_y, func_val, len(arr_x)//2 + 1, len(arr_y)//2 + 1)
            if ReimannSum:
                messagebox.showinfo("Kết quả", f"Tổng Riemann của hàm số f trên hình chữ nhật R là: {round(ReimannSum, 4)}")
                fig2 = simulate2D(data)
                simulate3D(arr_x[0], arr_y[0], d_x, d_y, func_val, len(arr_x)//2, len(arr_y)//2, fig2)

                canvas = FigureCanvasTkAgg(fig2, master=tab2)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            else:
                messagebox.showerror("Error", "Không thể dùng tổng Riemann trung tâm") 
                fig2 = simulate2D(data)  
                canvas = FigureCanvasTkAgg(fig2, master=tab2)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)   
    except Exception as e:
        messagebox.showerror("Error", f"Đã xảy ra lỗi: {e}")

def Create_data():
    from rectangleTest import generate_rectangle_data, save_to_csv
    import random
    start_x = random.randint(-10, 10)
    start_y = random.randint(-10, 10)
    d_x = random.randint(1, 5)
    d_y = random.randint(1, 5)
    num_x = random.randint(1, 10)
    num_y = random.randint(1, 10)
    data = generate_rectangle_data(start_x, start_y, d_x, d_y, num_x, num_y)
    save_to_csv(data, 'data.csv')

def Create_random_data():
    import random
    from randomtest import generate_random_data, save_to_csv
    num_points = random.randint(5, 100)
    data = generate_random_data(num_points)
    save_to_csv(data, './data.csv')

# Create tkinter window
root = tk.Tk()
root.title("Bài tập lớn Giải tích 2 - Tổng Reimann Trung tâm")

# Load logo image
logo_image = tk.PhotoImage(file="image.png")
logo_image = logo_image.subsample(2, 2) 
# Insert logo
logo_label = tk.Label(image=logo_image)
logo_label.pack(pady=20) 
logo_label.image = logo_image 

tab_control = ttk.Notebook(root)
tab_control.pack(fill=tk.BOTH, expand=True)

# First tab
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tính tổng Riemann (hàm số)")
# Button of tab1
btn_calculate1 = tk.Button(tab1, text="Tính", command=calculate_riemann_sum)
btn_calculate1.pack(pady=20)

# Second tab
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tính tổng Riemann (bảng số)")
# Button of tab2
btn_calculate2 = tk.Button(tab2, text="Lấy dữ liệu", command=calculate_riemann_sum_from_table)
btn_calculate2.pack(pady=20)

btn_calculate3 = tk.Button(tab2, text="Tạo dữ liệu", command=Create_data)
btn_calculate3.pack(pady=20)

btn_calculate4 = tk.Button(tab2, text="Tạo dữ liệu ngẫu nhiên", command=Create_random_data)
btn_calculate4.pack(pady=20)

exit_button = tk.Button(root, text="Thoát", command=exit_tkinter).pack()
restart_button = tk.Button(root, text="Tính tiếp", command=restart).pack()

root.protocol("WM_DELETE_WINDOW", root.destroy)
tab_control.pack(expand=1, fill="both")
root.mainloop()
