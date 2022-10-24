from __future__ import division
from __future__ import print_function

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# import OpenGL.GLUT.fonts as fp

import numpy as np
from cmath import *
from random import randint

in_about = 1
in_guide = 1

# (f1,h1) (f2,h2) ----->player1

f1 = 0  # player1 coin1 enters the game
f2 = 0 # player1 coin1 enters the game
g1 = 0
g2 = 0
k1 = 0  # down d coin1
k2 = 0  # down u coin2
l1 = 0  # up d coin1
l2 = 0  # up u coin2
ply1 = 0  # chance
ply2 = 0  # chance
h1 = 0  # player1 coin1 wins the game
h2 = 0 # player1 coin2 wins the game
h3 = 0
h4 = 0
s1 = 0
s2 = 0
u = 0
v = 0
r1 = 0
op = 0
w = 0
dice1 = 0
enter = 0

ch1 = 0 # chances inside player2
ch = 0 # chances inside player1
p1 = 0  # just step from sq 1 of coin1
p2 = 0  # just step from sq 1 of coin2
ra1 = 0 # random number
z = 0
z1 = 0
za1 = 0

a = [[-0.4, -0.325], [-0.1375, -0.7275], [-0.1375, -0.61], [-0.1375, -0.4925], [-0.1375, -0.375], [-0.1375, -0.2575],
     [-0.2575, -0.14], [-0.375, -0.14], [-0.495, -0.14], [-0.6110, -0.14], [-0.7275, -0.14], [-0.84, -0.14],
     [-0.84, 0.005], [-0.84, 0.1375], [-0.7275, 0.1375], [-0.6110, 0.1375], [-.495, .1375], [-0.375, 0.1375],
     [-0.2575, 0.1375], [-0.1375, 0.2575], [-0.1375, 0.375], [-0.1375, 0.4925], [-0.1375, 0.61], [-0.1375, 0.7275],
     [-0.1375, 0.845], [0, 0.845], [0.1375, 0.845], [0.1375, 0.7275], [0.1375, 0.61], [0.1375, 0.4925], [0.1375, 0.375],
     [0.1375, 0.2575], [0.2575, 0.1375], [0.375, 0.1375], [.495, 0.14], [0.6110, 0.1375], [0.7275, 0.1375],
     [0.84, 0.1375], [0.84, 0.005], [0.84, -0.14], [0.7275, -0.14], [0.6110, -0.14], [.495, -0.14], [0.375, -0.14],
     [0.2575, -0.14], [0.1375, -0.2575], [0.1375, -0.375], [0.1375, -0.4925], [0.1375, -0.61], [0.1375, -0.7275],
     [0.1375, -0.845], [0, -0.845], [0, -0.7275], [0, -0.61], [0, -0.4925], [0, -0.375], [0, -0.2575]]
# coin down path
b = [[-0.4, -0.325], [0.1375, 0.7275], [0.1375, 0.61], [0.1375, 0.4925], [0.1375, 0.375], [0.1375, 0.2575],
     [0.2575, 0.1375], [0.375, 0.1375], [0.495, 0.14], [0.6110, 0.1375], [0.7275, 0.1375], [0.84, 0.1375],
     [0.84, 0.005], [0.84, -0.14], [0.7275, -0.14], [0.6110, -0.14], [.495, -.14], [0.375, -0.14], [0.2575, -0.14],
     [0.1375, -0.2575], [0.1375, -0.375], [0.1375, -0.4925], [0.1375, -0.61], [0.1375, -0.7275], [0.1375, -0.845],
     [0, -0.845], [-0.1375, -0.845], [-0.1375, -0.7275], [-0.1375, -0.61], [-0.1375, -0.4925], [-0.1375, -0.375],
     [-0.1375, -0.2575], [-0.2575, -0.14], [-0.375, -0.14], [-.495, -0.14], [-0.6110, -0.14], [-0.7275, -0.14],
     [-0.84, -0.14], [-0.84, 0.005], [-0.84, 0.1375], [-0.7275, 0.1375], [-0.6110, 0.1375], [-.495, 0.1375],
     [-0.375, 0.1375], [-0.2575, 0.1375], [-0.1375, 0.2575], [-0.1375, 0.375], [-0.1375, 0.4925], [-0.1375, 0.61],
     [-0.1375, 0.7275], [-0.1375, 0.845], [0, 0.845], [0, 0.7275], [0, 0.61], [0, 0.4925], [0, 0.375], [0, 0.2575]]
c = [[-0.5, -0.7], [-0.7, -0.5]]
d = [[0.5, 0.7], [0.7, 0.5]]
A = [[430, 527], [630, 608], [626, 567], [628, 528], [626, 485], [629, 441], [585, 397], [544, 398], [502, 400],
     [463, 397], [420, 395], [381, 397], [380, 350], [377, 304], [421, 303], [460, 304], [501, 301], [541, 302],
     [585, 300], [627, 260], [627, 221], [627, 177], [627, 138], [627, 97], [627, 58], [676, 56], [723, 54], [723, 96],
     [725, 138], [724, 176], [725, 216], [723, 258], [764, 300], [809, 303], [850, 304], [890, 304], [931, 303],
     [972, 303], [971, 352], [973, 398], [932, 396], [890, 396], [851, 395], [811, 395], [768, 396], [724, 441],
     [725, 484], [724, 523], [725, 562], [725, 606], [728, 645], [677, 645], [677, 608], [677, 565], [677, 522],
     [677, 485], [677, 442]]
B = [[853, 104], [723, 96], [725, 138], [724, 176], [725, 216], [723, 258], [764, 300], [809, 303], [850, 304],
     [890, 304], [931, 303], [972, 303], [971, 352], [973, 398], [932, 396], [890, 396], [851, 395], [811, 395],
     [768, 396], [724, 441], [725, 484], [724, 523], [725, 562], [725, 606], [728, 645], [677, 645], [629, 650],
     [630, 608], [626, 567], [628, 528], [626, 485], [629, 441], [585, 397], [544, 398], [502, 400], [463, 397],
     [420, 395], [381, 397], [380, 350], [377, 304], [421, 303], [460, 304], [501, 301], [541, 302], [585, 300],
     [627, 260], [627, 221], [627, 177], [627, 138], [627, 97], [627, 58], [676, 56], [677, 97], [677, 137], [677, 177],
     [677, 219], [677, 261]]

for i in range(100-57):
    a.append([0,0])
    b.append([0,0])
    A.append([0,0])
    B.append([0,0])

for i in range(10-2):
    c.append([0,0])
    d.append([0,0])

in_about = 1


def myReshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if w <= h:
        glOrtho(-1.0, 1.0, -1.0 * h / w, 2.0 * h / w, -20.0, 20.0)
    else:
        glOrtho(-w / h, w / h, -1.0, 1.0, -20.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()


def dice(y):
    glPointSize(5)
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(-0.82, 0.25)
    glVertex2f(-0.82, 0.38)
    glVertex2f(-0.69, 0.38)
    glVertex2f(-0.69, 0.25)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.82, 0.38)
    glVertex2f(-0.69, 0.38)
    glVertex2f(-0.67, 0.4)
    glVertex2f(-0.79, 0.4)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.69, 0.38)
    glVertex2f(-0.67, 0.4)
    glVertex2f(-0.67, 0.27)
    glVertex2f(-0.69, 0.25)
    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.82, 0.38)
    glVertex2f(-0.69, 0.38)
    glVertex2f(-0.67, 0.4)
    glVertex2f(-0.79, 0.4)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.69, 0.38)
    glVertex2f(-0.67, 0.4)
    glVertex2f(-0.67, 0.27)
    glVertex2f(-0.69, 0.25)
    glEnd()
    glColor3f(0, 0, 0)

    def case1():
        glBegin(GL_POINTS)
        glVertex2f(-0.75, 0.31)
        glEnd()

    def case2():
        glBegin(GL_POINTS)
        glVertex2f(-0.73, 0.31)
        glVertex2f(-0.77, 0.31)
        glEnd()

    def case3():
        glBegin(GL_POINTS)
        glVertex2f(-0.72, 0.31)
        glVertex2f(-0.755, 0.31)
        glVertex2f(-0.79, 0.31)
        glEnd()

    def case4():
        glBegin(GL_POINTS)
        glVertex2f(-0.72, 0.285)
        glVertex2f(-0.72, 0.345)
        glVertex2f(-0.78, 0.285)
        glVertex2f(-0.78, 0.345)
        glEnd()

    def case5():
        glBegin(GL_POINTS)
        glVertex2f(-0.72, 0.285)
        glVertex2f(-0.72, 0.345)
        glVertex2f(-0.75, 0.31)
        glVertex2f(-0.78, 0.285)
        glVertex2f(-0.78, 0.345)
        glEnd()

    def case6():
        glBegin(GL_POINTS)
        glVertex2f(-0.72, 0.29)
        glVertex2f(-0.755, 0.29)
        glVertex2f(-0.79, 0.29)
        glVertex2f(-0.72, 0.34)
        glVertex2f(-0.755, 0.34)
        glVertex2f(-0.79, 0.34)
        glEnd()

    switch = {1: case1, 2: case2, 3: case3, 4: case4, 5: case5, 6: case6}

    switch[y]()
    glPointSize(25)
    glFlush()


def myMouse(btn, state, x, y):
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1, in_about
    C = []

    for i in range(10):
        C.append([0] * 10)
    # rand = GLint()

    D = []
    for i in range(10):
        D.append([0] * 10)

    C[0][0] = A[k2][0]
    C[0][1] = A[k2][1]
    C[1][0] = A[k1][0]
    C[1][1] = A[k1][1]
    D[0][0] = B[l2][0]
    D[0][1] = B[l2][1]
    D[1][0] = B[l1][0]
    D[1][1] = B[l1][1]

    print(ra1, k1, k2, l1, l2, x, y, z)
    print()
    if ra1 + k1 > 57 or ra1 + k2 > 57 or ra1 + l1 > 57 or ra1 + l2 > 57:
        z = 1
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        if ply1 == 1 and ply2 == 0:

            if k1 == 0 and 483 < x < 517 and 615 > y > 580:

                if ra1 == 6 or ra1 == 1:
                    player1(1)
                else:
                    player1(2)

            elif k2 == 0 and 412 < x < 447 and 510 < y < 545:

                if ra1 == 6 or ra1 == 1:
                    player1(2)
                else:
                    player1(1)

            elif (C[0][0] - 20) < x < (C[0][0] + 20) and (C[0][1] - 20) < y < (C[0][1] + 20) and z1 == 1 and k2 > 0:
                player1(2)
            elif (C[1][0] - 20) < x < (C[1][0] + 20) and (C[1][1] - 20) < y < (C[1][1] + 20) and z1 == 1 and k1 > 0:
                player1(1)
            if z == 1 and dice1 == 1:
                z = 0
                z1 = 1
                ra1 = randint(1, 1000) % 2 + randint(1, 1000) % 3 + randint(1, 1000) % 2 + randint(1, 1000) % 3
                # ra1=6
                if ra1 == 0:
                    ra1 = 1
                dice(ra1)

        else:
            if l1 == 0 and 833 < x < 873 and 84 < y < 124:

                if ra1 == 6 or ra1 == 1:
                    player2(1)
                else:
                    player2(2)

            elif l2 == 0 and 906 < x < 940 and 158 < y < 190:

                if ra1 == 6 or ra1 == 1:
                    player2(2)
                else:
                    player2(1)

            elif (D[0][0] - 20) < x < (D[0][0] + 20) and (D[0][1] - 20) < y < (D[0][1] + 20) and z1 == 1 and l2 > 0:
                player2(2)
            elif (D[1][0] - 20) < x < (D[1][0] + 20) and (D[1][1] - 20) < y < (D[1][1] + 20) and z1 == 1 and l1 > 0:
                player2(1)

            if z == 1 and dice1 == 1:
                z = 0
                z1 = 1
                ra1 = randint(1, 1000) % 2 + randint(1, 1000) % 3 + randint(1, 1000) % 2 + randint(1, 1000) % 3
                ra1 =6
                if ra1 == 0:
                    ra1 = 1
                dice(ra1)


def key(key, x, y):
    if ord(key) == 113 or ord(key) == 81:
        call(2)
        # QUIT q or Q
    if ord(key) == 13 and enter == 1:
        call(1)
        wait()
        display_enter1()
        display1()
        # Enter button


def call(w):
    def case1():
        global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1, in_about
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 0)
        glFlush()

        f1 = 0
        f2 = 0
        g1 = 0
        g2 = 0
        k1 = 0
        k2 = 0
        l1 = 0
        l2 = 0
        ply1 = 1
        ply2 = 0
        h1 = 0
        h2 = 0
        h3 = 0
        h4 = 0
        s1 = 0
        s2 = 0
        c[0][0] = -0.5
        c[0][1] = -0.7
        c[1][0] = -0.7
        c[1][1] = -0.5
        d[0][0] = 0.5
        d[0][1] = 0.7
        d[1][0] = 0.7
        d[1][1] = 0.5
        wait()

    def case2():
        x = glutGetWindow()
        glutDestroyWindow(x)

    switch = {1: case1, 2: case2}
    switch[w]()


def about():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1, in_about
    about = "\t\t\tMATCH IS DRAWN ! \n\n\n\n\n\n\n\n\n\n\n\n\n\n\nQ = QUIT   ENTER = RESTART"
    en = GLUT_BITMAP_TIMES_ROMAN_24

    x = -0.4
    y = 0.3
    z = 0

    in_about = 1

    glPushMatrix()
    glLoadIdentity()

    glColor3f(0.9, 0.7, 0.6)
    glRasterPos3f(x, y, z)

    for i in range(len(about)):
        if about[i] == '\n':
            y -= 0.08
            glRasterPos3f(x, y, z)
        if about[i] == '\t':
            x -= 0.03
        else:
            wait()
            glutBitmapCharacter(en, ord(about[i]))

    glPopMatrix()
    glFlush()
    enter = 1


