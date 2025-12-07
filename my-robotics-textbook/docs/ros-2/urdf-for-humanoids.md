# Describing Robots with URDF

This lesson introduces the Unified Robot Description Format (URDF) for modeling robots in ROS 2.

## Objective
By the end of this lesson, you will be able to:
- Understand the purpose and structure of URDF files.
- Define robot links and joints using URDF.
- Create a basic URDF model for a simple robotic arm or humanoid.

## Main Content
- Introduction to robot modeling: why URDF is essential for simulation and visualization.
- Anatomy of a URDF file: `<robot>`, `<link>`, `<joint>` elements.
- Defining physical properties: mass, inertia, visual, and collision elements.
- Joint types: fixed, revolute, prismatic, continuous.
- Advanced URDF features: Xacro for modularity.

## Tutorial/Example
A step-by-step tutorial on creating a URDF file for a two-link robotic arm. This includes defining the base link, two arm links, and two revolute joints. The tutorial will then guide you through visualizing the robot in `rviz` using `robot_state_publisher` and `joint_state_publisher`.

## Summary
- URDF is an XML format for describing the kinematic and dynamic properties of a robot.
- It defines the robot's physical structure (links) and how they are connected (joints).
- URDF is crucial for simulation, visualization, and motion planning in ROS 2.

## Further Reading
- [ROS 2 Documentation: URDF Overview](https://docs.ros.org/en/humble/Tutorials/URDF/URDF-Overview.html)
- [ROS 2 Documentation: Creating a URDF File](https://docs.ros.org/en/humble/Tutorials/URDF/Building-a-Visual-Robot-Model-with-URDF-from-Scratch.html)
- [Gazebo Documentation: URDF](http://classic.gazebosim.org/tutorials?tut=ros_urdf)
