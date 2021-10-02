import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, sin, cos, tan


def display():
    #     Clear color
    glClearColor(1,1,0.5,1)
    glClear(GL_COLOR_BUFFER_BIT)
    #     Draw square
    glBegin(GL_QUADS)
    glColor3f(0,1,1)
    glVertex2f( 0.5,-0.5) 
    glVertex2f(-0.5,-0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f( 0.5, 0.5)
    glEnd()
    glFlush()
    #     Draw circle 
    # posx, posy = 0,0    
    # sides = 50
    # radius = 0.5
    # glBegin(GL_POLYGON)
    # glColor3f(0,128,0)
    # for i in range(360):    
    #     cosine= 0.5*radius * cos(i*2*pi/sides) + posx    
    #     sine  = 0.625*radius * sin(i*2*pi/sides) + posy    
    #     glVertex2f(cosine,sine)
    # glEnd()
    # glFlush()
    
def main():
    Title = "Team Tank (H/W Week 2)"
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(800,600)
    glutCreateWindow(Title)    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":

    main()