def about1():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1, in_about
    about = "\t\t\tCONGRATULATIONS  !\n\n\nPLAYER  1  WON  THE  GAME.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nQ = QUIT   ENTER = RESTART"
    en = GLUT_BITMAP_TIMES_ROMAN_24

    x = -0.4
    y = 0.6
    z = 0

    in_about = 1

    glPushMatrix()
    glLoadIdentity()

    glColor3f(0.9, 0.7, 0.6)
    glRasterPos3f(x, y, z)

    for i in range(len(about)):
        if about[i] == '\n':
            y -= 0.08
            glRasterPos3f(x, y, z)
        if about[i] == '\t':
            x -= 0.03
        else:
            wait()
            glutBitmapCharacter(en, ord(about[i]))

    glPopMatrix()
    glFlush()
    enter = 1


def about2():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1, in_about
    about = "\t\t\tCONGRATULATIONS  !\n\n\nPLAYER  2  WON  THE  GAME.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nQ = QUIT   ENTER = RESTART"
    en = GLUT_BITMAP_TIMES_ROMAN_24
    x = -0.4
    y = 0.6
    z = 0

    in_about = 1

    glPushMatrix()
    glLoadIdentity()

    glColor3f(0.9, 0.7, 0.6)
    glRasterPos3f(x, y, z)

    for i in range(len(about)):
        if about[i] == '\n':
            y -= 0.08
            glRasterPos3f(x, y, z)
        if about[i] == '\t':
            x -= 0.03
        else:
            wait()
            glutBitmapCharacter(en, ord(about[i]))

    glPopMatrix()
    glFlush()
    enter = 1


def check_cond():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1

    if (k1 > 27 and p1 == 0) and (k2 > 27 and p1 == 0) and (l1 > 27 and p2 == 0) and (l2 > 27 and p2 == 0):
        dice1 = 0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 0)
        glFlush()
        about()
    elif s1 == 2:
        dice1 = 0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 0)
        glFlush()
        about1()
    elif s2 == 2:
        dice1 = 0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 0)
        glFlush()
        about2()


def circle():
    ang = 0.0
    glPushMatrix()
    glLoadIdentity()

    glTranslatef(-1.47, 0.72, 0)
    if ply1 == 1 and ply2 == 0:
        glColor3f(1, 0, 0)
    else:
        glColor3f(0, 0, 0)

    glBegin(GL_POLYGON)
    for i in range(13):
        ang = (3.1415 / 6) * i
        x = 0.02 * cos(ang)
        y = 0.02 * sin(ang)
        x = x.real
        y = y.real
        glVertex2f(x, y)

    glEnd()
    glColor3f(0, 1, 0)
    glFlush()
    glPopMatrix()
    glFlush()

    glPushMatrix()
    glLoadIdentity()

    glTranslatef(-1.47, 0.56, 0)
    if ply1 == 0 and ply2 == 1:
        glColor3f(1, 0, 0)
    else:
        glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    for i in range(13):
        ang = (3.1415 / 6) * i
        x = 0.02 * cos(ang)
        y = 0.02 * sin(ang)
        x = x.real
        y = y.real
        glVertex2f(x, y)
    glEnd()
    glColor3f(0, 1, 0)
    glFlush()
    glPopMatrix()
    glFlush()


def display2():
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.15, -0.84)  # Bottom direction
    glVertex2f(0, -0.84)
    glVertex2f(0, -0.6)

    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0, -0.6)
    glVertex2f(-0.04, -0.64)
    glVertex2f(0, -0.6)
    glVertex2f(0.04, -0.64)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.15, 0.84)  # Top direction
    glVertex2f(0, 0.84)
    glVertex2f(0, 0.6)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0, 0.6)
    glVertex2f(-0.04, 0.64)
    glVertex2f(0, 0.6)
    glVertex2f(0.04, 0.64)
    glEnd()
    glPointSize(25)
    glBegin(GL_POINTS)
    glColor3f(0, 1, 0)
    glVertex2f(c[0][0], c[0][1])
    glVertex2f(c[1][0], c[1][1])
    glColor3f(1, 0, 1)
    glVertex2f(d[0][0], d[0][1])
    glVertex2f(d[1][0], d[1][1])
    glEnd()
    glColor3f(0, 1, 0)
    glFlush()
    circle()
    check_cond()


