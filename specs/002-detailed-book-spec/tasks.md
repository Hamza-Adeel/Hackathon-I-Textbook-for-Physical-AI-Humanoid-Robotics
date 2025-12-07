# Tasks: Detailed Robotics Textbook

**Input**: Design documents from `specs/002-detailed-book-spec/`
**Prerequisites**: plan.md, spec.md

## Format: `- [ ] [ID] [P?] [Story?] Description`

---

## Phase 1: Project Setup

**Purpose**: Initialize a clean Docusaurus project.

- [X] T001 Scaffold a new Docusaurus site named `my-robotics-textbook` using `npx create-docusaurus@latest my-robotics-textbook classic`.
- [X] T002 [P] Remove the default `./blog` directory created by the installer.
- [X] T003 [P] Remove the default tutorial content from the `./docs` directory.
- [X] T004 Initialize a new git repository in the `my-robotics-textbook` directory.

---

## Phase 2: Foundational (Structure & Configuration)

**Purpose**: Create the folder and navigation structure for the 4 main chapters.

- [X] T005 [P] Create chapter directory `./docs/ros-2`.
- [X] T006 [P] Create chapter directory `./docs/digital-twin`.
- [X] T007 [P] Create chapter directory `./docs/nvidia-isaac`.
- [X] T008 [P] Create chapter directory `./docs/vla`.
- [X] T009 Configure the `sidebars.js` file to create a nested navigation menu for the four chapters.

---

## Phase 3: User Story 1 - Chapter 1: The Robotic Nervous System (ROS 2)

**Goal**: Write all content for the ROS 2 module.
**Independent Test**: The ROS 2 chapter and its lessons render correctly on the local dev server.

- [X] T010 [P] [US1] Write content for "Understanding ROS 2 Nodes, Topics, & Services" in `./docs/ros-2/understanding-nodes-topics-services.md`.
- [X] T011 [P] [US1] Write content for "Building ROS 2 Systems with Python (rclpy)" in `./docs/ros-2/python-rclpy.md`.
- [X] T012 [P] [US1] Write content for "Describing Robots with URDF" in `./docs/ros-2/urdf-for-humanoids.md`.

---

## Phase 4: User Story 2 - Chapter 2: The Digital Twin (Gazebo & Unity)

**Goal**: Write all content for the Digital Twin module.
**Independent Test**: The Digital Twin chapter and its lessons render correctly on the local dev server.

- [X] T013 [P] [US2] Write content for "Fundamentals of Physics Simulation" in `./docs/digital-twin/physics-simulation.md`.
- [X] T014 [P] [US2] Write content for "Setting up Environments in Gazebo and Unity" in `./docs/digital-twin/setup-environments.md`.
- [X] T015 [P] [US2] Write content for "Simulating Sensors (LiDAR, Depth Cameras, IMUs)" in `./docs/digital-twin/simulating-sensors.md`.

---

## Phase 5: User Story 3 - Chapter 3: The AI-Robot Brain (NVIDIA Isaac)

**Goal**: Write all content for the NVIDIA Isaac module.
**Independent Test**: The NVIDIA Isaac chapter and its lessons render correctly on the local dev server.

- [X] T016 [P] [US3] Write content for "Introduction to Isaac Sim for Photorealistic Simulation" in `./docs/nvidia-isaac/intro-to-isaac-sim.md`.
- [X] T017 [P] [US3] Write content for "Generating Synthetic Datasets" in `./docs/nvidia-isaac/synthetic-data.md`.
- [X] T018 [P] [US3] Write content for "Implementing Isaac ROS VSLAM & Navigation" in `./docs/nvidia-isaac/isaac-ros-vslam.md`.
- [X] T019 [P] [US3] Write content for "Advanced Path Planning with Nav2 for Humanoids" in `./docs/nvidia-isaac/nav2-path-planning.md`.

---

## Phase 6: User Story 4 - Chapter 4: Vision-Language-Action (VLA)

**Goal**: Write all content for the VLA module.
**Independent Test**: The VLA chapter and its lessons, including the capstone project, render correctly.

- [X] T020 [P] [US4] Write content for "Converting Speech to Text with Whisper" in `./docs/vla/whisper-voice-commands.md`.
- [X] T021 [P] [US4] Write content for "LLM-Based Cognitive Planning" in `./docs/vla/llm-cognitive-planning.md`.
- [X] T022 [P] [US4] Write content for "Capstone Project: Building an Autonomous Humanoid Assistant" in `./docs/vla/capstone-project.md`.

---

## Phase 7: Polish & Deployment

**Purpose**: Review the complete textbook and deploy it to a public URL.

- [ ] T023 Run the local dev server with `npm run start` and review the entire site for formatting, broken links, and image issues.
- [ ] T024 [P] Proofread all content for grammatical errors and clarity.
- [ ] T025 Configure `docusaurus.config.js` for deployment to GitHub Pages (update `organizationName`, `projectName`, etc.).
- [ ] T026 Install the `gh-pages` deployment package using `npm install --save gh-pages`.
- [ ] T027 Run `npm run deploy` to build the site and deploy it to GitHub Pages.
- [ ] T028 Verify that the live site at its GitHub Pages URL is rendered correctly.

---
## Dependencies & Execution Order

- **Phase 1** must be completed first.
- **Phase 2** depends on Phase 1.
- **Phases 3, 4, 5, and 6 (Content Authoring)** can happen in parallel after Phase 2 is complete.
- **Phase 7** depends on the completion of all content authoring phases.
