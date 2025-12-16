---
title: Using Whisper for Voice Commands
sidebar_label: Whisper Voice Commands
---

# Lesson 4.1: Using Whisper for Voice Commands

Welcome to our final chapter, where we bridge the gap between human language and robot action. Vision-Language-Action (VLA) models are at the forefront of AI, and the first step in building such a system is enabling the robot to understand spoken commands.

This lesson will introduce **OpenAI's Whisper**, a state-of-the-art speech-to-text model, and discuss how it can be used as the "ears" for our robot.

## What is Whisper?

Whisper is an automatic speech recognition (ASR) system developed by OpenAI. It was trained on a massive and diverse dataset of audio from the internet, making it incredibly robust at transcribing spoken language, even in the presence of background noise, different accents, and technical jargon.

Unlike traditional ASR systems, Whisper is a single, large model that can be applied to a wide variety of audio without needing to be fine-tuned for a specific domain.

## Integrating Whisper into a ROS 2 System

To use Whisper for robot control, we can create a ROS 2 node that listens for audio, transcribes it, and publishes the resulting text to a topic.

The high-level architecture would look like this:

1.  **Audio Input Node**:
    -   A ROS 2 node subscribes to a microphone or another audio source.
    -   It captures chunks of audio (e.g., in 5-second intervals).

2.  **Whisper Transcription Service**:
    -   The audio node sends the captured audio data to a service that hosts the Whisper model.
    -   This service can be running on the same machine or on a separate, more powerful computer with a GPU to speed up transcription.
    -   The Whisper model processes the audio and returns the transcribed text.

3.  **Command Publisher Node**:
    -   The Whisper service returns the text to the audio node (or another dedicated node).
    -   This node then publishes the transcribed text to a ROS 2 topic, for example, `/transcribed_text` (as a `std_msgs/msg/String`).

## From Text to Action

Once the spoken command is available as text on a ROS 2 topic, other nodes in the system can subscribe to it and act accordingly.

For example, a **Command Interpreter** node could subscribe to `/transcribed_text` and listen for specific keywords.
-   If it receives the text "go to the kitchen," it could look up the coordinates for "kitchen" and send a goal to the Nav2 navigation stack.
-   If it receives "pick up the red block," it could trigger a perception pipeline to find the red block and an arm manipulation routine to grasp it.

Whisper provides a powerful and surprisingly simple way to add a natural language interface to any robotics project. Its accuracy and robustness remove a major barrier to entry, allowing developers to focus on the more complex challenge of turning the transcribed text into meaningful robot actions, which we will explore in the next lesson.