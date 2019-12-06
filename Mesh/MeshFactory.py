import math


from Mesh import Mesh
from Math import Vec2
from Math import Vec4
from Math import GeometryMath




class MeshFactory:

    def __init__(self):
        print("Meshfactory is created");
        pass;

    def CreateMeshFromVertexStream(self):
        pass;

    def CreateCube(self) -> Mesh:
        tmp = Mesh.Mesh();
        tmp.PushVertices((1, -1, -1));
        tmp.PushVertices((1, 1, -1));
        tmp.PushVertices((-1, 1, -1));
        tmp.PushVertices((-1, -1, -1));
        tmp.PushVertices((1, -1, 1));
        tmp.PushVertices((1, 1, 1));
        tmp.PushVertices((-1, -1, 1));
        tmp.PushVertices((-1, 1, 1));

        tmp.PushEdges((0, 1));
        tmp.PushEdges((0, 3));
        tmp.PushEdges((0, 4));
        tmp.PushEdges((2, 1));
        tmp.PushEdges((2, 3));
        tmp.PushEdges((2, 7));
        tmp.PushEdges((6, 3));
        tmp.PushEdges((6, 4));
        tmp.PushEdges((6, 7));
        tmp.PushEdges((5, 1));
        tmp.PushEdges((5, 4));
        tmp.PushEdges((5, 7));

        return tmp;

    def CreateGrid(self, horizontalCut : int, verticalCut : int) -> Mesh:

            tmpmesh = Mesh.Mesh();

            #generovanie bodov mriezky
            for i in range(horizontalCut):
                for j in range(verticalCut):
                    tmpmesh.PushVertices((i - (horizontalCut-1)/2 , j - (verticalCut-1)/2, -5));
                    print("i: " + str(i) + " j: " + str(j));

            print("Number of grid vertices: " + str(len(tmpmesh.GetVertices())));
            print("Going to connect vertical edges");
            #generovanie vertikalnych edgov medzi bodmi
            for j in range(horizontalCut):
                for i in range(verticalCut - 1):
                    tempedge = (i + j*verticalCut, j*verticalCut + i +1);
                    tmpmesh.PushEdges(tempedge);
                    print("Connecting" + str(tempedge));

            print("Going to connect horizontal");

            #generovanie horizontalnych edgov medzi bodmi
            for j in range(verticalCut):
                for i in range(horizontalCut-1):
                    tempedge = [j+i*verticalCut, (j+i*verticalCut + verticalCut)];
                    tmpmesh.PushEdges(tempedge);
                    print("Connecting" + str(tempedge));

            print("Number of grid edges: " + str(len(tmpmesh.GetEdges())));
            print("Going to generate faces");

            #generovanie facov
            for i in range(verticalCut-1):
                for j in range(horizontalCut-1):
                    tmp1 = [0, 0, 0];
                    tmp1[0] = j*verticalCut + i;
                    tmp1[1] = j*verticalCut + i + 1;
                    tmp1[2] = j*verticalCut + i + verticalCut;

                    tmp2 = [0, 0, 0];
                    tmp2[2] = j*verticalCut + i + verticalCut;
                    tmp2[1] = j*verticalCut + i + verticalCut + 1;
                    tmp2[0] = j*verticalCut + i + 1;
                    tmpmesh.PushFaces(tmp1);
                    tmpmesh.PushFaces(tmp2);
                    pass;

            return tmpmesh;

    def CreateCylinder(self, facenumber : int) -> Mesh:
        tmpMesh = Mesh.Mesh();
        self.CreateCylinderBase(tmpMesh, 1, facenumber, 1);
        self.CreateCylinderBase(tmpMesh, 1, facenumber, -1);

        arrayOffset = len(tmpMesh._vertices)/2

        for i in range(facenumber):
            tmpMesh.PushEdges((i, i+facenumber));

        return tmpMesh;

    def CreateScrew(self, facenumber : int) -> Mesh:

        tmpMesh = Mesh.Mesh();
        self.CreateCylinderBase(tmpMesh, 1, facenumber, 0.5);
        self.CreateCylinderBase(tmpMesh, 1, facenumber, -1);
        self.CreateCylinderBase(tmpMesh, 0.5, facenumber, -1);
        self.CreateCylinderBase(tmpMesh, 0.5, facenumber, -4);

        self.CreateCylinderSide(tmpMesh, 0, facenumber);
        self.CreateCylinderSide(tmpMesh, facenumber, facenumber);
        self.CreateCylinderSide(tmpMesh, 2*facenumber, facenumber);

        return tmpMesh;

        pass;


    def CreateCylinderBase(self, mesh : Mesh.Mesh, length : int,  facenumber : int, zValue : int):
        tmpvertices = [];
        anglestep = 360 / facenumber;
        radius = 1;
        piAngles = [0];
        xValues = [math.cos(piAngles[0])];
        yValues = [math.sin(piAngles[0])];

        meshArrayOffset = len(mesh._vertices);


        for i in range(1, facenumber):
            piAngles.append(piAngles[i - 1] + anglestep);
            xValues.append(math.cos(GeometryMath.DegToRadians(piAngles[i])));
            yValues.append(math.sin(GeometryMath.DegToRadians(piAngles[i])));

            print("Sin of " + str(piAngles[i]) + " is " + str(
                math.sin(GeometryMath.DegToRadians(piAngles[i]))) + " Cos of " + str(piAngles[i]) + " is " + str(
                math.cos(GeometryMath.DegToRadians(piAngles[i]))));
            print("Adding angle of " + str(piAngles[i]));

        for i in range(len(xValues)):
            tmpvertices.append((xValues[i]*length, yValues[i]*length, zValue));
            mesh.PushVertices(tmpvertices[i]);

        for i in range(len(xValues)-1):
            mesh.PushEdges((i+meshArrayOffset, i+meshArrayOffset+1));
        mesh.PushEdges((0+meshArrayOffset, len(xValues)+meshArrayOffset-1));
        pass;

    def CreateCylinderSide(self, mesh : Mesh, start : int, arrayStep : int):
        for i in range(start, start + arrayStep):
            mesh.PushEdges((i, i + arrayStep));
        pass;








