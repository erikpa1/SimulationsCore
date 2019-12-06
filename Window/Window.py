import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Window:

    x = 10;
    y = 10;

    def Init(self):
        pygame.init()
        pass;

    def SetWindowSize(self, x : int, y : int):

        self.x = x;
        self.y = y;

        pygame.display.set_mode((x, y), DOUBLEBUF | OPENGL)
    pass;

    def SetDefaultCamera(self):
        gluPerspective(45, (self.x / self.y), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        pass;

    def IsQuitRequest(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True;
        return False;

    def Quit(self):
        pygame.quit()
        quit();
        pass;

    def DisplayFlip(self):
        pygame.display.flip();
        pass;

    def Wait(self, time : int):
        pygame.time.wait(time)
        pass;

    def Clear(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pass;