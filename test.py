from tkinter import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle


# создание окна и фрейма
# root = Tk()
# root.title('Var_13_3')
# f_top = Frame(root,relief=RIDGE,borderwidth=6)
# f_bottom = Frame(root,relief=RAISED,borderwidth=4)


#cilindre
def data_for_cylinder_along_z(center_x,center_y,radius,height_z):
    z = np.linspace(0, height_z, 15)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid,y_grid,z_grid

fig_1 = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig_1)
Xc,Yc,Zc = data_for_cylinder_along_z(1,1,3,5)
ax.plot_surface(Xc, Yc, Zc, alpha=0.5) #alpha - прозрачность
ax.scatter(Xc,Yc,Zc, color='red')

#верх\низ
top = Circle((1, 1), 3, alpha=0.5)
ax.add_patch(top)
art3d.pathpatch_2d_to_3d(top, 5)

floor = Circle((1, 1), 3, alpha=0.5)
ax.add_patch(floor)
art3d.pathpatch_2d_to_3d(floor, 0)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()