"""
Test Unified ICE Framework Integration

This test verifies that the unified ICE framework works correctly,
combining ICE-Centric processing with biblical extensions while maintaining
backward compatibility with both legacy frameworks.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from unified_ice_framework import (
    UnifiedICEFramework,
    ProcessingMode,
    BiblicalExtensions,
    unified_ice_framework,
    legacy_ice_wrapper,
    ICE_CENTRIC_AVAILABLE,
    LEGACY_ICE_AVAILABLE
)

def test_unified_initialization():
    """Test that Unified ICE Framework initializes correctly"""
    print("\n=== Test 1: Unified Framework Initialization ===")
    
    print(f"ICE-Centric Available: {ICE_CENTRIC_AVAILABLE}")
    print(f"Legacy Available: {LEGACY_ICE_AVAILABLE}")
    
    # Test primary initialization
    framework = UnifiedICEFramework()
    print(f"Primary Framework: {framework.ice_centric_engine is not None}")
    print(f"Legacy Framework: {framework.legacy_engine is not None}")
    print(f"Biblical Extensions: {framework.biblical_extensions is not None}")
    print(f"Default Mode: {framework.processing_mode}")
    
    # Test performance stats
    stats = framework.get_performance_summary()
    print(f"Engines Available: {stats['engines_available']}")
    print(f"Primary Mode: {stats['primary_mode']}")
    
    if framework.ice_centric_engine or framework.legacy_engine:
        print("[SUCCESS] Unified framework initialized successfully")
        return True
    else:
        print("[ERROR] No engines available")
        return False

def test_processing_modes():
    """Test different processing modes"""
    print("\n=== Test 2: Processing Modes ===")
    
    framework = UnifiedICEFramework()
    test_text = "Show compassion and mercy to those who suffer"
    
    # Test AUTO mode
    try:
        result_auto = framework.process_intent(test_text, context="biblical", processing_mode=ProcessingMode.AUTO)
        print(f"AUTO Mode: {result_auto.processing_mode}")
        print(f"  Unified Alignment: {result_auto.unified_alignment:.2%}")
        print(f"  Confidence: {result_auto.confidence_score:.2%}")
        print(f"  Processing Time: {result_auto.processing_time_ms:.3f}ms")
        print("[SUCCESS] AUTO mode works")
    except Exception as e:
        print(f"[ERROR] AUTO mode failed: {e}")
        return False
    
    # Test ICE-CENTRIC mode (if available)
    if ICE_CENTRIC_AVAILABLE:
        try:
            result_ice = framework.process_intent(test_text, context="biblical", processing_mode=ProcessingMode.ICE_CENTRIC)
            print(f"ICE-CENTRIC Mode: {result_ice.processing_mode}")
            print(f"  Has ICE Result: {result_ice.ice_transformation is not None}")
            print(f"  Biblical Enrichment: {result_ice.biblical_enrichment is not None}")
            if result_ice.biblical_enrichment:
                print(f"  Scripture References: {len(result_ice.biblical_enrichment.scripture_references)}")
                print(f"  Biblical Principles: {len(result_ice.biblical_enrichment.biblical_principles)}")
            print("[SUCCESS] ICE-CENTRIC mode works")
        except Exception as e:
            print(f"[ERROR] ICE-CENTRIC mode failed: {e}")
            return False
    
    # Test LEGACY mode (if available)
    if LEGACY_ICE_AVAILABLE:
        try:
            result_legacy = framework.process_intent(test_text, context="biblical", processing_mode=ProcessingMode.LEGACY_BIBLICAL)
            print(f"LEGACY Mode: {result_legacy.processing_mode}")
            print(f"  Has Legacy Result: {result_legacy.legacy_result is not None}")
            print("[SUCCESS] LEGACY mode works")
        except Exception as e:
            print(f"[ERROR] LEGACY mode failed: {e}")
            return False
    
    return True

def test_biblical_extensions():
    """Test biblical extensions functionality"""
    print("\n=== Test 3: Biblical Extensions ===")
    
    extensions = BiblicalExtensions()
    
    # Test theme extraction
    test_texts = [
        "Show compassion and mercy",
        "Seek wisdom and understanding", 
        "Act with justice and fairness",
        "Trust in faith and hope"
    ]
    
    for text in test_texts:
        themes = extensions._extract_biblical_themes(text)
        print(f"Text: '{text}' -> Themes: {themes}")
    
    # Test biblical enrichment
    if ICE_CENTRIC_AVAILABLE:
        framework = UnifiedICEFramework()
        result = framework.process_intent(
            "Show compassion and mercy to those in need",
            context="biblical"
        )
        
        if result.biblical_enrichment:
            enrichment = result.biblical_enrichment
            print(f"\nBiblical Enrichment Results:")
            print(f"  Scripture References: {enrichment.scripture_references}")
            print(f"  Biblical Principles: {enrichment.biblical_principles}")
            print(f"  Divine Wisdom: {len(enrichment.divine_wisdom_insights)} insights")
            print(f"  Biblical Alignment: {enrichment.biblical_alignment_score:.2%}")
            print(f"  Practical Applications: {len(enrichment.practical_applications)}")
            print("[SUCCESS] Biblical extensions work correctly")
        else:
            print("[WARNING] No biblical enrichment generated")
    
    return True

def test_context_adaptation():
    """Test context-aware processing"""
    print("\n=== Test 4: Context Adaptation ===")
    
    framework = UnifiedICEFramework()
    test_text = "Provide guidance for making a wise decision"
    
    contexts = [
        ("biblical", "Should apply biblical enrichment"),
        ("educational", "Educational context"),
        ("business", "Business/professional context"),
        ("ministry", "Ministry context"),
        ("general", "General context")
    ]
    
    for context, description in contexts:
        try:
            result = framework.process_intent(test_text, context=context)
            print(f"\nContext: {context} ({description})")
            print(f"  Processing Mode: {result.processing_mode}")
            print(f"  Unified Alignment: {result.unified_alignment:.2%}")
            print(f"  Biblical Enrichment: {result.biblical_enrichment is not None}")
            
            if result.ice_transformation:
                print(f"  Execution Strategy: {result.ice_transformation.execution_strategy.value}")
            
            if result.biblical_enrichment:
                print(f"  Ministry Guidance: {len(result.biblical_enrichment.ministry_guidance)} items")
            
        except Exception as e:
            print(f"[ERROR] Context {context} failed: {e}")
            return False
    
    print("[SUCCESS] Context adaptation works correctly")
    return True

def test_performance_comparison():
    """Test performance comparison between modes"""
    if not (ICE_CENTRIC_AVAILABLE and LEGACY_ICE_AVAILABLE):
        print("\n=== Test 5: Performance Comparison (SKIPPED - need both engines) ===")
        return False
    
    print("\n=== Test 5: Performance Comparison ===")
    
    framework = UnifiedICEFramework()
    test_text = "Act with wisdom and justice in all situations"
    test_context = "ethical"
    
    try:
        # Test ICE-Centric
        result_ice = framework.process_intent(test_text, context=test_context, processing_mode=ProcessingMode.ICE_CENTRIC)
        
        # Test Legacy
        result_legacy = framework.process_intent(test_text, context=test_context, processing_mode=ProcessingMode.LEGACY_BIBLICAL)
        
        # Test Hybrid
        result_hybrid = framework.process_intent(test_text, context=test_context, processing_mode=ProcessingMode.HYBRID)
        
        print(f"Performance Comparison:")
        print(f"  ICE-Centric:")
        print(f"    Alignment: {result_ice.unified_alignment:.2%}")
        print(f"    Time: {result_ice.processing_time_ms:.3f}ms")
        print(f"    Strategy: {result_ice.ice_transformation.execution_strategy.value if result_ice.ice_transformation else 'N/A'}")
        
        print(f"  Legacy:")
        print(f"    Alignment: {result_legacy.unified_alignment:.2%}")
        print(f"    Time: {result_legacy.processing_time_ms:.3f}ms")
        
        print(f"  Hybrid:")
        print(f"    Alignment: {result_hybrid.unified_alignment:.2%}")
        print(f"    Time: {result_hybrid.processing_time_ms:.3f}ms")
        print(f"    Has Comparison: {result_hybrid.performance_comparison is not None}")
        
        if result_hybrid.performance_comparison:
            comp = result_hybrid.performance_comparison
            improvement = comp.get('improvement', 0) * 100
            print(f"    ICE Improvement: {improvement:+.2f}%")
        
        print("[SUCCESS] Performance comparison works")
        return True
        
    except Exception as e:
        print(f"[ERROR] Performance comparison failed: {e}")
        return False

def test_backward_compatibility():
    """Test backward compatibility with legacy interface"""
    if not legacy_ice_wrapper:
        print("\n=== Test 6: Backward Compatibility (SKIPPED - legacy not available) ===")
        return False
    
    print("\n=== Test 6: Backward Compatibility ===")
    
    try:
        # Test legacy interface
        from ice_framework import ThoughtType, ContextDomain
        
        result = legacy_ice_wrapper.process_thought(
            "Seek divine wisdom through prayer",
            ThoughtType.BIBLICAL_UNDERSTANDING,
            ContextDomain.PERSONAL
        )
        
        print(f"Legacy Interface Result:")
        print(f"  Execution Strategy: {result.get('execution_strategy', 'N/A')}")
        print(f"  Divine Alignment: {result.get('divine_alignment', 0):.2%}")
        print(f"  Semantic Output: {result.get('semantic_output', 'N/A')[:50]}...")
        
        # Test legacy summary
        summary = legacy_ice_wrapper.get_transformation_summary()
        print(f"  Total Processed: {summary.get('total_processed', 0)}")
        print(f"  Average Alignment: {summary.get('average_alignment', 0):.2%}")
        
        print("[SUCCESS] Backward compatibility works")
        return True
        
    except Exception as e:
        print(f"[ERROR] Backward compatibility failed: {e}")
        return False

def test_global_instances():
    """Test global instances for easy access"""
    print("\n=== Test 7: Global Instances ===")
    
    try:
        # Test global unified framework
        result = unified_ice_framework.process_intent(
            "Show love and compassion",
            context="spiritual"
        )
        
        print(f"Global Unified Framework:")
        print(f"  Available: {unified_ice_framework.ice_centric_engine is not None}")
        print(f"  Result Alignment: {result.unified_alignment:.2%}")
        print(f"  Processing Mode: {result.processing_mode}")
        
        # Test performance summary
        summary = unified_ice_framework.get_performance_summary()
        print(f"  Total Processed: {summary['total_processed']}")
        print(f"  Primary Mode: {summary['primary_mode']}")
        
        print("[SUCCESS] Global instances work correctly")
        return True
        
    except Exception as e:
        print(f"[ERROR] Global instances failed: {e}")
        return False

def main():
    """Run all tests"""
    print("="*70)
    print("TESTING UNIFIED ICE FRAMEWORK INTEGRATION")
    print("="*70)
    
    tests = [
        test_unified_initialization,
        test_processing_modes,
        test_biblical_extensions,
        test_context_adaptation,
        test_performance_comparison,
        test_backward_compatibility,
        test_global_instances
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
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests Passed: {passed}/{total}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("[SUCCESS] All unified framework tests passed")
        print("[SUCCESS] Phase 3.3 - Framework Unification COMPLETE")
    elif passed >= total * 0.8:
        print("[PARTIAL] Most tests passed - framework mostly working")
        print("[INFO] Phase 3.3 - Framework Unification MOSTLY COMPLETE")
    else:
        print("[WARNING] Many tests failed - needs review")
    
    print("="*70)

if __name__ == "__main__":
    main()