import math


# R = float(input('Base radius\n'))
# L = float(input('Ogive length\n'))
# th = float(input('Thickness\n'))
# res = int(input('Resolution\n'))
# filename = input('Name your obj file\n')
# lip = input('Lip taper?\n')

# orad = (R**2 + L**2) / (2*R)

# print('Ogive Radius: ' + str(orad))

def div_circ(r,n=1000):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]

def von_karman(r, l, x):
    theta = math.acos(1-(2*x/l))
    y = r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2)
    return y

def gen_cone(radius, length, thickness, resolution=1000):
    orad = (radius**2 + length**2) / (2*radius)
    return div_circ(orad)

# def write_obj():
#     filename = input('Filename\n') + '.obj'
#     vertices = []
#     normals = []
#     faces = []
#     with open(filename, "w+") as obj:
#         for v in vertices:
#             obj.write(f'v {v[0]} {v[1]} {v[2]}\n')

#         for vn in normals:
#             obj.write(f'vn {vn[0]} {vn[1]} {vn[2]}\n')

#         for f in faces:
#             obj.write(f'f {f[0]}//{f[0]} {f[0]}//{f[0]} {f[0]}//{f[0]}\n')  

#         obj.close()

if __name__ == "__main__":
    print(gen_cone(input('Radius\n'), input('Length\n'), 2))