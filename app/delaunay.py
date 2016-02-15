# GEO3001 - Assignment 4
# Author: Luciana Toyoda
# Studentnumber: 4331605

import math

class Point(object):
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def __str__(self):
        """Well Known Text of this point
        """
        return "POINT({} {})".format(self.x, self.y)

    def __eq__(self, other):
        """Compare values (this object instance == other instance?).

        :param other: the point to compare with
        :type other: Point

        Returns True/False        """
        xequal = (self.x == other.x)
        yequal = (self.y == other.y)
        return xequal and yequal


    def distance(self, other):
        """Returns distance as float to the *other* point
        (assuming Euclidean geometry)

        :param other: the point to compute the distance to
        :type other: Point        """

        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**(0.5)
        return distance


class Circle(object):
    def __init__(self, center, radius):
        """Constructor"""
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """Returns WKT str, discretizing the circle into straight
        line segments         """
        N = 400
        step = 2.0 * math.pi / N
        pts = []
        for i in range(N):
            pts.append(Point(self.center.x + math.cos(i * step) * self.radius,
                             self.center.y + math.sin(i * step) * self.radius))
        pts.append(pts[0])
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON(({0}))".format(coordinates)

    def covers(self, pt):
        """Returns True when the circle covers point *pt*,
        False otherwise

        Note that we consider points that are near to the boundary of the
        circle also to be covered by the circle(arbitrary epsilon to use: 1e-8). """
        if pt.distance(self.center) <= self.radius + 1e-8:
            return True
        else:
            return False

    def area(self):
        """Returns area as float of this circle """
        area = math.pi * (self.radius**2)
        return area

    def perimeter(self):
        """Returns perimeter as float of this circle """
        perimeter  = 2 * math.pi * self.radius
        return perimeter


class Triangle(object):
    def __init__(self, p0, p1, p2):
        """Constructor
        Arguments: p0, p1, p2 -- Point instances
        """
        self.p0, self.p1, self.p2 = p0, p1, p2

    def __str__(self):
        """String representation"""
        points = ["{0.x} {0.y}".format(pt) for pt in (self.p0, self.p1, self.p2, self.p0)]
        return "POLYGON(({0}))".format(", ".join(points))

    def circumcircle(self):
        """Returns Circle instance that intersects the 3 points of the triangle"""
        a = self.p0
        b = self.p1
        c = self.p2
        D = 2.0*(a.x * (b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y))+ 1e-8
        d = (a.x**2 + a.y**2) * (b.y - c.y)
        e = (b.x**2 + b.y**2) * (c.y - a.y)
        f = (c.x**2 + c.y**2) * (a.y - b.y)
        ux = (d + e + f)/D
        g = (a.x**2 + a.y**2) * (c.x - b.x)
        h = (b.x**2 + b.y**2) * (a.x - c.x)
        i = (c.x**2 + c.y**2) * (b.x - a.x)
        uy = (g + h + i)/D
        u = Point(ux,uy)
        return u

    def area(self):
        """Area of this triangle, using heron's formula (see Assignment 1)."""
        a = abs(self.p0.distance(self.p1))
        b = abs(self.p1.distance(self.p2))
        c = abs(self.p0.distance(self.p2))
        s = ((a+b+c)/2)
        Area = (s*(s-a)*(s-b)*(s-c))**0.5
        return Area

    def perimeter(self):
        """Perimeter of this triangle (float)"""
        dist_p0_p1 = self.p0.distance(self.p1)
        dist_p1_p2 = self.p1.distance(self.p2)
        dist_p2_p0 = self.p0.distance(self.p2)
        perimeter = dist_p0_p1 + dist_p1_p2 + dist_p2_p0
        return perimeter


