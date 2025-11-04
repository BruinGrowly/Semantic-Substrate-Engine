# Semantic Substrate Engine - Quick Reference

## Installation & Setup
```python
import sys, os
sys.path.append(os.path.join('.', 'src'))
from divine_invitation_engine import DivineInvitationSemanticEngine

engine = DivineInvitationSemanticEngine()
```

## Core Methods

### Basic Analysis
```python
coords = engine.analyze_concept("love and justice")
distance = engine.get_distance_from_anchor(coords)
clarity = engine.get_semantic_clarity(coords)
```

### Extended Analysis
```python
# Semantic Harmony
harmony = engine.perform_semantic_harmony_analysis(["love", "justice"])

# Mathematical Inference  
inference = engine.perform_mathematical_inference("unknown", ["love", "kindness"])

# ICE Framework
ice = engine.perform_ice_analysis("intent", "context", "execution")

# Phi Optimization
phi = engine.perform_phi_optimization(["love", "justice"])

# Unified Analysis
unified = engine.perform_unified_analysis(["love", "justice"])
```

## Coordinate System
```
Coordinates(Love, Justice, Power, Wisdom)
Anchor Point: (1, 1, 1, 1) = Perfect Harmony
Range: 0.0 - 1.0 for each dimension
```

## Quick Examples

### Political Analysis
```python
statement = "We must protect our nation and ensure justice"
coords = engine.analyze_concept(statement)
unified = engine.perform_unified_analysis([statement])
print(f"Level: {unified['level']}")
```

### Philosophical Concepts
```python
concepts = ["virtue", "ethics", "enlightenment"]
for concept in concepts:
    coords = engine.analyze_concept(concept)
    clarity = engine.get_semantic_clarity(coords)
    print(f"{concept}: Clarity {clarity:.3f}")
```

### Decision Analysis (ICE)
```python
decision = "We want to help the community by providing education"
ice = engine.perform_ice_analysis(
    "help community", "education time", "provide education"
)
print(f"ICE Harmony: {ice['ice_harmony_level']}")
```

## Testing
```bash
python examples/demo.py
python -m unittest discover tests/ -v
python tests/test_core_functionality.py
```

## Key Insights
- **Distance from Anchor**: How far from perfect harmony (lower is better)
- **Semantic Clarity**: How focused the concept is (higher is clearer)
- **Unified Score**: Overall semantic quality (0.0-1.0)
- **ICE Alignment**: Balance of intent, context, and execution

## Common Patterns
```python
# Batch processing
results = {c: engine.analyze_concept(c) for c in concepts}

# Semantic comparison
def semantic_distance(c1, c2):
    coords1, coords2 = engine.analyze_concept(c1), engine.analyze_concept(c2)
    return sum((getattr(coords1, d) - getattr(coords2, d))**2 
               for d in ['love', 'justice', 'power', 'wisdom'])**0.5
```

## Troubleshooting
- **Zero coordinates**: Check vocabulary spelling
- **Import errors**: Add src/ to Python path
- **Unexpected results**: Review vocabulary mappings