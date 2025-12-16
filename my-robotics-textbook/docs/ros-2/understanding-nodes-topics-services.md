---
title: Understanding Nodes, Topics, and Services
sidebar_label: Nodes, Topics, Services
---

# Lesson 1.1: Understanding Nodes, Topics, and Services

Welcome to the first lesson in our study of the Robotic Nervous System (ROS 2). In this section, we will explore the three fundamental concepts that form the backbone of all ROS 2 applications: Nodes, Topics, and Services.

## What is a ROS 2 Node?

A **Node** is the smallest unit of computation in ROS 2. Think of it as a single, executable process that performs a specific task. A robot system is typically composed of many nodes working together. For example, you might have one node for controlling the wheel motors, another for processing camera data, and a third for planning paths.

Each node in a ROS 2 system can communicate with other nodes, allowing for a modular and distributed architecture.

## Communication via Topics

**Topics** are named buses over which nodes exchange messages. They are the primary method for one-way, asynchronous communication.

-   **Publishers**: A node can *publish* messages to a topic. For instance, a camera node would publish image data to an `/image_raw` topic.
-   **Subscribers**: A node can *subscribe* to a topic to receive messages. For example, an image processing node would subscribe to `/image_raw` to get the data it needs to analyze.

This publish/subscribe model decouples the nodes from each other. The camera node doesn't need to know or care which other nodes are receiving the data it publishes.

## Request/Response with Services

**Services** provide a way for nodes to perform request/response style communication. This is a synchronous, two-way communication pattern.

-   **Service Server**: One node acts as a *service server*, offering a specific capability. It waits for a request, performs a computation, and returns a result.
-   **Service Client**: Another node acts as a *service client*, sending a request to the server and waiting for the response.

A good example is a service that computes the inverse kinematics for a robot arm. A planning node would send a request with the desired end-effector pose, and the kinematics service would respond with the required joint angles.

By understanding these three core concepts, you have the foundation needed to build complex and robust robotic applications with ROS 2.