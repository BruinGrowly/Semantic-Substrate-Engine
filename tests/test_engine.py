import unittest
import sys
import os

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.divine_invitation_engine import DivineInvitationSemanticEngine, Coordinates

class TestDivineInvitationSemanticEngine(unittest.TestCase):
    """Thorough unit tests for the DivineInvitationSemanticEngine."""

    def setUp(self):
        """Set up a new engine for each test."""
        self.engine = DivineInvitationSemanticEngine()

    def assertCoordinatesAlmostEqual(self, coords1, coords2, places=3):
        """Assert that two Coordinates objects are almost equal."""
        self.assertAlmostEqual(coords1.love, coords2.love, places)
        self.assertAlmostEqual(coords1.justice, coords2.justice, places)
        self.assertAlmostEqual(coords1.power, coords2.power, places)
        self.assertAlmostEqual(coords1.wisdom, coords2.wisdom, places)

    def test_pure_love(self):
        """Test a concept that is purely love."""
        text = "Unconditional agape love, compassion, and kindness."
        expected = Coordinates(1.0, 0.0, 0.0, 0.0)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_pure_justice(self):
        """Test a concept that is purely justice."""
        text = "Absolute truth, perfect fairness, and unwavering integrity."
        expected = Coordinates(0.0, 1.0, 0.0, 0.0)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_pure_power(self):
        """Test a concept that is purely power."""
        text = "Sovereign might and absolute authority."
        expected = Coordinates(0.0, 0.0, 1.0, 0.0)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_pure_wisdom(self):
        """Test a concept that is purely wisdom."""
        text = "Deep understanding, insight, and profound knowledge."
        expected = Coordinates(0.0, 0.0, 0.0, 1.0)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_no_keywords(self):
        """Test text with no relevant keywords."""
        text = "The quick brown fox jumps over the lazy dog."
        expected = Coordinates(0.0, 0.0, 0.0, 0.0)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_perfectly_balanced(self):
        """Test text with an equal number of keywords for all axes."""
        text = "love justice power wisdom"
        expected = Coordinates(0.25, 0.25, 0.25, 0.25)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_mixed_case(self):
        """Test text with mixed-case keywords."""
        text = "LOVE is the highest TRUTH."
        expected = Coordinates(0.5, 0.5, 0.0, 0.0)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_punctuation(self):
        """Test that punctuation is handled correctly."""
        text = "Love, justice... power! (wisdom?)"
        expected = Coordinates(0.25, 0.25, 0.25, 0.25)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_long_string(self):
        """Test a long string with many keywords."""
        text = "love " * 10 + "justice " * 5 + "power " * 3 + "wisdom " * 2
        total = 10 + 5 + 3 + 2
        expected = Coordinates(10/total, 5/total, 3/total, 2/total)
        result = self.engine.analyze_concept(text)
        self.assertCoordinatesAlmostEqual(result, expected)

    def test_distance_from_anchor(self):
        """Test the distance calculation from the anchor point."""
        # Anchor point itself should have 0 distance
        self.assertAlmostEqual(self.engine.get_distance_from_anchor(Coordinates(1, 1, 1, 1)), 0.0)
        # A pure concept (1,0,0,0) should be sqrt(3) away
        self.assertAlmostEqual(self.engine.get_distance_from_anchor(Coordinates(1, 0, 0, 0)), 3**0.5)
        # A null concept (0,0,0,0) should be sqrt(4) or 2 away
        self.assertAlmostEqual(self.engine.get_distance_from_anchor(Coordinates(0, 0, 0, 0)), 2.0)
        # A balanced concept (0.5x4) should be sqrt(4 * 0.5^2) = 1 away
        self.assertAlmostEqual(self.engine.get_distance_from_anchor(Coordinates(0.5, 0.5, 0.5, 0.5)), 1.0)

    def test_semantic_clarity(self):
        """Test the semantic clarity calculation."""
        # A pure concept should have perfect clarity
        self.assertAlmostEqual(self.engine.get_semantic_clarity(Coordinates(1, 0, 0, 0)), 1.0)
        self.assertAlmostEqual(self.engine.get_semantic_clarity(Coordinates(0, 1, 0, 0)), 1.0)
        # A null concept has no clarity
        self.assertAlmostEqual(self.engine.get_semantic_clarity(Coordinates(0, 0, 0, 0)), 0.0)
        # A perfectly balanced (muddled) concept has clarity equal to its max component
        self.assertAlmostEqual(self.engine.get_semantic_clarity(Coordinates(0.25, 0.25, 0.25, 0.25)), 0.25)
        # A mixed concept's clarity is its dominant axis value
        self.assertAlmostEqual(self.engine.get_semantic_clarity(Coordinates(0.5, 0.3, 0.1, 0.1)), 0.5)

if __name__ == '__main__':
    unittest.main()
