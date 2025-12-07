# Understanding ROS 2 Nodes, Topics, & Services

This lesson will cover the fundamental concepts of ROS 2 communication: Nodes, Topics, and Services.

## Objective
By the end of this lesson, you will be able to:
- Understand the role of Nodes in a ROS 2 system.
- Differentiate between Topics and Services as communication mechanisms.
- Explain how data flows through a ROS 2 network.

## Main Content
- Introduction to ROS 2 architecture.
- Detailed explanation of Nodes: purpose, lifecycle, and interaction.
- In-depth look at Topics: publisher-subscriber model, message types, quality of service (QoS) settings.
- Understanding Services: client-server model, request-response mechanism.

## Tutorial/Example
A hands-on example demonstrating how to create a simple ROS 2 publisher node that publishes a string message on a topic, and a subscriber node that receives and prints it.
Another example showing how to create a ROS 2 service that adds two numbers, and a client that calls it.

## Summary
- Nodes are executable processes that perform computation.
- Topics enable asynchronous, many-to-many communication using a publisher-subscriber pattern.
- Services enable synchronous, one-to-one communication using a client-server, request-response pattern.

## Further Reading
- [ROS 2 Documentation: Concepts](https://docs.ros.org/en/humble/Concepts.html)
- [ROS 2 Documentation: Writing a Simple Publisher and Subscriber (C++)](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Writing-A-Simple-Publisher-And-Subscriber--Cpp.html)
- [ROS 2 Documentation: Writing a Simple Publisher and Subscriber (Python)](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Writing-A-Simple-Publisher-And-Subscriber--Python.html)
