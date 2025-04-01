import matplotlib.pyplot as plt
import numpy as np
import functools
from matplotlib.patches import ConnectionPatch
import matplotlib.animation as animation
# make figure and assign axis objects
fig, axs = plt.subplots(4, 3, figsize=(14, 8))
print(fig)
print(axs)
ax0 = axs[0,0]
ax1 = axs[0,1]
ax2 = axs[0,2]
# fig.subplots_adjust(wspace=0)

# pie chart parameters
overall_ratios = [.27, .56, .17]
labels = ['Approve', 'Disapprove', 'Undecided']
explode = [0.1, 0, 0]
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%.2f%%', startangle=angle,
                     labels=labels, explode=explode)
print(wedges)
# bar chart parameters
age_ratios = [.33, .54, .07, .06]
age_labels = ['Under 35', '35-49', '50-65', 'Over 65']
bottom = 1
width = .2

# Adding from the top matches the legend.
print(*zip(age_ratios, age_labels))
print(reversed([*zip(age_ratios, age_labels)]))
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

ax2.set_title('Age of approvers')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
print(center, r)
bar_height = sum(age_ratios)

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax1.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
print(t)
s = 1 + np.sin(2 * np.pi * t)
print(s)
ax0.plot(t, s)

ax0.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax0.grid()

t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2

# fig, axs = plt.subplots(3, 1, sharex=True)
# Remove vertical space between Axes
# fig.subplots_adjust(hspace=0)

# Plot each graph, and manually set the y tick values
axs[1,0].plot(t, s1)
axs[1,0].set_yticks(np.arange(-0.9, 1.0, 0.4))
axs[1,0].set_ylim(-1, 1)

axs[2,0].plot(t, s2)
axs[2,0].set_yticks(np.arange(0.1, 1.0, 0.2))
axs[2,0].set_ylim(0, 1)
axs[2,0].sharex(axs[1,0])

axs[3,0].plot(t, s3)
axs[3,0].set_yticks(np.arange(-0.9, 1.0, 0.4))
axs[3,0].set_ylim(-1, 1)
axs[3,0].sharex(axs[1,0])

gs = axs[1, 1].get_gridspec()
print(axs[1:3, 1:])
for ax in axs[1:3, 1:].flatten():
    ax.remove()
axbig = fig.add_subplot(gs[1:3, 1:], projection='3d')
# axbig.annotate('Big Axes \nGridSpec[1:, -1]', (0.1, 0.5),
#                xycoords='axes fraction', va='center')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = axbig.plot_surface(X, Y, Z, rstride=1, cstride=1,
                       linewidth=0, antialiased=False)
axbig.set_zlim(-1, 1)

gs = axs[3, 1].get_gridspec()
for ax in axs[3:, 1:].flatten():
    ax.remove()
axbig2 = fig.add_subplot(gs[3:, 1:])

# Setting up a random number generator with a fixed state for reproducibility.
rng = np.random.default_rng(seed=19680801)
# print(rng)
# Fixing bin edges.
HIST_BINS = np.linspace(-4, 4, 100)
# print(HIST_BINS)
# Histogram our data with numpy.
data = rng.standard_normal(1000)
# n, _ = np.histogram(data, HIST_BINS)
# print(data)
# print(n)
# print(sum(n))
def animate(frame_number, bar_container):
    # Simulate new data coming in.
    data = rng.standard_normal(1000)
    n, _ = np.histogram(data, HIST_BINS)
    # print(*zip(n, bar_container.patches))
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)

    return bar_container.patches

# Output generated via `matplotlib.animation.Animation.to_jshtml`.
_, _, bar_container = axbig2.hist(data, HIST_BINS, lw=1,
                              ec="yellow", fc="green", alpha=1)
# print(bar_container)
axbig2.set_ylim(top=55)  # set safe limit to ensure that all data is visible.

anim = functools.partial(animate, bar_container=bar_container)
ani = animation.FuncAnimation(fig, anim, 50, repeat=True, blit=True)

fig.subplots_adjust(hspace=0)
# fig.tight_layout()
fig.savefig("test.png")

plt.show()