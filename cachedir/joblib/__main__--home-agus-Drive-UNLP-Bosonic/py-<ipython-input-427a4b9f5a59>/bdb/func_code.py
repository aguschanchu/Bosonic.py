# first line: 1
@memory.cache    
def bdb(basis, i, j):
    mat = dok_matrix((basis.size, basis.size), dtype=np.float32)
    for k, v in enumerate(basis.base):
        if v[j] != 0 and v[i] != basis.d - 1:
            dest = list(v.copy())
            dest[j] -= 1
            dest[i] += 1
            tar = basis.rep_to_index(dest)
            mat[tar, k] = np.sqrt(v[i]+1)*np.sqrt(v[j])
    return mat
