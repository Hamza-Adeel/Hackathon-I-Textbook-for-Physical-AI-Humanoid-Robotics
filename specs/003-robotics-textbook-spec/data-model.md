# Data Model: Textbook Content

**Entity-Relationship Model**: This project is a static documentation site, so the "data model" refers to the file system structure used by Docusaurus to represent the content entities.

**Source of Truth**: The Markdown files within the `my-robotics-textbook/docs/` directory are the source of truth.

## Entity to Filesystem Mapping

### Textbook
- **Represents**: The entire "Physical AI & Humanoid Robotics" textbook.
- **Physical Representation**: The Docusaurus project located at the `my-robotics-textbook/` directory.

### Chapter
- **Represents**: A major learning module (e.g., "ROS 2", "Digital Twin").
- **Physical Representation**: A subdirectory within the `my-robotics-textbook/docs/` directory.
- **Example**: The "ROS 2" chapter is represented by the `my-robotics-textbook/docs/ros-2/` directory.
- **Hierarchy**: The order and nesting of chapters are defined in the `my-robotics-textbook/sidebars.ts` file.

### Lesson
- **Represents**: A specific instructional topic within a Chapter (e.g., "Understanding Nodes, Topics, and Services").
- **Physical Representation**: A Markdown file (`.md` or `.mdx`) within a chapter's subdirectory.
- **Example**: The "Understanding Nodes, Topics, and Services" lesson is represented by the file `my-robotics-textbook/docs/ros-2/understanding-nodes-topics-services.md`.
- **Attributes (Frontmatter)**: Each lesson file can contain metadata (frontmatter) at the top, such as `id`, `title`, and `sidebar_label`.
