# Quickstart: Detailed Robotics Textbook Project

This guide provides the essential steps to set up the development environment for the detailed robotics textbook.

## Prerequisites

- **Node.js**: Required for Docusaurus. Install the latest LTS version.
- **Git**: Required for version control and deployment to GitHub Pages.
- **ROS 2, Gazebo, NVIDIA Isaac Sim**: These are the core technologies the textbook covers. While not needed to *write* the content, they are required to *validate* the tutorials and code samples. Installation guides for these should be referenced from their official documentation.

## 1. Initialize the Docusaurus Site

This command scaffolds a new Docusaurus project.

```bash
npx create-docusaurus@latest my-robotics-textbook classic
```

## 2. Start the Development Server

Navigate into the project directory and start the local server to preview the site as you build it.

```bash
cd my-robotics-textbook
npm run start
```

The site will be available at `http://localhost:3000`.

## 3. Project Structure

The textbook content is organized into four main directories under `docs/`:

- `docs/ros-2/`
- `docs/digital-twin/`
- `docs/nvidia-isaac/`
- `docs/vla/`

The navigation for these chapters and their lessons is configured in `sidebars.js`. Refer to the `plan.md` for the full implementation details.
