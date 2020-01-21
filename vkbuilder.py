import math
import numpy
import json


def von_karman(r, l, th=0.1, cone_res=1000, rot_res=1000, conn=False):
    verts = []
    if conn == True:
        slant = bool(input('Slant: (True / False)\n'))
        lip = float(input('Lip:\n'))
        conn_rad = float(input('Connector inner radius:\n'))
    
    # Create points for outer wall of 2D cone drawing
    outer_wall = []
    for x in [n * (l / cone_res) for n in range(0,cone_res)]:
        theta = math.acos(1-(2*x/l))
        outer_wall.append([x, r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2), 0.0])

    # Create points for inner wall of 2D cone drawing
    inner_wall = []
    for x in [n * (l / cone_res) for n in range(0,cone_res)]:
        theta = math.acos(1-(2*x/l))
        if r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2)-th >= 0:
            inner_wall.append([x, r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2)-th, 0.0])

    # Rotate drawing around x axis by equal steps
    cv_rot = []
    t = 2*math.pi / rot_res
    [list(numpy.dot([[1, 0, 0],[0, math.cos(t), math.sin(t)],[0, math.sin(t)*(-1), math.cos(t)]], v)) for v in verts]
    # cv_rot.append()

    outjson = json.dumps({'Outer': outer_wall, 'Inner': inner_wall})
    
    with open('testfile.json', 'w+') as testfile:
        testfile.writelines(outjson)
    
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
    # print(list(numpy.dot([[1, 0, 0],[0, math.cos(math.pi), math.sin(math.pi)],[0, math.sin(math.pi)*(-1), math.cos(math.pi)]], [1,2,0])))
    print(von_karman(1, 4))