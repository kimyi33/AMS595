import numpy as np

### Task 1 ###
# Construct 5x5 random matrix
P = np.random.rand(5,5)

# Normalize each row so it sums to 1
for i in range(5):
    P[i] = P[i]/sum(P[i])   
print(f"P:\n {P}\n")



### Task 2 ###
# Generate randome 5x1 vector
p = np.random.rand(5,)    

# Normalize p so it sums to 1
p = p/sum(p)    # Normalize

# Apply the transition rul 50 times, it results p_50
for _ in range(50):
    p = np.dot(P.T, p)
p_50 = p

print(f"p: {p}\n")
print(f"p_50: {p_50}\n")



### Task 3 ###
# Calculate the eigenvalues and eigenvectors of P.T
eigenvalues, eigenvectors = np.linalg.eig(P.T)

# Locate the eigenvalue closest to 1
index_of_1 = np.argmin(np.abs(eigenvalues - 1))

# Get the corresponding eigenvector
eigenvector_of_1 = eigenvectors[:,index_of_1]

# Scale the eigenvector so it sums to 1
stationary_distribution = eigenvector_of_1 /sum(eigenvector_of_1) 

print(f"stationary distribution: {stationary_distribution}\n")



### Task 4 ###
# Calculate the difference between p_50 and stationary distribution
difference = np.abs(p_50 - stationary_distribution)
matches = np.all(difference < 1e-5)
print(f"Do they match within 1e-5? {matches}")