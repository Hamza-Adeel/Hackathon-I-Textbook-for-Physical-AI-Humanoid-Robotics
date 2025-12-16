# Quickstart: Local Development

This guide provides the steps to set up and run the Docusaurus textbook project locally for content development and preview.

## Prerequisites

- [Node.js](https://nodejs.org/) (version 18.x or higher)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

## 1. Install Dependencies

Navigate to the textbook's root directory and install the required npm packages.

```bash
cd my-robotics-textbook
npm install
```
*(Use `yarn install` if you prefer Yarn)*

## 2. Run the Development Server

Once the dependencies are installed, start the Docusaurus local development server.

```bash
npm run start
```
*(Use `yarn start` if you prefer Yarn)*

## 3. Preview the Textbook

The command will build the site and start a local server, typically on port 3000. Open your web browser and navigate to:

[http://localhost:3000](http://localhost:3000)

The website will automatically reload whenever you make changes to the Markdown files in the `/docs` directory or any other configuration/component file.
