

# Projection and its algorithm

<!-- ## Definition -->

**In this project, we will encounter an algorithm to take the projection of any 3D polyhedron onto a plane passing through a specific point inside it. We will be engaged with linear algebra, linear space transformation, 3D geometry involving equation of planes and lines, vector algebra and 3D spherical coordinate system. Let’s say that we have a cuboid placed in a 3D coordinate system and we are observing it from a given set of coordinates and focusing on a specific point. Then how will this cuboid appear to us?**

![Example of the projection](https://github.com/sumit-6/Projection-and-its-algorithm/blob/main/Diagram.png)

# Description🧠
There are 24 variable in the beginning of the code namely, x1, x2, .... x8 for storing x coordinates of the 8 vertices, y1, y2, y3, .... y8 for storing y coordinates of the 8 vertices and z1, z2, z3, .... z8 for storing z coordinates of the 8 vertices.
The values for all of these 24 variables has been assigned in the code but you can change it as per your choice.

Also, there are 3 variables focus_x, focus_y and focus_z that represents the coordinate of the point of "focus" of the observer. In the code, it has been initiated in such a way that it represents the center of mass of the cuboid.
But again, you can change it as per your choice.

 On execution of the code, you have to enter the coordinates of observer's position as an input. And then it will apply the algorithm to plot the projection of cuboid from the observer's point of view.

# Run Demo💻
There is only one python file in this project: 3D_cuboid_simulation.py
Packages required in order to run 3D_cuboid_simulation.py: Turtle and Numpy.
Steps to run the project :-
1. Install the package - numpy by using a command "pip install numpy" on command prompt.
2. Run the python file and enter the dimensions of cuboid along with the x, y and z coordinate of observer's location in 3D space as the input.
3. Press Enter and then you will get the projection of the cuboid to be plotted onto the screen.

 
 
