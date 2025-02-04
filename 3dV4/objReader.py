def lireObj(fichier):
    objet = open(fichier, "r")
    points = []
    liens = []
    forme = []

    for lines in objet.readlines():
        if lines[0] == "v":
            point = []
            for words in lines.split():
                if words != "v":
                    point.append(float(words))
            points.append(point)

        if lines[0] == "f":
            lien = []
            for words in lines.split():
                if words != "f":
                    lien.append(int(words) - 1)
            liens.append(lien)

    for lien in liens:
        triangle = [points[lien[0]], points[lien[1]], points[lien[2]]]
        forme.append(triangle)

    return forme
