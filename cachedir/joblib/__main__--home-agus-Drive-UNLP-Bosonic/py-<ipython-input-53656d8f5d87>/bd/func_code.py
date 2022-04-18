# first line: 1
@memory.cache   
def bd(basis_o, basis_d, i):
    mat = dok_matrix((basis_d.size, basis_o.size), dtype=np.float32)
    for k, v in enumerate(basis_o.base):
        dest = list(v.copy())
        dest[i] += 1   
        tar = basis_d.rep_to_index(dest)
        mat[tar, k] = np.sqrt(v[i]+1)
    return mat
