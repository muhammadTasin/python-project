import numpy as np
A = np.array([[2,3],[1,-1]])
B = B = np.array([8, 2])
solution = np.linalg.solve(A, B)
x, y = solution
print(f"Solution: x = {x}, y = {y}")