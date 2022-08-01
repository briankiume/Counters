import numpy as np

n = 5
a = [3, 4, 4, 6, 1, 4, 4, 6, 2, 1]
ini = np.zeros([len(a), n], int)
new_ini = []
for i, num in enumerate(a):
    if num <= n:
        ini[i][num - 1] += 1
        new_ini = ini.sum(axis=0)
    else:
        ini[i] = max(new_ini)
        new_ini = ini[i]
        ini[:i] = np.zeros([len(a[:i]), n], int)

print(new_ini)
