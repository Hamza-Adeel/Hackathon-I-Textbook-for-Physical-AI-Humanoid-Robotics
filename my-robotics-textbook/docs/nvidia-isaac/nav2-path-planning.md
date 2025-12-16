---
title: Integrating Nav2 for Path Planning
sidebar_label: Nav2 Path Planning
---

# Lesson 3.3: Integrating Nav2 for Path Planning

While Isaac Sim is a powerful tool for perception and AI training, robotics is fundamentally about moving and acting in an environment. To achieve autonomous navigation, we can integrate our Isaac Sim simulation with **Nav2**, the standard navigation stack in ROS 2.

This lesson provides a high-level overview of how to get a simulated robot in Isaac Sim to navigate its environment using Nav2.

## What is Nav2?

Nav2 is the second generation of the ROS Navigation Stack. It's a complete software package that enables a robot to move from a starting point to a destination while safely avoiding obstacles.

It is composed of many different nodes and algorithms, including:
-   **A global planner**: Finds a long-range path from the start to the goal on a map.
-   **A local planner**: Generates motor commands to follow the global plan while avoiding immediate obstacles detected by sensors.
-   **A costmap**: A data structure that represents the environment, marking where obstacles are and where it's safe for the robot to travel.
-   **An AMCL (Adaptive Monte Carlo Localization) module**: Helps the robot figure out where it is on the map based on sensor data.

## The Sim-to-Real Workflow with Nav2

The power of combining Isaac Sim and Nav2 is that you can develop and tune your entire navigation stack in simulation before deploying it to a physical robot. The workflow looks like this:

1.  **Build Your World**: Create a replica of your real-world environment inside Isaac Sim. This includes the static layout (walls, furniture) and any dynamic obstacles.

2.  **Import Your Robot**: Import your robot's URDF model into the Isaac Sim scene. Configure it with simulated sensors (LiDAR, cameras) and a differential drive controller (or another appropriate controller for your robot's base).

3.  **Bridge to ROS 2**: Use Isaac Sim's built-in ROS 2 bridge to publish the simulated sensor data (like `/scan` and `/odom`) to ROS 2 topics and to subscribe to the command velocity topic (typically `/cmd_vel`) that Nav2 will use to send motor commands.

4.  **Generate a Map**: Just as you would with a real robot, you can "drive" the simulated robot around the environment to build a map using ROS 2 SLAM (Simultaneous Localization and Mapping) tools like `slam_toolbox`.

5.  **Launch Nav2**: With the generated map, launch the Nav2 stack. You can now provide a goal pose in RViz (the ROS 2 visualizer), and Nav2 will take over.

6.  **Navigation in Action**:
    -   Nav2's global planner will find a path on the map.
    -   Nav2's local planner will generate velocity commands based on the simulated LiDAR data.
    -   These commands are sent to the `/cmd_vel` topic.
    -   Isaac Sim receives these commands and moves the simulated robot.
    -   The simulated LiDAR provides new data based on the robot's new position.
    -   This loop continues until the robot reaches its goal.

By using this workflow, you can perfect your Nav2 configuration and test its robustness in a safe, repeatable, and fast simulation environment, significantly speeding up your development time.