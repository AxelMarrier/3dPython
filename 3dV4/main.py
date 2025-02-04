import math

import matrice
import objReader
import fenetre
import vecteur
import triangle

monkey = objReader.lireObj("monkey.obj")
fenetre = fenetre.Fenetre("Caméra")
angle_x = 0.01
angle_z = 0.01
orientation = 0

forme = []
for triangles in monkey:
    forme.append(triangle.Triangle(vecteur.Vecteur(triangles[0][0], triangles[0][1], triangles[0][2]),
                                   vecteur.Vecteur(triangles[1][0], triangles[1][1], triangles[1][2]),
                                   vecteur.Vecteur(triangles[2][0], triangles[2][1], triangles[2][2])))


matProj = matrice.matrice_projection(90, fenetre.height/fenetre.width, 0.1, 1000)



#début boucle
def update():

    matRotZ = matrice.matrice_rotation_z(angle_z)
    matRotX = matrice.matrice_rotation_x(angle_x)
    matTrans = matrice.matrice_translation(0,0,5)
    matWorld = matrice.multMatriceMatrice(matRotZ, matRotX)
    matWorld = matrice.multMatriceMatrice(matWorld, matTrans)


    #gestion de la caméra
    up = vecteur.Vecteur(0, 1, 0)
    target = vecteur.Vecteur(0, 0, 1)
    matCameraRot = matrice.matrice_rotation_y(orientation)
    dir_regard = matrice.multMatriceVecteur(matCameraRot, target)
    target = vecteur.addVecteurVecteur(fenetre.position_camera, dir_regard)
    matCamera = matrice.matrice_point(fenetre.position_camera, target, up)
    matVue = matrice.matrice_inverse(matCamera)

    for triangle in forme:

        triangle.origine = matrice.multMatriceVecteur(matWorld, triangle.origine)
        triangle.vect1 = matrice.multMatriceVecteur(matWorld, triangle.vect1)
        triangle.vect2 = matrice.multMatriceVecteur(matWorld, triangle.vect2)

        triangle.orientation = triangle.setOrientation()

        cameraRay = vecteur.subVecteurVecteur(triangle.origine, fenetre.position_camera)

        if (vecteur.dot(triangle.orientation, cameraRay) < 0):
            triangle.origine = matrice.multMatriceVecteur(matVue, triangle.origine)
            triangle.vect1 = matrice.multMatriceVecteur(matVue, triangle.vect1)
            triangle.vect2 = matrice.multMatriceVecteur(matVue, triangle.vect2)

    forme.sort(key=lambda t: (t.origine.z + t.vect1.z + t.vect2.z) / 3.0, reverse=True)

    fenetre.canvas.delete("all")

    for triangle in forme:
        fenetre.placer_triangle(triangle)

    fenetre.canvas.after(15, update)


fenetre.canvas.after(20, update)

fenetre.run()