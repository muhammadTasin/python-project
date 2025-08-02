import torch
import time
import itertools
import threading
import sys
import numpy as np

matrix = np.array([[1,2,3],[4,5,6]])
print(matrix.T)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print(result)


# Check if CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"\n🔍 Using device: {device}\n")

# Spinner animation
spinner = itertools.cycle(['⣷','⣯','⣟','⡿','⢿','⣻','⣽','⣾'])

done = False

def animate():
    while not done:
        sys.stdout.write(f"\r🔥 GPU running... {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)

# Start animation thread
t = threading.Thread(target=animate)
t.start()

# GPU work (multiply large tensors in loop)
size = 2048
a = torch.randn(size, size, device=device)
b = torch.randn(size, size, device=device)

for _ in range(100):
    result = torch.mm(a, b)

# Finish
torch.cuda.synchronize()
done = True
t.join()

print("\n✅ GPU task complete!")
