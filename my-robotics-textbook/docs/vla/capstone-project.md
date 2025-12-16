---
title: Capstone Project - VLA-Powered Task Execution
sidebar_label: Capstone Project
---

# Lesson 4.3: Capstone Project - VLA-Powered Task Execution

In this final lesson, we will bring together all the concepts from this textbook to create a complete Vision-Language-Action (VLA) system. Our goal is to build a simulated robot that can understand a spoken, high-level command and execute the corresponding physical task in a simulated environment.

## Project Goal

To create a system where a user can say, "Please pick up the red cube and place it on the blue platform," and a simulated robot arm will perform the task.

## System Architecture

Our capstone project will integrate modules from all four chapters of this book:

1.  **ROS 2 (The Nervous System)**:
    -   The entire system will be orchestrated using ROS 2 nodes, topics, and services. All modules will communicate via the ROS 2 graph.

2.  **Isaac Sim (The Digital Twin & Environment)**:
    -   We will use Isaac Sim to create our world: a room containing a robot arm, a red cube, and a blue platform.
    -   Isaac Sim will provide the simulated camera feed (`/rgb_image`) and publish the robot's joint states (`/joint_states`).
    -   It will subscribe to joint commands to move the robot arm.

3.  **The VLA Pipeline (The Brain)**:
    -   **Whisper Node (Language)**: A ROS 2 node will listen for audio, use the Whisper ASR model to transcribe it into text (e.g., "pick up the red cube..."), and publish this text to a `/user_command` topic.
    -   **LLM Planner Node (Language)**: This node subscribes to `/user_command`. It also maintains a list of the robot's primitive skills (e.g., `goTo()`, `grasp()`, `place()`). It sends the user command and its available skills to an LLM (like GPT-4), asking it to generate a JSON plan. It then publishes this plan.
    -   **Object Detection Node (Vision)**: This node subscribes to the `/rgb_image` topic from Isaac Sim. It runs a simple color-based object detector to find the pixel coordinates of the "red cube" and "blue platform". It publishes these coordinates.
    -   **Action Executor Node (Action)**: This is the central coordinator.
        -   It subscribes to the JSON plan from the LLM Planner.
        -   It processes the plan step-by-step.
        -   For a `grasp('red cube')` action, it gets the cube's coordinates from the Object Detection node.
        -   It computes the necessary robot arm trajectory (inverse kinematics) to move to the cube.
        -   It sends the joint commands to Isaac Sim to execute the movement.
        -   It repeats this process for the `place()` action.

## The Flow of Execution

1.  User speaks a command.
2.  Whisper transcribes it to text.
3.  The LLM receives the text and generates a logical plan (e.g., `[grasp(red_cube), place(blue_platform)]`).
4.  The Action Executor receives the plan.
5.  The Executor asks the vision system, "Where is the red cube?"
6.  The vision system processes the image from Isaac Sim and returns coordinates.
7.  The Executor calculates the arm movement and sends commands to Isaac Sim.
8.  The simulated arm moves and grasps the cube.
9.  The process repeats for the "place" action.

This capstone project demonstrates a complete, albeit simplified, VLA loop. It shows how modern AI tools like large language models and speech recognition can be combined with classic robotics techniques within a ROS 2 framework to create intelligent, flexible, and interactive robots.