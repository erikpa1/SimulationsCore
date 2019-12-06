import pygame
from pygame.locals import *

from Mesh import Mesh
from Mesh import MeshFactory
from Mesh import MeshModifier

from OpenGL.GL import *
from OpenGL.GLU import *

def main():

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    temp = Mesh.Mesh();
    mfactory = MeshFactory.MeshFactory();
    cube = mfactory.CreateGrid(10, 5);
    #cube = mfactory.CreateScrew(12);


    #mmodifier = MeshModifier.MeshModifier(cube);
    #mmodifier.DecimatePlanar();

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube.DrawFaces();
        cube.DrawEdges();
        cube.DrawPoints();
        #cube.Rotate((1, 1, 3, 1));

        pygame.display.flip();
        pygame.time.wait(10)


main()