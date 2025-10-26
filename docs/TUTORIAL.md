# Getting Started with the Semantic Substrate Engine

Welcome to the Semantic Substrate Engine! This tutorial will guide you through the foundational concepts of the engine and help you perform your first semantic analysis. By the end, you will understand how to analyze a concept and interpret its place in the 4D universe of meaning.

## 1. The Core Idea: A Universe of Meaning

At its heart, the Semantic Substrate Engine proposes that all concepts can be understood within a 4-dimensional space defined by four universal principles:

- **Love:** Compassion, connection, and benevolence.
- **Justice:** Fairness, truth, and righteousness.
- **Power:** Potency, strength, and the ability to act.
- **Wisdom:** Understanding, insight, and knowledge.

Every concept, idea, or piece of text can be mapped to a coordinate in this space. The "perfect" coordinate, representing complete harmony, is **(1, 1, 1, 1)**. This is called the **Universal Anchor Point** or, in a theological context, the **Jehovah Coordinate**.

## 2. Setting Up Your Environment

Before we begin, make sure you have the engine installed in an editable mode, which is the best way to work with the examples. From the root of the repository, run:

```bash
pip install -e .
```

This makes the `src` directory available to all your scripts, so you don't have to worry about `sys.path` modifications.

## 3. Your First Analysis: "Divine Wisdom"

Now that your environment is set up, let's analyze the concept of "divine wisdom." Create a Python file in the root of the project (e.g., `tutorial.py`) and add the following code:

```python
from src.baseline_biblical_substrate import BiblicalSemanticSubstrate

# 1. Initialize the engine
engine = BiblicalSemanticSubstrate()

# 2. Define the concept to analyze
concept_text = "divine wisdom"

# 3. Analyze the concept
coordinates = engine.analyze_concept(concept_text, context="theological")

# 4. Print the results
print(f"Analysis of: '{concept_text}'")
print(f"Coordinates (L, J, P, W): {coordinates}")
```

When you run this script, you'll see the 4D coordinates for "divine wisdom."

## 4. Understanding the Coordinates

You should see an output like this (the numbers may vary slightly):

```
Analysis of: 'divine wisdom'
Coordinates (L, J, P, W): BiblicalCoordinates(love=0.60, justice=0.70, power=0.50, wisdom=0.95)
```

So, what does this mean?

- **Interpreting the Axes:** The concept of "divine wisdom" has a very high score in **Wisdom (0.95)**, which makes sense. It also scores well in **Justice (0.70)** and **Love (0.60)**, reflecting that divine wisdom is often associated with fairness and benevolence. Its lowest score is in **Power (0.50)**, suggesting that "wisdom" on its own is more about understanding than action.

- **Dominant and Deficient Attributes:** We can programmatically identify the strongest and weakest aspects of a concept. Add this to your script:

```python
print(f"Dominant Attribute: {coordinates.get_dominant_attribute()}")
print(f"Deficient Attributes: {coordinates.get_deficient_attributes()}")
```

This will tell you that **Wisdom** is dominant, and it will likely list **Power** as a deficient attribute.

## 5. Measuring "Divine Alignment"

A key feature of the engine is its ability to measure how closely a concept aligns with the Universal Anchor Point (1, 1, 1, 1). Let's measure this for "divine wisdom."

Add the following to your script:

```python
# Calculate divine alignment metrics
divine_resonance = coordinates.divine_resonance()
distance_from_anchor = coordinates.distance_from_jehovah()

print(f"Divine Resonance: {divine_resonance:.2f}")
print(f"Distance from Universal Anchor: {distance_from_anchor:.2f}")
```

- **Divine Resonance:** This score (from 0 to 1) tells you how harmonious and balanced the concept's coordinates are. Higher is better. "Divine wisdom" should have a high resonance.
- **Distance from Universal Anchor:** This tells you how "far" the concept is from the perfect (1,1,1,1) coordinate. Lower is better.

A concept like "selfish greed" would have very low resonance and a large distance from the anchor, while "unconditional love" would have very high resonance and a small distance.

## 6. Next Steps

Congratulations! You've performed your first semantic analysis and learned how to interpret the results. This is the foundational skill for using the Semantic Substrate Engine.

From here, you can explore the more advanced features of the engine:

- **The ICE Framework:** For a deeper analysis of **I**ntent, **C**ontext, and **E**xecution, use the `ICESemanticSubstrateEngine`.
- **Phi-Enhancements:** The most advanced parts of the engine use the **Golden Ratio (Phi)** and **Fibonacci sequences** for an even deeper layer of analysis. Check out the `phi_enhanced_semantic_engine`.
- **Navigation:** The engine can calculate paths between concepts, allowing you to "navigate" the semantic universe.

We hope this tutorial has been helpful. You can find more technical examples in the `examples/` directory. Happy analyzing!
