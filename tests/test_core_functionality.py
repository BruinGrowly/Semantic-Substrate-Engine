"""
Tests for the DivineInvitationSemanticEngine.
"""

import sys
import os
import unittest

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.divine_invitation_engine import DivineInvitationSemanticEngine

class TestDivineInvitationSemanticEngine(unittest.TestCase):
    """Test suite for the Divine Invitation Semantic Engine."""

    def setUp(self):
        """Set up the test case."""
        self.engine = DivineInvitationSemanticEngine()

    def test_analyze_concept_love(self):
        """Test the analyze_concept method with a concept of love."""
        concept = "love compassion kindness"
        coords = self.engine.analyze_concept(concept)
        self.assertGreater(coords.love, 0.5)
        self.assertEqual(coords.justice, 0)
        self.assertEqual(coords.power, 0)
        self.assertEqual(coords.wisdom, 0)

    def test_analyze_concept_justice(self):
        """Test the analyze_concept method with a concept of justice."""
        concept = "justice truth fairness"
        coords = self.engine.analyze_concept(concept)
        self.assertEqual(coords.love, 0)
        self.assertGreater(coords.justice, 0.5)
        self.assertEqual(coords.power, 0)
        self.assertEqual(coords.wisdom, 0)

    def test_analyze_concept_power(self):
        """Test the analyze_concept method with a concept of power."""
        concept = "power strength authority"
        coords = self.engine.analyze_concept(concept)
        self.assertEqual(coords.love, 0)
        self.assertEqual(coords.justice, 0)
        self.assertGreater(coords.power, 0.5)
        self.assertEqual(coords.wisdom, 0)

    def test_analyze_concept_wisdom(self):
        """Test the analyze_concept method with a concept of wisdom."""
        concept = "wisdom knowledge understanding"
        coords = self.engine.analyze_concept(concept)
        self.assertEqual(coords.love, 0)
        self.assertEqual(coords.justice, 0)
        self.assertEqual(coords.power, 0)
        self.assertGreater(coords.wisdom, 0.5)

    def test_analyze_concept_mixed(self):
        """Test the analyze_concept method with a mixed concept."""
        concept = "love and justice"
        coords = self.engine.analyze_concept(concept)
        self.assertGreater(coords.love, 0.4)
        self.assertGreater(coords.justice, 0.4)
        self.assertEqual(coords.power, 0)
        self.assertEqual(coords.wisdom, 0)

    def test_get_distance_from_anchor(self):
        """Test the get_distance_from_anchor method."""
        concept = "love"
        coords = self.engine.analyze_concept(concept)
        distance = self.engine.get_distance_from_anchor(coords)
        self.assertAlmostEqual(distance, 1.732, places=3)

    def test_get_semantic_clarity(self):
        """Test the get_semantic_clarity method."""
        concept = "love and justice"
        coords = self.engine.analyze_concept(concept)
        clarity = self.engine.get_semantic_clarity(coords)
        self.assertAlmostEqual(clarity, 0.5, places=3)

if __name__ == '__main__':
    unittest.main()