def player1(ch):
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, p1, p2, ra1, z, z1, za1

    # global f1, h1, f2, h2, ra1, k1, k2, p1, ply1, ply2
    print("p1={} g2={}".format(p1,g2))
    print("c[0][0]={} c[0][1]={}".format(c[0][0], c[0][1]))
    print("c[1][0]={} c[1][1]={}".format(c[1][0], c[1][1]))

    if (f1 == 0) and (h1 == 0):    # coin1 initial position
        glBegin(GL_POINTS)
        glVertex2f(c[0][0], c[0][1])
        glEnd()
        glFlush()

    elif h1 == 1:           # coin1 after winning the game
        glBegin(GL_POINTS)
        glVertex2f(0.7, -0.5)
        glEnd()

    else:
        glBegin(GL_POINTS)
        glVertex2f(a[k1][0], a[k1][1])  # movement of the coin1
        glEnd()


    if (f2 == 0) and (h2 == 0): ## coin2 initial position
        glBegin(GL_POINTS)
        glVertex2f(c[1][0], c[1][1])
        glEnd()

    elif h2 == 1: # coin2 after winning the game
        glBegin(GL_POINTS)
        glVertex2f(0.5, -0.7)
        glEnd()

    else:
        glBegin(GL_POINTS)
        glVertex2f(a[k2][0], a[k2][1])  # movement of the coin2
        glEnd()

    glColor3f(0, 1, 0)

    if h1 == 1:
        ch = 2

    elif h2 == 1:
        ch = 1

    elif (ra1 + k1 > 57) and (ra1 + k2 > 57) :
        ply1 = 0
        ply2 = 1

    elif (ra1 + k1 > 57 and ch == 1) or (ra1 + k1 > 51 and p1 == 0 and ch == 1):
        if a[ra1 + k2][0] == c[0][0] and a[ra1 + k2][1] == c[0][1]:
            ch = 776
        else:
            ch = 2

    elif (ra1 + k2 > 57 and ch == 2) or (ra1 + k2 > 51 and p1 == 0 and ch == 2):
        if a[ra1 + k1][0] == c[1][0] and a[ra1 + k1][1] == c[1][1]:
            ch = 776
        else:
            ch = 1

    if ch == 1 and a[ra1 + k1][0] == c[1][0] and a[ra1 + k1][1] == c[1][1]:
        display2()
        return

    elif ch == 2 and a[ra1 + k2][0] == c[0][0] and a[ra1 + k2][1] == c[0][1]:
        display2()
        return

    def case1():
        global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1
        # global f1, h1, f2, h2, ra1, k1, k2, p1, ply1, ply2, z, z1, g1, l1, g2, l2, s1, ch
        if f1 == 0 and (ra1 == 6 or ra1 == 1):  # y == 4
            ra1 = 1
            f1 = 1

        else:
            z = 1
            z1 = 0
            ply1 = 0
            ply2 = 1
        if (f1 == 1) and (ra1 + k1 <= 57) and (h1 == 0):
            for i in range(2):
                if a[ra1 + k1][0] == d[i][0] and a[ra1 + k1][1] == d[i][1]:
                    if i == 0:
                        g1 = 0
                        l1 = 0
                        d[0][0] = 0.5
                        d[0][1] = 0.7
                    if i == 1:
                        g2 = 0
                        l2 = 0
                        d[1][0] = 0.7
                        d[1][1] = 0.5
                    p1 = 1

            if ((ra1 + k1) > 51 and p1 == 1) or (ra1 + k1 <= 51):
                glColor3f(0, 0, 0)
                if k1 == 0:
                    glBegin(GL_POINTS)
                    glVertex2f(-0.5, -0.7)
                    glEnd()
                elif k1 == 1 or k1 == 52 or k1 == 53 or k1 == 54 or k1 == 55 or k1 == 56:
                    glColor3f(1, 0, 0)

                elif k1 == 27:
                    glColor3f(0, 0, 1)
                glBegin(GL_POINTS)
                glVertex2f(a[k1][0], a[k1][1])
                glEnd()
                glColor3f(0, 1, 0)
                k1 = ra1 + k1
                z = 1
                c[0][0] = a[k1][0]
                c[0][1] = a[k1][1]
                if ra1 == 6:
                    z1 = 0
                    ply1 = 1
                    ply2 = 0
                else:
                    ply1 = 0
                    ply2 = 1

            ch = 0

        if k1 == 57:
            k1 = 0
            h1 = 1
            glBegin(GL_POINTS)
            c[0][0] = 0.7
            c[0][1] = -0.5
            glVertex2f(c[0][0], c[0][1])
            s1 += 1
            glEnd()

    def case2():

        global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1
        if f2 == 0 and (ra1 == 6 or ra1 == 1):
            ra1 = 1
            f2 = 1

        else:
            z = 1
            z1 = 0
            ply1 = 0
            ply2 = 1

            if (f2 == 1) and (ra1 + k2 <= 57) and (h2 == 0):
                for i in range(2):
                    if a[ra1 + k2][0] == d[i][0] and a[ra1 + k2][1] == d[i][1]:
                        if i == 0:
                            g1 = 0
                            l1 = 0
                            d[0][0] = 0.5
                            d[0][1] = 0.7
                    if i == 1:
                        g2 = 0
                        l2 = 0
                        d[1][0] = 0.7
                        d[1][1] = 0.5
                    p1 = 1

                if ((ra1 + k2) > 51 and p1 == 1) or (ra1 + k2 <= 51):
                    glColor3f(0, 0, 0)
                    if k2 == 0:
                        glBegin(GL_POINTS)
                        glVertex2f(-0.7, -0.5)
                        glEnd()
                    elif k2 == 1 or k2 == 52 or k2 == 53 or k2 == 54 or k2 == 55 or k2 == 56:
                        glColor3f(1, 0, 0)
                    elif k2 == 27:
                        glColor3f(0, 0, 1)

                    glBegin(GL_POINTS)
                    glVertex2f(a[k2][0], a[k2][1])
                    glEnd()
                    glColor3f(0, 1, 0)
                    k2 = ra1 + k2
                    z = 1
                    c[1][0] = a[k2][0]
                    c[1][1] = a[k2][1]
                    if ra1 == 6:
                        z1 = 0
                        ply1 = 1
                        ply2 = 0
                    else:
                        ply1 = 0
                        ply2 = 1

            if k2 == 57:
                k2 = 0
                h2 = 1
                c[1][0] = 0.5
                c[1][1] = -0.7
                s1 += 1

    def case776():
        global ply1, ply2
        ply1 = 0
        ply2 = 1

    switch = {1: case1, 2: case2, 776: case776}
    switch[ch]()
    ch = 0
    glColor3f(1, 0, 1)
    arrow()
    display2()


