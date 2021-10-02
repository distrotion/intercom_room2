import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def display():
    glClearColor(1, 1, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex2f( 0.9,-0.9) 
    # glColor3f(1,1,0)
    glVertex2f(-0.9,-0.9)
    # glColor3f(1,1,1)
    glVertex2f(-0.9, 0.9)
    # glColor3f(1,0,0)
    glVertex2f( 0.9, 0.9)  
    glEnd()
    glFlush()


    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Program Template")
    glutDisplayFunc(display)


    glutMainLoop()


if __name__ == "__main__":
    main()