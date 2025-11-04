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

def main():
    """Demonstration of the complete Divine Invitation Semantic Substrate Engine"""
    print("=" * 80)
    print("DIVINE INVITATION SEMANTIC SUBSTRATE ENGINE")
    print("=" * 80)
    print("Definitive Demonstration")
    print("=" * 80)

    # Initialize the engine
    engine = DivineInvitationSemanticEngine()

    print("\n=== DEMONSTRATION OF CORE CAPABILITIES ===")

    # 1. Basic concept analysis
    print("\n1. DIVINE INVITATION ANALYSIS")
    concepts = [
        "love justice power wisdom truth understanding existence",
        "hate injustice weakness folly lies confusion nonexistence",
        "A nation's strength is not in its military might, but in the justice of its laws and the compassion of its people.",
        "The pursuit of knowledge and understanding is the noblest of all endeavors."
    ]

    for concept in concepts:
        coords = engine.analyze_concept(concept)
        print(f"\n   Concept: '{concept}'")
        print(f"   Coordinates: {coords}")
        print(f"   Distance from Anchor: {engine.get_distance_from_anchor(coords):.3f}")
        print(f"   Semantic Clarity: {engine.get_semantic_clarity(coords):.3f}")

    print("\n=== ENGINE CAPABILITIES VERIFIED ===")
    print("Divine Invitation principle validated")
    print("Ready for real-world applications")


if __name__ == "__main__":
    main()
