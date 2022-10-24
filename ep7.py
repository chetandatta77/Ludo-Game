import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

vertices = (
    (-1,1,1),
    (1,1,1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,1),
    (1,-1,1),
    (1,-1,-1),
    (-1,-1,-1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (1,2),
    (1,5),
    (2,3),
    (2,6),
    (3,7),
    (4,5),
    (4,7),
    (5,6),
    (6,7)
)

surfaces = (
    (0,1,2,3),
    (4,5,6,7),  #front view

    (0,1,5,4),
    (2,3,7,6),  #top view

    (0,4,7,3),
    (1,5,6,2)   #side view
)

colors =(
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,1),
    (1,0,0),
    (0,1,0)
)

ground_vertices = (
    (-20, -2.5, 20),
    (20, -2.5, 20),
    (20, -2.5, -300),
    (-20, -2.5, -300),
)

def ground():

    glBegin(GL_QUADS)
    for vert in ground_vertices:
        glColor3fv((0,0.5,0.5))
        glVertex3fv(vert)

    glEnd()

def cube(vertices):

    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        glColor3fv(colors[x])
        for vertex in surface:

            glVertex3fv(vertices[vertex])
        x += 1
    glEnd()


def set_vertices(max_distance):
    x_value_change = random.randrange(-10,10)
    y_value_change = -1
    z_value_change = random.randrange(-1 * max_distance, -20)

    new_vertices = []

    for vert in vertices:
        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vertices.append([new_x, new_y, new_z])

    return new_vertices


def cc():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50)

    glTranslatef(random.randrange(-5,5), random.randrange(-5,5), -40)



    x_move = 0
    y_move = 0

    cube_dict =[]
    max_distance = 100
    for x in range(40):
        cube_dict.append(set_vertices(max_distance))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = 0.3
                if event.key == pygame.K_RIGHT:
                    x_move = -0.3
                if event.key == pygame.K_DOWN:
                    y_move = 0.3
                if event.key == pygame.K_UP:
                    y_move = -0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_move = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)

        # print x
        # p = [[ c for c in r] for r in x]

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glTranslatef(x_move,y_move,0.3)

        # creating cubes

        for each_cube in cube_dict:
            cube(each_cube)
        ground()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    cc()
    pygame.quit()
    quit()
