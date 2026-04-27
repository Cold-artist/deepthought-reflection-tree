# 🌳 Daily Reflection Tree

A deterministic, psychological reflection system designed to track behavioral locus of control, contribution, and radius of impact. 

## 🧠 Project Overview
Unlike conversational AI bots that generate dynamic text, this project is built as a strictly **deterministic Directed Graph**. The system avoids hallucination and moralizing by forcing users through a mathematically rigid map of behavioral nodes. 

If a user supplies identical inputs, they will always receive the exact same outputs.

## 🧭 The Three Psychological Axes
The core of the graph evaluates users on three independent psychological frames:
- **Axis 1: Locus of Control:** Do you orient toward Agency vs. Victimhood?
- **Axis 2: Contribution vs Entitlement:** Do you lean towards creating momentum vs. waiting to receive it?
- **Axis 3: Radius of Impact:** Are you strictly self-focused vs. integrating others into your awareness?

## 📂 Project Structure
```text
DeepThought-Assignment/
├── tree/
│   └── reflection-tree.json  # Core state machine containing 27 mapping nodes
├── agent/
│   └── main.py               # Native execution engine
├── tree-diagram.png          # Visual flowchart representing the structural logic
└── write-up.md               # Extensive background on psychology and decision rules
```

## 🚀 How to Run the System
The project is equipped with a functional Python CLI that acts as the node-traversal engine. It dynamically evaluates JSON routing paths, string interpolations, and Boolean signal checks entirely offline.

1. Ensure Python 3.x is installed on your machine.
2. Open your terminal and navigate to this project folder.
3. Run the CLI engine using:
   ```bash
   python agent/main.py
   ```
   *(Note: Windows users may need to use `py agent/main.py` or `python3 agent/main.py`)*

Enjoy interacting with the structural flow!
