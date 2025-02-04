import math
from canva import *
from triangle import *


def lireObj(fichier):
    objet = open(fichier, "r")
    points = []
    liens = []
    forme = []

    for lines in objet.readlines():
        if (lines[0] == "v"):
            point = []
            for words in lines.split():
                if (words != "v"):
                    point.append(float(words))
            points.append(point)

        if (lines[0] == "f"):
            lien = []
            for words in lines.split():
                if (words != "f"):
                    lien.append(int(words) - 1)
            liens.append(lien)

    for lien in liens:
        triangle = Triangle(points[lien[0]], points[lien[1]], points[lien[2]])
        forme.append(triangle)

    return forme

camera = Canvas3D(600, 500, 90, 1000, 0.1, "Caméra")

cube = lireObj("monkey.obj")

rotation_Z = 0
rotation_X = 0
rotation_Y = 0

def update():
    global rotation_Z
    global rotation_Y
    global rotation_X

    rotation_Z += 0.02
    rotation_Y += 0.04
    rotation_Z += 0.03
    camera.canvas.delete("all")  # Clear the canvas

    copy_cube = []
    for triangle in cube:
        copy_cube.append(triangle.copy())

    for copy_triangle in copy_cube:

        # Applique la rotation uniquement
        copy_triangle.rotateZ(rotation_Z)
        copy_triangle.rotateY(rotation_Y)
        copy_triangle.rotateZ(rotation_X)
        copy_triangle.setOrientation()
        copy_triangle.setAvgZ()

    copy_cube = sorted(copy_cube, key=lambda triangle: -triangle.avgZ)

    for copy_triangle in copy_cube:
        # Ajuste temporairement la position en Z pour l'affichage
        copy_triangle.origine[2] += 3
        copy_triangle.point1[2] += 3
        copy_triangle.point2[2] += 3

        # Projette et affiche le triangle
        camera.projection_triangle(copy_triangle)
        
        if(copy_triangle.orientation[2] < 0):
            camera.placer_triangle(copy_triangle)

    camera.root.after(20, update)

camera.root.after(1, update)
camera.run()


