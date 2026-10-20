"""Stored practical programs. Each ``practicalN()`` prints its code."""
import sys

# key -> source code of the practical (raw strings keep the \n escapes intact)
_SNIPPETS = {
    'practical1': r'''# ==================================================
# Question 1: Recurrence a(n) = a(n-1) + 3, a(0) = 2
# ==================================================
import sympy as sp
n = sp.symbols('n', integer=True, nonnegative=True)
a = sp.Function('a')
# Define the recurrence relation
recurrence = sp.Eq(a(n), a(n-1) + 3)

# Solve the recurrence
solution = sp.rsolve(recurrence, a(n), {a(0): 2})
print(solution)


# ==================================================
# Question 2: Recurrence a(n) = 7a(n-1) - 10a(n-2), a(0) = 2, a(1) = 3
# ==================================================
import sympy as sp
n = sp.symbols('n', integer=True, nonnegative=True)
a = sp.Function('a')
# Define the recurrence relation
recurrence = sp.Eq(a(n), 7*a(n-1) - 10*a(n-2))
# Solve the recurrence
solution = sp.rsolve(recurrence, a(n), {a(0): 2, a(1): 3})
print("Solution:")
print(solution)
''',
    'practical2_bfs': r'''from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'H'],
    'F': ['C', 'G'],
    'G': ['C', 'F'],
    'H': ['D', 'E']
}


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs(graph, "A")
''',
    'practical2_dfs': r'''graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'H'],
    'F': ['C', 'G'],
    'G': ['C', 'F'],
    'H': ['D', 'E']
}


def dfs(start, graph, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for n in graph[start]:
            dfs(n, graph, visited)


dfs("A", graph)
''',
    'practical2_dijkstra': r'''import heapq

# Weighted graph: each vertex -> list of (neighbour, weight)
graph = {
    'A': [('B', 4), ('C', 2), ('D', 7)],
    'B': [('A', 4), ('C', 1), ('E', 3)],
    'C': [('A', 2), ('B', 1), ('D', 2), ('F', 5)],
    'D': [('A', 7), ('C', 2), ('E', 4), ('G', 6)],
    'E': [('B', 3), ('D', 4), ('F', 1), ('G', 8)],
    'F': [('C', 5), ('E', 1), ('G', 5)],
    'G': [('D', 6), ('E', 8), ('F', 5)]
}

# All distances start at infinity, except the source A
dist = {v: float('inf') for v in graph}
print(dist)
dist['A'] = 0

# Min-heap of (distance, vertex)
pq = [(0, 'A')]

while pq:
    d, u = heapq.heappop(pq)          # vertex with smallest distance
    for v, w in graph[u]:
        if d + w < dist[v]:           # shorter path to v found via u
            dist[v] = d + w
            heapq.heappush(pq, (dist[v], v))

print(dist)
''',
    'practical3': r'''# ==================================================
# Question 1: Prim's Algorithm
# ==================================================


g = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 3, 'B': 2, 'D': 7, 'E': 8},
    'D': {'B': 5, 'C': 7, 'E': 6},
    'E': {'C': 8, 'D': 6}
}


visited = {'A'}
mst = []
cost = 0


while len(visited) < len(g):
    edge = min(
        (w, u, v)
        for u in visited
        for v, w in g[u].items()
        if v not in visited
    )


    w, u, v = edge
    visited.add(v)
    mst.append((u, v, w))
    cost += w
    print(u, "-", v, ":", w)


print("MST =", mst)
print("Total Cost =", cost)


# ==================================================
# Question 2: Kruskal's Algorithm
# ==================================================


def find(p, x):
    while p[x] != x:
        x = p[x]
    return x


edges = [
    (1,'A','D'), (2,'B','D'), (3,'A','B'),
    (4,'B','C'), (5,'C','D'), (6,'C','E'),
    (7,'D','E'), (8,'D','F'), (9,'E','F')
]


p = {x:x for x in 'ABCDEF'}
mst = []
cost = 0


for w, u, v in edges:
    a, b = find(p, u), find(p, v)


    if a != b:
        p[a] = b
        mst.append((u, v, w))
        cost += w


print("MST:", mst)
print("Total Cost:", cost)
''',
    'practical4_gradient': r'''import sympy as sp

# Define variables
x, y = sp.symbols('x y')
# ==================================================
# Q1: Partial Derivatives and Gradient
# ==================================================
f = x**2 + x*y + y**2

# Partial derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)
print("Q1: Partial Derivatives")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)

# Gradient
gradient = sp.Matrix([df_dx, df_dy])
print("\nGradient:")
sp.pprint(gradient)
print("gradient:",gradient)

# Gradient at (1,2)
gradient_point = gradient.subs({x: 1, y: 2})

print("\nGradient at (1,2):")
sp.pprint(gradient_point)
''',
    'practical4_jacobian': r'''import sympy as sp


# Define variables
x, y = sp.symbols('x y')

# ==================================================
# Q2: Jacobian Matrix
# ==================================================


F = sp.Matrix([
    x**2 + y,
    x*y + y**2
])

# Jacobian
J = F.jacobian([x, y])

print("\n\nQ2: Jacobian Matrix")
sp.pprint(J)

# Jacobian at (1,2)
J_point = J.subs({x: 1, y: 2})

print("\nJacobian at (1,2):")
sp.pprint(J_point)
''',
    'practical4_hessian': r'''import sympy as sp

# Define variables
x, y = sp.symbols('x y')

# ==================================================
# Q1: Partial Derivatives and Gradient
# ==================================================
f = x**2 + x*y + y**2

# ==================================================
# Q3: Hessian Matrix
# ==================================================
H = sp.hessian(f, (x, y))
print("\n\nQ3: Hessian Matrix")
sp.pprint(H)
# Hessian at (1,2)
H_point = H.subs({x: 1, y: 2})
print("\nHessian at (1,2):")
sp.pprint(H_point)
# Eigenvalues
eigenvalues = H_point.eigenvals()
print("\nEigenvalues of Hessian:")
print(eigenvalues)
''',
    'practical5': r'''"""
Practical 5: Optimization of a Multivariable Function

Aim:
To find the critical points of a multivariable function and classify
them as local minimum, local maximum, or saddle point using partial
derivatives and the Hessian matrix.

Given Function:
f(x, y) = x^3 + y^3 - 3xy

Step 1: Calculate First-Order Partial Derivatives

df/dx = 3x^2 - 3y
df/dy = 3y^2 - 3x

Step 2: Find Critical Points

Set both partial derivatives equal to zero:

3x^2 - 3y = 0  =>  y = x^2
3y^2 - 3x = 0  =>  x = y^2

Substituting y = x^2 into x = y^2:

x = (x^2)^2
x = x^4
x(x^3 - 1) = 0

Real solutions: x = 0 or x = 1

Therefore, the critical points are:
(0, 0) and (1, 1)

Step 3: Calculate the Hessian Matrix

Second-order partial derivatives:

f_xx = 6x
f_yy = 6y
f_xy = f_yx = -3

Hessian matrix:

        [ 6x  -3 ]
H(x,y) =[          ]
        [ -3  6y ]

Step 4: Classify Critical Point (0, 0)

H(0,0) = [  0  -3 ]
         [ -3   0 ]

Eigenvalues: 3 and -3

Since one eigenvalue is positive and the other is negative,
the point (0,0) is a Saddle Point.

Function value: f(0,0) = 0

Step 5: Classify Critical Point (1, 1)

H(1,1) = [  6  -3 ]
         [ -3   6 ]

Eigenvalues: 9 and 3

Since both eigenvalues are positive, the point (1,1)
is a Local Minimum.

Function value: f(1,1) = 1 + 1 - 3 = -1

Step 6: Plot the Function

Generate x and y values between -2 and 2.
Calculate f(x,y) for every coordinate pair and draw a 3D surface.
Mark the critical points on the graph.

Final Result:
(0, 0) -> Saddle Point
(1, 1) -> Local Minimum

No local maximum is found among the real critical points.
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# Define variables
x, y = sp.symbols('x y')


# Define the function
f = x**3 + y**3 - 3*x*y


print("Function:")
print("f(x,y) =", f)


# --------------------------------------------------
# Step 1: First-order partial derivatives
# --------------------------------------------------


df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)


print("\nFirst-order partial derivatives:")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)


# --------------------------------------------------
# Step 2: Find critical points
# --------------------------------------------------


critical_points = sp.solve(
    [df_dx, df_dy],
    [x, y],
    dict=True
)

# Keep only real critical points
critical_points = [
    point for point in critical_points
    if point[x].is_real and point[y].is_real
]


# --------------------------------------------------
# Step 3: Hessian matrix
# --------------------------------------------------


H = sp.hessian(f, (x, y))


print("\nHessian Matrix:")
sp.pprint(H)


# --------------------------------------------------
# Step 4 & 5: Evaluate Hessian and find eigenvalues
# --------------------------------------------------


print("\nClassification of Critical Points:")


for point in critical_points:


    H_point = H.subs(point)


    print("\nPoint:", point)


    print("Hessian:")
    sp.pprint(H_point)


    eigenvalues = H_point.eigenvals()


    print("Eigenvalues:")
    print(eigenvalues)


    # Classification
    eigenvalue_list = list(eigenvalues.keys())

    if all(ev.is_real and ev > 0 for ev in eigenvalue_list):
        print("Classification: Local Minimum")

    elif all(ev.is_real and ev < 0 for ev in eigenvalue_list):
        print("Classification: Local Maximum")

    elif all(ev.is_real for ev in eigenvalue_list) and any(
        ev > 0 for ev in eigenvalue_list
    ) and any(ev < 0 for ev in eigenvalue_list):
        print("Classification: Saddle Point")

    else:
        print("Classification: Inconclusive")


# --------------------------------------------------
# Step 6: 3D Surface Plot
# --------------------------------------------------

# Convert the function into a NumPy-compatible function
f_lambdified = sp.lambdify((x, y), f, 'numpy')

# Generate x and y values
X, Y = np.meshgrid(
    np.linspace(-2, 2, 100),
    np.linspace(-2, 2, 100)
)

# Calculate function values
Z = f_lambdified(X, Y)

# Plot the 3D surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.7)

# Mark critical points on the graph
for point in critical_points:
    ax.scatter(
        float(point[x]),
        float(point[y]),
        float(f.subs(point)),
        s=60
    )

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title('Optimization of a Multivariable Function')

plt.savefig("optimization_plot.png")
plt.show()
''',
    'practical6': r'''import sympy as sp


# Define variables
x, y, lam = sp.symbols('x y lam')

# Objective function
P = x * y

# Constraint
constraint = x + y - 10


# Lagrangian
L = P + lam * (10 - x - y)


print("Objective function:")
print("P(x,y) =", P)


print("\nConstraint:")
print("x + y = 10")


print("\nLagrangian:")
sp.pprint(L)


# Partial derivatives of Lagrangian
dL_dx = sp.diff(L, x)
dL_dy = sp.diff(L, y)
dL_dlam = sp.diff(L, lam)


print("\nPartial derivatives:")
print("∂L/∂x =", dL_dx)
print("∂L/∂y =", dL_dy)
print("∂L/∂λ =", dL_dlam)


# Solve the system of equations
solution = sp.solve(
    [dL_dx, dL_dy, dL_dlam],
    [x, y, lam],
    dict=True
)


print("\nSolution:")
for sol in solution:
    print(sol)


# Calculate the objective function at the solution
for sol in solution:
    production = P.subs(sol)


    print("\nOptimal values:")
    print("x =", sol[x])
    print("y =", sol[y])
    print("Maximum production =", production)


    # Verify constraint
    constraint_value = (x + y).subs(sol)


    print("Constraint value =", constraint_value)
''',
    'practical7': r'''import numpy as np


# ---------------------------------------
# Part 1: Vectors and Matrix
# ---------------------------------------


v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
v3 = np.array([1, 1, 2])


# Form a matrix using vectors as columns
A_vectors = np.column_stack((v1, v2, v3))


print("Matrix formed by the vectors:")
print(A_vectors)


# ---------------------------------------
# Part 2: Rank
# ---------------------------------------


rank = np.linalg.matrix_rank(A_vectors)


print("\nRank of the matrix:", rank)


# ---------------------------------------
# Part 3: Linear Independence
# ---------------------------------------


if rank == A_vectors.shape[1]:
    print("The vectors are linearly independent.")
else:
    print("The vectors are linearly dependent.")


# ---------------------------------------
# Part 4: Numerical Solution of AX = B
# ---------------------------------------


A = np.array([
    [2, 1, 1],
    [4, 3, 2],
    [2, 3, 3]
], dtype=float)


b = np.array([5, 11, 13], dtype=float)


# Solve AX = B
x = np.linalg.solve(A, b)


print("\nSolution of the linear system:")
print(x)


# ---------------------------------------
# Part 5: Verification using Residual
# ---------------------------------------


residual = A @ x - b


print("\nResidual:")
print(residual)


print("\nResidual norm:")
print(np.linalg.norm(residual))
''',
    'practical8': r'''import numpy as np
from scipy.linalg import lu


# Define the matrix
A = np.array([
    [4, 2, 2],
    [2, 5, 1],
    [2, 1, 6]
], dtype=float)


print("Original Matrix A:")
print(A)


# ------------------------------------------------
# 1. LU Factorization
# ------------------------------------------------


P, L, U = lu(A)


print("\nLU Factorization:")
print("\nP =")
print(P)


print("\nL =")
print(L)


print("\nU =")
print(U)


# Verify PA = LU
LU_error = np.linalg.norm(P @ A - L @ U)


print("\nLU Reconstruction Error:")
print(LU_error)


# ------------------------------------------------
# 2. QR Factorization
# ------------------------------------------------


Q, R = np.linalg.qr(A)


print("\nQR Factorization:")
print("\nQ =")
print(Q)


print("\nR =")
print(R)


# Verify A = QR
QR_error = np.linalg.norm(A - Q @ R)


print("\nQR Reconstruction Error:")
print(QR_error)


# ------------------------------------------------
# 3. Cholesky Factorization
# ------------------------------------------------


L_chol = np.linalg.cholesky(A)


print("\nCholesky Factorization:")
print("\nL =")
print(L_chol)


# Verify A = LL^T
Chol_error = np.linalg.norm(A - L_chol @ L_chol.T)


print("\nCholesky Reconstruction Error:")
print(Chol_error)
''',
    'practical9': r'''import numpy as np


# Define the matrix
A = np.array([
    [3, 1, 1],
    [-1, 3, 1],
    [0, 2, 4],
    [2, 1, 3]
], dtype=float)


print("Original Matrix A:")
print(A)


# ------------------------------------------------
# 1. Singular Value Decomposition
# ------------------------------------------------


U, singular_values, VT = np.linalg.svd(A)


print("\nMatrix U:")
print(U)


print("\nSingular Values:")
print(singular_values)


print("\nMatrix V^T:")
print(VT)


# Construct Sigma
Sigma = np.zeros_like(A, dtype=float)
Sigma[:len(singular_values), :len(singular_values)] = np.diag(singular_values)


print("\nSigma:")
print(Sigma)


# ------------------------------------------------
# 2. Reconstruction using all singular values
# ------------------------------------------------


A_reconstructed = U @ Sigma @ VT


print("\nReconstructed Matrix:")
print(A_reconstructed)


# Reconstruction error
error_full = np.linalg.norm(A - A_reconstructed, 'fro')


print("\nFull Reconstruction Error:")
print(error_full)


# ------------------------------------------------
# 3. Rank-2 Approximation
# ------------------------------------------------


k = 2


U_k = U[:, :k]
Sigma_k = np.diag(singular_values[:k])
VT_k = VT[:k, :]


A_rank2 = U_k @ Sigma_k @ VT_k


print("\nRank-2 Approximation:")
print(A_rank2)


# ------------------------------------------------
# 4. Rank-2 Reconstruction Error
# ------------------------------------------------


error_rank2 = np.linalg.norm(A - A_rank2, 'fro')


print("\nRank-2 Approximation Error:")
print(error_rank2)
''',
    'practical10': r'''import numpy as np


# Define the matrix
A = np.array([
    [4, 1, 0],
    [1, 3, 1],
    [0, 1, 2]
], dtype=float)


# ---------------------------------------
# Part 1: Eigenvalues and Eigenvectors
# ---------------------------------------


eigenvalues, eigenvectors = np.linalg.eig(A)


print("Eigenvalues:")
print(eigenvalues)


print("\nEigenvectors (columns):")
print(eigenvectors)


# Identify the dominant eigenvalue
idx = np.argmax(np.abs(eigenvalues))
dominant_eigenvalue = eigenvalues[idx]


print("\nDominant Eigenvalue:")
print(dominant_eigenvalue)


# ---------------------------------------
# Part 2: Power Method
# ---------------------------------------


x = np.array([1.0, 1.0, 1.0])
tolerance = 1e-10
max_iterations = 1000


lambda_old = 0.0


for iteration in range(1, max_iterations + 1):


    y = A @ x


    # Normalize the vector
    x_new = y / np.linalg.norm(y)


    # Rayleigh quotient estimates the eigenvalue
    lambda_new = x_new @ A @ x_new


    # Check convergence
    if abs(lambda_new - lambda_old) < tolerance:
        x = x_new
        break


    x = x_new
    lambda_old = lambda_new


print("\nPower Method:")
print("Dominant Eigenvalue:", lambda_new)
print("Corresponding Eigenvector:", x)
print("Number of Iterations:", iteration)


# ---------------------------------------
# Part 3: Error Calculation
# ---------------------------------------


error = abs(dominant_eigenvalue - lambda_new)


print("\nAbsolute Error:")
print(error)
''',
    'practical11': r'''import numpy as np


# Define matrices
A = np.array([
    [4, 1],
    [2, 3]
], dtype=float)


B = np.array([
    [1, 1],
    [1, 1.0001]
], dtype=float)


# ---------------------------------------
# Part 1: Matrix Norms
# ---------------------------------------


matrices = {"A": A, "B": B}


for name, M in matrices.items():
    print(f"\nMatrix {name}:")
    print(M)


    print("Frobenius Norm:", np.linalg.norm(M, 'fro'))
    print("1-Norm:", np.linalg.norm(M, 1))
    print("Infinity Norm:", np.linalg.norm(M, np.inf))


# ---------------------------------------
# Part 2: Condition Numbers
# ---------------------------------------


print("\nCondition Numbers (2-norm):")
print("Condition number of A:", np.linalg.cond(A))
print("Condition number of B:", np.linalg.cond(B))


# ---------------------------------------
# Part 3: Solve the Original System
# ---------------------------------------


b = np.array([5, 5], dtype=float)


x_A = np.linalg.solve(A, b)
x_B = np.linalg.solve(B, b)


print("\nOriginal Solutions:")
print("Solution for A:", x_A)
print("Solution for B:", x_B)


# ---------------------------------------
# Part 4: Perturb the Right-Hand Side
# ---------------------------------------


delta_b = np.array([0.001, -0.001])


b_perturbed = b + delta_b


x_A_perturbed = np.linalg.solve(A, b_perturbed)
x_B_perturbed = np.linalg.solve(B, b_perturbed)


print("\nSolutions after Perturbation:")
print("Perturbed solution for A:", x_A_perturbed)
print("Perturbed solution for B:", x_B_perturbed)


# ---------------------------------------
# Part 5: Change in Solutions
# ---------------------------------------


print("\nChange in Solutions:")
print("Change for A:", np.linalg.norm(x_A_perturbed - x_A))
print("Change for B:", np.linalg.norm(x_B_perturbed - x_B))
''',
    'practical12': r'''import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# ---------------------------------------
# Part 1: Create the Dataset
# ---------------------------------------


data = pd.DataFrame({
    'X1': [2, 3, 4, 5, 6, 7, 8, 9],
    'X2': [4, 5, 6, 8, 9, 10, 12, 13],
    'X3': [7, 8, 9, 10, 12, 13, 15, 16]
})


print("Original Dataset:")
print(data)


# ---------------------------------------
# Part 2: Standardize the Data
# ---------------------------------------


scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)


print("\nStandardized Data:")
print(np.round(X_scaled, 3))


# ---------------------------------------
# Part 3: Apply PCA
# ---------------------------------------


pca = PCA()
X_pca = pca.fit_transform(X_scaled)


print("\nPrincipal Components:")
print(np.round(pca.components_, 3))


print("\nExplained Variance:")
print(np.round(pca.explained_variance_, 4))


print("\nExplained Variance Ratio:")
print(np.round(pca.explained_variance_ratio_, 4))


# ---------------------------------------
# Part 4: Cumulative Explained Variance
# ---------------------------------------


cumulative_variance = np.cumsum(
    pca.explained_variance_ratio_
)


print("\nCumulative Explained Variance:")
print(np.round(cumulative_variance, 4))


# Number of components for at least 95% variance
k = np.argmax(cumulative_variance >= 0.95) + 1


print("\nNumber of Components Required:", k)


# ---------------------------------------
# Part 5: Dimensionality Reduction
# ---------------------------------------


pca_reduced = PCA(n_components=k)
X_reduced = pca_reduced.fit_transform(X_scaled)


reduced_data = pd.DataFrame(
    X_reduced,
    columns=[f'PC{i+1}' for i in range(k)]
)


print("\nReduced Dataset:")
print(reduced_data.round(3))
''',
    'practical13': r'''# ==================================================
# Question 1: Absolute, Relative and Percentage Error
# ==================================================
import math


# True and approximate values
true_value = math.pi
approx_value = 3.14


# Calculate errors
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
percentage_error = relative_error * 100


print("True Value:", true_value)
print("Approximate Value:", approx_value)
print("Absolute Error:", absolute_error)
print("Relative Error:", relative_error)
print("Percentage Error:", percentage_error, "%")


# ==================================================
# Question 2: Rounding Error
# ==================================================

x = 1.23456789
decimal_places = [2, 4, 6]


print("Original Value:", x)
print()


for d in decimal_places:
    approx_value = round(x, d)
    error = abs(x - approx_value)


    print("Decimal Places:", d)
    print("Rounded Value:", approx_value)
    print("Absolute Error:", error)
    print()


# ==================================================
# Question 3: Truncation Error (Taylor Series of e^x)
# ==================================================

x = 1.0
term_counts = [3, 5, 10]


true_value = math.exp(x)


for N in term_counts:
    approximation = sum(x**n / math.factorial(n)
                        for n in range(N))


    error = abs(true_value - approximation)


    print("Number of Terms:", N)
    print("Approximation:", approximation)
    print("Absolute Error:", error)
    print()


# ==================================================
# Question 4: Loss of Significance (Subtractive Cancellation)
# ==================================================

a = 1.0000001
b = 1.0000000


# Direct computation
difference_1 = a**2 - b**2


# Algebraically equivalent computation
difference_2 = (a - b) * (a + b)


print("Direct Computation:", difference_1)
print("Rearranged Computation:", difference_2)
print("Difference between Results:",
      abs(difference_1 - difference_2))
''',
    'practical14': r'''# ==================================================
# Question 1: Bisection Method
# ==================================================
def f(x):
    return x**3 - x - 2


a = 1.0
b = 2.0
tol = 1e-6
max_iter = 100

if f(a) * f(b) >= 0:
    print("Bisection method cannot be applied.")

else:
    previous_c = None

    for i in range(1, max_iter + 1):

        # Step 1: Calculate midpoint
        c = (a + b) / 2

        # Step 2: Check successive approximations
        if previous_c is not None and abs(c - previous_c) < tol:
            break

        # Step 3: Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Step 4: Store current approximation
        previous_c = c

    print("Approximate Root:", c)
    print("Iterations:", i)
    print("f(root):", f(c))


# ==================================================
# Question 2: Secant Method
# ==================================================
def f(x):
    return x**3 - x - 2


x0 = 1.0
x1 = 2.0
tol = 1e-6
max_iter = 100

for i in range(1, max_iter + 1):

    # Step 1: Calculate the next approximation
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

    # Step 2: Check the difference between approximations
    if abs(x2 - x1) < tol:
        x1 = x2
        break

    # Step 3: Update the approximations
    x0 = x1
    x1 = x2

print("Approximate Root:", x1)
print("Iterations:", i)
print("f(root):", f(x1))


# ==================================================
# Question 3: Newton-Raphson Method
# ==================================================
def f(x):
    return x**3 - x - 2


def df(x):
    return 3*x**2 - 1


x = 1.5
tol = 1e-6
max_iter = 100

for i in range(1, max_iter + 1):

    # Step 1: Calculate the next approximation
    x_new = x - f(x) / df(x)

    # Step 2: Check the difference between approximations
    if abs(x_new - x) < tol:
        x = x_new
        break

    # Step 3: Update the approximation
    x = x_new

print("Approximate Root:", x)
print("Iterations:", i)
print("f(root):", f(x))
''',
    'practical15': r'''# Practical 15: Numerical Integration
# Aim: To implement the Trapezoidal Rule and Simpson's 1/3 Rule in Python for
# numerical evaluation of definite integrals and compare their accuracy with
# exact values.


# ==================================================
# Question 1: Trapezoidal Rule
# ==================================================
import math
from scipy.integrate import quad


def f(x):
    return math.exp(-x**2)


a, b = 0.0, 1.0
n = 10
h = (b - a) / n

total = f(a) + f(b)

for i in range(1, n):
    total += 2 * f(a + i * h)

trapezoidal_value = (h / 2) * total

reference_value, _ = quad(f, a, b)
absolute_error = abs(reference_value - trapezoidal_value)

print("Trapezoidal Approximation:", trapezoidal_value)
print("Reference Value:", reference_value)
print("Absolute Error:", absolute_error)


# ==================================================
# Question 2: Simpson's 1/3 Rule
# ==================================================
import math
from scipy.integrate import quad


def f(x):
    return math.exp(-x**2)


a, b = 0.0, 1.0
n = 10

if n % 2 != 0:
    raise ValueError("n must be even for Simpson's 1/3 Rule")

h = (b - a) / n

total = f(a) + f(b)

for i in range(1, n):
    x = a + i * h

    if i % 2 == 0:
        total += 2 * f(x)
    else:
        total += 4 * f(x)

simpson_value = (h / 3) * total

reference_value, _ = quad(f, a, b)
absolute_error = abs(reference_value - simpson_value)

print("Simpson's Approximation:", simpson_value)
print("Reference Value:", reference_value)
print("Absolute Error:", absolute_error)
''',
    'practical16': r'''# Practical 16: Iterative Numerical Methods
# Aim: To implement the Jacobi and Gauss-Seidel iterative methods in Python for
# solving systems of linear equations and compare their convergence.


# ==================================================
# Question 1: Jacobi Method
# ==================================================
import numpy as np

A = np.array([
    [10, -1,  2],
    [-1, 11, -1],
    [2, -1, 10]
], dtype=float)

b = np.array([6, 25, -11], dtype=float)

x = np.zeros(len(b))
tol = 1e-6
max_iter = 100

D = np.diag(A)
R = A - np.diagflat(D)

for i in range(1, max_iter + 1):
    x_new = (b - np.dot(R, x)) / D

    if np.linalg.norm(x_new - x, ord=np.inf) < tol:
        x = x_new
        break

    x = x_new

print("Approximate Solution:", x)
print("Iterations:", i)
print("Residual Norm:", np.linalg.norm(A @ x - b))


# ==================================================
# Question 2: Gauss-Seidel Method
# ==================================================
import numpy as np

A = np.array([
    [10, -1,  2],
    [-1, 11, -1],
    [2, -1, 10]
], dtype=float)

b = np.array([6, 25, -11], dtype=float)

x = np.zeros(len(b))
tol = 1e-6
max_iter = 100

for i in range(1, max_iter + 1):
    x_old = x.copy()

    for j in range(len(b)):
        sum1 = np.dot(A[j, :j], x[:j])
        sum2 = np.dot(A[j, j+1:], x_old[j+1:])

        x[j] = (b[j] - sum1 - sum2) / A[j, j]

    if np.linalg.norm(x - x_old, ord=np.inf) < tol:
        break

print("Approximate Solution:", x)
print("Iterations:", i)
print("Residual Norm:", np.linalg.norm(A @ x - b))
''',
}

