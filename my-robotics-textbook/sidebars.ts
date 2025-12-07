import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  roboticsTextbookSidebar: [
    {
      type: 'category',
      label: 'Chapter 1: The Robotic Nervous System (ROS 2)',
      link: {
        type: 'generated-index',
        title: 'ROS 2 Fundamentals',
        description: 'Learn the core concepts of ROS 2 for robotic communication.',
        slug: '/ros-2',
      },
      items: [
        'ros-2/understanding-nodes-topics-services',
        'ros-2/python-rclpy',
        'ros-2/urdf-for-humanoids',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 2: The Digital Twin (Gazebo & Unity)',
      link: {
        type: 'generated-index',
        title: 'Digital Twin Simulation',
        description: 'Explore creating and simulating a digital twin of a robot.',
        slug: '/digital-twin',
      },
      items: [
        'digital-twin/physics-simulation',
        'digital-twin/setup-environments',
        'digital-twin/simulating-sensors',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 3: The AI-Robot Brain (NVIDIA Isaac)',
      link: {
        type: 'generated-index',
        title: 'AI-Robot Brain with NVIDIA Isaac',
        description: 'Dive into advanced simulation and AI for robotics.',
        slug: '/nvidia-isaac',
      },
      items: [
        'nvidia-isaac/intro-to-isaac-sim',
        'nvidia-isaac/synthetic-data',
        'nvidia-isaac/isaac-ros-vslam',
        'nvidia-isaac/nav2-path-planning',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 4: Vision-Language-Action (VLA)',
      link: {
        type: 'generated-index',
        title: 'Vision-Language-Action Systems',
        description: 'Integrate voice commands and LLMs for cognitive planning.',
        slug: '/vla',
      },
      items: [
        'vla/whisper-voice-commands',
        'vla/llm-cognitive-planning',
        'vla/capstone-project',
      ],
    },
  ],
};

export default sidebars;
