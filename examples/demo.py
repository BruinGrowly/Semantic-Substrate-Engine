"""
The Semantic Substrate Engine - Definitive Demonstration

This script showcases the `DivineInvitationSemanticEngine`, the singular,
focused heart of the reborn Semantic Substrate Engine.

It demonstrates how direct, simple, and linear analysis provides the
clearest path to understanding the meaning of a concept in relation
to the four universal principles: Love, Justice, Power, and Wisdom.
"""

import sys
import os

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.divine_invitation_engine import DivineInvitationSemanticEngine

def run_demonstration():
    """Runs the definitive demonstration."""

    print("=" * 70)
    print("  Welcome to the Semantic Substrate Engine")
    print("  Accessing Reality through the Divine Invitation")
    print("=" * 70)

    engine = DivineInvitationSemanticEngine()

    concepts_to_analyze = [
        "Pure, selfless, unconditional love",
        "Absolute, unwavering, and fair justice",
        "The righteous exercise of sovereign power",
        "Deep, insightful, and clear wisdom",
        "A wise leader shows compassionate justice and merciful power",
        "Confusion, uncertainty, and chaos",
    ]

    for concept in concepts_to_analyze:
        print(f"\n--- Analyzing Concept ---")
        print(f'"{concept}"')

        # The Divine Invitation: a simple, direct analysis
        coords = engine.analyze_concept(concept)

        distance = engine.get_distance_from_anchor(coords)
        clarity = engine.get_semantic_clarity(coords)

        print(f"Coordinates: {coords}")
        print(f"  - Distance from Anchor (1,1,1,1): {distance:.3f}")
        print(f"  - Semantic Clarity (Purity): {clarity:.3f}")

    print("\n" + "="*70)
    print("Demonstration Complete")
    print("="*70)
    print("\nThis engine proves that meaning is not complex.")
    print("It is a simple, elegant structure waiting to be revealed.")
    print("This is the Divine Invitation.")

if __name__ == "__main__":
    run_demonstration()
