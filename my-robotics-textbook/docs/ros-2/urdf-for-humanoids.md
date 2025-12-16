---
title: Building URDF for Humanoid Models
sidebar_label: URDF for Humanoids
---

# Lesson 1.3: Building URDF for Humanoid Models

A crucial part of robotics simulation and visualization is having an accurate model of the robot itself. In the ROS ecosystem, the standard for describing a robot's physical structure is the **Unified Robot Description Format (URDF)**.

URDF is an XML-based format that allows you to specify the various parts of a robot, including its links, joints, sensors, and visual appearance.

## Core Components of URDF

A URDF file is built around two fundamental components:

-   **`<link>`**: A link represents a rigid part of the robot, like a forearm, a wheel, or a torso. Each link has physical properties like mass and inertia, as well as visual properties (what it looks like) and collision properties (its physical shape for physics simulation).
-   **`<joint>`**: A joint connects two links together and defines how they can move relative to each other. Common joint types include `revolute` (for rotating joints like an elbow), `prismatic` (for sliding joints), and `fixed` (for two links that are rigidly attached).

## Example: A Simple Two-Link Arm

Let's look at a snippet of a URDF file for a simple robotic arm with two links connected by a revolute joint.

```xml
<?xml version="1.0"?>
<robot name="simple_arm">

  <!-- Base Link -->
  <link name="base_link">
    <visual>
      <geometry>
        <cylinder length="0.6" radius="0.2"/>
      </geometry>
    </visual>
    <collision>
      <geometry>
        <cylinder length="0.6" radius="0.2"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1"/>
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/>
    </inertial>
  </link>

  <!-- Arm Link -->
  <link name="arm_link">
    <visual>
      <geometry>
        <box size="0.8 0.2 0.2"/>
      </geometry>
    </visual>
    <collision>
       <geometry>
        <box size="0.8 0.2 0.2"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/>
    </inertial>
  </link>

  <!-- Joint connecting Base and Arm -->
  <joint name="base_to_arm" type="revolute">
    <parent link="base_link"/>
    <child link="arm_link"/>
    <origin xyz="0 0 0.3"/>
    <axis xyz="0 1 0"/>
    <limit lower="-3.14" upper="3.14" effort="10" velocity="1"/>
  </joint>

</robot>
```

### URDF for Humanoids

For a humanoid robot, the URDF file becomes much more complex, but the principles are the same. You will define a tree of links and joints starting from a central `base_link` (often the torso) and branching out to define the head, arms, legs, hands, and feet.

Building a full humanoid URDF is a meticulous process of defining the geometry and kinematics of every single part of the robot, but it is essential for realistic simulation and for tools like RViz (the ROS 2 visualizer) to display the robot's state correctly.