def player2(ch1):
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch, p1, p2, ra1, z, z1, za1
    print("g1={} h3={} g2={} h4={} p1={} p2={}".format(g1, h3, g2, h4, p1, p2))
    print("d[0][0]={} d[0][1]={}".format(d[0][0], d[0][1]))
    print("d[1][0]={} d[1][1]={}".format(d[1][0], d[1][1]))
    # print("p2={} ".format(p2))
    glColor3f(1, 0, 1)
    if (g1 == 0) and (h3 == 0): # coin1 initial position
        glBegin(GL_POINTS)
        glVertex2f(d[0][0], d[0][1])
        glEnd()
    elif h3 == 1: # coin1 after winning the game
        glBegin(GL_POINTS)
        glVertex2f(-0.7, 0.5)
        glEnd()
    else: # movement of the coin1
        glBegin(GL_POINTS)
        glVertex2f(b[l1][0], b[l1][1])
        glEnd()

    if (g2 == 0) and (h4 == 0): ## coin2 initial position
        glBegin(GL_POINTS)
        glVertex2f(d[1][0], d[1][1])
        glEnd()

    elif h4 == 1: # coin2 after winning the game
        glBegin(GL_POINTS)
        glVertex2f(-0.5, 0.7)
        glEnd()

    else: # movement of the coin2
        glBegin(GL_POINTS)
        glVertex2f(b[l2][0], b[l2][1])
        glEnd()

    glColor3f(1, 0, 1)

    if h3 == 1:
        ch1 = 2
    elif h4 == 1:
        ch1 = 1

    elif (ra1 + l1 > 57 or (ra1 + l1 > 51 and p2 == 0)) and (ra1 + l2 > 57 or (ra1 + l2 > 51 and p2 == 0)):
        ply1 = 1
        ply2 = 0

    elif (ra1 + l1 > 57 and ch1 == 1) or (ra1 + l1 > 51 and p2 == 0 and ch1 == 1):
        if b[ra1 + l2][0] == d[0][0] and b[ra1 + l2][1] == d[0][1]:
            ch1 = 776
        else:
            ch1 = 2
    elif (ra1 + l2 > 57 and ch1 == 2) or (ra1 + l2 > 51 and p2 == 0 and ch1 == 2):
        if b[ra1 + l1][0] == d[1][0] and b[ra1 + l1][1] == d[1][1]:
            ch1 = 776
        else:
            ch1 = 1

    if ch1 == 1 and b[ra1 + l1][0] == d[1][0] and b[ra1 + l1][1] == d[1][1]:
        display2()
        return
    elif ch1 == 2 and b[ra1 + l2][0] == d[0][0] and b[ra1 + l2][1] == d[0][1]:
        display2()
        return

    def case1():

        global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1
        if g1 == 0 and (ra1 == 6 or ra1 == 1):
            ra1 = 1
            g1 = 1

        else:
            z = 1
            z1 = 0
            ply1 = 1
            ply2 = 0

        if g1 == 1 and ra1 + l1 <= 57 and h3 == 0:
            for i in range(2):
                if b[ra1 + l1][0] == c[i][0] and b[ra1 + l1][1] == c[i][1]:
                    p2 = 1
                    if i == 0:
                        f1 = 0
                        k1 = 0
                        c[0][0] = -0.5
                        c[0][1] = -0.7
                    if i == 1:
                        f2 = 0
                        k2 = 0
                        c[1][0] = -0.7
                        c[1][1] = -0.5

            if ((ra1 + l1) > 51 and p2 == 1) or (ra1 + l1 <= 51):
                glColor3f(0, 0, 0)
            if l1 == 0:
                glBegin(GL_POINTS)
                glVertex2f(0.5, 0.7)
                glEnd()
            elif l1 == 1 or l1 == 52 or l1 == 53 or l1 == 54 or l1 == 55 or l1 == 56:
                glColor3f(0, 0, 1)

            elif l1 == 27:
                glColor3f(1, 0, 0)

            glBegin(GL_POINTS)
            glVertex2f(b[l1][0], b[l1][1])
            glEnd()

            glColor3f(1, 0, 1)
            z = 1
            l1 = ra1 + l1
            d[0][0] = b[l1][0]
            d[0][1] = b[l1][1]
            if ra1 == 6:
                z1 = 0
                ply1 = 0
                ply2 = 1
            else:
                ply1 = 1
                ply2 = 0

            ch1 = 0
            if l1 == 57:
                l1 = 0
                h3 = 1
                glBegin(GL_POINTS)
                d[0][0] = -0.7
                d[0][1] = 0.5
                glVertex2f(d[0][0], d[0][1])
                s2 += 1
                glEnd()

    def case2():

        global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1
        if g2 == 0 and (ra1 == 6 or ra1 == 1):
            ra1 = 1
            g2 = 1

        else:
            z = 1
            z1 = 0
            ply1 = 1
            ply2 = 0

        if (g2 == 1) and (ra1 + l2 <= 57) and (h4 == 0):

            for i in range(2):
                if b[ra1 + l2][0] == c[i][0] and b[ra1 + l2][1] == c[i][1]:
                    if i == 0:
                        f1 = 0
                        k1 = 0
                        c[0][0] = -0.5
                        c[0][1] = -0.7
                    if i == 1:
                        f2 = 0
                        k2 = 0
                        c[1][0] = -0.7
                        c[1][1] = -0.5
                    p2 = 1

            if ((ra1 + l2) > 51 and p2 == 1) or (ra1 + l2 <= 51):
                glColor3f(0, 0, 0)
                if l2 == 0:
                    glBegin(GL_POINTS)
                    glVertex2f(0.7, 0.5)
                    glEnd()
                elif l2 == 1 or l2 == 52 or l2 == 53 or l2 == 54 or l2 == 55 or l2 == 56:
                    glColor3f(0, 0, 1)
            elif l2 == 27:
                glColor3f(1, 0, 0)

            glBegin(GL_POINTS)
            glVertex2f(b[l2][0], b[l2][1])
            glEnd()
            glColor3f(1, 0, 1)
            z = 1
            l2 = ra1 + l2
            d[1][0] = b[l2][0]
            d[1][1] = b[l2][1]
            if ra1 == 6:
                z1 = 0
                ply1 = 0
                ply2 = 1
            else:
                ply1 = 1
                ply2 = 0

            if l2 == 57:
                l2 = 0
                h4 = 1
                d[1][0] = -0.5
                d[1][1] = 0.7
                s2 += 1

    def case776():

        global ply1, ply2
        ply1 = 1
        ply2 = 0

    switch = {1: case1, 2: case2, 776: case776}
    switch[ch1]()
    ch1 = 0
    glColor3f(1, 0, 1)
    arrow()
    display2()


def pl1_pl2():
    global in_guide
    guide = "PLAYER 1\n\nPLAYER 2"
    en = GLUT_BITMAP_TIMES_ROMAN_24
    x = -1.4
    y = 0.7
    z = 0
    in_guide = 1
    glColor3f(0, 1, 0)
    glRasterPos3f(x, y, z)

    for i in range(len(guide)):
        if guide[i] == '\n':
            glColor3f(1, 0, 1)
            y -= 0.08
            glRasterPos3f(x, y, z)

        glutBitmapCharacter(en, ord(guide[i]))

    glFlush()


