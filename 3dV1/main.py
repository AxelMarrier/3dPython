import tkinter as tk
import math

""" Fonctions """
def ligne(points):
    canvas.create_line(points[0][0] + 4,
                       points[0][1] + 4,
                       points[1][0] + 4,
                       points[1][1] + 4)

def crdToCanvas(point):
    x = (focal_length * point[0]) / (point[2] + focal_length)
    y = -(focal_length * point[1]) / (point[2] + focal_length)
    offset = 4
    return [x + canvas_width // 2 - offset,
            y + canvas_height // 2 - offset,
            x + canvas_width // 2 + offset,
            y + canvas_height // 2 + offset]

def rotateX(point):
    new_x = point[0]
    new_y = (point[1] * math.cos(math.radians(angle))) - (point[2] * math.sin(math.radians(angle)))
    new_z = (point[1] * math.sin(math.radians(angle))) + (point[2] * math.cos(math.radians(angle)))
    return [new_x,new_y,new_z]
def rotateY(point):
    new_x = (point[0] * math.cos(math.radians(angle))) - (point[2] * math.sin(math.radians(angle)))
    new_y = point[1]
    new_z = (point[0] * math.sin(math.radians(angle))) + (point[2] * math.cos(math.radians(angle)))
    return [new_x,new_y,new_z]

def rotateZ(point):
    new_x = (point[0] * math.cos(math.radians(angle))) - (point[1] * math.sin(math.radians(angle)))
    new_y = (point[0] * math.sin(math.radians(angle))) + (point[1] * math.cos(math.radians(angle)))
    new_z = point[2]
    return [new_x,new_y,new_z]

def update():
    canvas.delete("all")

    global liste_point
    liste_point = [rotateX(point) for point in liste_point]
    liste_point = [rotateY(point) for point in liste_point]
    liste_point = [rotateZ(point) for point in liste_point]

    liste_point_translation = [apply_translation(point, global_position) for point in liste_point]

    liste_point_perspective = [crdToCanvas(point) for point in liste_point_translation]

    [canvas.create_oval(point[0], point[1], point[2], point[3], fill="black") for point in liste_point_perspective]

    lignes = [
        [liste_point_perspective[0],liste_point_perspective[1]],
        [liste_point_perspective[1], liste_point_perspective[3]],
        [liste_point_perspective[2], liste_point_perspective[3]],
        [liste_point_perspective[2], liste_point_perspective[0]],
        [liste_point_perspective[0], liste_point_perspective[4]],
        [liste_point_perspective[1], liste_point_perspective[4]],
        [liste_point_perspective[2], liste_point_perspective[4]],
        [liste_point_perspective[3], liste_point_perspective[4]],
    ]

    [ligne(points) for points in lignes]
    root.after(20, update)

def on_key_press(event):
    global global_position
    if event.keysym == "Left":
        global_position[0] += 10
    elif event.keysym == "Right":
        global_position[0] -= 10
    elif event.keysym == "Up":
        global_position[1] -= 10
    elif event.keysym == "Down":
        global_position[1] += 10

def apply_translation(point, translation):
    return [point[0] + translation[0], point[1] + translation[1], point[2] + translation[2]]


"""  Crée la fenêtre principale """
root = tk.Tk()

""" Crée le canevas """
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

""" Variables """

focal_length = 500

global_position = [0, 0, 0]

angle = 2

a = [-100, -100, -100]
b = [100, -100, -100]
c = [-100, -100, 100]
d = [100, -100, 100]
e = [0, 100, 0]

liste_point = [a,b,c,d,e]

# input

root.bind("<KeyPress>", lambda event: on_key_press(event))


update()

root.mainloop()
