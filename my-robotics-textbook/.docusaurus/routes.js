import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/robotics-textbook/__docusaurus/debug',
    component: ComponentCreator('/robotics-textbook/__docusaurus/debug', '71b'),
    exact: true
  },
  {
    path: '/robotics-textbook/__docusaurus/debug/config',
    component: ComponentCreator('/robotics-textbook/__docusaurus/debug/config', 'a18'),
    exact: true
  },
  {
    path: '/robotics-textbook/__docusaurus/debug/content',
    component: ComponentCreator('/robotics-textbook/__docusaurus/debug/content', 'd5c'),
    exact: true
  },
  {
    path: '/robotics-textbook/__docusaurus/debug/globalData',
    component: ComponentCreator('/robotics-textbook/__docusaurus/debug/globalData', 'd1c'),
    exact: true
  },
  {
    path: '/robotics-textbook/__docusaurus/debug/metadata',
    component: ComponentCreator('/robotics-textbook/__docusaurus/debug/metadata', '125'),
    exact: true
  },
  {
    path: '/robotics-textbook/__docusaurus/debug/registry',
    component: ComponentCreator('/robotics-textbook/__docusaurus/debug/registry', '5d3'),
    exact: true
  },
  {
    path: '/robotics-textbook/__docusaurus/debug/routes',
    component: ComponentCreator('/robotics-textbook/__docusaurus/debug/routes', 'cca'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog',
    component: ComponentCreator('/robotics-textbook/blog', 'c7c'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/archive',
    component: ComponentCreator('/robotics-textbook/blog/archive', '73b'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/authors',
    component: ComponentCreator('/robotics-textbook/blog/authors', '8a9'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/authors/all-sebastien-lorber-articles',
    component: ComponentCreator('/robotics-textbook/blog/authors/all-sebastien-lorber-articles', '07c'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/authors/yangshun',
    component: ComponentCreator('/robotics-textbook/blog/authors/yangshun', 'd0b'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/first-blog-post',
    component: ComponentCreator('/robotics-textbook/blog/first-blog-post', 'd3c'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/long-blog-post',
    component: ComponentCreator('/robotics-textbook/blog/long-blog-post', 'b53'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/mdx-blog-post',
    component: ComponentCreator('/robotics-textbook/blog/mdx-blog-post', 'ba7'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/tags',
    component: ComponentCreator('/robotics-textbook/blog/tags', '0d9'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/tags/docusaurus',
    component: ComponentCreator('/robotics-textbook/blog/tags/docusaurus', '348'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/tags/facebook',
    component: ComponentCreator('/robotics-textbook/blog/tags/facebook', 'bfa'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/tags/hello',
    component: ComponentCreator('/robotics-textbook/blog/tags/hello', '370'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/tags/hola',
    component: ComponentCreator('/robotics-textbook/blog/tags/hola', 'a63'),
    exact: true
  },
  {
    path: '/robotics-textbook/blog/welcome',
    component: ComponentCreator('/robotics-textbook/blog/welcome', 'f9d'),
    exact: true
  },
  {
    path: '/robotics-textbook/markdown-page',
    component: ComponentCreator('/robotics-textbook/markdown-page', 'a62'),
    exact: true
  },
  {
    path: '/robotics-textbook/docs',
    component: ComponentCreator('/robotics-textbook/docs', '2de'),
    routes: [
      {
        path: '/robotics-textbook/docs',
        component: ComponentCreator('/robotics-textbook/docs', 'f8a'),
        routes: [
          {
            path: '/robotics-textbook/docs',
            component: ComponentCreator('/robotics-textbook/docs', 'e40'),
            routes: [
              {
                path: '/robotics-textbook/docs/digital-twin/physics-simulation',
                component: ComponentCreator('/robotics-textbook/docs/digital-twin/physics-simulation', '9dc'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/digital-twin/setup-environments',
                component: ComponentCreator('/robotics-textbook/docs/digital-twin/setup-environments', 'bca'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/digital-twin/simulating-sensors',
                component: ComponentCreator('/robotics-textbook/docs/digital-twin/simulating-sensors', '9b2'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/nvidia-isaac/intro-to-isaac-sim',
                component: ComponentCreator('/robotics-textbook/docs/nvidia-isaac/intro-to-isaac-sim', 'aca'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/nvidia-isaac/isaac-ros-vslam',
                component: ComponentCreator('/robotics-textbook/docs/nvidia-isaac/isaac-ros-vslam', '20b'),
                exact: true
              },
              {
                path: '/robotics-textbook/docs/nvidia-isaac/nav2-path-planning',
                component: ComponentCreator('/robotics-textbook/docs/nvidia-isaac/nav2-path-planning', 'ffd'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/nvidia-isaac/synthetic-data',
                component: ComponentCreator('/robotics-textbook/docs/nvidia-isaac/synthetic-data', 'a11'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/ros-2/python-rclpy',
                component: ComponentCreator('/robotics-textbook/docs/ros-2/python-rclpy', '7e9'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/ros-2/understanding-nodes-topics-services',
                component: ComponentCreator('/robotics-textbook/docs/ros-2/understanding-nodes-topics-services', '200'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/ros-2/urdf-for-humanoids',
                component: ComponentCreator('/robotics-textbook/docs/ros-2/urdf-for-humanoids', '617'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/vla/capstone-project',
                component: ComponentCreator('/robotics-textbook/docs/vla/capstone-project', '763'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/vla/llm-cognitive-planning',
                component: ComponentCreator('/robotics-textbook/docs/vla/llm-cognitive-planning', 'ce8'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/robotics-textbook/docs/vla/whisper-voice-commands',
                component: ComponentCreator('/robotics-textbook/docs/vla/whisper-voice-commands', '550'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/robotics-textbook/',
    component: ComponentCreator('/robotics-textbook/', '608'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