class DelaunayTriangulation(object):
    def __init__(self, points):
        """Constructor
        To call the Class: trid = DelaunayTriangulation([point1, point2, point3])"""
        self.triangles = []
        self.points = points

    def triangulate(self,points):
        """Triangulates the given set of points.

        This method takes the set of points to be triangulated
        (with at least 3 points) and for each 3-group of points instantiates
        a triangle and checks whether the triangle conforms to Delaunay
        criterion. If so, the triangle is added to the triangle list.

        To determine the 3-group of points, the group3 function is used.

        Returns None
        """
        # pre-condition: we should have at least 3 points
        self.points = points
        assert len(self.points) > 2
        N = len(self.points)
        a = self.points
        triangles = self.triangles
        lista = []
        for item in group3(N):
            lista.append(item)
        for i in range(len(lista)):
            point1 = a[lista[i][0]]
            point2 = a[lista[i][1]]
            point3 = a[lista[i][2]]
            points = point1, point2, point3
            trid = DelaunayTriangulation([point1, point2, point3])
            if trid.are_collinear(point1, point2, point3) is False:
                if trid.is_delaunay([point1, point2, point3]) is True:
                    triangles.append(points)
            else:
                pass
        self.triangles = triangles
        return triangles
        pass

    def is_delaunay(self, tri):
        """Does a triangle *tri* conform to the Delaunay criterion?
        Algorithm:
        Are 3 points of the triangle collinear?
            No:
                Get circumcircle
                Count number of points inside circumcircle
                if number of points inside == 3:
                    Delaunay
                else:
                    not Delaunay
            Yes:
                not Delaunay

        Arguments:
            tri -- Triangle instance
        Returns:
            True/False        """
        self.point1 = tri[0]
        self.point2 = tri[1]
        self.point3 = tri[2]
        trid = DelaunayTriangulation([self.point1, self.point2, self.point3])
        if trid.are_collinear(self.point1, self.point2, self.point3) is False:
            triangle = Triangle(self.point1, self.point2, self.point3)  #Get circumcircle
            circ_center = triangle.circumcircle() # OK
            radius = self.point1.distance(circ_center)
            roda1 = Circle(circ_center,radius)
            n=0
            for i in range (len(self.points)):
                if n > 3:
                    return False
                if roda1.covers(self.points[i]) is True:
                    n = n+1
            if n == 3:
                    return True
            return True
        return False

    def are_collinear(self, pa, pb, pc):
        """Orientation test to determine whether 3 points are collinear
        (on straight line).

        Note that we consider points that are nearly collinear also to be on
        a straight line (arbitrary epsilon to use: 1e-8).

        Returns True / False
        To call the function: trid.are_collinear(point1, point2, point3)"""
        self.pa = pa
        self.pb = pb
        self.pc = pc
        a = self.pa
        b = self.pb
        c = self.pc
        a_b = a.distance(b)
        a_c = a.distance(c)
        b_c = b.distance(c)
        if (a.x == c.x and b.x == c.x) or (a.y == c.y and b.y == c.y) is True: #Same x or y line
            return True
        elif a_b == (a_c + b_c) or a_c == (a_b + b_c) or b_c == (a_b + a_c) is True:
            return True
        return False

    def output_points(self, open_file_obj,triangle):
        """Outputs the points of the triangulation to an open file.       """
        fh = open_file_obj
        self.triangle = triangle
        fh.write('wkt\n')
        for i in range(len(self.triangle[0])):
            tri = self.triangle[0][i]
            point1 = tri[0]
            point2 = tri[1]
            point3 = tri[2]
            point1_str = str(point1)
            fh.write(point1_str)
            fh.write (' \n')
            point2_str = str(point2)
            fh.write(point2_str)
            fh.write (' \n')
            point3_str = str(point3)
            fh.write(point3_str)
            fh.write (' \n')

    def output_triangles(self, open_file_obj, triangle):
        """Outputs the triangles of the triangulation to an open file.        """
        fh = open_file_obj
        self.triangle = triangle
        for i in range(len(self.triangle[0])):
            tri = self.triangle[0][i]
            point1 = tri[0]
            point2 = tri[1]
            point3 = tri[2]
            tri = Triangle(point1, point2, point3)
            area = str(tri.area())
            perimeter = str(tri.perimeter())
            fh.write('wkt; ')
           # fh.write('tid:')
            fh.write(str(i+1))
            fh.write('; ')
            fh.write(area)
            fh.write('; ')
            fh.write(perimeter)
            fh.write (' \n')
            fh.write(str(tri))
            fh.write (' \n')

    def output_circumcircles(self, open_file_obj, triangle):
        """Outputs the circumcircles of the triangles of the triangulation
        to an open file        """
        fh = open_file_obj
        self.triangle = triangle
        for i in range(len(self.triangle[0])):
            tri = self.triangle[0][i]
            point1 = tri[0]
            point2 = tri[1]
            point3 = tri[2]
            triangle = Triangle(point1, point2, point3)  #Get circumcircle
            circ_center = triangle.circumcircle() # OK
            radius = point1.distance(circ_center)
            # getting the circle, area and perimeter
            circle1 = Circle(point1,radius)
            area1 = str(circle1.area())
            perimeter1 = str(circle1.perimeter())
            circle2 = Circle(point2,radius)
            area2 = str(circle2.area())
            perimeter2 = str(circle2.perimeter())
            circle3 = Circle(point3,radius)
            area3 = str(circle3.area())
            perimeter3 = str(circle3.perimeter())
            # Writtning to the file
            fh.write('wkt; ')
            fh.write(str(i+1))
            fh.write('; ')
            fh.write(area1)
            fh.write('; ')
            fh.write(perimeter1)
            fh.write (' \n')
            fh.write(str(circle1))
            fh.write (' \n')
            fh.write('wkt; ')
            fh.write(str(i+1))
            fh.write('; ')
            fh.write(area2)
            fh.write('; ')
            fh.write(perimeter2)
            fh.write (' \n')
            fh.write(str(circle2))
            fh.write (' \n')
            fh.write('wkt; ')
            fh.write(str(i+1))
            fh.write('; ')
            fh.write(area3)
            fh.write('; ')
            fh.write(perimeter3)
            fh.write (' \n')
            fh.write(str(circle3))
            fh.write (' \n')


