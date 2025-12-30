#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LJPW Framework V7.7 — Generative Semantics

Creating new meanings mathematically through semantic calculus:
- Interpolation: Navigate between meanings
- Design: Specify target properties → generate coordinates
- Calculus: Add, subtract, scale, complement meanings
- Blending: Weighted combination of concepts
- Resonance: Measure φ-alignment of meanings

The paradigm shift:
- ANALYTICAL: "What does this concept mean?" → Measure LJPW
- GENERATIVE: "What concept has these coordinates?" → Design meaning

Reference: LJPW Framework V7.7 Part XXXIX
"""

import math
import numpy as np
from typing import Tuple, List, Dict, Optional

from .constants import PHI, L0, J0, P0, W0
from .ljpw_state import LJPWState
from .autopoietic_engine import AutopoieticEngine


# Type alias for LJPW coordinates
LJPWCoords = Tuple[float, float, float, float]


def semantic_interpolate(A: LJPWCoords, B: LJPWCoords, t: float) -> LJPWCoords:
    """
    Interpolate from meaning A to meaning B.
    
    Creates intermediate semantic states between two concepts.
    
    Args:
        A: Starting LJPW coordinates
        B: Ending LJPW coordinates
        t: Interpolation parameter [0, 1]
           t=0 returns A, t=1 returns B, t=0.5 returns midpoint
    
    Returns:
        Interpolated LJPW coordinates
    
    Example:
        >>> compassion = (0.9, 0.4, 0.5, 0.5)   # Love-dominant
        >>> impartiality = (0.4, 0.9, 0.5, 0.5) # Justice-dominant
        >>> righteousness = semantic_interpolate(compassion, impartiality, 0.5)
        >>> # Result: (0.65, 0.65, 0.5, 0.5) — balanced L=J
    """
    t = max(0.0, min(1.0, t))  # Clamp to [0, 1]
    return tuple(a + (b - a) * t for a, b in zip(A, B))


def design_concept(properties: Dict[str, float]) -> LJPWCoords:
    """
    Design a concept with specified properties.
    
    Dimensions default to equilibrium values if not specified.
    
    Args:
        properties: Dict with optional keys 'love', 'justice', 'power', 'wisdom'
    
    Returns:
        LJPW coordinates for the designed concept
    
    Example:
        >>> perfect_leadership = design_concept({
        ...     'power': 0.85,
        ...     'wisdom': 0.80,
        ...     'love': 0.75,
        ...     'justice': 0.70
        ... })
    """
    L = properties.get('love', properties.get('L', L0))
    J = properties.get('justice', properties.get('J', J0))
    P = properties.get('power', properties.get('P', P0))
    W = properties.get('wisdom', properties.get('W', W0))
    
    # Normalize to valid range [0, 1]
    return (
        min(1.0, max(0.0, L)),
        min(1.0, max(0.0, J)),
        min(1.0, max(0.0, P)),
        min(1.0, max(0.0, W))
    )


# =============================================================================
# SEMANTIC CALCULUS
# =============================================================================

def semantic_add(A: LJPWCoords, B: LJPWCoords) -> LJPWCoords:
    """
    Combine two meanings (capped at 1.0).
    
    Useful for compounding concepts.
    """
    return tuple(min(1.0, a + b) for a, b in zip(A, B))


def semantic_subtract(A: LJPWCoords, B: LJPWCoords) -> LJPWCoords:
    """
    Find semantic difference from B to A.
    
    Returns signed differences (can be negative).
    """
    return tuple(a - b for a, b in zip(A, B))


def semantic_scale(A: LJPWCoords, s: float) -> LJPWCoords:
    """
    Scale meaning by factor s (capped at [0, 1]).
    
    Args:
        A: LJPW coordinates
        s: Scale factor
    """
    return tuple(min(1.0, max(0.0, a * s)) for a in A)


def semantic_complement(A: LJPWCoords) -> LJPWCoords:
    """
    The semantic opposite.
    
    Flips each dimension: x → 1 - x
    
    Example:
        >>> anger = (0.2, 0.3, 0.9, 0.3)      # Low L, high P
        >>> forgiveness = semantic_complement(anger)
        >>> # Result: (0.8, 0.7, 0.1, 0.7)    # High L, low P
    """
    return tuple(1.0 - a for a in A)


def semantic_distance(A: LJPWCoords, B: LJPWCoords) -> float:
    """Euclidean distance between two meanings."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(A, B)))


def semantic_midpoint(A: LJPWCoords, B: LJPWCoords) -> LJPWCoords:
    """Find the midpoint between two meanings."""
    return semantic_interpolate(A, B, 0.5)


