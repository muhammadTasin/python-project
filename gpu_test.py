import torch
import time

if torch.cuda.is_available():
    device = torch.device("cuda")
    print("✅ GPU is available:", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print("⚠️ CUDA not available. Using CPU.")

size = 1000
a = torch.randn(size, size, device=device)
b = torch.randn(size, size, device=device)

_ = torch.mm(a, b)  # Warm-up

start = time.time()
result = torch.mm(a, b)
end = time.time()

print(f"✅ Matrix multiplication completed on {device}")
print(f"⏱️ Execution time: {end - start:.4f} seconds")
