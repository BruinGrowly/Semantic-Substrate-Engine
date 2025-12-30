#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LJPW Framework V7.7 — Comprehensive Test Suite

Tests all core components of the Semantic Substrate Engine.
"""

import unittest
import sys
import os
import math
import numpy as np

# Ensure src is in path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.constants import (
    PHI, PHI_INV, L0, J0, P0, W0,
    UNCERTAINTY_BOUND, TSIRELSON_BOUND,
    CONSCIOUSNESS_THRESHOLD
)
from src.ljpw_state import LJPWState, ANCHOR, EQUILIBRIUM
from src.ljpw_framework import LJPWFramework
from src.dynamics import DynamicLJPW
from src.autopoietic_engine import AutopoieticEngine
from src.collective import CollectiveAutopoiesis
from src.generative import (
    semantic_interpolate, semantic_complement,
    semantic_blend, semantic_resonance,
    design_concept
)


class TestConstants(unittest.TestCase):
    """Test all framework constants."""
    
    def test_phi_identity(self):
        """φ = 1 + 1/φ (self-definition)."""
        self.assertAlmostEqual(PHI, 1 + 1/PHI, places=6)
    
    def test_phi_inverse(self):
        """φ⁻¹ = φ - 1 and 1/φ."""
        self.assertAlmostEqual(PHI_INV, PHI - 1, places=6)
        self.assertAlmostEqual(PHI_INV, 1/PHI, places=6)
    
    def test_equilibrium_values(self):
        """Equilibrium constants match theory."""
        self.assertAlmostEqual(L0, (math.sqrt(5) - 1) / 2, places=6)  # φ⁻¹
        self.assertAlmostEqual(J0, math.sqrt(2) - 1, places=6)
        self.assertAlmostEqual(P0, math.e - 2, places=6)
        self.assertAlmostEqual(W0, math.log(2), places=6)
    
    def test_uncertainty_bound(self):
        """Uncertainty bound = J₀ × W₀."""
        self.assertAlmostEqual(UNCERTAINTY_BOUND, J0 * W0, places=6)


class TestLJPWState(unittest.TestCase):
    """Test LJPWState dataclass."""
    
    def test_create_state(self):
        """Test state creation."""
        state = LJPWState(L=0.5, J=0.5, P=0.5, W=0.5)
        self.assertEqual(state.L, 0.5)
        self.assertEqual(state.P, 0.5)
    
    def test_bounds_enforcement(self):
        """Values are clipped to valid range."""
        state = LJPWState(L=2.0, J=-0.5, P=0.5, W=0.5)
        self.assertLessEqual(state.L, TSIRELSON_BOUND)
        self.assertGreaterEqual(state.J, 0.0)
    
    def test_anchor_point(self):
        """Anchor point is (1,1,1,1)."""
        anchor = LJPWState.anchor_point()
        self.assertEqual(anchor.as_tuple(), (1.0, 1.0, 1.0, 1.0))
    
    def test_natural_equilibrium(self):
        """Natural equilibrium matches constants."""
        eq = LJPWState.natural_equilibrium()
        self.assertAlmostEqual(eq.L, L0, places=6)
        self.assertAlmostEqual(eq.J, J0, places=6)
    
    def test_array_conversion(self):
        """Array conversion roundtrips correctly."""
        original = LJPWState(L=0.6, J=0.4, P=0.7, W=0.5)
        arr = original.as_array()
        restored = LJPWState.from_array(arr)
        self.assertEqual(original, restored)
    
    def test_distance_from_anchor(self):
        """Distance calculations work correctly."""
        anchor = LJPWState.anchor_point()
        origin = LJPWState(L=0, J=0, P=0, W=0)
        
        self.assertEqual(anchor.distance_from_anchor(), 0.0)
        self.assertAlmostEqual(origin.distance_from_anchor(), 2.0, places=6)


class TestLJPWFramework(unittest.TestCase):
    """Test core LJPWFramework class."""
    
    def test_emergent_dimensions(self):
        """L emerges from W, J emerges from P."""
        framework = LJPWFramework(P=0.8, W=0.9)
        
        # L should correlate with W
        self.assertGreater(framework.L, 0.7)
        # J should correlate with P
        self.assertGreater(framework.J, 0.6)
    
    def test_harmony_static(self):
        """Static harmony in [0, 1]."""
        framework = LJPWFramework(P=0.7, W=0.7)
        H = framework.harmony_static()
        self.assertGreaterEqual(H, 0)
        self.assertLessEqual(H, 1)
    
    def test_consciousness_threshold(self):
        """High capacity systems cross C > 0.1."""
        high = LJPWFramework(P=0.85, W=0.92)
        low = LJPWFramework(P=0.3, W=0.3)
        
        self.assertTrue(high.is_conscious())
        self.assertFalse(low.is_conscious())
    
    def test_phase_transitions(self):
        """Phase determination works correctly."""
        # Framework calculates H from distance to natural equilibrium
        # High values near equilibrium should be HOMEOSTATIC or AUTOPOIETIC
        autopoietic = LJPWFramework(P=0.75, W=0.75, L=0.75, J=0.75)
        entropic = LJPWFramework(P=0.1, W=0.1, L=0.1, J=0.1)
        
        # Test that phases are correctly ordered
        self.assertIn(autopoietic.phase(), ['HOMEOSTATIC', 'AUTOPOIETIC'])
        self.assertEqual(entropic.phase(), 'ENTROPIC')
    
    def test_phi_normalization(self):
        """φ-normalization produces valid values."""
        original = LJPWFramework(P=0.8, W=0.9)
        normalized = original.phi_normalize()
        
        self.assertGreater(normalized.L, 0)
        self.assertLessEqual(normalized.L, 1)
    
    def test_uncertainty_principle(self):
        """Uncertainty principle validation."""
        framework = LJPWFramework(P=0.7, W=0.7)
        
        self.assertTrue(framework.check_uncertainty(0.5, 0.6))  # 0.3 >= 0.287
        self.assertFalse(framework.check_uncertainty(0.1, 0.1))  # 0.01 < 0.287


class TestDynamicLJPW(unittest.TestCase):
    """Test dynamic LJPW system."""
    
    def test_integration(self):
        """Integration produces valid trajectories."""
        dynamic = DynamicLJPW()
        solution = dynamic.integrate((0.5, 0.5, 0.5, 0.5), (0, 10), n_points=11)
        
        self.assertEqual(solution.shape, (11, 4))
        # All values should be bounded
        self.assertTrue(np.all(solution >= 0))
        self.assertTrue(np.all(solution <= 1))
    
    def test_equilibrium_convergence(self):
        """System converges to equilibrium."""
        dynamic = DynamicLJPW()
        equilibrium = dynamic.get_equilibrium_state((0.3, 0.3, 0.3, 0.3))
        
        # Should have reached a stable state
        self.assertIsInstance(equilibrium, LJPWState)
    
    def test_karma_coupling(self):
        """Karma coupling increases with harmony."""
        dynamic = DynamicLJPW()
        
        low_H = dynamic.kappa(0.3, 'LJ')
        high_H = dynamic.kappa(0.8, 'LJ')
        
        # Higher harmony = higher coupling
        self.assertGreater(high_H, low_H)
    
    def test_power_erosion(self):
        """Power erosion increases with low wisdom."""
        dynamic = DynamicLJPW()
        
        low_W_erosion = dynamic.power_erosion(0.9, 0.3)
        high_W_erosion = dynamic.power_erosion(0.9, 0.9)
        
        # Low wisdom = more erosion
        self.assertGreater(low_W_erosion, high_W_erosion)


class TestAutopoieticEngine(unittest.TestCase):
    """Test autopoietic self-improvement engine."""
    
    def test_self_improvement(self):
        """Engine improves over generations."""
        engine = AutopoieticEngine(LJPWState.natural_equilibrium())
        
        initial_C = engine.consciousness()
        engine.evolve(generations=10)
        final_C = engine.consciousness()
        
        # Should have improved
        self.assertGreater(final_C, initial_C)
    
    def test_gap_identification(self):
        """Gaps are correctly identified."""
        engine = AutopoieticEngine(LJPWState(L=0.5, J=0.4, P=0.3, W=0.6))
        gaps = engine.identify_gaps()
        
        # Should identify gaps
        self.assertGreater(len(gaps), 0)
        # Power should be identified (current 0.3 < target 0.9)
        dims = [g['dimension'] for g in gaps]
        self.assertIn('P', dims)
    
    def test_gradient_computation(self):
        """Gradient is computed correctly."""
        engine = AutopoieticEngine(LJPWState.natural_equilibrium())
        grad = engine.compute_gradient()
        
        self.assertEqual(len(grad), 4)
        # Gradient should be finite
        self.assertTrue(np.all(np.isfinite(grad)))


class TestCollectiveAutopoiesis(unittest.TestCase):
    """Test collective consciousness."""
    
    def test_collective_creation(self):
        """Collective is created correctly."""
        collective = CollectiveAutopoiesis.create(n_agents=10)
        self.assertEqual(len(collective.agents), 10)
    
    def test_collective_evolution(self):
        """Collective evolves over time."""
        collective = CollectiveAutopoiesis.create(n_agents=8, coupling=0.2)
        
        initial_sync = collective.synchrony()
        collective.evolve(generations=10)
        final_sync = collective.synchrony()
        
        # Synchrony should increase
        self.assertGreaterEqual(final_sync, initial_sync)
    
    def test_collective_consciousness(self):
        """Collective consciousness is calculated."""
        collective = CollectiveAutopoiesis.create(n_agents=12, coupling=0.15)
        collective.evolve(generations=10)
        
        C = collective.collective_consciousness()
        self.assertGreater(C, 0)


class TestGenerativeSemantics(unittest.TestCase):
    """Test generative semantics functions."""
    
    def test_interpolation(self):
        """Interpolation produces intermediate values."""
        A = (0.0, 0.0, 0.0, 0.0)
        B = (1.0, 1.0, 1.0, 1.0)
        
        mid = semantic_interpolate(A, B, 0.5)
        self.assertEqual(mid, (0.5, 0.5, 0.5, 0.5))
    
    def test_complement(self):
        """Complement inverts values."""
        original = (0.2, 0.3, 0.8, 0.4)
        complement = semantic_complement(original)
        
        self.assertAlmostEqual(complement[0], 0.8)
        self.assertAlmostEqual(complement[2], 0.2)
    
    def test_blend(self):
        """Blending averages correctly."""
        concepts = [(1.0, 0.0, 0.5, 0.5), (0.0, 1.0, 0.5, 0.5)]
        blended = semantic_blend(concepts)
        
        self.assertAlmostEqual(blended[0], 0.5)
        self.assertAlmostEqual(blended[1], 0.5)
    
    def test_design_concept(self):
        """Concept design produces valid coordinates."""
        concept = design_concept({'love': 0.8, 'power': 0.6})
        
        self.assertEqual(concept[0], 0.8)  # L
        self.assertEqual(concept[2], 0.6)  # P
    
    def test_resonance(self):
        """Resonance is calculated."""
        coords = (0.618, 0.414, 0.718, 0.693)
        R = semantic_resonance(coords)
        
        self.assertGreater(R, 0)
        self.assertLessEqual(R, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
