import vecteur
import math

def matrice():
    return [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]


def matrice_identite():
    mat = matrice()
    mat[0][0] = 1
    mat[1][1] = 1
    mat[2][2] = 1
    mat[3][3] = 1
    return mat


def multMatriceVecteur(mat, vect):
    new_x = vect.x * mat[0][0] + vect.y * mat[1][0] + vect.z * mat[2][0] + vect.w * mat[3][0]
    new_y = vect.x * mat[0][1] + vect.y * mat[1][1] + vect.z * mat[2][1] + vect.w * mat[3][1]
    new_z = vect.x * mat[0][2] + vect.y * mat[1][2] + vect.z * mat[2][2] + vect.w * mat[3][2]
    new_w = vect.x * mat[0][3] + vect.y * mat[1][3] + vect.z * mat[2][3] + vect.w * mat[3][3]
    return vecteur.Vecteur(new_x, new_y, new_z, new_w)


def matrice_rotation_x(angle):
    mat = matrice()
    mat[0][0] = 1
    mat[1][1] = math.cos(angle)
    mat[1][2] = math.sin(angle)
    mat[2][1] = -(math.sin(angle))
    mat[2][2] = math.cos(angle)
    mat[3][3] = 1
    return mat


def matrice_rotation_y(angle):
    mat = matrice()
    mat[0][0] = math.cos(angle)
    mat[0][2] = math.sin(angle)
    mat[2][0] = -(math.sin(angle))
    mat[1][1] = 1
    mat[2][2] = math.cos(angle)
    mat[3][3] = 1
    return mat


def matrice_rotation_z(angle):
    mat = matrice()
    mat[0][0] = math.cos(angle)
    mat[0][1] = math.sin(angle)
    mat[1][0] = -(math.sin(angle))
    mat[1][1] = math.cos(angle)
    mat[2][2] = 1
    mat[3][3] = 1
    return mat


def matrice_translation(x, y, z):
    mat = matrice_identite()
    mat[3][0] = x
    mat[3][1] = y
    mat[3][2] = z
    return mat


def matrice_projection(fov, ratio, zProche, zLoin):
    fov = 1 / math.tan(math.radians(fov)/2)
    mat = matrice()
    mat[0][0] = ratio * fov
    mat[1][1] = fov
    mat[2][2] = zLoin / (zLoin - zProche)
    mat[3][2] = (-zLoin * zProche) / (zLoin - zProche)
    mat[2][3] = 1
    return mat


def multMatriceMatrice(mat1, mat2):
    new_mat = matrice()
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat1[j][0] * mat2[0][i] + mat1[j][1] * mat2[1][i] + mat1[j][2] * mat2[2][i] + mat1[j][3] * mat2[3][i]
    return new_mat


def matrice_point(position, cible, haut):
    new_forward = vecteur.subVecteurVecteur(cible, position)
    new_forward = vecteur.normalise(new_forward)

    a = vecteur.multVecteurNombre(new_forward, vecteur.dot(haut, new_forward))
    new_haut = vecteur.subVecteurVecteur(haut, a)
    new_haut = vecteur.normalise(new_haut)

    new_droit = vecteur.cross(new_haut, new_forward)

    mat = matrice_identite()
    mat[0][0] = new_droit.x
    mat[0][1] = new_droit.y
    mat[0][2] = new_droit.z

    mat[1][0] = new_haut.x
    mat[1][1] = new_haut.y
    mat[1][2] = new_haut.z

    mat[2][0] = new_forward.x
    mat[2][1] = new_forward.y
    mat[2][2] = new_forward.z

    mat[3][0] = position.x
    mat[3][1] = position.y
    mat[3][2] = position.z

    return mat


def matrice_inverse(m):
    mat = matrice_identite()
    mat[0][0] = m[0][0]
    mat[0][1] = m[1][0]
    mat[0][2] = m[2][0]

    mat[1][0] = m[0][1]
    mat[1][1] = m[1][1]
    mat[1][2] = m[2][1]

    mat[2][0] = m[0][2]
    mat[2][1] = m[1][2]
    mat[2][2] = m[2][2]

    mat[3][0] = -(m[3][0] * mat[0][0] + m[3][1] * mat[1][0] + m[3][2] * mat[2][0])
    mat[3][1] = -(m[3][0] * mat[0][1] + m[3][1] * mat[1][1] + m[3][2] * mat[2][1])
    mat[3][2] = -(m[3][0] * mat[0][2] + m[3][1] * mat[1][2] + m[3][2] * mat[2][2])

    return mat