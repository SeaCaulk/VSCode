
# from numpy import array
# # array=array([['---' for _ in range(12)] for _ in range(12)])

# # print(array)
# # for i in range(5):
# #     print((1-i)%5)
# import numpy as np

# # Set print options to show more precision and prevent scientific notation
# np.set_printoptions(precision=2, suppress=True)

# # Create an array with large numbers
# a = np.array([12345, 67890, 1234567, 987654321])

# print(a)
# with open("test.txt", "w") as file:
#     file.write("Hello, World!")
# print(open("test.txt", "r").read())
# import tkinter as tk

# # Create the main window
# window = tk.Tk()
# window.title("PythonExamples.org")
# window.geometry("600x400")

# label = tk.Label(window, text="Enter your input")
# label.pack()

# # Create an Entry widget
# entry = tk.Entry(window, bg="lightgreen")
# entry.pack()

# # Run the application
# window.mainloop()
# import sys
# print(sys.path)
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
defib=[]
defibMin=''
lon = input()
lat = input()
n = int(input())
minDist=0
RanOnce=False
for i in range(n):
    defib.append(input().split(";;"))
    j=defib[i][0].split(";")+[float(x) for x in defib[i][1].replace(",",".").split(";")]
    defib[i]=j
    j=6371*math.sqrt((((defib[i][4]-float(lon))*math.pi/180)*math.cos(((defib[i][3]+float(lat))*math.pi/180)/2))**2+((defib[i][3]-float(lat))*math.pi/180)**2)
    if not RanOnce:
        RanOnce=True
        minDist=j
        defibMin=defib[i][1]
    elif minDist>j:
        minDist=j
        defibMin=defib[i][1]
    # Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(defibMin)


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x_list=[]
y_list=[]
flatSurfaces=[]
surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    x_list.append(land_x)
    y_list.append(land_y)
for i in range(1,len(x_list)):
    if x_list[i]!=x_list[i-1]:
        if y_list[i]==y_list[i-1]:
            flatSurfaces.append([(x_list[i]+x_list[i-1])/2,y_list[i]])
ranOnce=False
P=0
R=0
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    LSX=0
    LSY=0
    while ranOnce==False:
        min=0
        for i in range(len(flatSurfaces)):
            if flatSurfaces[i][0]-x<min:
                min=flatSurfaces[i][0]-x
                LSX=flatSurfaces[i][0]
                LSY=flatSurfaces[i][1]
        ranOnce=True

    if x>LSX and R>-90:
        R-=15
    elif x<LSX and R<90:
        R+=15
    if v_speed<-40 and P<4:
        P+=1
    elif v_speed>0 and P>0:
        P-=1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(R,P)
L=[]
n = int(input())
for i in range(n):
    L.append(w=input().split(''))