# practicals made of several files: key -> [(snippet key, heading), ...]
_GROUPS = {
    'practical2': [
        ('practical2_bfs', 'bfs (practical_bfs.py)'),
        ('practical2_dfs', 'dfs (practical_dfs.py)'),
        ('practical2_dijkstra', 'Dijkstra (practical_Dij.py)'),
    ],
    'practical4': [
        ('practical4_gradient', 'gradient (gradient.py)'),
        ('practical4_jacobian', 'jacobian (jacobian.py)'),
        ('practical4_hessian', 'hessian (hessian.py)'),
    ],
}


def _group_code(key):
    sections = []
    for snippet_key, title in _GROUPS[key]:
        sections.append("# --- %s ---\n\n%s" % (title, _SNIPPETS[snippet_key]))
    return "\n\n".join(sections)


def _code(name):
    if name in _GROUPS:
        return _group_code(name)
    return _SNIPPETS[name]


def _show(text):
    try:
        print(text, end="")
    except UnicodeEncodeError:
        # consoles that cannot show symbols such as the partial-derivative sign
        enc = getattr(sys.stdout, "encoding", None) or "ascii"
        print(text.encode(enc, "replace").decode(enc), end="")


def practical1():
    'Print the code of Practical 1.'
    _show(_code('practical1'))


