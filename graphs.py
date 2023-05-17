import matplotlib.pyplot as plt
import numpy as np

with open("settings.txt", "r") as settings:
    str_tmp = np.array([i for i in settings.read().split("\n")])

# tmp = np.frombuffer(str_tmp, dtype=float)
tmp = [0.0134]

data_array = np.loadtxt("data.txt", dtype=int)
fig, ax = plt.subplots(figsize=(16, 10))

ax.grid(linestyle='-', linewidth=1)
ax.grid(which = 'minor')
ax.minorticks_on()

print(len(data_array))
print(str_tmp[0])

plt.title(r"Voltage from time dependence for RC chain", fontsize=15)
plt.xlabel(r"Time, s", fontsize=15)
plt.ylabel(r"Voltage, max_number", fontsize=15)

time = tmp[0]*len(data_array)
print(tmp[0])

t = np.linspace(0, time, 1000)
plt.plot(t, data_array, c='red', marker='*', markevery = 30, ms = 10, mec = "blue")

label_str = 'charging time = {max_time}'.format(max_time=t[np.argmax(t)])

plt.text(2, 1.2, label_str, fontsize=13)
plt.legend("V(t)", fontsize=15)

fig.savefig("test.png")
