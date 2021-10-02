import sys
import os
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5,-0.5)
    glVertex2f(0.5,-0.5)
    glVertex2f(0,0.5)
    glEnd()
    glutSwapBuffers()


def reshape(w,h):
    xSpan = 1.0
    ySpan = 1.0
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if (w/h > 1):
        # Width > Height, so scale xSpan accordinly.
        xSpan = w/h
    else:
        #Height >= Width, so scale ySpan accordingly.
        ySpan = h/w
    
    gluOrtho2D(-1*xSpan,xSpan,-1*ySpan,ySpan) #(left,right,bottom,top)

def moveUp():
    glTranslate(0,0.0005,0)
    glutPostRedisplay()
def moveDown():
    glTranslate(0,-0.0005,0)
    glutPostRedisplay()
def moveLeft():
    glTranslate(-0.0005,0,0)
    glutPostRedisplay()

def moveRight():
    glTranslate(0.0005,0,0)
    glutPostRedisplay()

def spin():
    glRotate(0.1,0,0,1)
    glutPostRedisplay()
    
up,rotate,down,left,right = False,False,False,False,False
def keyboard(key,x,y):
    global up,rotate,down,left,right
    key = key.decode("utf-8")
    
    if key == ' ':
        rotate = not rotate
        glutIdleFunc(spin if rotate else None)
    if key == 'i':
        up = not up
        glutIdleFunc(moveUp if up else None)
    if key == 'k':
        down = not down
        glutIdleFunc(moveDown if down else None)
    if key == 'j':
        left = not left
        glutIdleFunc(moveLeft if left else None)
    if key == 'l':
        right = not right
        glutIdleFunc(moveRight if right else None)
    glutPostRedisplay()

def my_init():
    glEnable(GL_DEPTH_TEST)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE|GLUT_DEPTH)
    glutInitWindowSize(1024,768)
    glutCreateWindow("Key board Control")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    my_init()
    glutMainLoop()

if __name__=="__main__":
    main()