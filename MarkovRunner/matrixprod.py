import numpy as np
P = 0.6

matrix = np.array(
    [[0, 1- P, P, 0, 0],
    [P, 0, 0, 0, 0],
    [1- P, 0, 0, 0, 0],
    [0, P, 0, 1, 0],
    [0, 0, 1-P, 0, 1]]
)

print(matrix)
m2= np.dot(matrix,matrix)
print(m2)
m3 = np.dot(m2,matrix)
print(m3)
mn=matrix
for i in range(50):
    mn = np.dot(mn,matrix)
print(mn)
print(f"Freq A wins from deuce: {mn[3][0]}")
print(f"Freq B wins from deuce: {mn[4][0]}")