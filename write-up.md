# Problem Understanding

The objective of this assignment is to design a deterministic reflection system that guides users through structured self-reflection.

Unlike traditional conversational AI-based systems, this system avoids dynamic runtime generation and instead relies exclusively on a predefined decision tree architecture. The goal is to make reflection predictable, consistent, psychologically safe, and fundamentally free from hallucination.

The system helps users rigorously analyze their day across three core psychological axes:
- **Locus of Control:** Determining agency and tracking victim vs. victor mentalities.
- **Contribution vs. Entitlement:** Shifting the lens from mere external expectations to proactive value creation.
- **Radius of Concern:** Measuring systems-level awareness by moving from self-centric to other-centric impact.

# Approach

I approached this problem by first deconstructing the psychological intent behind the three axes. Instead of designing a flat, linear questionnaire, I focused on mapping a progressively guided conversational graph.

Each axis was intentionally designed to:
1. Capture the user’s current emotional or situational state through targeted questions.
2. Interpret behavior objectively using fixed options that act as behavioral markers.
3. Provide a reflection that reframes their perspective contextually—without preaching or judgment.

The system scales progressively from:
- Grounding the user in evaluating their direct control (Axis 1).
- Shifting to evaluate their outward contribution (Axis 2).
- Expanding their awareness to see the relational impact of their behavior (Axis 3).

This ensures a cognitive momentum that feels like a natural journey of realization rather than an isolated survey.

# Design Decisions

- **Fixed Options Only:** All questions utilize predefined, constrained choices. This ensures that the system logic remains fully deterministic and eliminates the messy ambiguity of parsing free text.
- **Signal-Based Tracking:** The architecture relies on telemetry rather than just sequential routing. Each option strictly maps to a behavioral signal (e.g., `axis1.internal` or `axis2.entitlement`), allowing the central engine to mathematically tally tendencies across the session.
- **Mathematical Decision Nodes:** Branching routes and reflections are triggered by deterministic conditions (e.g., `axis3.others > axis3.self`) evaluated at explicitly programmed decision forks, securely avoiding opaque AI interpretation logic.
- **Neutral, Observational Tone:** The reflection nodes were vigorously tested to remain non-judgmental. Reframing friction naturally encourages deeper awareness rather than sparking defensiveness or imposing moralized conclusions.
- **Rigid Topological Flow:** The bridging structure ensures a cohesive narrative thread from entry (`START`) to exit (`END`), maintaining structural integrity.

# AI Usage & Hallucination Control

To strictly prevent hallucination in production, **no AI is used at runtime.** All nodes, reflections, and variables are predefined and statically stored locally within `reflection-tree.json`.

AI was exclusively used as a development and sparring tool during the initial build phase to:
- Quickly iterate on the JSON structural schemas.
- Brainstorm subtle behavioral variations for the fixed options to ensure neutral tone alignment.
- Stress-test the branching logic and validate signal mappings.

However, all outputs from the AI were critically reviewed, manually overwritten where necessary, and heavily pruned to adhere to psychological rigor. Negative constraints were utilized during development (e.g., *"Do not generate vague or interpretive responses. Keep outputs deterministic and structured"*) to keep the AI functioning strictly as an engineering assistant rather than a product copywriter. 

# Challenges

One of the more profound challenges was constructing fixed options that are both highly realistic and mutually distinct. Users needed to identify deeply with an option without finding the alternatives indistinguishable or artificially forced.

Maintaining a supportive, neutral tone while still confronting behavioral deficits (like entitlement or victim mentalities) was another hurdle. Avoiding guilt-tripping while still providing sharp behavioral insight required immense focus on word choice and empathy during the writing of the reflection nodes.

Finally, securely mapping logic thresholds natively through a static JSON schema without relying on overly complex nested scripting required several iterative structural refinements to the decision engine.

# Future Improvements

- **Longitudinal Analytics:** Add a database layer capturing historical signal tallies to present users with weekly data tracking (like a radar chart mapping Contribution vs. Entitlement ratios over the month).
- **Adaptive Scenario Depth:** Expand the graph to dynamically adjust resolution based on user time-box constraints (e.g., a streamlined 5-minute path vs. an extensive 15-minute path).
- **Dynamic Context Injection:** Safely introduce basic string tracking (like maintaining the user's specific role or department context set at `START`) to subtly personalize the phrasing of later options without breaking the deterministic bounds.
