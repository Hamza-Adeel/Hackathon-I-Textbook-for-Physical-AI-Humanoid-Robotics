import type { ReactNode } from "react";
import clsx from "clsx";
import Heading from "@theme/Heading";
import styles from "./styles.module.css";

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<"svg">>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: "Easy to Learn, Easy to Build",
    Svg: require("@site/static/img/undraw_docusaurus_mountain.svg").default,
    description: (
      <>
        Learn how robots think, move, and interact with the real world. This
        textbook introduces Physical AI and Humanoid Robotics in a simple,
        beginner-friendly way.{" "}
      </>
    ),
  },
  {
    title: "Focus on Real Robotics Skills",
    Svg: require("@site/static/img/undraw_docusaurus_tree.svg").default,
    description: (
      <>
        Each chapter focuses on essential robotics skills—from ROS 2 and
        simulation to perception, navigation, and Vision-Language-Action
        systems. You'll build real technical abilities step by step.{" "}
      </>
    ),
  },
  {
    title: "Powered by Modern AI and Robotics Technology",
    Svg: require("@site/static/img/undraw_docusaurus_react.svg").default,
    description: (
      <>
        Using modern tools like ROS 2, Gazebo, Unity, and NVIDIA Isaac, this
        book helps you turn AI concepts into real robotic motion and prepares
        you to build intelligent humanoid systems.{" "}
      </>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
