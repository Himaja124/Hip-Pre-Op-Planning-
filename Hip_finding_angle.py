import math 
  
# # function for finding the angle 
# def angle_triangle(x1, x2, x3, y1, y2, y3, z1, z2, z3): 
  
#     num = (x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)+(z2-z1)*(z3-z1) 
  
#     den = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)*\
#                 math.sqrt((x3-x1)**2+(y3-y1)**2+(z3-z1)**2) 
  
#     angle = math.degrees(math.acos(num / den)) 
  
#     return round(angle, 3) 
  
# # driver code     
# x1 = 0.13952302932739258
# y1 = 5.028444290161133
# z1 = 3.8233423233032227
# x2 = 0
# y2 = 0
# z2 = 0
# x3 = 3.074296236038208
# y3 = 6.263617038726807
# z3 = -0.5652801394462585
# angle_A = angle_triangle(x1, x2, x3, y1, y2, y3, z1, z2, z3) 
# angle_B = angle_triangle(x2, x3, x1, y2, y3, y1, z2, z3, z1) 
# angle_C = angle_triangle(x3, x2, x1, y3, y2, y1, z3, z2, z1) 
# print("Angles are :") 
# print("angle A = ", angle_A, "degree") 
# print("angle B = ", angle_B, "degree") 
# print("angle C = ", angle_C, "degree") 




import numpy as np

def angle_triangle(x1, x2, x3, y1, y2, y3, z1, z2, z3):
    a = np.array([x1, x2, x3])
    b = np.array([y1, y2, y3])
    c = np.array([z1, z2, z3])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)