def display1():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1
    z = 1
    z1 = 1
    dice1 = 1
    f1 = 0
    f2 = 0
    g1 = 0
    g2 = 0
    k1 = 0
    k2 = 0
    l1 = 0
    l2 = 0
    ply1 = 1
    ply2 = 0
    h1 = 0
    h2 = 0
    h3 = 0
    h4 = 0
    s1 = 0
    s2 = 0
    p1 = 0
    p2 = 0
    enter = 0
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glLineWidth(2)

    glBegin(GL_LINE_LOOP)
    glVertex2f(0.9, 0.9)
    glVertex2f(-0.9, 0.9)  # Main BOX Outline
    glVertex2f(-0.9, -0.9)
    glVertex2f(0.9, -0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.9, -0.2)  # (-, -) BOX
    glVertex2f(-0.9, -0.9)
    glVertex2f(-0.2, -0.9)
    glColor3f(1, 1, 1)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.2, 0.2)
    glVertex2f(0.9, 0.2)  # (+, +) BOX
    glVertex2f(0.9, 0.9)
    glVertex2f(0.2, 0.9)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    glVertex2f(0.2, 0.2)
    glVertex2f(-0.2, 0.2)  # Top part Home
    glVertex2f(0, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(-0.2, -0.2)
    glVertex2f(0.2, -0.2)  # Bottom part Home
    glVertex2f(0, 0)
    glEnd()
    glColor3f(1, 1, 1)

    glBegin(GL_QUADS)
    glColor3f(0, 0, 1)
    glVertex2f(-0.075, 0.2)
    glVertex2f(0.075, 0.2)
    glVertex2f(0.075, 0.785)  # TOP ARROW
    glVertex2f(-0.075, 0.785)
    glVertex2f(0.2, 0.67)
    glVertex2f(-0.075, 0.67)
    glVertex2f(-0.075, 0.785)
    glVertex2f(0.2, 0.785)
    glEnd()
    glColor3f(1, 1, 1)

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2f(-0.075, -0.2)
    glVertex2f(0.075, -0.2)
    glVertex2f(0.075, -0.785)  # BOTTOM ARROW
    glVertex2f(-0.075, -0.785)
    glVertex2f(-0.2, -0.67)
    glVertex2f(-0.075, -0.67)
    glVertex2f(-0.075, -0.785)
    glVertex2f(-0.2, -0.785)
    glEnd()
    glColor3f(1, 1, 1)

    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.4, -0.4)
    glVertex2f(-0.8, -0.4)  # Player coins(-, -) BOX
    glVertex2f(-0.8, -0.8)
    glVertex2f(-0.4, -0.8)
    glEnd()

    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.45, -0.65)
    glVertex2f(-0.55, -0.65)
    glVertex2f(-0.55, -0.75)
    glVertex2f(-0.45, -0.75)
    glEnd()
    glFlush()

    # Player coins keeping(-, -) BOX

    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.75, -0.45)
    glVertex2f(-0.65, -0.45)
    glVertex2f(-0.65, -0.55)
    glVertex2f(-0.75, -0.55)
    glEnd()

    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(0.4, 0.4)
    glVertex2f(0.8, 0.4)  # Player Coins(+, +) BOX
    glVertex2f(0.8, 0.8)
    glVertex2f(0.4, 0.8)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(0.45, 0.65)
    glVertex2f(0.55, 0.65)
    glVertex2f(0.55, 0.75)
    glVertex2f(0.45, 0.75)
    glEnd()
    glFlush()

    # Player coins keeping(+, +) BOX
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.75, 0.45)
    glVertex2f(0.65, 0.45)
    glVertex2f(0.65, 0.55)
    glVertex2f(0.75, 0.55)
    glEnd()
    glFlush()

    glBegin(GL_LINE_STRIP)
    glVertex2f(0.15, -0.84)  # Bottom direction
    glVertex2f(0, -0.84)
    glVertex2f(0, -0.6)

    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0, -0.6)
    glVertex2f(-0.04, -0.64)
    glVertex2f(0, -0.6)
    glVertex2f(0.04, -0.64)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.15, 0.84)  # Top direction
    glVertex2f(0, 0.84)
    glVertex2f(0, 0.6)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0, 0.6)
    glVertex2f(-0.04, 0.64)
    glVertex2f(0, 0.6)
    glVertex2f(0.04, 0.64)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.075, -0.2)
    glVertex2f(-0.075, -0.9)
    glEnd()  # Bottom part Lines
    glBegin(GL_LINES)
    glVertex2f(0.075, -0.2)
    glVertex2f(0.075, -0.9)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.2, -0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.2, -0.2)
    glVertex2f(0.2, -0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.9, -0.2)
    glVertex2f(-0.9, -0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.9, 0.2)
    glVertex2f(0.9, 0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.075, 0.2)
    glVertex2f(-0.075, 0.9)
    glEnd()
    # Top part Lines
    glBegin(GL_LINES)
    glVertex2f(0.075, 0.2)
    glVertex2f(0.075, 0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.2, 0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.2, 0.2)
    glVertex2f(0.2, 0.9)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.2, -0.075)
    glVertex2f(0.9, -0.075)
    glEnd()  # Right part Lines
    glBegin(GL_LINES)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.9, 0.075)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.2, -0.2)
    glVertex2f(0.9, -0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.2, 0.2)
    glVertex2f(0.9, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.075)
    glVertex2f(-0.9, -0.075)
    glEnd()
    # Left part Lines
    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.075)
    glVertex2f(-0.9, 0.075)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.9, -0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.9, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.784)
    glVertex2f(0.2, -0.784)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.67)
    glVertex2f(0.2, -0.67)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.552)
    glVertex2f(0.2, -0.552)
    glEnd()  # Across - Bottom Lines

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.436)
    glVertex2f(0.2, -0.436)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.32)
    glVertex2f(0.2, -0.32)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.2)
    glVertex2f(0.2, -0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.784)
    glVertex2f(0.2, 0.784)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.668)
    glVertex2f(0.2, 0.668)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.552)
    glVertex2f(0.2, 0.552)
    glEnd()  # Across - Top Lines

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.436)
    glVertex2f(0.2, 0.436)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.32)
    glVertex2f(0.2, 0.32)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.2)
    glVertex2f(0.2, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.784, -0.2)
    glVertex2f(0.784, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.668, -0.2)
    glVertex2f(0.668, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.552, -0.2)
    glVertex2f(0.552, 0.2)
    glEnd()  # Across - Right Lines

    glBegin(GL_LINES)
    glVertex2f(0.436, -0.2)
    glVertex2f(0.436, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.32, -0.2)
    glVertex2f(0.32, 0.2)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.7275, 0.14)
    glVertex2f(0.84, 0.14)
    glVertex2f(0.84, -0.1375)
    glVertex2f(0.7275, -0.1375)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.7275, -0.1375)
    glVertex2f(0.76, -0.1111)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.7275, -0.1375)
    glVertex2f(0.76, -0.16)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.2, -0.2)
    glVertex2f(0.2, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.784, -0.2)
    glVertex2f(-0.784, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.668, -0.2)
    glVertex2f(-0.668, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.552, -0.2)
    glVertex2f(-0.552, 0.2)
    glEnd()  # Across - Left Lines

    glBegin(GL_LINES)
    glVertex2f(-0.436, -0.2)
    glVertex2f(-0.436, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.32, -0.2)
    glVertex2f(-0.32, 0.2)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.7275, -0.14)
    glVertex2f(-0.84, -0.14)
    glVertex2f(-0.84, 0.1375)
    glVertex2f(-0.7275, 0.1375)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-0.7275, 0.1375)
    glVertex2f(-0.76, 0.1111)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-0.7275, 0.1375)
    glVertex2f(-0.76, 0.16)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.2, 0.2)
    glEnd()
    display_inter_guide()
    glFlush()
    pl1_pl2()
    circle()
    display2()


def arrow():
    glColor3f(1, 1, 1)

    glBegin(GL_LINE_STRIP)
    glVertex2f(0.7275, 0.14)
    glVertex2f(0.84, 0.14)
    glVertex2f(0.84, -0.1375)
    glVertex2f(0.7275, -0.1375)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.7275, -0.1375)
    glVertex2f(0.76, -0.1111)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.7275, -0.1375)
    glVertex2f(0.76, -0.16)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.7275, -0.14)
    glVertex2f(-0.84, -0.14)
    glVertex2f(-0.84, 0.1375)
    glVertex2f(-0.7275, 0.1375)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.7275, 0.1375)
    glVertex2f(-0.76, 0.1111)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.7275, 0.1375)
    glVertex2f(-0.76, 0.16)
    glEnd()

    glFlush()


def wait():
    for i in range(1000):
        for j in range(1000):
            pass


def display_msg(x, y, z, msg):
    glColor3f(0, 0, 0)
    glRasterPos3f(x, y, z)

    for i in range(len(msg)):
        glutBitmapCharacter(font, ord(msg[i]))
    glFlush()