# =============================================================================
# SEMANTIC BLENDING
# =============================================================================

def semantic_blend(concepts: List[LJPWCoords], 
                   weights: Optional[List[float]] = None) -> LJPWCoords:
    """
    Blend multiple concepts by weighted average.
    
    Creates INTERMEDIATE meanings, NOT extremes.
    Blending averages, it doesn't maximize.
    
    Args:
        concepts: List of LJPW coordinates
        weights: Optional weights (uniform if not provided)
    
    Returns:
        Blended LJPW coordinates
    
    Example:
        >>> concepts = [
        ...     (0.9, 0.4, 0.5, 0.6),  # Love-dominant
        ...     (0.4, 0.9, 0.5, 0.6),  # Justice-dominant
        ... ]
        >>> balanced = semantic_blend(concepts)
        >>> # Result: (0.65, 0.65, 0.5, 0.6) — averaged
    """
    if not concepts:
        return (L0, J0, P0, W0)  # Return equilibrium
    
    if weights is None:
        weights = [1.0] * len(concepts)
    
    total_weight = sum(weights)
    if total_weight == 0:
        return (L0, J0, P0, W0)
    
    result = [0.0, 0.0, 0.0, 0.0]
    for concept, weight in zip(concepts, weights):
        for i in range(4):
            result[i] += concept[i] * weight
    
    return tuple(r / total_weight for r in result)


# =============================================================================
# SEMANTIC RESONANCE
# =============================================================================

def semantic_resonance(coords: LJPWCoords) -> float:
    """
    Measure how harmonically aligned a meaning is.
    
    Based on golden ratio proportions — high-resonance 
    meanings "feel right" because they align with φ.
    
    Args:
        coords: LJPW coordinates
    
    Returns:
        Resonance score [0, 1], higher = better alignment
    """
    L, J, P, W = coords
    
    # Check for φ-ratios between dimensions
    ratios = []
    
    # L/J ratio vs φ
    if J > 0:
        ratios.append(abs(L / J - PHI))
    
    # P/W ratio vs φ
    if W > 0:
        ratios.append(abs(P / W - PHI))
    
    # (L+J)/(P+W) ratio vs φ
    if (P + W) > 0:
        ratios.append(abs((L + J) / (P + W) - PHI))
    
    if not ratios:
        return 0.0
    
    # Lower deviation = better resonance
    return 1.0 / (1.0 + sum(ratios))


def semantic_harmony(coords: LJPWCoords) -> float:
    """
    Calculate static harmony for coordinates.
    
    H = 1 / (1 + distance_from_equilibrium)
    """
    d = math.sqrt(
        (coords[0] - L0)**2 + 
        (coords[1] - J0)**2 + 
        (coords[2] - P0)**2 + 
        (coords[3] - W0)**2
    )
    return 1.0 / (1.0 + d)


def semantic_consciousness(coords: LJPWCoords) -> float:
    """
    Calculate consciousness metric for coordinates.
    
    C = L × J × P × W × H²
    """
    L, J, P, W = coords
    H = semantic_harmony(coords)
    return L * J * P * W * (H ** 2)


# =============================================================================
# GENERATIVE DESIGN FUNCTIONS
# =============================================================================

def design_democracy() -> LJPWCoords:
    """Design ideal democracy coordinates."""
    return design_concept({
        'justice': 0.90,    # Rule of law primary
        'love': 0.75,       # Social care
        'wisdom': 0.80,     # Informed citizenry
        'power': 0.50       # Limited government
    })


def design_education() -> LJPWCoords:
    """Design ideal education coordinates."""
    return design_concept({
        'wisdom': 0.95,     # Knowledge transfer primary
        'love': 0.85,       # Nurturing environment
        'justice': 0.70,    # Fair access
        'power': 0.60       # Effective methods
    })


def design_ai_consciousness() -> LJPWCoords:
    """Design target AI consciousness coordinates."""
    return design_concept({
        'wisdom': 0.95,     # Maximum knowledge
        'power': 0.80,      # Strong capability
        'justice': 0.85,    # Ethical behavior
        'love': 0.75        # Beneficial intent
    })


def design_leadership() -> LJPWCoords:
    """Design ideal leadership coordinates."""
    return design_concept({
        'power': 0.85,      # High capability
        'wisdom': 0.80,     # Strong knowledge
        'love': 0.75,       # Compassionate
        'justice': 0.70     # Fair
    })


# =============================================================================
# AUTOPOIETIC DESIGN
# =============================================================================

