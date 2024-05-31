import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def simulate2D(data):
    plt.clf()
    x_val = np.array([float(x) for x, _, _ in data])
    y_val = np.array([float(y) for _, y, _ in data])
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(121)
    ax1.set_xlabel("Trục x")
    ax1.set_ylabel("Trục y")
    ax1.scatter(x_val, y_val)
    ax1.grid(True)
    return fig1

def draw_3d_rects(rectangles, fig):
    ax = fig.add_subplot(122, projection='3d')
    if ax in fig.get_axes():
        fig.delaxes(ax)
    ax = fig.add_subplot(122, projection='3d')
    for vertices in rectangles:
        # Các mặt của khối chữ nhật 3D dựa trên các đỉnh
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # Mặt dưới
            [vertices[1], vertices[2], vertices[6], vertices[5]],  # Mặt bên
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # Mặt trên
            [vertices[3], vertices[0], vertices[4], vertices[7]],  # Mặt bên
            [vertices[0], vertices[1], vertices[2], vertices[3]],  # Mặt đáy
            [vertices[4], vertices[5], vertices[6], vertices[7]]   # Mặt trên cùng
        ]

        # Tạo bề mặt từ các mặt của khối chữ nhật
        rect = Poly3DCollection(faces, alpha=0.5, linewidths=1, edgecolors='r')
        rect.set_facecolor('cyan')
        ax.add_collection3d(rect)

    # Đặt tên cho các trục
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Tính toán giới hạn cho các trục
    all_vertices = [vertex for rect in rectangles for vertex in rect]
    ax.set_xlim(min(v[0] for v in all_vertices), max(v[0] for v in all_vertices))
    ax.set_ylim(min(v[1] for v in all_vertices), max(v[1] for v in all_vertices))
    ax.set_zlim(0, max(v[2] for v in all_vertices) + 1)

    return fig


def simulate3D(s_x, s_y, d_x, d_y, f_val, num_x, num_y, fig):
    rectangular_prism = []
    for i in range(num_y):
        for j in range(num_x):
            vertices = []
            s_x_cur = s_x + j * d_x * 2
            s_y_cur = s_y + i * d_y * 2
            vertices.append((s_x_cur, s_y_cur, 0))
            vertices.append((s_x_cur + 2*d_x, s_y_cur, 0))
            vertices.append((s_x_cur + 2*d_x, s_y_cur + 2*d_y, 0))
            vertices.append((s_x_cur, s_y_cur + 2*d_y, 0))
            
            vertices.append((s_x_cur, s_y_cur, f_val[round(s_x_cur + d_x, 10)][round(s_y_cur + d_y, 10)]))
            vertices.append((s_x_cur + 2*d_x, s_y_cur, f_val[round(s_x_cur + d_x, 10)][round(s_y_cur + d_y, 10)]))
            vertices.append((s_x_cur + 2*d_x, s_y_cur + 2*d_y, f_val[round(s_x_cur + d_x, 10)][round(s_y_cur + d_y, 10)]))
            vertices.append((s_x_cur, s_y_cur + 2*d_y, f_val[round(s_x_cur + d_x, 10)][round(s_y_cur + d_y, 10)]))
            
            rectangular_prism.append(vertices)

    return draw_3d_rects(rectangular_prism,fig)