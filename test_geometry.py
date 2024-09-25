import unittest
from geometry import *


class TestGeometry(unittest.TestCase):

    def setUp(self):
        # We create a bunch of ponts first 

        # The center of the coordinate system is called the origin
        self.origin = Point(0,0,0)
        self.one_above_origin = Point(0, 1, 0)
        self.one_under_origin = Point(0, -1, 0)
        self.out_point= Point(0, 1000, 0)

        self.one_radius_sphere = Sphere(0, 0, 0, 1)
        self.ten_radius_sphere = Sphere(0, -1, 0, 10)

        self.one_cube = Cube(0, 0, 0, 1)
        self.ten_cube = Cube(0, 0, 0, 10)

    

    def test_001_point_distance(self):
        self.assertEqual(int(self.one_above_origin.distance(self.one_under_origin)), 2)
        self.assertEqual(int(self.origin.distance(self.out_point)), 1000)


# Implement the following test cases
# create objects as needed in setup or other places 

    #TODO! Implement this 
    def test_002_point_equality(self):
         self.assertTrue(self.origin == Point(0, 0, 0))
         self.assertFalse(self.origin == Point(1, 1, 1))

    #TODO! Implement this 
    def test_003_sphere_area(self):
        self.assertAlmostEqual(self.one_radius_sphere.area(), 12.566370614, places = 6)
        self.assertAlmostEqual(self.ten_radius_sphere.area(), 1256.63706144, places = 6)


    
    #TODO! Implement this 
    def test_004_sphere_volume(self):
        self.assertAlmostEqual(self.one_radius_sphere.volume(), 4.18879020479, places = 6)
        self.assertAlmostEqual(self.ten_radius_sphere.volume(), 4188.79020479, places = 6)



    #TODO! Implement this 
    def test_005_sphere_is_inside_point(self):
        self.assertTrue(self.one_radius_sphere.is_inside_point(self.origin))
        self.assertFalse(self.one_radius_sphere.is_inside_point(self.out_point))


    #TODO! Implement this 
    def test_006_sphere_is_inside_sphere(self):
        self.assertTrue(self.ten_radius_sphere.is_inside_sphere(self.one_radius_sphere))
        self.assertFalse(self.one_radius_sphere.is_inside_sphere(self.ten_radius_sphere))



   #TODO! Implement this 
    def test_006_cube_is_inside_point(self):
        self.assertTrue(self.one_cube.is_inside_point(self.origin))
        self.assertFalse(self.ten_cube.is_inside_point(self.out_point))

   #TODO! Implement this 
    def test_007_is_inside_sphere(self):
        self.assertTrue(self.ten_cube.is_inside_sphere(self.one_radius_sphere))
        self.assertFalse(self.one_cube.is_inside_sphere(self.ten_radius_sphere))



# Here we have the test but we do not have the implementation of the method is_inside_cube()
# 
# No need to change these tests here 
# You need to implement the method is_inside_cube()
    def test_000_is_inside_cube(self):
        self.assertTrue(self.one_cube.is_inside_cube(self.ten_cube))
        self.assertFalse(self.one_cube.is_inside_cube(self.one_cube))

    def test_000_has_same_volume(self): 
        self.assertTrue(self.one_cube.has_same_volume(self.one_cube)) 




if __name__ == '__main__':
    unittest.main()