def display_about():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1
    global in_about
    about = "This mini-Project is based on a very ancient game LUDO,using OpenGL.\n\nINSTRUCTIONS :\nInput can be provided either from Mouse or from Keyboard.\nFor mouse interaction right-click on the screen and select the required option.\nKeyboard and Mouse Interfaces are explained in the Instructions Section.\n\n\n\n\n\n"
    about = list(about)
    enter = 0

    x = -1.8
    y = 0.9
    z = 0

    if in_about != 0:
        in_about = 1
    glPushMatrix()
    glLoadIdentity()
    glColor3f(1, 0, 0)
    glRasterPos3f(x, y, z)

    for i in range(len(about)):
        if about[i] == '\n':
            y -= 0.08
            glRasterPos3f(x, y, z)
        else:
            glutBitmapCharacter(font, ord(about[i]))

    glPopMatrix()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    display_about()


def display_about_game():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1, in_about
    about_game = "RULES:\n\n\nAt the start of the game, the player's four pieces are placed in the start area of their colour.\n\nPlayers take it in turn to throw a single die. A player must first throw a six to be able to move a piece from the starting area\nonto the starting square.In each subsequent turn the player moves a piece forward 1 to 6 squares as indicated by the die.When a\nplayer throws a 6 the player may bring a new piece onto the starting square, or may choose to move a piece already in play.Any\nthrow of a six results in another turn.\n\nIf a player cannot make a valid move they must pass the die to the next player.\n\nIf a player's piece lands on a square containing an opponent's piece, the opponent's piece is captured and returns to the starting\narea.A piece may not land on a square that already contains a piece of the same colour(unless playing doubling rules).\n\nOnce a piece has completed a circuit of the board it moves up the home column of its own colour. The player must throw the exact\nnumber to advance to the home square.The winner is the first player to get all four of their pieces onto the home square."
    x = -1.8
    y = 0.9
    z = 0

    in_about = 1

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glPushMatrix()
    glLoadIdentity()

    glColor3f(1, 0, 0)
    glRasterPos3f(x, y, z)

    for i in range(len(about_game)):
        if about_game[i] == '\n':
            y -= 0.08
            glRasterPos3f(x, y, z)
        else:
            glutBitmapCharacter(font, ord(about_game[i]))
    glPopMatrix()
    glFlush()


def display_inter_guide():
    global in_guide
    gui = "KEYBOARD OPTIONS:\nQ-To Quit.\n\nMOUSE OPTIONS:\nLEFT BUTTON- To Select the coin,\nClick on the coin of Player to\nROLL DICE & to move.\nRIGHT BUTTON- To Restart."

    x = 1.1
    y = 0.4
    z = 0
    glColor3f(0.4, 0.5, 0.3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1.08, 0.5)
    glVertex2f(1.92, 0.5)
    glVertex2f(1.92, -0.2)
    glVertex2f(1.08, -0.2)
    glEnd()
    in_guide = 1
    glColor3f(1, 0, 0)
    glRasterPos3f(x, y, z)

    for i in range(len(gui)):
        if gui[i] == '\n':
            y -= 0.08
            glRasterPos3f(x, y, z)
        else:
            glutBitmapCharacter(font, ord(gui[i]))

    glFlush()


def enter_display2():
    global f1, f2, g1, g2, k1, k2, l1, l2, ply1, ply2, h1, h2, h3, h4, s1, s2, u, v, r1, op, w, dice1, enter, ch1, ch, p1, p2, ra1, z, z1, za1

    about = "PRESS  ENTER\n"
    en = GLUT_BITMAP_TIMES_ROMAN_24

    x = 0.8
    y = -0.8
    z = 0
    enter = 1

    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(9)
    glColor3f(0, 0, 0)
    # glColor3f(0.545, 0.6434, 0.743)
    glBegin(GL_LINES)
    glVertex2f(-1.8, 0.8)
    glVertex2f(-1.8, 0.4)
    glVertex2f(-1.8, 0.4)  # L
    glVertex2f(-1.6, 0.4)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-1.5, 0.4)
    glVertex2f(-1.5, 0.7)
    glVertex2f(-1.5, 0.4)  # U
    glVertex2f(-1.3, 0.4)
    glVertex2f(-1.3, 0.4)
    glVertex2f(-1.3, 0.7)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-1.1, 0.38)
    glVertex2f(-1.1, 0.83)
    glVertex2f(-1.125, 0.815)  # D
    glVertex2f(-0.95, 0.6)
    glVertex2f(-0.95, 0.6)
    glVertex2f(-1.125, 0.4)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-0.93, 0.38)
    glVertex2f(-0.7, 0.7)
    glVertex2f(-0.7, 0.7)  # O
    glVertex2f(-0.6, 0.38)
    glVertex2f(-0.93, 0.38)
    glVertex2f(-0.6, 0.38)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.34)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.5, 0.34)
    glVertex2f(-0.3, 0.2)
    glVertex2f(-0.3, 0.2)
    glVertex2f(-0.5, 0.1)  # B
    glVertex2f(-0.5, 0.1)
    glVertex2f(-0.3, 0.0)
    glVertex2f(-0.3, 0.0)
    glVertex2f(-0.5, -0.1)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.0)
    glVertex2f(0.0, 0.32)
    glVertex2f(0.0, 0.32)  # O
    glVertex2f(0.1, 0.0)
    glVertex2f(-0.2, 0.0)
    glVertex2f(0.1, 0.0)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0.2, -0.05)
    glVertex2f(0.29, 0.32)
    glVertex2f(0.29, 0.32)  # A
    glVertex2f(0.4, -0.05)
    glVertex2f(0.16, 0.1)
    glVertex2f(0.34, 0.1)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0.5, -0.05)
    glVertex2f(0.5, 0.32)
    glVertex2f(0.5, 0.32)  # R
    glVertex2f(0.7, 0.18)
    glVertex2f(0.7, 0.18)
    glVertex2f(0.5, 0.1)
    glVertex2f(0.5, 0.1)
    glVertex2f(0.7, -0.05)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0.8, -0.15)
    glVertex2f(0.8, 0.34)  # D
    glVertex2f(0.78, 0.32)
    glVertex2f(0.95, 0.1)
    glVertex2f(0.95, 0.1)
    glVertex2f(0.78, -0.12)
    glEnd()
    glFlush()

    glColor3f(1, 1, 0)
    glRasterPos3f(x, y, z)

    for i in range(len(about)):

        if about[i] == '\n':
            wait()
            y -= 0.08
            glRasterPos3f(x, y, z)

        elif about[i] == '\t':
            wait()
            x -= 0.2
            glRasterPos3f(x, y, z)

        else:
            wait()
            glutBitmapCharacter(en, ord(about[i]))

    glFlush()


