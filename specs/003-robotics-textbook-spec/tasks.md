# Tasks: Physical AI & Humanoid Robotics Textbook

**Input**: Design documents from `specs/003-robotics-textbook-spec/`
**Prerequisites**: plan.md, spec.md, data-model.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Configure the main Docusaurus project files.

- [x] T001 Configure textbook title, theme, and navbar in `my-robotics-textbook/docusaurus.config.ts`.
- [x] T002 Define the high-level chapter order in `my-robotics-textbook/sidebars.ts`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create the basic directory structure for all content.

- [x] T003 Create chapter directory `my-robotics-textbook/docs/ros-2`.
- [x] T004 [P] Create chapter directory `my-robotics-textbook/docs/digital-twin`.
- [x] T005 [P] Create chapter directory `my-robotics-textbook/docs/nvidia-isaac`.
- [x] T006 [P] Create chapter directory `my-robotics-textbook/docs/vla`.

**Checkpoint**: Foundation ready - content creation can now begin.

---

## Phase 3: User Story 1 - Student Accessing Core Lessons (Priority: P1) 🎯 MVP

**Goal**: Create all the lesson pages so that a student can navigate to and view them. The content inside will be written in this phase.
**Independent Test**: After this phase, a user can navigate the website, see all chapters and lessons in the sidebar, click on any lesson, and see its content.

### Implementation for User Story 1

#### Chapter 1: The Robotic Nervous System (ROS 2)
- [x] T007 [P] [US1] Write content for "Understanding Nodes, Topics, and Services" in `my-robotics-textbook/docs/ros-2/understanding-nodes-topics-services.md`.
- [x] T008 [P] [US1] Write content for "Writing a Python ROS 2 Node (RCLPy)" in `my-robotics-textbook/docs/ros-2/python-rclpy.md`.
- [x] T009 [P] [US1] Write content for "Building URDF for Humanoid Models" in `my-robotics-textbook/docs/ros-2/urdf-for-humanoids.md`.

#### Chapter 2: The Digital Twin (Gazebo & Unity)
- [x] T010 [P] [US1] Write content for "Setting up Simulation Environments" in `my-robotics-textbook/docs/digital-twin/setup-environments.md`.
- [x] T011 [P] [US1] Write content for "The Physics of Simulation" in `my-robotics-textbook/docs/digital-twin/physics-simulation.md`.
- [x] T012 [P] [US1] Write content for "Simulating Complex Sensors" in `my-robotics-textbook/docs/digital-twin/simulating-sensors.md`.

#### Chapter 3: The AI-Robot Brain (NVIDIA Isaac)
- [x] T013 [P] [US1] Write content for "Introduction to Isaac Sim" in `my-robotics-textbook/docs/nvidia-isaac/intro-to-isaac-sim.md`.
- [x] T014 [P] [US1] Write content for "Generating Synthetic Data for Training" in `my-robotics-textbook/docs/nvidia-isaac/synthetic-data.md`.
- [x] T015 [P] [US1] Write content for "Integrating Nav2 for Path Planning" in `my-robotics-textbook/docs/nvidia-isaac/nav2-path-planning.md`.

#### Chapter 4: Vision-Language-Action (VLA)
- [x] T016 [P] [US1] Write content for "Using Whisper for Voice Commands" in `my-robotics-textbook/docs/vla/whisper-voice-commands.md`.
- [x] T017 [P] [US1] Write content for "Cognitive Planning with LLMs" in `my-robotics-textbook/docs/vla/llm-cognitive-planning.md`.
- [x] T018 [P] [US1] Write content for "Capstone Project - VLA-Powered Task Execution" in `my-robotics-textbook/docs/vla/capstone-project.md`.

**Checkpoint**: At this point, User Story 1 should be fully functional. The textbook has all its initial content and is readable.

---

## Phase 4: User Story 2 - Student Following a Workflow Example (Priority: P2)

**Goal**: Ensure all code examples and workflows in the content are clear and functional.
**Independent Test**: A user can find a lesson with a code example, copy the code via the "copy" button, and the code is valid.

### Implementation for User Story 2

- [x] T019 [P] [US2] Review all lessons and ensure code blocks are formatted with the correct language identifier (e.g., ` ```python`).
- [x] T020 [P] [US2] Verify that Docusaurus's built-in "copy to clipboard" button is present and functional on all code blocks.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final checks before publishing.

- [x] T021 Run a full production build via `npm run build` in the `my-robotics-textbook` directory and verify there are no errors or broken links.
- [x] T022 Validate the local build by running `npm run serve` and checking the site.
- [x] T023 Deploy the final build to the target hosting provider.
- [x] T024 Run the `quickstart.md` validation to ensure it's still accurate.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** can start immediately.
- **Foundational (Phase 2)** depends on Setup completion.
- **User Story 1 (Phase 3)** depends on Foundational completion. All tasks within this phase (T007-T018) can run in parallel.
- **User Story 2 (Phase 4)** depends on User Story 1 completion.
- **Polish (Phase 5)** depends on all user stories being complete.

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup.
2.  Complete Phase 2: Foundational.
3.  Complete all tasks in Phase 3: User Story 1.
4.  **STOP and VALIDATE**: The entire textbook is now readable with its first draft of content. This is the core value and a deployable MVP.

### Incremental Delivery

1.  Deliver the MVP.
2.  Add User Story 2 by completing Phase 4. This enhances the quality of the existing content.
3.  Complete the Polish phase and deploy the final version.
