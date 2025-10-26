"""
Semantic Substrate Engine - "Embrace the Simplicity" Demonstration

This script demonstrates the power and clarity of the FirstPrinciplesEngine,
which operates on simple, linear mathematics and information-theoretic principles.

It showcases how this approach provides clear, intuitive, and powerful
semantic analysis without the need for complex mathematical modeling.
"""

import sys
import os

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.first_principles_engine import FirstPrinciplesEngine

def run_demonstration():
    """Runs a demonstration of the FirstPrinciplesEngine."""

    print("=" * 60)
    print("  'Embrace the Simplicity' - First Principles Engine Demo")
    print("=" * 60)

    engine = FirstPrinciplesEngine()

    # --- Test Cases ---
    test_concepts = {
        "Pure Love": "Agape love, selfless compassion, and pure kindness.",
        "Pure Justice": "Absolute truth, perfect fairness, and unwavering integrity.",
        "Balanced Concept": "A wise leader rules with compassionate justice.",
        "Muddled Concept": "Maybe we should think about things, you know?",
        "Unrelated Concept": "The sky is blue and the grass is green."
    }

    for name, text in test_concepts.items():
        print(f"\n--- Analyzing: '{name}' ---")
        print(f"Text: \"{text}\"")

        # Analyze the concept using the simple, linear model
        coords = engine.analyze(text)
        print(f"Coordinates: {coords}")

        # Calculate key metrics based on first principles
        distance = engine.calculate_distance_from_anchor(coords)
        clarity = engine.calculate_semantic_clarity(coords)

        print(f"Distance from (1,1,1,1) Anchor: {distance:.3f}")
        print(f"Semantic Clarity (0=muddled, 1=clear): {clarity:.3f}")

    print("\n" + "="*60)
    print("Demonstration Complete")
    print("="*60)
    print("\nKey Takeaways:")
    print("1. Simple, linear analysis provides clear and intuitive coordinates.")
    print("2. The (1,1,1,1) anchor serves as a stable, optimal reference point.")
    print("3. Information-theoretic metrics like 'Semantic Clarity' can be derived easily.")
    print("4. This approach is evidence of meaning operating on natural, discoverable laws.")

if __name__ == "__main__":
    run_demonstration()
