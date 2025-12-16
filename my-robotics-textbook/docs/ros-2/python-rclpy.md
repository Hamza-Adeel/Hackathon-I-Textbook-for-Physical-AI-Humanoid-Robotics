---
title: Writing a Python ROS 2 Node (RCLPy)
sidebar_label: Python Node (RCLPy)
---

# Lesson 1.2: Writing a Python ROS 2 Node (RCLPy)

In our previous lesson, we learned about the theoretical concepts of nodes, topics, and services. Now, it's time to put that theory into practice by writing our first ROS 2 node using `rclpy`, the official Python client library for ROS 2.

## Setting Up Your Environment

Before we start, ensure you have a ROS 2 workspace sourced. If you've followed the standard ROS 2 installation, you can source it with the following command in your terminal:

```bash
source /opt/ros/humble/setup.bash
```

We will also create a simple Python package to house our node.

## The "Hello, World" of ROS 2: A Simple Publisher

The most common first step is to create a node that publishes a message to a topic. Let's create a publisher that sends a simple string message.

Here is the complete code for a minimal publisher node:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### Code Breakdown

1.  **`rclpy.init()`**: Initializes the ROS 2 client library.
2.  **`MinimalPublisher(Node)`**: We create a class that inherits from `rclpy.node.Node`.
3.  **`super().__init__('minimal_publisher')`**: The node is given a name, in this case, `minimal_publisher`.
4.  **`self.create_publisher(String, 'topic', 10)`**: We create a publisher. It will publish messages of type `std_msgs.msg.String` on a topic named `topic`. The `10` is the queue size.
5.  **`self.create_timer(...)`**: We create a timer that will call the `timer_callback` function every 0.5 seconds.
6.  **`timer_callback`**: This function creates a `String` message, populates it with data, publishes it, and logs it to the console.
7.  **`rclpy.spin()`**: This function keeps the node running so it can continue to publish messages.

This simple example demonstrates the core workflow of creating a ROS 2 node that communicates with the outside world.