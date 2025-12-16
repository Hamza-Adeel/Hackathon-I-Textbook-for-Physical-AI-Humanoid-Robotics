import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * This file defines the sidebar structure for the textbook.
 *
 * The sidebar is structured as a series of categories, where each category
 * represents a chapter, and the items within it are the lessons.
 * The paths directly correspond to the markdown files in the `docs` directory.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  // We can define our own sidebar structure here
  roboticsTextbookSidebar: [
    {
      type: 'category',
      label: 'Chapter 1: The Robotic Nervous System (ROS 2)',
      items: [
        'ros-2/understanding-nodes-topics-services',
        'ros-2/python-rclpy',
        'ros-2/urdf-for-humanoids',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 2: The Digital Twin (Gazebo & Unity)',
      items: [
        'digital-twin/setup-environments',
        'digital-twin/physics-simulation',
        'digital-twin/simulating-sensors',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 3: The AI-Robot Brain (NVIDIA Isaac)',
      items: [
        'nvidia-isaac/intro-to-isaac-sim',
        'nvidia-isaac/synthetic-data',
        'nvidia-isaac/nav2-path-planning',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 4: Vision-Language-Action (VLA)',
      items: [
        'vla/whisper-voice-commands',
        'vla/llm-cognitive-planning',
        'vla/capstone-project',
      ],
    },
  ],
};

export default sidebars;
