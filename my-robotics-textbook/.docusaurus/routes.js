import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/blog',
    component: ComponentCreator('/blog', 'b2f'),
    exact: true
  },
  {
    path: '/blog/archive',
    component: ComponentCreator('/blog/archive', '182'),
    exact: true
  },
  {
    path: '/blog/authors',
    component: ComponentCreator('/blog/authors', '0b7'),
    exact: true
  },
  {
    path: '/blog/authors/all-sebastien-lorber-articles',
    component: ComponentCreator('/blog/authors/all-sebastien-lorber-articles', '4a1'),
    exact: true
  },
  {
    path: '/blog/authors/yangshun',
    component: ComponentCreator('/blog/authors/yangshun', 'a68'),
    exact: true
  },
  {
    path: '/blog/first-blog-post',
    component: ComponentCreator('/blog/first-blog-post', '89a'),
    exact: true
  },
  {
    path: '/blog/long-blog-post',
    component: ComponentCreator('/blog/long-blog-post', '9ad'),
    exact: true
  },
  {
    path: '/blog/mdx-blog-post',
    component: ComponentCreator('/blog/mdx-blog-post', 'e9f'),
    exact: true
  },
  {
    path: '/blog/tags',
    component: ComponentCreator('/blog/tags', '287'),
    exact: true
  },
  {
    path: '/blog/tags/docusaurus',
    component: ComponentCreator('/blog/tags/docusaurus', '704'),
    exact: true
  },
  {
    path: '/blog/tags/facebook',
    component: ComponentCreator('/blog/tags/facebook', '858'),
    exact: true
  },
  {
    path: '/blog/tags/hello',
    component: ComponentCreator('/blog/tags/hello', '299'),
    exact: true
  },
  {
    path: '/blog/tags/hola',
    component: ComponentCreator('/blog/tags/hola', '00d'),
    exact: true
  },
  {
    path: '/blog/welcome',
    component: ComponentCreator('/blog/welcome', 'd2b'),
    exact: true
  },
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '3d7'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '4cb'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '291'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', 'de8'),
            routes: [
              {
                path: '/docs/digital-twin/physics-simulation',
                component: ComponentCreator('/docs/digital-twin/physics-simulation', '87c'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/digital-twin/setup-environments',
                component: ComponentCreator('/docs/digital-twin/setup-environments', '7c9'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/digital-twin/simulating-sensors',
                component: ComponentCreator('/docs/digital-twin/simulating-sensors', '8d6'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/nvidia-isaac/intro-to-isaac-sim',
                component: ComponentCreator('/docs/nvidia-isaac/intro-to-isaac-sim', '8e8'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/nvidia-isaac/isaac-ros-vslam',
                component: ComponentCreator('/docs/nvidia-isaac/isaac-ros-vslam', '98c'),
                exact: true
              },
              {
                path: '/docs/nvidia-isaac/nav2-path-planning',
                component: ComponentCreator('/docs/nvidia-isaac/nav2-path-planning', '668'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/nvidia-isaac/synthetic-data',
                component: ComponentCreator('/docs/nvidia-isaac/synthetic-data', '530'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/ros-2/python-rclpy',
                component: ComponentCreator('/docs/ros-2/python-rclpy', '676'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/ros-2/understanding-nodes-topics-services',
                component: ComponentCreator('/docs/ros-2/understanding-nodes-topics-services', '63d'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/ros-2/urdf-for-humanoids',
                component: ComponentCreator('/docs/ros-2/urdf-for-humanoids', '2e3'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/vla/capstone-project',
                component: ComponentCreator('/docs/vla/capstone-project', '4a9'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/vla/llm-cognitive-planning',
                component: ComponentCreator('/docs/vla/llm-cognitive-planning', '574'),
                exact: true,
                sidebar: "roboticsTextbookSidebar"
              },
              {
                path: '/docs/vla/whisper-voice-commands',
                component: ComponentCreator('/docs/vla/whisper-voice-commands', '1e6'),
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
    path: '/',
    component: ComponentCreator('/', 'e5f'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
