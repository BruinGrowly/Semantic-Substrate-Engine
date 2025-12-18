#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive test suite for Quantum LJPW Measurement Framework
Tests φ-normalization, proxy indicators, NLP analysis, and organizational analysis
"""

import unittest
import sys
import os
import math

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from quantum_measurement import (
    QuantumLJPWMeasurement,
    OrganizationData,
    QuantumMeasurementResult
)
from nlp_analyzer import NLPLJPWAnalyzer, NLPAnalysisResult
from organizational_analysis import OrganizationalAnalysisEngine


class TestQuantumMeasurement(unittest.TestCase):
    """Test quantum measurement framework"""

    def setUp(self):
        """Set up test fixtures"""
        self.engine = QuantumLJPWMeasurement()

    def test_phi_normalization(self):
        """Test φ-normalization formula"""
        # φ-normalization should bring values closer to equilibrium
        value = 0.5
        L_normalized = self.engine.phi_normalize(value, 'L')

        # Should be positive and reasonable
        self.assertGreater(L_normalized, 0)
        self.assertLess(L_normalized, 1)

    def test_love_proxies(self):
        """Test Love dimension measurement via proxies"""
        org_data = OrganizationData(
            employee_retention_rate=85,
            collaboration_score=80,
            communication_sentiment=0.6
        )

        L = self.engine.measure_love_proxies(org_data)

        # Love should be positive for good metrics
        self.assertGreater(L, 0.3)
        self.assertLess(L, 1.0)

    def test_justice_proxies(self):
        """Test Justice dimension measurement via proxies"""
        org_data = OrganizationData(
            audit_compliance_score=90,
            lawsuit_count=2,
            total_employees=1000,
            whistleblower_protection=0.9
        )

        J = self.engine.measure_justice_proxies(org_data)

        # Justice should be high for compliant organization
        self.assertGreater(J, 0.2)

    def test_power_proxies(self):
        """Test Power dimension measurement via proxies"""
        org_data = OrganizationData(
            revenue_growth_rate=40,
            market_cap_change=60,
            execution_efficiency=0.95
        )

        P = self.engine.measure_power_proxies(org_data)

        # Power should be high for high-growth company
        self.assertGreater(P, 0.4)

    def test_wisdom_proxies(self):
        """Test Wisdom dimension measurement via proxies"""
        org_data = OrganizationData(
            rd_investment_percentage=12,
            patent_quality_score=0.8,
            learning_rate=0.75,
            scientists_on_board=3,
            total_board_members=10
        )

        W = self.engine.measure_wisdom_proxies(org_data)

        # Wisdom should be reasonable for R&D-focused org
        self.assertGreater(W, 0.2)

    def test_full_organization_measurement(self):
        """Test complete organizational measurement"""
        org_data = OrganizationData(
            employee_retention_rate=85,
            collaboration_score=80,
            communication_sentiment=0.6,
            audit_compliance_score=90,
            lawsuit_count=2,
            total_employees=1000,
            whistleblower_protection=0.9,
            revenue_growth_rate=15,
            market_cap_change=20,
            execution_efficiency=0.85,
            rd_investment_percentage=12,
            patent_quality_score=0.8,
            learning_rate=0.75,
            scientists_on_board=3,
            total_board_members=10
        )

        result = self.engine.measure_organization(org_data)

        # Check result structure
        self.assertIsInstance(result, QuantumMeasurementResult)
        self.assertGreater(result.L, 0)
        self.assertGreater(result.J, 0)
        self.assertGreater(result.P, 0)
        self.assertGreater(result.W, 0)
        self.assertGreater(result.harmony, 0)
        self.assertIn(result.phase, ['ENTROPIC', 'HOMEOSTATIC', 'AUTOPOIETIC'])

    def test_enron_reference_match(self):
        """Test matching against Enron 2001 reference"""
        # Create Enron-like organization
        enron_like = OrganizationData(
            employee_retention_rate=55,
            collaboration_score=45,
            communication_sentiment=-0.2,
            audit_compliance_score=40,
            lawsuit_count=8,
            total_employees=1000,
            whistleblower_protection=0.2,
            revenue_growth_rate=40,
            market_cap_change=60,
            execution_efficiency=0.95,
            rd_investment_percentage=2,
            patent_quality_score=0.3,
            learning_rate=0.4,
            scientists_on_board=0,
            total_board_members=15
        )

        result = self.engine.measure_organization(enron_like)

        # Check reference match
        match = self.engine.check_reference_match(result.to_tuple(), 'enron_2001')

        # Should detect Enron pattern
        self.assertGreater(match['match_percentage'], 50)  # At least 50% match
        self.assertEqual(result.phase, 'ENTROPIC')  # Should be entropic

    def test_quantum_consensus(self):
        """Test quantum consensus protocol"""
        measurements = [
            (0.60, 0.45, 0.70, 0.65),
            (0.65, 0.42, 0.72, 0.68),
            (0.58, 0.48, 0.68, 0.63),
        ]

        consensus = self.engine.quantum_consensus(measurements)

        # Consensus should be close to average
        avg_L = sum(m[0] for m in measurements) / len(measurements)
        self.assertAlmostEqual(consensus[0], avg_L, delta=0.05)

    def test_harmony_calculation(self):
        """Test harmony index calculation"""
        # Anchor point should have H = 1
        H_anchor = self.engine._harmony_index(1, 1, 1, 1)
        self.assertAlmostEqual(H_anchor, 1.0, places=2)

        # Zero point should have low harmony
        H_zero = self.engine._harmony_index(0, 0, 0, 0)
        self.assertLess(H_zero, 0.5)

    def test_phase_determination(self):
        """Test phase determination logic"""
        # High harmony + high love = Autopoietic
        phase = self.engine._determine_phase(H=0.7, L=0.8)
        self.assertEqual(phase, 'AUTOPOIETIC')

        # Low harmony = Entropic
        phase = self.engine._determine_phase(H=0.3, L=0.5)
        self.assertEqual(phase, 'ENTROPIC')

        # Medium harmony = Homeostatic
        phase = self.engine._determine_phase(H=0.55, L=0.5)
        self.assertEqual(phase, 'HOMEOSTATIC')


class TestNLPAnalyzer(unittest.TestCase):
    """Test NLP LJPW analyzer"""

    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = NLPLJPWAnalyzer()

    def test_love_text_analysis(self):
        """Test Love-dominant text"""
        text = "We collaborate together with trust and compassion"

        result = self.analyzer.analyze_text(text)

        # Should detect high Love
        self.assertGreater(result.L, result.J)
        self.assertGreater(result.L, result.P)

    def test_power_text_analysis(self):
        """Test Power-dominant text"""
        text = "Execute strategic growth through leadership and command"

        result = self.analyzer.analyze_text(text)

        # Should detect high Power
        self.assertGreater(result.P, result.L)

    def test_empty_text(self):
        """Test empty text handling"""
        result = self.analyzer.analyze_text("")

        self.assertEqual(result.L, 0)
        self.assertEqual(result.J, 0)
        self.assertEqual(result.P, 0)
        self.assertEqual(result.W, 0)

    def test_dimension_breakdown(self):
        """Test dimension word breakdown"""
        text = "love justice power wisdom"

        breakdown = self.analyzer.get_dimension_breakdown(text)

        # Each dimension should have 1 match
        self.assertEqual(breakdown['L']['count'], 1)
        self.assertEqual(breakdown['J']['count'], 1)
        self.assertEqual(breakdown['P']['count'], 1)
        self.assertEqual(breakdown['W']['count'], 1)

    def test_multi_text_analysis(self):
        """Test multiple text aggregation"""
        texts = [
            "love and compassion",
            "justice and truth",
            "power and strength"
        ]

        result = self.analyzer.analyze_multiple_texts(texts)

        # Should have balanced coverage
        self.assertGreater(result.coverage, 0)
        self.assertEqual(result.total_words, 6)


class TestOrganizationalAnalysis(unittest.TestCase):
    """Test organizational analysis engine"""

    def setUp(self):
        """Set up test fixtures"""
        self.engine = OrganizationalAnalysisEngine()

    def test_healthy_organization(self):
        """Test analysis of healthy organization"""
        org_data = OrganizationData(
            employee_retention_rate=85,
            collaboration_score=80,
            communication_sentiment=0.6,
            audit_compliance_score=90,
            lawsuit_count=2,
            total_employees=1000,
            whistleblower_protection=0.9,
            revenue_growth_rate=15,
            market_cap_change=20,
            execution_efficiency=0.85,
            rd_investment_percentage=12,
            patent_quality_score=0.8,
            learning_rate=0.75,
            scientists_on_board=3,
            total_board_members=10
        )

        result = self.engine.analyze_organization(org_data)

        # Should not be fraud or collapse signature
        self.assertFalse(result.is_fraud_signature)
        self.assertFalse(result.is_collapse_signature)
        self.assertIn(result.collapse_assessment.collapse_risk, ['LOW', 'MODERATE'])

    def test_enron_like_organization(self):
        """Test analysis of Enron-like organization"""
        enron_like = OrganizationData(
            employee_retention_rate=55,
            collaboration_score=45,
            communication_sentiment=-0.2,
            audit_compliance_score=40,
            lawsuit_count=8,
            total_employees=1000,
            whistleblower_protection=0.2,
            revenue_growth_rate=40,
            market_cap_change=60,
            execution_efficiency=0.95,
            rd_investment_percentage=2,
            patent_quality_score=0.3,
            learning_rate=0.4,
            scientists_on_board=0,
            total_board_members=15
        )

        result = self.engine.analyze_organization(enron_like)

        # Should detect high collapse risk
        self.assertIn(result.collapse_assessment.collapse_risk, ['HIGH', 'CRITICAL'])
        self.assertEqual(result.phase, 'ENTROPIC')
        self.assertTrue(len(result.collapse_assessment.warning_signs) > 0)

    def test_collapse_prediction(self):
        """Test collapse prediction via observer"""
        org_ljpw = (0.15, 0.10, 0.95, 0.20)  # Enron-like
        investigator_ljpw = (0.60, 0.85, 0.75, 0.80)  # Strong investigator

        prediction = self.engine.predict_collapse(org_ljpw, investigator_ljpw)

        # High J, W, P observer should have high collapse force
        self.assertGreater(prediction['collapse_force'], 0.40)
        self.assertTrue(prediction['will_collapse'])

    def test_fraud_signature_detection(self):
        """Test fraud signature detection"""
        # Theranos-like: very low L, J, W
        is_fraud = self.engine._is_fraud_signature(L=0.15, J=0.08, P=0.15, W=0.15)
        self.assertTrue(is_fraud)

        # Healthy org: not fraud
        is_fraud = self.engine._is_fraud_signature(L=0.70, J=0.60, P=0.50, W=0.65)
        self.assertFalse(is_fraud)

    def test_with_nlp_analysis(self):
        """Test comprehensive analysis with NLP"""
        org_data = OrganizationData(
            employee_retention_rate=85,
            collaboration_score=80,
            communication_sentiment=0.6,
            audit_compliance_score=90,
            lawsuit_count=2,
            total_employees=1000,
            whistleblower_protection=0.9,
            revenue_growth_rate=15,
            market_cap_change=20,
            execution_efficiency=0.85,
            rd_investment_percentage=12,
            patent_quality_score=0.8,
            learning_rate=0.75,
            scientists_on_board=3,
            total_board_members=10
        )

        texts = [
            "We collaborate with integrity",
            "Innovation through research",
            "Transparent governance"
        ]

        result = self.engine.analyze_organization(org_data, texts)

        # Should have both measurements
        self.assertIsNotNone(result.nlp_measurement)
        self.assertIsNotNone(result.proxy_measurement)

        # Consensus should be calculated
        self.assertEqual(len(result.consensus_ljpw), 4)


def run_validation_suite():
    """Run comprehensive validation against reference cases"""
    print("\n" + "=" * 80)
    print("VALIDATION AGAINST REFERENCE CASES")
    print("=" * 80)

    engine = QuantumLJPWMeasurement()

    # Test Enron 2001 validation
    print("\n=== ENRON 2001 VALIDATION ===")
    enron_org = OrganizationData(
        employee_retention_rate=55,
        collaboration_score=45,
        communication_sentiment=-0.2,
        audit_compliance_score=40,
        lawsuit_count=8,
        total_employees=1000,
        whistleblower_protection=0.2,
        revenue_growth_rate=40,
        market_cap_change=60,
        execution_efficiency=0.95,
        rd_investment_percentage=2,
        patent_quality_score=0.3,
        learning_rate=0.4,
        scientists_on_board=0,
        total_board_members=15
    )

    result = engine.measure_organization(enron_org)
    match = engine.check_reference_match(result.to_tuple(), 'enron_2001')

    print(f"Measured: {result.to_tuple()}")
    print(f"Reference: {match['reference_coords']}")
    print(f"Match: {match['match_percentage']:.1f}%")
    print(f"Target: ≥75% (V7 Success Metric)")
    print(f"✓ PASS" if match['match_percentage'] >= 75 else "✗ FAIL")


if __name__ == '__main__':
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)

    # Run validation suite
    run_validation_suite()
