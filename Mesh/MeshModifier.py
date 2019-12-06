from Math import Vec4;
from Math import Vec2;

from Mesh import Mesh;

class MeshModifier:

    _meshToManage = None;
    _oldMeshData = None;

    def __init__(self, mesh : Mesh.Mesh):
        self._meshToManage = mesh;
        pass;

    def DecimatePlanar(self):
        tmpMesh = self._meshToManage;
        tmpVertices = tmpMesh._vertices;
        tmpEdges = tmpMesh._edges;

        leftDown = [999999999, 999999999, 0];
        leftUp = [999999999, -999999999, 0];
        rightDown = [-999999999, 999999999, 0];
        rightUp = [-999999999, -999999999, 0];

        leftDownIndex = -1;
        leftUpIndex = -1;
        rightDownIndex = -1;
        rightUpIndex = -1;

        #vyhladanie topleft, downleft, topright a downleft

        iIteration = 0;
        for i in tmpVertices:
            if (i[0] <= leftDown[0]) and (i[1] <= leftDown[1]):
                leftDown = i;
                leftDownIndex = iIteration;
            if (i[0] <= leftUp[0]) and (i[1] >= leftUp[1]):
                leftUp = i;
                leftUpIndex = iIteration;
            if (i[0] >= rightDown[0]) and (i[1] <= rightDown[1]):
                rightDown = i;
                rightDownIndex = iIteration;
            if (i[0] >= rightUp[0]) and (i[1] >= rightUp[1]):
                rightUp = i;
                rightUpIndex = iIteration;
            iIteration += 1;
        del iIteration;

        #now computer find straight edge and choose pivot
        #if left down and up has same X position i can dedicate, there can be something in middle of them

        print("Left down is: " + str(leftDown));
        print("Left up is: " + str(leftUp));
        print("Right down is: " + str(rightDown));
        print("Right up is: " + str(rightUp));

        top = self.FindHalfBoundary(leftUpIndex, rightUpIndex, tmpMesh, True, False);
        down = self.FindHalfBoundary(leftDownIndex, rightDownIndex, tmpMesh, False, False);
        #left = self.FindHalfBoundary(leftDownIndex, leftUpIndex, tmpMesh, True, True);
        #right = self.FindHalfBoundary(rightUpIndex, rightUpIndex, tmpMesh, False, True);
        result = { leftUpIndex };

        for i in top:
            result.add(i);
        for i in down:
            result.add(i);

        print("Result is " + str(result));


        pass;

    #funkcia vyhladava hranice pre urcenu polovicu
    def FindHalfBoundary(self, startVertex, endVertex, tmpMesh, directoryX, directoryY) -> []:

        tmpVertices = tmpMesh._vertices;
        tmpEdges = tmpMesh._edges;

        minmax = 0;
        if directoryX == True:
            minmax = -999999;
        else:
            minmax = 999999;

        topLeftVertices = [startVertex];
        actualIndexLeft = startVertex;

        #triedenie vertexov podla vzdialenosti od objektu
        iIteration = 0;
        availableEdges = [];
        while actualIndexLeft != endVertex:
            if iIteration == len(tmpEdges):
                neighbours = {actualIndexLeft};
                for edge in availableEdges:
                    neighbours.add(edge[0]);
                    neighbours.add(edge[1]);
                    pass;
                lastIndex = [-1, minmax];
                #print("Susedia vrcholu " + str(actualIndexLeft) + " " + str(neighbours));
                for vertex in neighbours:
                    if directoryX == True and directoryY == False:
                        if (tmpVertices[vertex][0] > tmpVertices[actualIndexLeft][0]) and (tmpVertices[vertex][1] > lastIndex[1]):
                             lastIndex[0] = vertex;
                             lastIndex[1] = tmpVertices[vertex][1];
                             pass;
                    if directoryX == False and directoryX == False:
                         if (tmpVertices[vertex][0] > tmpVertices[actualIndexLeft][0]) and (tmpVertices[vertex][1] < lastIndex[1]):
                             lastIndex[0] = vertex;
                             lastIndex[1] = tmpVertices[vertex][1];
                             pass;
                    if directoryX == True and directoryY == True:
                        if (tmpVertices[vertex][0] < tmpVertices[actualIndexLeft][0]) and (tmpVertices[vertex][1] < lastIndex[1]):
                             lastIndex[0] = vertex;
                             lastIndex[1] = tmpVertices[vertex][1];
                             pass;
                    if directoryX == False and directoryY == True:
                         if (tmpVertices[vertex][0] > tmpVertices[actualIndexLeft][0]) and (tmpVertices[vertex][1] < lastIndex[1]):
                             lastIndex[0] = vertex;
                             lastIndex[1] = tmpVertices[vertex][1];
                             pass;

                     
                    pass;
                actualIndexLeft = lastIndex[0];
                topLeftVertices.append(actualIndexLeft);
                iIteration = 0;
                availableEdges.clear();
                pass;
            if (tmpEdges[iIteration][0] ==  actualIndexLeft) or (tmpEdges[iIteration][1] == actualIndexLeft):
                availableEdges.append(tmpEdges[iIteration]);
                #print("Pridavam spriateleny edge" + str(tmpEdges[iIteration]));
                pass;
            iIteration += 1;
            pass;
        print("Boundary is " + str(topLeftVertices));
        return topLeftVertices;

        pass;

    

    