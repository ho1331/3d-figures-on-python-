from tkinter import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle


# создание окна
root = Tk()
root.title('Var_13_3')
f_top = Frame(root,relief=RIDGE,borderwidth=6)
f_bottom = Frame(root,relief=RAISED,borderwidth=4)


#cilindre
def data_for_cylinder_along_z(center_x,center_y,radius,height_z):
    z = np.linspace(0, height_z, 15)
    theta = np.linspace(0, 2*np.pi, 15)
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

bar1 = FigureCanvasTkAgg(fig_1, master=f_top)
bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)


#поверхня
fig_2 = plt.figure()
ax2=Axes3D(fig_2, xlim=(-5, 5), ylim=(-5, 5), zlim=(-5,5))
bar2 = FigureCanvasTkAgg(fig_2, master=f_top)
bar2.get_tk_widget().pack(side=LEFT, fill=BOTH)
f_top.pack()
x1 = np.linspace(-np.pi,np.pi,50)
y1 = np.linspace(-np.pi,np.pi,50)
X1,Y1=np.meshgrid(x1,y1)
Z1 = (X1**2 + Y1**2)*np.sin(X1)*np.sin(Y1)
ax2.plot_surface(X1,Y1,Z1,rstride=1,cstride=1,cmap=mpl.cm.hsv, alpha=0.8)

# парабалоїд
fig_3 = plt.figure()
ax_3=Axes3D(fig_3, xlim=(-1, 1), ylim=(-1, 1), zlim=(0,3))
bar3 = FigureCanvasTkAgg(fig_3, master=f_bottom)
bar3.get_tk_widget().pack(side=LEFT, fill=BOTH)
f_bottom.pack()
x2 = np.linspace(-1,1,30)
y2 = np.linspace(-1,1,30)
X2,Y2=np.meshgrid(x2,y2)
Z2 = X2**2 + Y2**2
ax_3.plot_surface(X2,Y2,Z2,rstride=1,cstride=1,cmap=mpl.cm.hsv, alpha=0.8)


# добавление кнопки «Выход»
def m_quit():
    root.quit()    # stops mainloop
    root.destroy() # используется в Windows

button = Button(master=root, text=' Выход', command=m_quit)
button.pack(side=LEFT)

ax.mouse_init() # подключение событий мыши
root.mainloop()
