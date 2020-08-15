import numpy as np
def load_mat(file):
    with open(file) as f:
        char = f.read()

    char = char.replace(".\n","").split(",")
    char = [x.split(" ") for x in char]

    for i in char:
        for j in range(len(i)):
            i[j] = int(i[j])
    return np.array(char)

mat1 = load_mat("mat1.txt")
mat2 = load_mat("mat2.txt")

mat3 = np.dot(mat1, mat2)

print(sum(np.diag(mat3)))


