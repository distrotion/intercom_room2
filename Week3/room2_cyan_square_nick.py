import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, sin, cos, tan

def display():
    glClearColor(1,1,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,1,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,-0.5,0.0)
    glVertex3f(-0.5,0.5,0.0)
    glVertex3f(0.5,0.5,0.0)
    glVertex3f(0.5,-0.5,0.0)
    glEnd()
    # Draw circle 
    posx, posy = 0,0   
    sides = 50
    radius = 0.3
    glBegin(GL_POLYGON)
    glColor3f(0,128,0)
    for i in range(360):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    
    glFlush()

def reshape(w,h):
    
    xSpan = 1.0
    ySpan = 1.0
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    if (w/h > 1):
        # Width > Height, so scale xSpan accordinly.
        xSpan = w/h
    else:
        #Height >= Width, so scale ySpan accordingly.
        ySpan = h/w
    
    gluOrtho2D(-1*xSpan,xSpan,-1*ySpan,ySpan) #(left,right,bottom,top)
    glViewport(0,0,w,h)
   
def main():

    Title = "Team Tank (H/W Week 2)"
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Program Template")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__== "__main__":
    main()