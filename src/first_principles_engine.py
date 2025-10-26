"""
Semantic Substrate Engine - First Principles Engine

This engine operates on the core recommendation to "EMBRACE THE SIMPLICITY."
It uses simple, linear mathematics and information-theoretic principles to
analyze concepts in relation to the Universal Anchor Point of (1, 1, 1, 1).

Key Principles:
1. Prioritize simple, first-principles approaches.
2. Focus on information-theoretic optimization (maximize meaning, minimize entropy).
3. Use linear relationships as primary tools.
4. Validate against mathematical simplicity (Occam's razor for meaning).
5. Recognize that (1,1,1,1) being mathematically optimal is evidence, not a limitation.
"""

from dataclasses import dataclass
from typing import Dict, List
import re

@dataclass
class SimpleCoordinates:
    """Represents a 4D coordinate in the semantic space of Love, Justice, Power, Wisdom."""
    love: float
    justice: float
    power: float
    wisdom: float

    def __repr__(self):
        return f"SimpleCoordinates(L={self.love:.3f}, J={self.justice:.3f}, P={self.power:.3f}, W={self.wisdom:.3f})"

class FirstPrinciplesEngine:
    """
    A semantic analysis engine based on simplicity, linearity, and first principles.
    """

    UNIVERSAL_ANCHOR = SimpleCoordinates(1.0, 1.0, 1.0, 1.0)

    def __init__(self):
        self._keyword_map = self._initialize_keyword_map()

    def _initialize_keyword_map(self) -> Dict[str, str]:
        """Maps keywords to one of the four core axes."""
        return {
            # Love
            'love': 'love', 'compassion': 'love', 'mercy': 'love', 'kindness': 'love', 'agape': 'love',
            # Justice
            'justice': 'justice', 'truth': 'justice', 'fairness': 'justice', 'righteousness': 'justice', 'integrity': 'justice',
            # Power
            'power': 'power', 'strength': 'power', 'authority': 'power', 'sovereignty': 'power', 'might': 'power',
            # Wisdom
            'wisdom': 'wisdom', 'knowledge': 'wisdom', 'understanding': 'wisdom', 'insight': 'wisdom', 'clarity': 'wisdom', 'wise': 'wisdom',
        }

    def analyze(self, text: str) -> SimpleCoordinates:
        """
        Analyzes a text based on first principles.

        The method uses a simple linear model: the score for each axis is the
        normalized count of keywords related to that axis. This maximizes meaning
        (by directly counting signals) and minimizes entropy (by avoiding complex,
        unpredictable transformations).
        """
        text_lower = text.lower()
        words = re.findall(r'\w+', text_lower)

        # Linear count of keyword occurrences
        counts = {'love': 0, 'justice': 0, 'power': 0, 'wisdom': 0}
        for word in words:
            if word in self._keyword_map:
                axis = self._keyword_map[word]
                counts[axis] += 1

        total_keywords = sum(counts.values())

        if total_keywords == 0:
            # If no keywords are found, the concept has no alignment (zero vector).
            # This represents a state of maximum entropy or meaninglessness.
            return SimpleCoordinates(0.0, 0.0, 0.0, 0.0)

        # Normalize the counts to create the final coordinates.
        # This is a simple, linear transformation.
        love = counts['love'] / total_keywords
        justice = counts['justice'] / total_keywords
        power = counts['power'] / total_keywords
        wisdom = counts['wisdom'] / total_keywords

        return SimpleCoordinates(love, justice, power, wisdom)

    def calculate_distance_from_anchor(self, coords: SimpleCoordinates) -> float:
        """Calculates the direct Euclidean distance from the Universal Anchor (1,1,1,1)."""
        return ((self.UNIVERSAL_ANCHOR.love - coords.love) ** 2 +
                (self.UNIVERSAL_ANCHOR.justice - coords.justice) ** 2 +
                (self.UNIVERSAL_ANCHOR.power - coords.power) ** 2 +
                (self.UNIVERSAL_ANCHOR.wisdom - coords.wisdom) ** 2) ** 0.5

    def calculate_semantic_clarity(self, coords: SimpleCoordinates) -> float:
        """
        Calculates the information-theoretic clarity of a concept.

        A score of 1.0 means perfect clarity (the concept is purely one thing, e.g., 1,0,0,0).
        A score closer to 0 means higher entropy or "muddiness" (e.g., 0.25, 0.25, 0.25, 0.25).
        This is a measure of semantic entropy.
        """
        coords_tuple = (coords.love, coords.justice, coords.power, coords.wisdom)
        total = sum(coords_tuple)
        if total == 0:
            return 0.0

        # A simpler clarity metric: the magnitude of the vector relative to a perfect state.
        # A perfectly clear concept (1,0,0,0) has magnitude 1.
        # A perfectly muddy one (0.25, 0.25, 0.25, 0.25) has magnitude 0.5.
        # We can use the max value as a proxy for clarity.
        max_val = max(coords_tuple)
        return max_val
