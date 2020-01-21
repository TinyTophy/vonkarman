import math
import numpy
import json


def von_karman(r=1, l=4, th=0, cone_res=1000, rot_res=1000, conn=False):
    verts = []
    if conn == True:
        slant = bool(input('Slant: (True / False)\n'))
        lip = float(input('Lip:\n'))
        conn_rad = float(input('Connector inner radius:\n'))
        conn_len = float(input('Connector length\n'))
    if th == 0:
        th = r*0.07

    # Create points for outer wall of 2D cone drawing
    outer_wall = []
    for x in [n * (l / cone_res) for n in range(0,cone_res+1)]:
        theta = math.acos(1-(2*x/l))
        outer_wall.append([x, round(r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2),6), 0.0])
    # outer_wall.append([r,])Inn

    # Create points for inner wall of 2D cone drawing
    inner_wall = []
    for x in [n * (l / cone_res) for n in range(0,cone_res+1)]:
        theta = math.acos(1-(2*x/l))
        if r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2)-th >= 0 and x <= 0.9375*l:
            inner_wall.append([x, round(r/math.sqrt(math.pi)*math.sqrt(theta - math.sin(2*theta)/2)-th,6), 0.0])
    inner_wall[0][1] = 0.0
    slant_eq = [0.0625*l + l, inner_wall[-1][1] , 0.0] - x

    # Rotate drawing around x axis by equal steps
    cv_rot = []
    t = 2*math.pi / rot_res
    [list(numpy.dot([[1, 0, 0],[0, math.cos(t), math.sin(t)],[0, math.sin(t)*(-1), math.cos(t)]], v)) for v in verts]
    # cv_rot.append()

    outjson = json.dumps({'Outer': outer_wall, 'Inner': inner_wall})
    
    with open('testfile.json', 'w+') as testfile:
        testfile.writelines(outjson)

    def pt_slope_solver(pt1, m):
        pt2 = y - y1 = m*(x-x1)
        return pt2
    
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
    von_karman()