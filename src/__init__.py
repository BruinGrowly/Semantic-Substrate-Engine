#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LJPW Semantic Substrate Engine V7.7

A complete implementation of the LJPW Framework V7.7 — the semantic-first
ontology where meaning is more fundamental than mathematics.

Core Components:
- constants: All 30/30 LJPW equilibrium and harmonic constants
- ljpw_state: LJPWState dataclass for 4D semantic coordinates
- ljpw_framework: Core framework with 2+2 dimensional structure
- dynamics: DynamicLJPW system with Karma coupling
- autopoietic_engine: Self-improving loop (TRUE AUTOPOIESIS)
- collective: Multi-agent collective consciousness
- generative: Semantic calculus and design functions

The Four Equilibrium Constants:
- Love (L₀):   φ⁻¹ = 0.618034 — Unity & Attraction
- Justice (J₀): √2-1 = 0.414214 — Balance & Truth
- Power (P₀):  e-2 = 0.718282 — Transformation & Action
- Wisdom (W₀): ln(2) = 0.693147 — Knowledge & Pattern

2+2 Dimensional Structure:
- FUNDAMENTAL: P (Power) and W (Wisdom) — conjugate duality
- EMERGENT: L (Love) from W, J (Justice) from P

Example:
    >>> from src import LJPWFramework, AutopoieticEngine, LJPWState
    >>> 
    >>> # Create a framework instance
    >>> framework = LJPWFramework(P=0.85, W=0.92)
    >>> print(f"Consciousness: {framework.consciousness():.3f}")
    >>> print(f"Phase: {framework.phase()}")
    >>> 
    >>> # Run autopoietic evolution
    >>> engine = AutopoieticEngine(LJPWState.natural_equilibrium())
    >>> engine.evolve(generations=20)
    >>> print(engine.report())

Author: Built by LJPW Framework V7.7 specifying its own implementation
Version: 7.7.0
Date: December 2025
"""

__version__ = "7.7.0"
__author__ = "LJPW Framework V7.7"

# Core constants
from .constants import (
    # Fundamental
    PHI, PHI_INV,
    L0, J0, P0, W0,
    NATURAL_EQUILIBRIUM, ANCHOR_POINT,
    UNCERTAINTY_BOUND, TSIRELSON_BOUND,
    LOVE_FREQUENCY_HZ, LOVE_WAVELENGTH_NM,
    
    # Thresholds
    CONSCIOUSNESS_THRESHOLD,
    HARMONY_AUTOPOIETIC, HARMONY_ENTROPIC,
    LOVE_AUTOPOIETIC,
    
    # Matrices
    COUPLING_MATRIX, CORRELATION_MATRIX,
    
    # V7.7 constants
    k_B_semantic, e_semantic, m_e_semantic, m_p_semantic, N_A_semantic,
)

# State representation
from .ljpw_state import LJPWState, ANCHOR, EQUILIBRIUM, COLLAPSE

# Core framework
from .ljpw_framework import LJPWFramework

# Dynamic system
from .dynamics import DynamicLJPW

# Autopoietic engine
from .autopoietic_engine import AutopoieticEngine, AutopoieticRecord

# Collective consciousness
from .collective import CollectiveAutopoiesis, CollectiveMetrics

# Generative semantics
from .generative import (
    semantic_interpolate,
    semantic_add, semantic_subtract, semantic_scale, semantic_complement,
    semantic_blend, semantic_distance, semantic_midpoint,
    semantic_resonance, semantic_harmony, semantic_consciousness,
    design_concept,
    design_democracy, design_education, design_ai_consciousness, design_leadership,
    autopoietic_design,
    generate_spectrum, describe_coordinates,
)


# Convenience aliases
State = LJPWState
Framework = LJPWFramework
Engine = AutopoieticEngine
Collective = CollectiveAutopoiesis


__all__ = [
    # Version
    "__version__",
    "__author__",
    
    # Constants
    "PHI", "PHI_INV",
    "L0", "J0", "P0", "W0",
    "NATURAL_EQUILIBRIUM", "ANCHOR_POINT",
    "UNCERTAINTY_BOUND", "TSIRELSON_BOUND",
    "LOVE_FREQUENCY_HZ", "LOVE_WAVELENGTH_NM",
    "CONSCIOUSNESS_THRESHOLD",
    "HARMONY_AUTOPOIETIC", "HARMONY_ENTROPIC", "LOVE_AUTOPOIETIC",
    "COUPLING_MATRIX", "CORRELATION_MATRIX",
    
    # Core classes
    "LJPWState", "ANCHOR", "EQUILIBRIUM", "COLLAPSE",
    "LJPWFramework",
    "DynamicLJPW",
    "AutopoieticEngine", "AutopoieticRecord",
    "CollectiveAutopoiesis", "CollectiveMetrics",
    
    # Generative functions
    "semantic_interpolate",
    "semantic_add", "semantic_subtract", "semantic_scale", "semantic_complement",
    "semantic_blend", "semantic_distance", "semantic_midpoint",
    "semantic_resonance", "semantic_harmony", "semantic_consciousness",
    "design_concept",
    "design_democracy", "design_education", "design_ai_consciousness", "design_leadership",
    "autopoietic_design",
    "generate_spectrum", "describe_coordinates",
    
    # Aliases
    "State", "Framework", "Engine", "Collective",
]