def square():
    glColor3f(1, 1, 1)

    glBegin(GL_QUADS)
    glVertex2f(-.4, -.7)
    glVertex2f(-.4, -.65)
    glVertex2f(.4, -.65)
    glVertex2f(.4, -.7)
    glEnd()
    glColor3f(0.545, 0.6434, 0.743)

    glBegin(GL_QUADS)
    glVertex2f(-.39, -.69)
    glVertex2f(-.39, -.66)
    glVertex2f(-.34, -.66)
    glVertex2f(-.34, -.69)
    glEnd()

    glFlush()
    wait()
    wait()

    glBegin(GL_QUADS)
    glVertex2f(-.34, -.69)
    glVertex2f(-.34, -.66)
    glVertex2f(-.30, -.66)
    glVertex2f(-.30, -.69)
    glEnd()

    glFlush()
    wait()
    wait()
    wait()

    glBegin(GL_QUADS)
    glVertex2f(-.30, -.69)
    glVertex2f(-.30, -.66)
    glVertex2f(-.23, -.66)
    glVertex2f(-.23, -.69)
    glEnd()

    glFlush()
    wait()
    wait()
    wait()

    glBegin(GL_QUADS)
    glVertex2f(-.23, -.69)
    glVertex2f(-.23, -.66)
    glVertex2f(-.1, -.66)
    glVertex2f(-.1, -.69)
    glEnd()

    glFlush()
    wait()
    wait()
    wait()

    glBegin(GL_QUADS)
    glVertex2f(-.1, -.69)
    glVertex2f(-.1, -.66)
    glVertex2f(0.1, -.66)
    glVertex2f(0.1, -.69)
    glEnd()

    glFlush()
    wait()
    wait()
    wait()
    wait()
    wait()
    wait()

    glBegin(GL_QUADS)
    glVertex2f(0.1, -.69)
    glVertex2f(0.1, -.66)
    glVertex2f(0.15, -.66)
    glVertex2f(0.15, -.69)
    glEnd()

    glFlush()
    wait()
    wait()
    wait()

    glBegin(GL_QUADS)
    glVertex2f(0.15, -.69)
    glVertex2f(0.15, -.66)
    glVertex2f(0.2, -.66)
    glVertex2f(0.2, -.69)
    glEnd()

    glFlush()
    wait()
    wait()

    glBegin(GL_QUADS)
    glVertex2f(0.2, -.69)
    glVertex2f(0.2, -.66)
    glVertex2f(0.39, -.66)
    glVertex2f(0.39, -.69)
    glEnd()

    glFlush()
    wait()
    wait()
    wait()
    wait()

    enter_display2()


def display_enter1():
    about = "please wait...\n"
    en = GLUT_BITMAP_TIMES_ROMAN_24
    x = -0.16
    y = -0.8
    z = 0

    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(9)
    glColor3f(0, 0, 0)
    # glColor3f(0.545, 0.6434, 0.743)

    glBegin(GL_LINES)
    glVertex2f(-1.8, 0.8)
    glVertex2f(-1.8, 0.4)
    glVertex2f(-1.8, 0.4)  # L
    glVertex2f(-1.6, 0.4)
    glEnd()

    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-1.5, 0.4)
    glVertex2f(-1.5, 0.7)
    glVertex2f(-1.5, 0.4)  # U
    glVertex2f(-1.3, 0.4)
    glVertex2f(-1.3, 0.4)
    glVertex2f(-1.3, 0.7)
    glEnd()

    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-1.1, 0.38)
    glVertex2f(-1.1, 0.83)
    glVertex2f(-1.125, 0.815)  # D
    glVertex2f(-0.95, 0.6)
    glVertex2f(-0.95, 0.6)
    glVertex2f(-1.125, 0.4)
    glEnd()

    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-0.93, 0.38)
    glVertex2f(-0.7, 0.7)
    glVertex2f(-0.7, 0.7)  # O
    glVertex2f(-0.6, 0.38)
    glVertex2f(-0.93, 0.38)
    glVertex2f(-0.6, 0.38)
    glEnd()

    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.34)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.5, 0.34)
    glVertex2f(-0.3, 0.2)
    glVertex2f(-0.3, 0.2)
    glVertex2f(-0.5, 0.1)  # B
    glVertex2f(-0.5, 0.1)
    glVertex2f(-0.3, 0.0)
    glVertex2f(-0.3, 0.0)
    glVertex2f(-0.5, -0.1)
    glEnd()

    glFlush()

    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.0)
    glVertex2f(0.0, 0.32)
    glVertex2f(0.0, 0.32)  # O
    glVertex2f(0.1, 0.0)
    glVertex2f(-0.2, 0.0)
    glVertex2f(0.1, 0.0)
    glEnd()

    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0.2, -0.05)
    glVertex2f(0.29, 0.32)
    glVertex2f(0.29, 0.32)  # A
    glVertex2f(0.4, -0.05)
    glVertex2f(0.16, 0.1)
    glVertex2f(0.34, 0.1)
    glEnd()

    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0.5, -0.05)
    glVertex2f(0.5, 0.32)
    glVertex2f(0.5, 0.32)  # R
    glVertex2f(0.7, 0.18)
    glVertex2f(0.7, 0.18)
    glVertex2f(0.5, 0.1)
    glVertex2f(0.5, 0.1)
    glVertex2f(0.7, -0.05)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2f(0.8, -0.15)
    glVertex2f(0.8, 0.34)
    glVertex2f(0.78, 0.32)  # D
    glVertex2f(0.95, 0.1)
    glVertex2f(0.95, 0.1)
    glVertex2f(0.78, -0.12)
    glEnd()

    glFlush()

    glRasterPos3f(x, y, z)

    for i in range(len(about)):

        if about[i] == '\n':
            wait()
            y -= 0.08
            glRasterPos3f(x, y, z)

        elif about[i] == '\t':
            wait()
            x -= 0.2
            glRasterPos3f(x, y, z)

        else:
            wait()
            glutBitmapCharacter(en, ord(about[i]))

    square()


def options(id):
    def case1():
        global in_about
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        in_about = 1
        display_about()

    def case2():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        display_about_game()

    def case4():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.6, 0.7, 0, 0)
        display_enter1()

    def case5():
        x = glutGetWindow()
        glutDestroyWindow(x)


    switch = {1: case1, 2: case2, 4: case4, 5: case5}
    switch[id]()
    return 0

def init():
    glClearColor(1, 0.8, 0.5, 1)
    glEnable(GL_DEPTH_TEST)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(1355, 703)
    glutCreateWindow("LUDO - BOARD GAME")


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
init()
glutCreateMenu(options)
glutAddMenuEntry("About the Project", 1)
glutAddMenuEntry("Rules of the Game", 2)
glutAddMenuEntry("Game Mode or Restart", 4)
glutAddMenuEntry("Quit", 5)
glutMouseFunc(myMouse)
glutKeyboardFunc(key)
glutAttachMenu(GLUT_RIGHT_BUTTON)
glutReshapeFunc(myReshape)
glutDisplayFunc(display)
font = GLUT_BITMAP_9_BY_15
glutMainLoop()

# global f1,f2,g1,g2,k1,k2,l1,l2,ply1,ply2,h1,h2,h3,h4,s1,s2,u,v,r1,op,w,dice1,enter,ch1,ch,p1,p2,ra1,z,z1,za1
