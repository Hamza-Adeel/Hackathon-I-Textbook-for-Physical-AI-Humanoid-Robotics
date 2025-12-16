---
title: The Physics of Simulation
sidebar_label: Physics Simulation
---

# Lesson 2.2: The Physics of Simulation

A digital twin is more than just a 3D model; it's a dynamic representation that behaves like its real-world counterpart. The magic behind this realism is the **physics engine**, a core component of any robotics simulator.

This lesson explores the fundamental concepts that a physics engine simulates to create a believable virtual world for our robots.

## 1. Collision Modeling

At its most basic, a simulator must prevent objects from passing through each other. This is handled through collision modeling. Each link of a robot (and every object in the world) has a `collision` geometry associated with it. This is often a simplified version of the `visual` geometry, using primitive shapes like spheres, boxes, and cylinders to make the math faster.

When the collision geometries of two objects overlap, the physics engine detects a **collision event**.

## 2. Dynamics and Forces

Once a collision is detected, the engine must calculate the result. This is where dynamics come in. Using the principles of classical mechanics, the engine simulates forces and their effects on the objects.

-   **Gravity**: A constant downward force is usually applied to all dynamic objects.
-   **Friction**: When objects are in contact, the engine calculates frictional forces that oppose motion. This includes both static friction (to keep objects from sliding) and kinetic friction (to slow them down once they are moving).
-   **Contact Forces**: When objects collide, the engine calculates the impulse or force that should be applied to them to prevent penetration and cause them to bounce or react realistically.

These calculations rely on the **inertial properties** defined in the URDF for each link, specifically its `mass` and `inertia tensor` (which describes how the mass is distributed).

## 3. Joint Dynamics

Joints are the constraints that define how a robot's links can move. The physics engine is responsible for enforcing these constraints.

-   **Joint Limits**: The engine ensures that a joint does not move beyond its specified upper and lower limits. For a `revolute` joint, this is an angle; for a `prismatic` joint, this is a distance.
-   **Actuation**: To make a robot move, we apply a force or torque to its joints. A controller in ROS 2 might send a command to apply a certain torque to a wheel joint. The physics engine takes this input and calculates the resulting acceleration and movement of the link, taking into account all other forces like friction and gravity.

Understanding these physical principles is key to creating realistic simulations. When a simulated robot behaves unexpectedly, it is often due to incorrect mass or inertia values, misconfigured collision models, or unrealistic friction coefficients. Debugging a simulation often feels a lot like being a physicist.