import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import pandas as pd

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*(centroid+(0, 10, max(bbox))), *centroid, 0, 1, 0)
    glRotatef(degree, 0, 1, 0)
    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(0.5 * (normals[i] + 1))
        glVertex3fv(positions[i])
    glEnd()

    ### create triangle mesh
    if trimesh:
        drawMesh()
        if wireframe:    
            glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    ### create normal line
    if normLine:
        drawNormVector()

    glutSwapBuffers()

def drawMesh():
    
    glColor4f(1,1,1,1)
    ##no shader function
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    ###Draw triangle mesh 
    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glVertex3fv(positions[i])
    glEnd()
    
    ####Another method to draw a triagle mesh
    # glVertexPointer(3, GL_FLOAT, 0, positions)
    # glEnableClientState(GL_VERTEX_ARRAY)
    # glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    # glDrawArrays(GL_TRIANGLES,0,n_vertices)
    # glDisableClientState(GL_VERTEX_ARRAY)
 

def drawNormVector():
    # glPointSize(5) 
    glBegin(GL_LINES)
    for i in range(n_vertices):
      if i%3 == 0:
        ###Find vector of all 3 points
        aVector = positions[i]
        bVector = positions[i+1]
        cVector = positions[i+2]

        ###Find vector of each connected point
        uVector = aVector-bVector
        vVector = cVector-bVector
        
        ###Find middle point of triangle 
        sumVector = (aVector+bVector+cVector)
        midStartPoint = sumVector/3 

        ###Find end point of normal vector
        normalVector =midStartPoint-np.cross(uVector,vVector)

        ###Find end point of unit normal vector
        unitNVector = normalVector / np.linalg.norm(normalVector)

        ###Find normal vector coordiate (Start Point + End Point)
        normalVector = midStartPoint + unitNVector
        
        glColor3f(1,0,0)
        glVertex3fv(midStartPoint)
        glColor3f(0,1,0)
        glVertex3fv(normalVector)

    glEnd()  

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1, 50)

degree = 0
def idle():
    global degree
    degree = degree + 1
    glutPostRedisplay()

wireframe, animation,trimesh,normLine = False, False, False, False
def keyboard(key, x, y):
    global wireframe, animation, trimesh, normLine

    key = key.decode("utf-8")
    if key == ' ':
        animation = not animation
        glutIdleFunc(idle if animation else None)
    elif key == 'w':
        wireframe = not wireframe
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe else GL_FILL)
    elif key == 'd': ##turn on/off triangle mesh
        trimesh = not trimesh
    elif key == 's': ##turn on/off normal line
        normLine = not normLine
    elif key == 'q':
        exit(0)
    glutPostRedisplay()

def my_init():
    global n_vertices, positions, colors, normals, uvs
    global centroid, bbox

    glClearColor(0.2, 0.8, 0.8, 1)
    df = pd.read_csv("./ashtray.tri", delim_whitespace=True, comment='#',
                     header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    n_vertices = len(positions)
    print("no. of vertices: %d, no. of triangles: %d" % 
          (n_vertices, n_vertices//3))    
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glLineWidth(1)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1024, 768)
    glutCreateWindow("Show Normals")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    my_init()
    glutMainLoop()    

if __name__ == "__main__":
    main()