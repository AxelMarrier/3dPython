import tkinter as tk
import math


class Canvas3D:

    def __init__(self, width, height, fov, Zmax, Zmin, nom):

        self.width = width
        self.height = height
        self.fov = math.radians(fov)
        self.Zmax = Zmax
        self.Zmin = Zmin

        # Initialisation de Tkinter
        self.root = tk.Tk()
        self.root.title(nom)
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="green")
        self.canvas.pack()

    def projection_point(self, coords):
        a = self.height / self.width                #Aspect ratio, X s'adapte à la hauteur pour pas tout déformer
        f = 1/math.tan(self.fov / 2)                #Field Of View, fov bas signifie zoom
        q = self.Zmax / (self.Zmax - self.Zmin)     #Normalisation de Z
        p = (-self.Zmax * self.Zmin) / (self.Zmax - self.Zmin)

        x, y, z = coords

        if z != 0:
            return [(a * f * x) / z,
                    (f * y) / z,
                    z * q + p]
        else:
            return [(a * f * x),
                    (f * y),
                    z * q - q * self.Zmin]

    def projection_triangle(self, triangle):
        triangle.setOrigine(self.projection_point(triangle.origine))
        triangle.setPoint1(self.projection_point(triangle.point1))
        triangle.setPoint2(self.projection_point(triangle.point2))
        triangle.setOrientation()

    def placer_point(self, coords):
        x, y, z = coords

        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")



    def placer_ligne(self, start, end):
        start_x, start_y, start_z = start
        end_x, end_y, end_z = end

        self.canvas.create_line(start_x,
                                start_y,
                                end_x,
                                end_y,
                                fill="black")



    def placer_triangle(self, triangle):
        origine0 = triangle.origine[0] + 1
        origine1 = triangle.origine[1] + 1
        origine2 = triangle.origine[2]
        point10 = triangle.point1[0] + 1
        point11 = triangle.point1[1] + 1
        point12 = triangle.point1[2]
        point20 = triangle.point2[0] + 1
        point21 = triangle.point2[1] + 1
        point22 = triangle.point2[2]

        origine0 *= 0.5 * self.width
        origine1 *= 0.5 * self.height
        point10 *= 0.5 * self.width
        point11 *= 0.5 * self.height
        point20 *= 0.5 * self.width
        point21 *= 0.5 * self.height
        
        color_value = int(triangle.orientation[2] * -255)
        color = f"#{color_value:02x}{color_value:02x}{color_value:02x}"

        self.canvas.create_polygon(origine0, origine1,
                                   point10, point11, 
                                   point20, point21,
                                   fill=color)
        
        #self.placer_point([origine0, origine1, origine2])
        #self.placer_point([point10, point11, point12])
        #self.placer_point([point20, point21, point22])

        #self.placer_ligne([origine0, origine1, origine2], [point10, point11, point12])
        #self.placer_ligne([origine0, origine1, origine2], [point20, point21, point22])
        #self.placer_ligne([point20, point21, point22], [point10, point11, point12])


    def run(self):
        """
        Lance la boucle principale de Tkinter.
        """
        self.root.mainloop()