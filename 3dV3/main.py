import math

import objReader
import forme
import fenetre
import triangle
import vecteur

suzanne = objReader.lireObj("monkey.obj")
objet = forme.Objet(suzanne)
canva = fenetre.Fenetre()
canva.position_camera = vecteur.Vecteur(0, 0, 0)


rotateX = 0
rotateY = 0
rotateZ = 0

orientation = 10

matrice_reverse = [[1,0,0,0],
                   [0,1,0,0],
                   [0,0,1,0],
                   [0,0,0,1],]

def update():
    global triangle, copy_triangle, rotateZ, rotateX, rotateY

    canva.canvas.delete("all")

    rotateX += 0.02
    rotateY += 0.04
    rotateZ += 0.03
    copy_objet = []
    for triangle in objet.triangles:
        # copie les cubes pour ne pas modifier les originaux
        copy_triangle = triangle.copy()

        # applique la rotation
        copy_triangle.rotateX(rotateX)
        #copy_triangle.rotateY(rotateY)
        copy_triangle.rotateZ(rotateZ)

        # écarte de la camera
        copy_triangle.origine.z += 3
        copy_triangle.vect1.z += 3
        copy_triangle.vect2.z += 3

        # positionne les triangles par rapport à la camera
        copy_triangle = copy_triangle.camera_transform(matrice_reverse)

        # projette en 2D
        canva.projection_triangle(copy_triangle)




        # met a jour la profondeur
        copy_triangle.avg_z = min((( copy_triangle.origine.z + copy_triangle.vect1.z + copy_triangle.vect2.z ) / 3), min(copy_triangle.origine.z, copy_triangle.vect1.z, copy_triangle.vect2.z))
        copy_objet.append(copy_triangle)

    # trier en fonction de la profondeur
    copy_objet = sorted(copy_objet, key=lambda copy_triangle: -copy_triangle.avg_z)

    vect_camera = vecteur.add_vect_vect(canva.look, canva.position_camera)

    # dessiner les triangles qui font face à la camera
    for copy_triangle in copy_objet:

        copy_triangle.orientation = copy_triangle.setOrientation()
        if (vecteur.dot_product(vect_camera, copy_triangle.orientation) < 0.0):
            canva.placer_triangle(copy_triangle)

    canva.root.after(20, update)

def on_left_arrow(event):
    global matrice_reverse
    canva.look.rotate_y(math.radians(15))
    cible = vecteur.add_vect_vect(canva.position_camera, canva.look)

    # matrice pointAt
    new_forward = vecteur.add_vect_vect(canva.position_camera, cible)
    new_forward = vecteur.normaliser(new_forward)

    a = vecteur.mult_vect_int(new_forward, vecteur.dot_product(canva.up, new_forward))
    new_up = vecteur.sub_vect_vect(canva.up, a)
    new_up = vecteur.normaliser(new_up)

    new_right = vecteur.cross_product(new_up, new_forward)

    m = [[new_right.x, new_right.y, new_right.z, 0],
               [new_up.x,new_up.y,new_up.z,0],
               [new_forward.x,new_forward.y,new_forward.z,0],
               [canva.position_camera.x,canva.position_camera.y,canva.position_camera.z,1]
              ]

    matrice_reverse = [[m[0][0], m[1][0], m[2][0]],
                       [m[0][1], m[1][1], m[2][1]],
                       [m[0][2], m[1][2], m[2][2]],
                       [-(m[3][0] * m[0][0] + m[3][1] * m[0][1] + m[3][2] * m[0][2]),
                        -(m[3][0] * m[1][0] + m[3][1] * m[1][1] + m[3][2] * m[1][2]),
                        -(m[3][0] * m[2][0] + m[3][1] * m[2][1] + m[3][2] * m[2][2])
                       ]
                      ]

def on_right_arrow(event):
    global matrice_reverse
    canva.look.rotate_y(math.radians(-15))
    cible = vecteur.add_vect_vect(canva.position_camera, canva.look)

    # matrice pointAt
    new_forward = vecteur.add_vect_vect(canva.position_camera, cible)
    new_forward = vecteur.normaliser(new_forward)

    a = vecteur.mult_vect_int(new_forward, vecteur.dot_product(canva.up, new_forward))
    new_up = vecteur.sub_vect_vect(canva.up, a)
    new_up = vecteur.normaliser(new_up)

    new_right = vecteur.cross_product(new_up, new_forward)

    m = [[new_right.x, new_right.y, new_right.z, 0],
         [new_up.x, new_up.y, new_up.z, 0],
         [new_forward.x, new_forward.y, new_forward.z, 0],
         [canva.position_camera.x, canva.position_camera.y, canva.position_camera.z, 1]
         ]

    matrice_reverse = [[m[0][0], m[1][0], m[2][0]],
                       [m[0][1], m[1][1], m[2][1]],
                       [m[0][2], m[1][2], m[2][2]],
                       [-(m[3][0] * m[0][0] + m[3][1] * m[0][1] + m[3][2] * m[0][2]),
                        -(m[3][0] * m[1][0] + m[3][1] * m[1][1] + m[3][2] * m[1][2]),
                        -(m[3][0] * m[2][0] + m[3][1] * m[2][1] + m[3][2] * m[2][2])
                        ]
                       ]

canva.root.bind("<Left>", on_left_arrow)
canva.root.bind("<Right>", on_right_arrow)
canva.root.after(1, update)
canva.run()