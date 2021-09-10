import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, sin, cos, tan

def display():
    glClearColor(1,1,0.5,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3f(0,1,1)
    glVertex2f( 0.5,-0.5) 
    glVertex2f(-0.5,-0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f( 0.5, 0.5)  
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Program Template")
    glutDisplayFunc(display)

    glutMainLoop()

if __name__== "__main__":
    main()