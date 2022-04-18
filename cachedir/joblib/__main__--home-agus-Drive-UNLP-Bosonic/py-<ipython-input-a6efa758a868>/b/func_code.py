# first line: 1
@memory.cache   
def b(basis_o, basis_d, i):
    mat = dok_matrix((basis_d.size, basis_o.size), dtype=np.float32)
    for k, v in enumerate(basis_o.base):
        if v[i] != 0:
            dest = list(v.copy())
            dest[i] -= 1   
            tar = basis_d.rep_to_index(dest)
            mat[tar, k] = np.sqrt(v[i])
    return mat