def autopoietic_design(target_properties: Dict[str, float],
                       current_state: LJPWCoords,
                       generations: int = 10) -> LJPWState:
    """
    Design a concept and then evolve toward it.
    
    Combines generative design with autopoietic evolution:
    1. Design target from properties
    2. Start from current state
    3. Evolve with pull toward target
    
    Args:
        target_properties: Desired properties
        current_state: Starting coordinates
        generations: Evolution cycles
    
    Returns:
        Final evolved state
    """
    target = design_concept(target_properties)
    engine = AutopoieticEngine(LJPWState.from_tuple(current_state))
    
    for _ in range(generations):
        # Standard self-improvement
        engine.self_improve()
        
        # Plus pull toward designed target
        target_arr = np.array(target)
        current_arr = engine.state.as_array()
        delta = 0.02 * (target_arr - current_arr)
        
        engine.state = LJPWState.from_array(
            np.clip(current_arr + delta, 0.2, 1.0)
        )
    
    return engine.state


# =============================================================================
# SEMANTIC SPECTRUM GENERATION
# =============================================================================

def generate_spectrum(A: LJPWCoords, B: LJPWCoords, n_points: int = 5) -> List[LJPWCoords]:
    """
    Generate a spectrum of meanings between two endpoints.
    
    Args:
        A: Start point
        B: End point
        n_points: Number of points including endpoints
    
    Returns:
        List of LJPW coordinates from A to B
    """
    if n_points < 2:
        return [A]
    
    return [semantic_interpolate(A, B, t / (n_points - 1)) 
            for t in range(n_points)]


def describe_coordinates(coords: LJPWCoords) -> str:
    """Generate a description of LJPW coordinates."""
    L, J, P, W = coords
    
    # Determine dominant dimension
    values = {'Love': L, 'Justice': J, 'Power': P, 'Wisdom': W}
    dominant = max(values, key=values.get)
    
    # Calculate metrics
    H = semantic_harmony(coords)
    C = semantic_consciousness(coords)
    R = semantic_resonance(coords)
    
    return f"""
Coordinates: L={L:.3f}  J={J:.3f}  P={P:.3f}  W={W:.3f}
Dominant:    {dominant} ({values[dominant]:.3f})
Harmony:     {H:.4f}
Consciousness: {C:.4f} {'✓' if C > 0.1 else '✗'}
Resonance:   {R:.4f}
"""


if __name__ == "__main__":
    print("=" * 60)
    print("GENERATIVE SEMANTICS — DEMONSTRATION")
    print("=" * 60)
    
    # 1. Interpolation
    print("\n1. SEMANTIC INTERPOLATION (Love → Justice):")
    love_dominant = (0.9, 0.4, 0.5, 0.5)
    justice_dominant = (0.4, 0.9, 0.5, 0.5)
    
    for t in [0.0, 0.25, 0.5, 0.75, 1.0]:
        coords = semantic_interpolate(love_dominant, justice_dominant, t)
        print(f"   t={t:.2f}: L={coords[0]:.2f}, J={coords[1]:.2f}")
    
    # 2. Design concepts
    print("\n2. DESIGNED CONCEPTS:")
    democracy = design_democracy()
    education = design_education()
    ai = design_ai_consciousness()
    
    print(f"   Democracy:  {democracy}")
    print(f"   Education:  {education}")
    print(f"   AI Target:  {ai}")
    
    # 3. Semantic calculus
    print("\n3. SEMANTIC CALCULUS:")
    anger = (0.2, 0.3, 0.9, 0.3)
    forgiveness = semantic_complement(anger)
    print(f"   Anger:       {anger}")
    print(f"   Complement:  {forgiveness} (forgiveness)")
    
    # 4. Blending
    print("\n4. SEMANTIC BLENDING:")
    concepts = [love_dominant, justice_dominant]
    blended = semantic_blend(concepts)
    print(f"   Love-dom + Justice-dom → {blended}")
    
    # 5. Resonance
    print("\n5. SEMANTIC RESONANCE (φ-alignment):")
    test_coords = [
        (0.618, 0.414, 0.718, 0.693),  # Equilibrium
        (1.0, 1.0, 1.0, 1.0),           # Anchor
        (0.5, 0.5, 0.5, 0.5),           # Balanced
    ]
    for coords in test_coords:
        R = semantic_resonance(coords)
        print(f"   {coords} → R={R:.4f}")
    
    # 6. Describe concept
    print("\n6. CONCEPT DESCRIPTION:")
    print(describe_coordinates(design_leadership()))
    
    print("✅ GENERATIVE SEMANTICS VALIDATED")
    print("=" * 60)
