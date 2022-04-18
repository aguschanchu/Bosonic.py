# first line: 1
@memory.cache    
def bbd(basis, i, j):
    mat = dok_matrix((basis.size, basis.size), dtype=np.float32)
    for k, v in enumerate(basis.base):
        if v[i] != 0 and v[j] != basis.d - 1:
            dest = list(v.copy())
            dest[i] -= 1
            dest[j] += 1
            tar = basis.rep_to_index(dest)
            mat[tar, k] = np.sqrt(v[j]+1)*np.sqrt(v[i])
    return mat
