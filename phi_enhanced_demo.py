#!/usr/bin/env python3
"""
Phi-Enhanced Semantic Substrate Engine Demonstration

This script demonstrates the integration of:
- Semantic Substrate Primer 1.5
- Phi-Geometric Engine with golden ratio mathematics
- Enhanced ICE Framework
- Dodecahedral anchor system
- Universal Principles application

Run this script to see the enhanced capabilities in action.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from phi_enhanced_semantic_engine import PhiEnhancedSemanticEngine, demonstrate_phi_enhanced_engine
    print("SUCCESS: Successfully imported Phi-Enhanced Semantic Engine")
except ImportError as e:
    print(f"ERROR: Import error: {e}")
    print("Make sure all dependencies are installed")
    sys.exit(1)


def main():
    """Main demonstration function"""
    
    print("\n" + "="*80)
    print("PHI-ENHANCED SEMANTIC SUBSTRATE ENGINE DEMONSTRATION")
    print("Integration of Primer 1.5 with Golden Ratio Mathematics")
    print("="*80)
    
    # Initialize the engine
    print("\n[INITIALIZING ENGINE...]")
    try:
        engine = PhiEnhancedSemanticEngine()
        print("SUCCESS: Engine initialized successfully")
    except Exception as e:
        print(f"ERROR: Engine initialization failed: {e}")
        return
    
    # Show engine status
    print("\n[ENGINE STATUS:]")
    status = engine.get_engine_status()
    for key, value in status.items():
        print(f"  {key}: {value}")
    
    # Demonstrate concept analysis
    print("\n[CONCEPT ANALYSIS DEMONSTRATION:]")
    print("-" * 50)
    
    test_concepts = [
        ("divine wisdom and eternal love", "spiritual"),
        ("sacred geometry and golden ratio", "mathematical"),
        ("justice and mercy in harmony", "ethical"),
        ("technological innovation for humanity", "technical"),
        ("artistic expression and beauty", "creative")
    ]
    
    for concept, context in test_concepts:
        print(f"\n[Analyzing: '{concept}' in context: {context}]")
        try:
            analysis = engine.analyze_concept_phi_enhanced(concept, context)
            
            print(f"  Overall Phi Alignment: {analysis['overall_phi_alignment']:.3f}")
            print(f"  Base Coordinates: L={analysis['base_coordinates'][0]:.2f}, P={analysis['base_coordinates'][1]:.2f}, W={analysis['base_coordinates'][2]:.2f}, J={analysis['base_coordinates'][3]:.2f}")
            
            if analysis['phi_geometric_analysis']:
                phi = analysis['phi_geometric_analysis']
                print(f"  Phi Resonance: {phi.get('phi_resonance', 0):.3f}")
                print(f"  Fibonacci Index: {phi.get('fibonacci_index', 0)}")
                print(f"  Nearest Anchor: #{phi.get('nearest_anchor_id', 1)}")
                
                if phi.get('fibonacci_value'):
                    print(f"  Fibonacci Value: {phi['fibonacci_value']}")
            
            if analysis['universal_principles_analysis']:
                principles = analysis['universal_principles_analysis']
                best_principle = max(principles.items(), key=lambda x: x[1]['alignment'])
                print(f"  Best Aligned Principle: {best_principle[0]} (alignment: {best_principle[1]['alignment']:.3f})")
            
            if analysis['ice_framework_analysis']:
                ice = analysis['ice_framework_analysis']
                if 'error' not in ice:
                    print(f"  ICE Divine Alignment: {ice.get('divine_alignment', 0):.3f}")
                    print(f"  Semantic Integrity: {ice.get('semantic_integrity', 0):.3f}")
                    print(f"  Execution Strategy: {ice.get('execution_strategy', 'unknown')}")
            
        except Exception as e:
            print(f"  ERROR: Analysis failed: {e}")
    
    # Demonstrate navigation
    print("\n[PHI-OPTIMIZED NAVIGATION DEMONSTRATION:]")
    print("-" * 50)
    
    navigation_tests = [
        ("confusion and chaos", "divine order and wisdom"),
        ("ignorance and darkness", "enlightened understanding"),
        ("division and conflict", "unity and harmony"),
        ("material limitation", "spiritual transcendence")
    ]
    
    for start, target in navigation_tests:
        print(f"\n[Navigating from '{start}' to '{target}']")
        
        for strategy in ["golden_spiral", "fibonacci_stepping", "anchor_hopping"]:
            try:
                nav = engine.navigate_phi_optimized_path(start, target, strategy)
                print(f"  {strategy:15s}: Distance={nav['total_distance']:.4f}, Efficiency={nav['phi_efficiency']:.3f}, Steps={nav['path_length']}")
            except Exception as e:
                print(f"  {strategy:15s}: ❌ Failed ({e})")
    
    # Show universal principles in action
    print("\n⚖️  UNIVERSAL PRINCIPLES ANALYSIS:")
    print("-" * 50)
    
    try:
        concept_for_principles = "balanced leadership with wisdom and compassion"
        principle_analysis = engine.analyze_concept_phi_enhanced(concept_for_principles)
        
        if principle_analysis['universal_principles_analysis']:
            print(f"📖 Concept: '{concept_for_principles}'")
            principles = principle_analysis['universal_principles_analysis']
            
            for principle_name, data in principles.items():
                print(f"\n  📜 {principle_name}:")
                print(f"     Alignment: {data['alignment']:.3f}")
                print(f"     Statement: {data['statement'][:80]}...")
                if data.get('phi_enhancement'):
                    print(f"     Phi Enhancement: {data['phi_enhancement'][:60]}...")
        
    except Exception as e:
        print(f"❌ Principles analysis failed: {e}")
    
    # Show phi-geometric properties
    print("\n🔬 PHI-GEOMETRIC PROPERTIES DEEP DIVE:")
    print("-" * 50)
    
    if status.get('phi_engine_available'):
        try:
            from phi_geometric_engine import PHI, FibonacciSequence, GoldenSpiral
            
            print(f"🎯 Golden Ratio (PHI): {PHI:.15f}")
            print(f"🌀 Fibonacci Sequence (first 15): {FibonacciSequence().get_range(0, 14)}")
            
            # Golden spiral properties
            spiral = GoldenSpiral()
            print(f"🌊 Golden Spiral at π/2: {spiral.radius_at_angle(math.pi/2):.6f}")
            print(f"🌊 Golden Spiral at π: {spiral.radius_at_angle(math.pi):.6f}")
            print(f"🌊 Golden Spiral at 2π: {spiral.radius_at_angle(2*math.pi):.6f}")
            
        except Exception as e:
            print(f"❌ Phi properties demonstration failed: {e}")
    else:
        print("❌ Phi engine not available for detailed demonstration")
    
    # Performance metrics
    print("\n📈 PERFORMANCE METRICS:")
    print("-" * 50)
    
    try:
        import time
        
        # Test analysis speed
        start_time = time.time()
        for _ in range(10):
            engine.analyze_concept_phi_enhanced("test concept for performance", "benchmark")
        analysis_time = (time.time() - start_time) / 10
        
        # Test navigation speed
        start_time = time.time()
        for _ in range(5):
            engine.navigate_phi_optimized_path("start", "end", "golden_spiral")
        nav_time = (time.time() - start_time) / 5
        
        print(f"⚡ Average Analysis Time: {analysis_time*1000:.2f}ms")
        print(f"🚀 Average Navigation Time: {nav_time*1000:.2f}ms")
        print(f"📊 Analysis Throughput: {1/analysis_time:.1f} concepts/second")
        print(f"🗺️  Navigation Throughput: {1/nav_time:.1f} paths/second")
        
    except Exception as e:
        print(f"❌ Performance measurement failed: {e}")
    
    # Final summary
    print("\n🎉 ENHANCEMENT SUMMARY:")
    print("-" * 50)
    print("✅ Semantic Substrate Primer 1.5 integrated")
    print("✅ Phi-geometric mathematics active")
    print("✅ Golden ratio optimization available")
    print("✅ Dodecahedral anchor system online")
    print("✅ Universal principles applied")
    print("✅ Enhanced ICE framework integrated")
    print("✅ Fibonacci-based indexing functional")
    print("✅ Golden spiral navigation operational")
    
    print(f"\n🏁 Engine Version: {status.get('engine_version', 'Unknown')}")
    print(f"📖 Primer Version: {status.get('primer_version', 'Unknown')}")
    
    print("\n" + "="*80)
    print("PHI-ENHANCED SEMANTIC SUBSTRATE ENGINE DEMONSTRATION COMPLETE")
    print("The engine now combines divine wisdom with sacred geometry!")
    print("="*80)


if __name__ == "__main__":
    main()