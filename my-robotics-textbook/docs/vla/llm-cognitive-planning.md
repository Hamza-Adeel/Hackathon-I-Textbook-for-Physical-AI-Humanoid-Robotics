---
title: Cognitive Planning with LLMs
sidebar_label: Cognitive Planning with LLMs
---

# Lesson 4.2: Cognitive Planning with LLMs

Once a robot can understand spoken commands via a speech-to-text model like Whisper, the next challenge is to turn a high-level command like "clean up the table" into a concrete sequence of actions. This is the domain of **task planning**.

Traditionally, task planning has relied on complex symbolic logic systems (like PDDL - Planning Domain Definition Language). However, a revolutionary new approach is to use a **Large Language Model (LLM)** as the robot's cognitive planning brain.

## LLMs as Planners

An LLM, such as GPT-4 or Gemini, excels at reasoning and breaking down complex problems. We can leverage this capability for robotics. Instead of just "chatting" with the LLM, we present it with a structured prompt that gives it the context it needs to act as a planner.

The workflow looks like this:

1.  **System Prompt**: We give the LLM a detailed "system prompt" that defines its role. This prompt tells the LLM:
    -   "You are a robot's planning module."
    -   "Here is a list of all the actions you are capable of performing," e.g., `goTo(location)`, `pickUp(object)`, `putDown(object, location)`.
    -   "Here are the objects you currently see in your environment," which can be provided by a perception system.
    -   "Your task is to take a user's command and break it down into a sequence of these available actions."
    -   "You must only output the sequence of actions in a specific format, like JSON."

2.  **User Command**: We take the user's transcribed command (e.g., "please pick up the apple and put it in the bowl") and insert it into the prompt.

3.  **LLM Inference**: We send the complete prompt to the LLM API.

4.  **Action Plan**: The LLM processes the prompt and, instead of a conversational reply, it returns a structured plan. For the command above, the LLM might return the following JSON:
    ```json
    [
      { "action": "goTo", "parameters": ["table"] },
      { "action": "pickUp", "parameters": ["apple"] },
      { "action": "goTo", "parameters": ["counter"] },
      { "action": "putDown", "parameters": ["apple", "bowl"] }
    ]
    ```

## From Plan to Execution

This JSON plan is now a simple, machine-readable list of steps that the robot's **Action Executor** can process. The executor would:
1.  Read the first action: `goTo('table')`.
2.  Call the Nav2 stack to navigate to the table.
3.  Once successful, read the second action: `pickUp('apple')`.
4.  Invoke the perception and manipulation stacks to find and grasp the apple.
5.  ... and so on, until the plan is complete.

This approach is incredibly powerful because it allows the robot to handle a near-infinite variety of high-level commands without requiring a programmer to manually write logic for every possible scenario. The LLM's general-world knowledge and reasoning capabilities serve as a flexible and powerful planning engine. The primary engineering challenge shifts from writing complex planning logic to designing a robust system for prompting the LLM and reliably executing the actions it outputs.