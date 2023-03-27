import numpy as np

n = 3  # change to desired dimension
num_trials = 1000  # number of trials to run

count = 0
for i in range(num_trials):
    A = np.random.uniform(-1, 1, (n**n, n**n))
    if np.linalg.matrix_rank(A) < n**0:
        count += 1

print(f"Number of times rank(A) < n^0: {count}/{num_trials}")

