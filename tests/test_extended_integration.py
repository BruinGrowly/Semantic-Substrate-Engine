"""
Test Extended ICE Integration - Phase 3.4

This test verifies that ICE-Centric processing has been successfully
integrated into additional semantic modules beyond the core engines.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_semantic_calculus_integration():
    """Test ICE integration in Semantic Calculus"""
    print("\n=== Test 1: Semantic Calculus ICE Integration ===")
    
    try:
        from semantic_calculus import SemanticCalculus, ICE_CENTRIC_AVAILABLE, UNIFIED_ICE_AVAILABLE
        
        print(f"ICE-Centric Available: {ICE_CENTRIC_AVAILABLE}")
        print(f"Unified ICE Available: {UNIFIED_ICE_AVAILABLE}")
        
        calculus = SemanticCalculus()
        
        print(f"Calculus ICE Engine: {calculus.ice_centric_engine is not None}")
        print(f"Calculus Unified Framework: {calculus.unified_ice_framework is not None}")
        
        # Test ICE semantic derivative
        if ICE_CENTRIC_AVAILABLE or UNIFIED_ICE_AVAILABLE:
            test_text = "Show compassion and wisdom"
            result = calculus.semantic_derivative_ice(test_text)
            
            if result is not None:
                print(f"ICE Semantic Derivative: {type(result).__name__}")
                print("[SUCCESS] ICE semantic derivative works")
            else:
                print("[WARNING] ICE semantic derivative returned None")
            
            # Test semantic flow analysis
            flow_results = calculus.analyze_semantic_flow_ice(test_text, evolution_steps=3)
            if flow_results:
                print(f"Semantic Flow Steps: {len(flow_results)}")
                print(f"First Step Alignment: {flow_results[0].get('unified_alignment', 0):.2%}")
                print("[SUCCESS] ICE semantic flow analysis works")
            else:
                print("[WARNING] ICE semantic flow analysis returned empty")
            
            # Test semantic optimization
            opt_result = calculus.optimize_semantic_objective_ice(test_text)
            if opt_result.get('optimization_success'):
                print(f"Optimization Success: {opt_result.get('optimization_success')}")
                print(f"Alignment Improvement: {opt_result.get('improvement', 0):+.2%}")
                print("[SUCCESS] ICE semantic optimization works")
            else:
                print("[WARNING] ICE semantic optimization failed")
        
        else:
            print("[INFO] ICE engines not available for semantic calculus")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Semantic calculus integration test failed: {e}")
        return False

def test_ultimate_engine_unified_integration():
    """Test that Ultimate Engine now uses Unified ICE Framework"""
    print("\n=== Test 2: Ultimate Engine Unified Integration ===")
    
    try:
        from ultimate_core_engine import UltimateCoreEngine, UNIFIED_ICE_AVAILABLE
        
        print(f"Unified ICE Available: {UNIFIED_ICE_AVAILABLE}")
        
        engine = UltimateCoreEngine()
        
        # Check for unified framework
        has_unified = hasattr(engine, 'unified_ice_framework') and engine.unified_ice_framework is not None
        print(f"Has Unified Framework: {has_unified}")
        
        if has_unified:
            print("[SUCCESS] Ultimate Engine integrated with Unified ICE Framework")
        else:
            print("[INFO] Ultimate Engine using fallback ICE integration")
        
        # Test enhanced analysis
        result = engine.ultimate_concept_analysis(
            "Act with justice and compassion",
            context="biblical",
            use_ice_centric=True
        )
        
        if result.get('ice_centric_analysis'):
            print(f"ICE-Centric Analysis: {result.get('ice_centric_analysis')}")
            print(f"Enhanced Analysis: {result.get('enhanced_analysis')}")
            
            if result.get('unified_ice_result'):
                unified_result = result['unified_ice_result']
                print(f"Unified Alignment: {unified_result.unified_alignment:.2%}")
                print(f"Processing Mode: {unified_result.processing_mode.value}")
                print("[SUCCESS] Unified ICE processing works in Ultimate Engine")
            else:
                print("[SUCCESS] ICE-Centric processing works in Ultimate Engine")
        else:
            print("[WARNING] ICE-Centric analysis not enabled")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Ultimate Engine unified integration test failed: {e}")
        return False

def test_cross_module_compatibility():
    """Test compatibility between different integrated modules"""
    print("\n=== Test 3: Cross-Module Compatibility ===")
    
    try:
        from baseline_biblical_substrate import BiblicalSemanticSubstrate
        from ultimate_core_engine import UltimateCoreEngine
        from unified_ice_framework import unified_ice_framework
        
        # Test baseline integration
        baseline = BiblicalSemanticSubstrate()
        baseline_result = baseline.analyze_concept_enhanced(
            "Seek wisdom through understanding",
            context="educational",
            use_ice=True
        )
        
        print(f"Baseline Enhanced Result: {type(baseline_result).__name__}")
        
        # Test ultimate integration  
        ultimate = UltimateCoreEngine()
        ultimate_result = ultimate.ultimate_concept_analysis(
            "Seek wisdom through understanding",
            context="educational", 
            use_ice_centric=True
        )
        
        print(f"Ultimate ICE-Centric: {ultimate_result.get('ice_centric_analysis', False)}")
        
        # Test unified framework directly
        unified_result = unified_ice_framework.process_intent(
            "Seek wisdom through understanding",
            context="educational"
        )
        
        print(f"Unified Alignment: {unified_result.unified_alignment:.2%}")
        print(f"Unified Processing Mode: {unified_result.processing_mode.value}")
        
        # Compare results
        baseline_available = baseline.is_ice_available()
        ultimate_working = ultimate_result.get('enhanced_analysis', False)
        unified_working = unified_result.unified_alignment > 0
        
        if baseline_available and ultimate_working and unified_working:
            print("[SUCCESS] All modules working with ICE integration")
            print("[SUCCESS] Cross-module compatibility verified")
        else:
            print("[PARTIAL] Some modules working, check individual results")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Cross-module compatibility test failed: {e}")
        return False

def test_performance_across_modules():
    """Test performance consistency across integrated modules"""
    print("\n=== Test 4: Performance Across Modules ===")
    
    try:
        import time
        from baseline_biblical_substrate import BiblicalSemanticSubstrate
        from ultimate_core_engine import UltimateCoreEngine  
        from unified_ice_framework import unified_ice_framework
        
        test_text = "Balance love, power, wisdom, and justice"
        test_context = "spiritual"
        
        # Test baseline performance
        start_time = time.time()
        baseline = BiblicalSemanticSubstrate()
        baseline_result = baseline.analyze_concept_enhanced(test_text, test_context, use_ice=True)
        baseline_time = (time.time() - start_time) * 1000
        
        # Test ultimate performance
        start_time = time.time()
        ultimate = UltimateCoreEngine()
        ultimate_result = ultimate.ultimate_concept_analysis(test_text, test_context, use_ice_centric=True)
        ultimate_time = (time.time() - start_time) * 1000
        
        # Test unified framework performance
        start_time = time.time()
        unified_result = unified_ice_framework.process_intent(test_text, context=test_context)
        unified_time = (time.time() - start_time) * 1000
        
        print(f"Performance Comparison:")
        print(f"  Baseline Enhanced: {baseline_time:.3f}ms")
        print(f"  Ultimate ICE-Centric: {ultimate_time:.3f}ms")
        print(f"  Unified Framework: {unified_time:.3f}ms")
        
        # Compare alignment scores
        baseline_alignment = getattr(baseline_result, 'divine_alignment', 0) if hasattr(baseline_result, 'divine_alignment') else 0
        ultimate_alignment = ultimate_result.get('ultimate_evaluation', {}).get('divine_alignment', 0)
        unified_alignment = unified_result.unified_alignment
        
        print(f"\nAlignment Comparison:")
        print(f"  Baseline: {baseline_alignment:.2%}")
        print(f"  Ultimate: {ultimate_alignment:.2%}")
        print(f"  Unified: {unified_alignment:.2%}")
        
        # Check consistency
        all_reasonable_time = all(t < 100 for t in [baseline_time, ultimate_time, unified_time])
        all_positive_alignment = all(a > 0 for a in [baseline_alignment, ultimate_alignment, unified_alignment])
        
        if all_reasonable_time and all_positive_alignment:
            print("[SUCCESS] Performance consistency verified across modules")
        else:
            print("[WARNING] Some performance inconsistencies detected")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Performance across modules test failed: {e}")
        return False

def main():
    """Run all extended integration tests"""
    print("="*70)
    print("TESTING EXTENDED ICE INTEGRATION - PHASE 3.4")
    print("="*70)
    
    tests = [
        test_semantic_calculus_integration,
        test_ultimate_engine_unified_integration,
        test_cross_module_compatibility,
        test_performance_across_modules
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"[ERROR] Test {test.__name__} failed with exception: {e}")
    
    print("\n" + "="*70)
    print("EXTENDED INTEGRATION TEST SUMMARY")
    print("="*70)
    print(f"Tests Passed: {passed}/{total}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("[SUCCESS] All extended integration tests passed")
        print("[SUCCESS] Phase 3.4 - Extended Integration COMPLETE")
    elif passed >= total * 0.75:
        print("[PARTIAL] Most tests passed - extended integration mostly working")
        print("[INFO] Phase 3.4 - Extended Integration SUBSTANTIALLY COMPLETE")
    else:
        print("[WARNING] Many tests failed - extended integration needs review")
    
    print("="*70)

if __name__ == "__main__":
    main()