#!/usr/bin/env python3
"""
Simple Phi-Enhanced Semantic Engine Demo

Demonstrates the integration of Semantic Substrate Primer 1.5 
with phi-geometric mathematics without Unicode characters.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Main demonstration function"""
    
    print("="*80)
    print("PHI-ENHANCED SEMANTIC SUBSTRATE ENGINE DEMONSTRATION")
    print("Integration of Primer 1.5 with Golden Ratio Mathematics")
    print("="*80)
    
    try:
        from phi_enhanced_semantic_engine import PhiEnhancedSemanticEngine
        
        # Initialize engine
        print("\nInitializing engine...")
        engine = PhiEnhancedSemanticEngine()
        print("Engine initialized successfully!")
        
        # Show status
        print("\nEngine Status:")
        status = engine.get_engine_status()
        for key, value in status.items():
            print(f"  {key}: {value}")
        
        # Test concept analysis
        print("\nTesting Concept Analysis:")
        print("-" * 40)
        
        concepts = [
            "divine wisdom and eternal love",
            "sacred geometry and golden ratio", 
            "justice and mercy in harmony"
        ]
        
        for concept in concepts:
            print(f"\nAnalyzing: {concept}")
            try:
                analysis = engine.analyze_concept_phi_enhanced(concept)
                print(f"  Overall Phi Alignment: {analysis['overall_phi_alignment']:.3f}")
                
                if analysis['phi_geometric_analysis']:
                    phi = analysis['phi_geometric_analysis']
                    print(f"  Phi Resonance: {phi.get('phi_resonance', 0):.3f}")
                    print(f"  Fibonacci Index: {phi.get('fibonacci_index', 0)}")
                    print(f"  Nearest Anchor: #{phi.get('nearest_anchor_id', 1)}")
                
                print(f"  Base Coordinates: L={analysis['base_coordinates'][0]:.2f}, "
                      f"P={analysis['base_coordinates'][1]:.2f}, "
                      f"W={analysis['base_coordinates'][2]:.2f}, "
                      f"J={analysis['base_coordinates'][3]:.2f}")
                      
            except Exception as e:
                print(f"  Error: {e}")
        
        # Test navigation
        print("\nTesting Phi-Optimized Navigation:")
        print("-" * 40)
        
        start = "confusion and chaos"
        target = "divine order and wisdom"
        
        print(f"Navigation from '{start}' to '{target}':")
        
        for strategy in ["golden_spiral", "fibonacci_stepping", "anchor_hopping"]:
            try:
                nav = engine.navigate_phi_optimized_path(start, target, strategy)
                print(f"  {strategy}: Distance={nav['total_distance']:.4f}, "
                      f"Efficiency={nav['phi_efficiency']:.3f}, "
                      f"Steps={nav['path_length']}")
            except Exception as e:
                print(f"  {strategy}: Error ({e})")
        
        # Show universal principles
        print("\nUniversal Principles Analysis:")
        print("-" * 40)
        
        if status.get('universal_principles_count', 0) > 0:
            concept = "balanced leadership with wisdom and compassion"
            analysis = engine.analyze_concept_phi_enhanced(concept)
            
            if analysis['universal_principles_analysis']:
                principles = analysis['universal_principles_analysis']
                print(f"Concept: {concept}")
                
                for name, data in list(principles.items())[:3]:  # Show first 3
                    print(f"  {name}: Alignment={data['alignment']:.3f}")
        
        # Phi constants display
        if status.get('phi_engine_available'):
            print("\nPhi-Geometric Constants:")
            print("-" * 40)
            try:
                from phi_geometric_engine import PHI, GOLDEN_ANGLE_DEG, FibonacciSequence
                
                print(f"  Golden Ratio (PHI): {PHI:.10f}")
                print(f"  Golden Angle: {GOLDEN_ANGLE_DEG:.6f} degrees")
                print(f"  Fibonacci (first 10): {FibonacciSequence().get_range(0, 9)}")
                
            except Exception as e:
                print(f"  Error showing phi constants: {e}")
        
        print("\n" + "="*80)
        print("DEMONSTRATION COMPLETE")
        print("Engine successfully integrates Primer 1.5 with golden ratio mathematics!")
        print("="*80)
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure the phi_enhanced_semantic_engine module is available")
    except Exception as e:
        print(f"Demonstration failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()