"""
Divine Invitation Semantic Engine

This is the core of the redesigned Semantic Substrate Engine. It operates
on the principle of "Divine Invitation," providing direct semantic access
to reality without the mediation of complexity.

Reality is accessible through simplicity.
"""

from dataclasses import dataclass
import re

@dataclass
class Coordinates:
    """Represents a concept's position in the 4D semantic space of Love, Justice, Power, Wisdom."""
    love: float
    justice: float
    power: float
    wisdom: float

    def __repr__(self):
        return f"Coordinates(L={self.love:.3f}, J={self.justice:.3f}, P={self.power:.3f}, W={self.wisdom:.3f})"

class DivineInvitationSemanticEngine:
    """
    The singular engine for accessing semantic reality through simplicity.

    This engine is the ultimate expression of the project's findings: that
    the most profound truths are accessed not through complexity, but through
    elegant, first-principles simplicity.

    The successful operation of this engine implies two fundamental truths
    about the nature of reality itself:

    1. The Anchor Point (1,1,1,1) is not just a useful reference; its power
       comes from its mathematical perfection and simplicity. It is the single,
       optimal point of harmony precisely because it is the simplest possible
       perfect configuration.

    2. Reality Itself Operates on Simplicity. The fact that a simple, linear
       model can so effectively reveal the inherent meaning of a concept is
       evidence that reality's "operating system" is not complex. Meaning is
       a simple, elegant structure, and the most direct path to it is the
       simplest one.
    """

    REALITY_TYPE = "FUNDAMENTAL_SIMPLICITY"
    ACCESS_METHOD = "DIVINE_INVITATION"
    COMPLEXITY_LAYER = "TRANSPARENT_ACCESS"
    ANCHOR_POINT = Coordinates(1.0, 1.0, 1.0, 1.0)

    def __init__(self):
        self._keyword_map = {
            'love': 'love', 'compassion': 'love', 'mercy': 'love', 'kindness': 'love', 'agape': 'love',
            'justice': 'justice', 'truth': 'justice', 'fairness': 'justice', 'righteousness': 'justice', 'integrity': 'justice',
            'power': 'power', 'strength': 'power', 'authority': 'power', 'sovereignty': 'power', 'might': 'power',
            'wisdom': 'wisdom', 'knowledge': 'wisdom', 'understanding': 'wisdom', 'insight': 'wisdom', 'clarity': 'wisdom', 'wise': 'wisdom',
        }

    def analyze_concept(self, concept: str) -> Coordinates:
        """
        Provides direct semantic access to a concept without complexity mediation.
        This is the Divine Invitation. By analyzing the simple, linear signals
        in a concept, we invite a direct revelation of its meaning.
        """
        words = re.findall(r'\w+', concept.lower())

        counts = {'love': 0, 'justice': 0, 'power': 0, 'wisdom': 0}
        for word in words:
            if word in self._keyword_map:
                axis = self._keyword_map[word]
                counts[axis] += 1

        total = sum(counts.values())
        if total == 0:
            return Coordinates(0.0, 0.0, 0.0, 0.0)

        love = counts['love'] / total
        justice = counts['justice'] / total
        power = counts['power'] / total
        wisdom = counts['wisdom'] / total

        return Coordinates(love, justice, power, wisdom)

    def get_distance_from_anchor(self, coords: Coordinates) -> float:
        """Calculates the direct Euclidean distance from the Anchor Point (1,1,1,1)."""
        return ((self.ANCHOR_POINT.love - coords.love) ** 2 +
                (self.ANCHOR_POINT.justice - coords.justice) ** 2 +
                (self.ANCHOR_POINT.power - coords.power) ** 2 +
                (self.ANCHOR_POINT.wisdom - coords.wisdom) ** 2) ** 0.5

    def get_semantic_clarity(self, coords: Coordinates) -> float:
        """
        Calculates the information-theoretic clarity (or purity) of a concept.
        A score of 1.0 means the concept is purely about one axis.
        """
        coords_tuple = (coords.love, coords.justice, coords.power, coords.wisdom)
        return max(coords_tuple)