def practical2():
    'Print the code of Practical 2.'
    _show(_code('practical2'))


def practical2_bfs():
    'Print the code of Practical 2 - bfs.'
    _show(_code('practical2_bfs'))


def practical2_dfs():
    'Print the code of Practical 2 - dfs.'
    _show(_code('practical2_dfs'))


def practical2_dijkstra():
    'Print the code of Practical 2 - dijkstra.'
    _show(_code('practical2_dijkstra'))


def practical3():
    'Print the code of Practical 3.'
    _show(_code('practical3'))


def practical4():
    'Print the code of Practical 4.'
    _show(_code('practical4'))


def practical4_gradient():
    'Print the code of Practical 4 - gradient.'
    _show(_code('practical4_gradient'))


def practical4_jacobian():
    'Print the code of Practical 4 - jacobian.'
    _show(_code('practical4_jacobian'))


def practical4_hessian():
    'Print the code of Practical 4 - hessian.'
    _show(_code('practical4_hessian'))


def practical5():
    'Print the code of Practical 5.'
    _show(_code('practical5'))


def practical6():
    'Print the code of Practical 6.'
    _show(_code('practical6'))


def practical7():
    'Print the code of Practical 7.'
    _show(_code('practical7'))


def practical8():
    'Print the code of Practical 8.'
    _show(_code('practical8'))


def practical9():
    'Print the code of Practical 9.'
    _show(_code('practical9'))


def practical10():
    'Print the code of Practical 10.'
    _show(_code('practical10'))


def practical11():
    'Print the code of Practical 11.'
    _show(_code('practical11'))


def practical12():
    'Print the code of Practical 12.'
    _show(_code('practical12'))


def practical13():
    'Print the code of Practical 13.'
    _show(_code('practical13'))


def practical14():
    'Print the code of Practical 14.'
    _show(_code('practical14'))


def practical15():
    'Print the code of Practical 15.'
    _show(_code('practical15'))


def practical16():
    'Print the code of Practical 16.'
    _show(_code('practical16'))
