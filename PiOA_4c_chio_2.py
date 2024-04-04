import numpy as np
import sys

# mat = np.array([
#     [1,1,3,1],
#     [3,1,2,2],
#     [0,1,2,0],
#     [1,4,3,1],
# ])

# mat = np.array([
#     [1,1,3,1,3 ],
#     [3,1,2,2,5 ],
#     [0,1,2,0,2 ],
#     [1,4,3,1,1 ],
#     [1,1,6,2,0 ],
# ])
mat = np.array([
    [1,1,3,1,3, 5 ],
    [3,1,2,2,5, 5 ],
    [0,1,2,0,2, 5 ],
    [1,4,3,1,1, 5 ],
    [1,1,6,2,0, 5 ],
    [1,2,0,1,0, 3 ],
])

def get_sparse_matrix(m, indexes):
    return m[:,sorted(indexes[0])][sorted(indexes[1]),:]

def calc_sparse_minor(m, indexes):
    return np.linalg.det(get_sparse_matrix(m, indexes))

def find_norm_minor(m: np.ndarray) -> tuple[np.ndarray, float]:
    minors = []
    for l_c in range(m.shape[1]-1):
        for r_c in range(l_c+1, m.shape[1]):
            for t_r in range(m.shape[0]-1):
                for b_r in range(t_r+1, m.shape[0]):
                    key = np.array([[l_c, r_c], 
                            [t_r, b_r]])
                    minors.append((key, calc_sparse_minor(m, key)))
                    if minors[-1][1] in (1, -1): return (key, minors[-1][1])
            
    for key, value in minors:
        if value in (2,3,4,10):
            return (key, value)
    
    for key, value in minors:
        if value != 0:
            return (key, value)
    
    raise ValueError("All minors are zero")

def chio_2(m):
    dims = m.shape

    if dims[0] != dims[1]:
        raise ValueError("Matrix must be square")
    
    if dims[0] <= 3:
        return np.linalg.det(m)

    n = dims[0]
    k = 2

    indexes, minor = find_norm_minor(m)

    print(f"Using minor at indexes \n{indexes+1} with determinant {minor:.2f}")
    new_mat = np.zeros((dims[0]-k, dims[1]-k))

    factor = 1 / (minor ** (n-k-1)) 
    print(f'factor = 1 / det ** (n-k-1) = 1 / {minor:.2f} ** ({n}-{k}-1) = {factor:.2f}')
    n_c = n_r = 0
    for c in range(n):
        if c not in indexes[0]:
            n_r = 0
            for r in range(n):
                if r not in indexes[1]:
                    new_mat[n_r, n_c] = calc_sparse_minor(m, np.hstack((indexes, [[c],[r]])))
                    n_r += 1
            n_c += 1
    print(f'next matrix:\n{np.round(new_mat, 2)}')
    return factor * chio_2(new_mat)
    

def main():
    print(f'Original matrix:\n{mat}\n')
    print(f"choi_2: {chio_2(mat)}")
    print(f'Expected: {np.linalg.det(mat)}')

    print()
    print("Если что, индексы, выводимые в консоли, начинаются с 1, а не с 0")

if __name__ == '__main__':
    main()