def group3(N):
    """Returns generator with 3-tuples with indices to form 3-groups
    of a list of length N.

    Total number of tuples that is generated: N! / (3! * (N-3)!)

    For N = 3: [(0, 1, 2)]
    For N = 4: [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    For N = 5: [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3),
                (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4),
                (1, 3, 4), (2, 3, 4)]

    Example use:

        >>> for item in group3(3):
        ...     print item
        ...
        (0, 1, 2)

    """
    for i in xrange(N - 2):
        for j in xrange(i+1, N - 1):
            for k in xrange(j+1, N):
                yield (i, j, k)


def make_random_points(n):
    """Makes n points distributed randomly in x,y between [0,1000]

    Note, no duplicate points will be created, but might result in slightly
    less than the n number of points requested.
    """
    import random
    pts = list(set([Point(random.randint(0,1000),
                          random.randint(0,1000)) for i in xrange(n)]))
    return pts


def main(n):
    """Perform triangulation of n points and write the resulting geometries
    to text files.
    """
    pts = make_random_points(n)
    dt = DelaunayTriangulation(pts)
    teste = dt.triangulate(pts)
    # using the with statement, we do not need to close explicitly the file
    with open("points.wkt", "w") as fh:
        dt.output_points(fh,[teste])
    with open("triangles.wkt", "w") as fh:
        dt.output_triangles(fh,[teste])
    with open("circumcircles.wkt", "w") as fh:
        dt.output_circumcircles(fh,[teste])


#def _test():

    # # Testing for point
# point1 = Point(1.0, 1.0)
# point2 = Point(5.0, 7.0)
# point3 = Point(5.0, 7.0)
# print point2.distance(point3)  # OK

# # Testing for Circle
# point1 = Point(1.0, 1.0)
# point2 = Point(5.0, 7.0)
# radius = 3
# roda1 = Circle(Point(1.0, 1.0),radius)
# print 'the area of the circle is',
# print roda1.area()
# print 'the perimeter of the circle is',
# print roda1.perimeter()
# print roda1
# print roda1
# print roda1.covers(point1)
# print roda1.covers(point2)

# # Testing for triangle
# point1 = Point(-2.0, 0.0)
# point2 = Point(2.0, 0.0)
# point3 = Point(0.0, 4.0)
# tri = Triangle(point1, point2, point3)
# print tri  # OK
# print 'circumcircle', tri.circumcircle() # OK
# print tri.area()  # OK
# print tri.perimeter()  # OK

# # # Testing for delaunay
#     point1 = Point(-2.0, 0.0)
#     point2 = Point(2.0, 0.0)
#     point3 = Point(0.0, 4.0)
#     point4 = Point(0.1, 4.3)
#     points = (point1, point2, point3)
#     tri = Triangle(point1, point2, point3)
#     tri_del = DelaunayTriangulation([point1, point2, point3])
# #    print tri_del.are_collinear()
# #    print trid.are_collinear()
#     print trid.are_collinear(point1, point2, point3)
#  #   print trid.are_collinear(tri.pa, tri.pb,tri.pc)
# #    print (are_collinear([point1, point2, point3]))
#
#     pass

if __name__ == "__main__":
    main(5)