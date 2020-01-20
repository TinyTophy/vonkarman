import math


def von_karman(r, l, resolution=1000):
    cone_verts = []
    for x in [n * (l / resolution) for n in range(0,resolution)]:
        theta = math.acos(1-(2*x/l))
        cone_verts.append((x, r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2), 0.0))
    return cone_verts

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
    print(von_karman(1, 4))