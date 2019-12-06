

from Mesh import Mesh
from Mesh import MeshFactory
from Mesh import MeshModifier

from Window import Window



def main():


    window = Window.Window();
    window.SetWindowSize(800, 600);
    window.SetDefaultCamera();


    temp = Mesh.Mesh();
    mfactory = MeshFactory.MeshFactory();
    cube = mfactory.CreateCube();
    #cube = mfactory.CreateScrew(12);


    #mmodifier = MeshModifier.MeshModifier(cube);
    #mmodifier.DecimatePlanar();

    while window.IsQuitRequest() == False:

        window.Clear();

        cube.DrawFaces();
        cube.DrawEdges();
        cube.DrawPoints();
        cube.Rotate((1, 1, 3, 1));

        window.DisplayFlip();
        window.Wait(10);
        pass;

    window.Quit();


main();