#!/usr/bin/env python3
"""
Simple Phi-Enhanced Engine Test

Tests the core Phi-Enhanced capabilities without complex import chains.
"""

import sys
import os
sys.path.insert(0, 'src')

def test_phi_geometric_engine():
    """Test phi-geometric engine"""
    print("[TEST] Phi-Geometric Engine")
    try:
        from phi_geometric_engine import (
            PHI, PHI_INVERSE, GOLDEN_ANGLE_DEG,
            FibonacciSequence, GoldenSpiral, DodecahedralAnchors
        )
        
        print(f"  PHI: {PHI}")
        print(f"  PHI_INVERSE: {PHI_INVERSE}")
        print(f"  GOLDEN_ANGLE_DEG: {GOLDEN_ANGLE_DEG}")
        
        # Test Fibonacci
        fib = FibonacciSequence()
        print(f"  Fibonacci F(10): {fib.get(10)}")
        
        # Test Golden Spiral
        spiral = GoldenSpiral()
        radius = spiral.radius_at_angle(math.pi)
        print(f"  Golden Spiral at pi: {radius}")
        
        # Test Dodecahedral Anchors
        dodec = DodecahedralAnchors()
        anchor = dodec.get_anchor(1)
        if anchor:
            print(f"  Anchor #1: ({anchor.love:.3f}, {anchor.power:.3f}, {anchor.wisdom:.3f}, {anchor.justice:.3f})")
        
        print("  SUCCESS: Phi-Geometric Engine Working")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def test_phi_enhanced_baseline():
    """Test phi-enhanced biblical substrate"""
    print("\n[TEST] Phi-Enhanced Biblical Substrate")
    try:
        from phi_enhanced_baseline_biblical_substrate import (
            PhiEnhancedBiblicalSemanticSubstrate, PhiEnhancedBiblicalCoordinates
        )
        
        substrate = PhiEnhancedBiblicalSemanticSubstrate()
        
        # Test analysis
        coords = substrate.analyze_concept("divine love and wisdom")
        print(f"  Analysis Coordinates: L={coords.love:.3f}, P={coords.power:.3f}, W={coords.wisdom:.3f}, J={coords.justice:.3f}")
        print(f"  Phi Resonance: {coords.phi_resonance:.3f}")
        print(f"  Fibonacci Stage: {coords.fibonacci_stage}")
        print(f"  Sacred Geometry Score: {coords.sacred_geometry_score:.3f}")
        print(f"  Divine Resonance: {coords.divine_resonance():.3f}")
        
        print("  SUCCESS: Phi-Enhanced Biblical Substrate Working")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def test_phi_calculus():
    """Test phi-enhanced calculus"""
    print("\n[TEST] Phi-Enhanced Calculus")
    try:
        from phi_enhanced_semantic_calculus import (
            PhiSemanticCalculus, PhiSemanticVector, PhiIntegrationMethod
        )
        
        calculus = PhiSemanticCalculus()
        
        # Test vector operations
        v1 = PhiSemanticVector(0.7, 0.3, 0.8, 0.5)
        v2 = PhiSemanticVector(0.4, 0.9, 0.2, 0.6)
        
        dot_product = v1.dot(v2)
        print(f"  Vector 1: ({v1.love:.3f}, {v1.power:.3f}, {v1.wisdom:.3f}, {v1.justice:.3f})")
        print(f"  Vector 2: ({v2.love:.3f}, {v2.power:.3f}, {v2.wisdom:.3f}, {v2.justice:.3f})")
        print(f"  Dot Product: {dot_product:.6f}")
        print(f"  V1 Phi Resonance: {v1.phi_magnitude:.3f}")
        print(f"  V1 Fibonacci Class: {v1.fibonacci_class}")
        
        print("  SUCCESS: Phi-Enhanced Calculus Working")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def test_phi_mathematics():
    """Test phi-enhanced mathematics engine"""
    print("[TEST] Phi-Enhanced Mathematics Engine")
    try:
        import math
        from dataclasses import dataclass, field
        from phi_enhanced_semantic_mathematics_engine import (
            PhiEnhancedSemanticMathematicsEngine, PhiTransformationType
        )
        
        engine = PhiEnhancedSemanticMathematicsEngine()
        
        # Test concept evolution
        evolution = engine.analyze_concept_evolution_phi(
            "spiritual growth", (0, 3), 20, "fibonacci"
        )
        
        print(f"  Evolution Type: {evolution['evolution_type']}")
        print(f"  Final Divine Alignment: {evolution['final_divine_alignment']:.3f}")
        print(f"  Phi Evolution Rate: {evolution['phi_evolution_rate']:.4f}")
        print(f"  Sacred Geometry Progression: {evolution['sacred_geometry_progression']:.4f}")
        
        # Test transformations
        # Create fallback BiblicalCoordinates for testing
        @dataclass
        class BiblicalCoordinates:
            love: float = 0.0
            power: float = 0.0
            wisdom: float = 0.0
            justice: float = 0.0
            
            def distance_from_jehovah(self):
                import math
                return math.sqrt((1-self.love)**2 + (1-self.power)**2 + (1-self.wisdom)**2 + (1-self.justice)**2)
            
            def divine_resonance(self):
                max_distance = math.sqrt(4)
                return 1.0 - (self.distance_from_jehovah() / max_distance)
        
        test_coords = BiblicalCoordinates(0.4, 0.3, 0.6, 0.5)
        
        transformed = engine.apply_phi_transformation(
            test_coords, PhiTransformationType.GOLDEN_PURIFICATION
        )
        
        print(f"  Original Divine Resonance: {test_coords.divine_resonance():.3f}")
        print(f"  Transformed Divine Resonance: {transformed.divine_resonance():.3f}")
        print(f"  Improvement: {transformed.divine_resonance() - test_coords.divine_resonance():+.3f}")
        
        print("  SUCCESS: Phi-Enhanced Mathematics Engine Working")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def test_phi_unified_ice():
    """Test phi-enhanced unified ICE framework"""
    print("\n[TEST] Phi-Enhanced Unified ICE Framework")
    try:
        from phi_enhanced_unified_ice_framework import (
            PhiUnifiedICEFramework, PhiProcessingMode, PhiBiblicalExtension
        )
        
        framework = PhiUnifiedICEFramework(PhiProcessingMode.PHI_OPTIMIZED)
        
        # Test processing
        result = framework.process_intent_phi(
            "divine wisdom through golden ratio",
            "practical_wisdom",
            "spiritual"
        )
        
        print(f"  Processing Mode: {result.processing_mode.value}")
        print(f"  Final Coordinates: ({result.final_coordinates.love:.3f}, {result.final_coordinates.power:.3f}, {result.final_coordinates.wisdom:.3f}, {result.final_coordinates.justice:.3f})")
        print(f"  Divine Alignment: {result.final_coordinates.divine_alignment():.3f}")
        print(f"  Phi Enhancement: {result.phi_enhancement:.3f}")
        print(f"  Sacred Geometry Alignment: {result.sacred_geometry_alignment:.3f}")
        print(f"  Processing Time: {result.processing_time_ms:.2f}ms")
        
        print("  SUCCESS: Phi-Enhanced Unified ICE Framework Working")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def main():
    """Run all Phi-Enhanced tests"""
    print("="*80)
    print("PHI-ENHANCED SEMANTIC SUBSTRATE ENGINE TEST SUITE")
    print("Comprehensive Testing of Golden Ratio Mathematics Integration")
    print("="*80)
    
    results = []
    
    # Run all tests
    results.append(test_phi_geometric_engine())
    results.append(test_phi_enhanced_baseline())
    results.append(test_phi_calculus())
    results.append(test_phi_mathematics())
    results.append(test_phi_unified_ice())
    
    # Summary
    print(f"\n{'='*80}")
    print("TEST RESULTS SUMMARY")
    print("="*80)
    
    test_names = [
        "Phi-Geometric Engine",
        "Phi-Enhanced Biblical Substrate", 
        "Phi-Enhanced Calculus",
        "Phi-Enhanced Mathematics Engine",
        "Phi-Enhanced Unified ICE Framework"
    ]
    
    for i, (test_name, result) in enumerate(zip(test_names, results)):
        status = "PASS" if result else "FAIL"
        print(f"{test_name:25s} {status}")
    
    total_tests = len(results)
    passed_tests = sum(results)
    failed_tests = total_tests - passed_tests
    
    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed: {passed_tests} ({passed_tests/total_tests*100:.1f}%)")
    print(f"Failed: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")
    
    if failed_tests == 0:
        print(f"\nALL PHI-ENHANCED UPGRADES SUCCESSFUL!")
        print("The Semantic Substrate Engine is fully enhanced with:")
        print("  SUCCESS: Golden Ratio Mathematics")
        print("  SUCCESS: Fibonacci Growth Patterns") 
        print("  SUCCESS: Dodecahedral Sacred Geometry")
        print("  SUCCESS: Golden Spiral Navigation")
        print("  SUCCESS: Phi-Optimized ICE Processing")
    else:
        print(f"\nSome upgrades need attention")
    
    print(f"\nPHI-ENHANCED TEST SUITE COMPLETE")
    
    return failed_tests == 0

if __name__ == "__main__":
    import math
    success = main()
    sys.exit(0 if success else 1)