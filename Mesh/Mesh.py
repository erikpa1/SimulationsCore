from Math import Vec4
from Math import Vec2

from OpenGL.GL import *
from OpenGL.GLU import *


class Mesh:

    _vertices = [];
    _edges = [];
    _faces = [];
    _uv = [];

    def __init__(self):
        print("Mesh created");


    def GetVertices(self) -> []: return self._vertices; pass;
    def GetEdges(self) -> []: return self._edges; pass;


    def Step(self):
        pass;

    def Rotate(self, vector):
        glRotate(vector[0], vector[1], vector[2], vector[3]);
        pass;

    #adding vertices to mesh
    def PushVertices(self, vec4: Vec4):
        self._vertices.append(vec4);
        pass

    #adding edges to mesh
    def PushEdges(self, vec2: Vec2):
        self._edges.append(vec2);
        pass

    #adding faces to mesh
    def PushFaces(self, face):
        self._faces.append(face);
        pass;


    def DrawFaces(self):
        glBegin(GL_TRIANGLES);
        glColor3fv((0, 1, 1));
        for face in self._faces:
            for i in range(3):
                glVertex3fv(self._vertices[face[i]]);
        glEnd();

        glBegin(GL_LINES);
        glColor3fv((0, 0.5, 0.5));
        for face in self._faces:
            for i in range(3):
                glVertex3fv(self._vertices[face[i]]);
        glEnd();
        pass;

        #self.Draw(GL_TRIANGLES, (0,1,1));
        #pass;

    def DrawPoints(self):
        glPointSize(10);

        glBegin(GL_POINTS);
        for vertex in self._vertices:
            glColor3fv((0.9, 0, 0));
            glVertex3fv(vertex);
        glEnd();

        pass;

    def DrawEdges(self):
        glBegin(GL_LINES);
        for edge in self._edges:
            for vertex in edge:
                glColor3fv((1,1,1));
                glVertex3fv(self._vertices[vertex]);
        glEnd();
        pass;

    def RebuildFaces(self):
        pass;

