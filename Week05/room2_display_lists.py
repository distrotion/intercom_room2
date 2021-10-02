import sys, os
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import pandas as pd
import math as m
import time

win_w, win_h = 1024, 768
models = {}


def reshape(w, h):
    global win_w, win_h

    win_w, win_h = w, h
    glViewport(0, 0, w, h)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1,50)

wireframe, pause = False, True
def keyboard(key, x, y):
    global wireframe, pause

    key = key.decode("utf-8")
    if key == ' ':
        pause = not pause
        glutIdleFunc(None if pause else idle)
    elif key == 'w':
        wireframe = not wireframe
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe else GL_FILL)
    elif key == 'q':
        os._exit(0)
    glutPostRedisplay()

tick, frame_cnt = 0, 0
def idle():
    global tick, frame_cnt

    tick += 1
    frame_cnt += 1
    glutPostRedisplay()

def display():
    global start_time, frame_cnt
    if frame_cnt == 20:
        print("%.2f fps" % (frame_cnt/(time.time()-start_time)), tick, end='\r')
        start_time = time.time()
        frame_cnt = 0    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*(centroid+(0,5, max(bbox))), *centroid, 0, 1, 0)
    
    callList = 1
    for i in range(5):
        for j in range(6):
            if callList == 1 and i==0 and j==0:
                glScale(0.1,0.1,0.1)     
            else: 
                glScale(1,1,1)
            if i==0 and j==0:
                glTranslate(-60,0,0)
            glTranslate(15,0,0)   
            glCallList(callList)
        glTranslate(-15*(j+1),0,-15)
    
    # callList = 2
    # glScale(10,10,10) 
    # glCallList(callList)  
            
            
    # glBegin(GL_TRIANGLES)
    # for i in range(n_vertices):
    #     glColor3fv(0.5 * (normals[i] + 1))
    #     glVertex3fv(positions[i])
    # glEnd()
    
    glutSwapBuffers()

def compile_list_on_model(model_filename, list_id):
    global positions,n_vertices,normals
    df = pd.read_csv(model_filename, delim_whitespace=True, comment='#',
                     header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)
    
    positions = df.values[:, 0:3]
    normals = df.values[:, 3:6]
    n_vertices = len(positions)

    glNewList(list_id,GL_COMPILE)
    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(0.5 * (normals[i] + 1))
        glVertex3fv(positions[i])
    glEnd()
    glEndList()

    # glNewList(list_id,GL_COMPILE)
    # glEnableClientState(GL_VERTEX_ARRAY)
    # glEnableClientState(GL_COLOR_ARRAY)
    # glVertexPointer(3,GL_FLOAT,0,positions)
    # glColorPointer(3,GL_FLOAT,0,normals)
    # glDrawArrays(GL_TRIANGLES,0,n_vertices)
    # glDisableClientState(GL_VERTEX_ARRAY)
    # glEndList()

    return list_id, centroid, bbox

def gl_init_models():
    global centroid, bbox, start_time

    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    models["bunny"], centroid, bbox = compile_list_on_model("./bunny.tri",1)
    models["horse"], _, _ = compile_list_on_model("./horse.tri", 2)
    # models["monkey"], _, _ = compile_list_on_model("./monkey.tri", 3)
    start_time = time.time() - 0.0001

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(win_w, win_h)
    glutCreateWindow("Display Lists Exercise")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    gl_init_models()
    glutMainLoop()

if __name__ == "__main__":
    main()