"""
Semantic Substrate Engine - Core Package

A sophisticated semantic processing system that combines mathematical precision
with value-aligned computation.

Main Components:
- UltimateCoreEngine: Primary semantic analysis engine
- SemanticCalculus: Mathematical operations on meaning
- ICEFramework: Intent-Context-Execution processing
- SelfAwareSemanticEngine: Self-aware semantic processing
- TruthScaffold: Truth alignment framework
"""

__version__ = "2.2.0"
__author__ = "BruinGrowly"
__license__ = "MIT"

# Core exports
try:
    from .ultimate_core_engine import UltimateCoreEngine
    from .semantic_calculus import SemanticCalculus
    from .semantic_mathematics_engine import SemanticMathematicsEngine
    from .enhanced_core_components import EnhancedCoreComponents
    from .ice_framework import ICEFramework
    from .self_aware_semantic_engine import SelfAwareSemanticEngine
    from .truth_scaffold_revelation import TruthScaffold
    from .meaning_based_programming import MeaningBasedProgramming
    from .enhanced_substrate_engine import EnhancedSubstrateEngine

    __all__ = [
        'UltimateCoreEngine',
        'SemanticCalculus',
        'SemanticMathematicsEngine',
        'EnhancedCoreComponents',
        'ICEFramework',
        'SelfAwareSemanticEngine',
        'TruthScaffold',
        'MeaningBasedProgramming',
        'EnhancedSubstrateEngine',
    ]
except ImportError as e:
    # Handle import errors gracefully during development
    import warnings
    warnings.warn(f"Some modules could not be imported: {e}")
    __all__ = []
