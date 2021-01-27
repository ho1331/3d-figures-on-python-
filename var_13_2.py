import numpy as np
import matplotlib
from matplotlib.patches import Circle, Polygon, Rectangle, Wedge
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
# print(dir(matplotlib.patches))

fig, ax = plt.subplots()
fig.set_facecolor('white')
patches = []

patches += [Rectangle((3, 0),14,10, angle=0,facecolor='grey',linestyle='solid'),\
    Rectangle((12, 0),4,6, angle=0,facecolor='black',edgecolor="#ffffff",linewidth=4),
    Polygon([[3,10],[2,10],[10,17],[18,10],[17,10]], color='blue'),
    Polygon([[15,3],[16,3]], edgecolor="#ffffff",linewidth=4),
    Circle((7.5, 6), 3, edgecolor="#ffffff",linewidth=4),
    Wedge((20, 20), 5, 180, 270, color="yellow")]

#добавляем и рисуем колекцию
ppat=PatchCollection(patches,match_original=True)
ax.add_collection(ppat)

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')
xlocs =np.linspace(0,20,21)
ax.set_xticks(xlocs, minor = False)
ax.set_yticks(xlocs, minor = False)
ax.grid(True)

plt.show()



#######################


""" rec=Rectangle((3, 0),14,10, angle=0,facecolor='grey',linestyle='solid')
ax.add_patch(rec)

rec2=Rectangle((12, 0),4,6, angle=0,facecolor='black',edgecolor="#ffffff",linewidth=4)
ax.add_patch(rec2)

polygon = Polygon([[3,10],[2,10],[10,17],[18,10],[17,10]], color='blue')
ax.add_patch(polygon)

polygon = Polygon([[15,3],[16,3]], edgecolor="#ffffff",linewidth=4)
ax.add_patch(polygon)

circle = Circle((7.5, 6), 3, edgecolor="#ffffff",linewidth=4)
ax.add_patch(circle)

wedge = Wedge((20, 20), 5, 180, 270, color="yellow")
ax.add_patch(wedge) """



# задание цвета в коллекции фигур
# 
# colors = 80*np.random.rand(len(patches))
# p.set_array(np.array(colors))
# 