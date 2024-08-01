import matplotlib as mpl;
import matplotlib.pyplot as plt;
mpl.style.use('ggplot');
x1= [1, 3];
y1= [2, 4];
# Formato orientado a objetos
fig, ax = plt.subplots();
ax.plot(x1, y1);