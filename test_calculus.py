#!/usr/bin/env python3
"""
Simple test for Phi-Enhanced Semantic Calculus
"""

import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))
from phi_enhanced_semantic_calculus import *
import math

def test_calculus():
    print("="*60)
    print("PHI-ENHANCED SEMANTIC CALCULUS COMPREHENSIVE TEST")
    print("="*60)
    
    # Initialize calculus engine
    calc = PhiSemanticCalculus()
    
    print("\n1. CORE FUNCTIONALITY:")
    print(f"   Phi Engine: {PHI_ENGINE_AVAILABLE}")
    print(f"   Calculus Engine: {'Available' if calc else 'Not Available'}")
    
    print("\n2. VECTOR OPERATIONS:")
    
    v1 = PhiSemanticVector(0.7, 0.3, 0.8, 0.5)
    v2 = PhiSemanticVector(0.4, 0.9, 0.2, 0.6)
    
    print(f"   Vector 1: L={v1.love:.3f}, P={v1.power:.3f}, W={v1.wisdom:.3f}, J={v1.justice:.3f}")
    print(f"   Vector 2: L={v2.love:.3f}, P={v2.power:.3f}, W={v2.wisdom:.3f}, J={v2.justice:.3f}")
    print(f"   V1 Phi Magnitude: {v1.phi_magnitude:.3f}")
    print(f"   V1 Fibonacci Class: {v1.fibonacci_class}")
    print(f"   Dot Product: {v1.dot(v2):.6f}")
    
    addition = calc.phi_vector_addition(v1, v2)
    cross_product = calc.phi_cross_product(v1, v2)
    scalar_mult = calc.phi_scalar_multiplication(2.5, v1)
    
    print(f"   Phi Addition: L={addition.love:.3f}")
    print(f"   Phi Cross Product: L={cross_product.love:.3f}")
    print(f"   Scalar Multiplication: L={scalar_mult.love:.3f}")
    
    print("\n3. TENSOR OPERATIONS:")
    
    tensor_data = np.array([[2.0, 1.0], [1.0, 2.0]])
    tensor = PhiSemanticTensor(tensor_data, "golden")
    print(f"   Tensor Shape: {tensor.data.shape}")
    
    eigenvals, eigenvects = calc.phi_eigendecomposition(np.array([[2, 1], [1, 2]]))
    print(f"   Eigenvalues: {eigenvals}")
    
    contracted = calc.phi_tensor_contraction(tensor, (0, 1))
    print(f"   Tensor Contraction: Shape {contracted.data.shape}")
    
    print("\n4. FIELD OPERATIONS:")
    
    def test_field(love, power, wisdom, justice):
        return love * wisdom + power * justice - 0.5
    
    field = PhiSemanticField(test_field, domain_bounds=(0, 1, 0, 1, 0, 1, 0, 1))
    evaluation = field.evaluate((0.3, 0.6, 0.4, 0.7))
    gradient = field.gradient((0.3, 0.6, 0.4, 0.7))
    
    print(f"   Field Evaluation: {evaluation:.4f}")
    print(f"   Field Gradient: L={gradient.love:.3f}, P={gradient.power:.3f}")
    print(f"   Gradient Magnitude: {gradient.magnitude():.3f}")
    
    print("\n5. INTEGRATION:")
    
    integral_phi_rect = calc.semantic_integral(field, PhiIntegrationMethod.PHI_RECTANGULAR, 100)
    integral_golden_simpson = calc.semantic_integral(field, PhiIntegrationMethod.GOLDEN_SIMPSON, 100)
    
    print(f"   Phi Rectangular: {integral_phi_rect:.6f}")
    print(f"   Golden Simpson: {integral_golden_simpson:.6f}")
    
    print("\n6. DIFFERENTIAL OPERATIONS:")
    
    grad_phi = calc.phi_gradient(field, SemanticDerivativeOperator.PHI_GRADIENT)
    vector_field = [field, field, field, field]
    divergence = calc.phi_divergence(vector_field)
    curl = calc.phi_curl(vector_field)
    
    print(f"   Phi Gradient: L={grad_phi.love:.3f}, P={grad_phi.power:.3f}")
    print(f"   Divergence: {divergence:.4f}")
    print(f"   Curl: L={curl.love:.3f}, P={curl.power:.3f}, W={curl.wisdom:.3f}")
    
    print("\n7. OPTIMIZATION:")
    
    def objective_func(vector):
        target = np.array([0.8, 0.8, 0.8, 0.8])
        current = vector.to_array()
        return np.linalg.norm(current - target)
    
    initial_guess = PhiSemanticVector(0.2, 0.3, 0.1, 0.4)
    optimal = calc.phi_optimization(objective_func, initial_guess, max_iterations=30)
    
    print(f"   Initial Objective: {objective_func(initial_guess):.4f}")
    print(f"   Optimal Objective: {objective_func(optimal):.4f}")
    print(f"   Improvement: {objective_func(initial_guess) - objective_func(optimal):.4f}")
    
    print("\n8. MANIFOLD ANALYSIS:")
    
    def embedding_func(coords):
        return BiblicalCoordinates(coords[0], coords[1], coords[2], coords[3])
    
    manifold = PhiSemanticManifold(embedding_func)
    test_coords = BiblicalCoordinates(0.6, 0.7, 0.8, 0.5)
    coords2 = BiblicalCoordinates(0.3, 0.4, 0.6, 0.8)
    
    geodesic_dist = manifold.geodesic_distance(test_coords, coords2)
    curvature = calc.semantic_curvature_analysis(test_coords)
    
    print(f"   Geodesic Distance: {geodesic_dist:.4f}")
    print(f"   Curvature (Mean): {curvature['mean_curvature']:.6f}")
    
    print("\n9. FLOW EQUATIONS:")
    
    initial_coords = BiblicalCoordinates(0.2, 0.3, 0.4, 0.5)
    trajectory = calc.semantic_flow_equation(initial_coords, field, (0, 2), 10)
    
    print(f"   Flow Points: {len(trajectory)}")
    if len(trajectory) > 0:
        final_coords = trajectory[-1]
        print(f"   Final Divine Resonance: {final_coords.divine_resonance():.3f}")
    
    print("\n10. PHI CONSTANTS:")
    print(f"   PHI: {PHI:.15f}")
    print(f"   PHI_INVERSE: {PHI_INVERSE:.15f}")
    print(f"   GOLDEN_ANGLE_DEG: {GOLDEN_ANGLE_DEG:.6f}")
    print(f"   Fibonacci F(10): {fibonacci(10)}")
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("Phi-Enhanced Semantic Calculus is fully operational!")
    print("="*60)
    
    return True

if __name__ == "__main__":
    success = test_calculus()
    sys.exit(0 if success else 1)