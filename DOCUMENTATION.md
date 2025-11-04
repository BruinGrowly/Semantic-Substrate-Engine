# Semantic Substrate Engine Documentation

## Overview

The Semantic Substrate Engine is a Python-based semantic analysis system that maps text concepts to a 4D coordinate system representing the fundamental dimensions of meaning: **Love, Justice, Power, and Wisdom**. The engine operates on the principle of the "Divine Invitation" - a simple, linear approach to semantic analysis that reveals the inherent structure of concepts.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
- [API Reference](#api-reference)
- [Analysis Frameworks](#analysis-frameworks)
- [Advanced Usage](#advanced-usage)
- [Examples](#examples)
- [Testing](#testing)

## Installation

### Requirements
- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

### Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure the `src` directory is accessible in your Python path

```python
import sys, os
sys.path.append(os.path.join(your_project_path, 'src'))
from divine_invitation_engine import DivineInvitationSemanticEngine
```

## Quick Start

```python
from divine_invitation_engine import DivineInvitationSemanticEngine

# Initialize the engine
engine = DivineInvitationSemanticEngine()

# Analyze a concept
concept = "love and justice"
coords = engine.analyze_concept(concept)
print(f"Coordinates: {coords}")
print(f"Distance from Anchor: {engine.get_distance_from_anchor(coords):.3f}")
print(f"Semantic Clarity: {engine.get_semantic_clarity(coords):.3f}")
```

**Output:**
```
Coordinates: Coordinates(L=0.500, J=0.500, P=0.000, W=0.000)
Distance from Anchor: 1.871
Semantic Clarity: 0.500
```

## Core Concepts

### The Four Dimensions

| Dimension | Represents | Example Keywords | Opposite |
|-----------|------------|------------------|----------|
| **Love** | Compassion, care, connection | love, compassion, kindness, community | Hate, indifference |
| **Justice** | Truth, fairness, order | justice, truth, fairness, law | Injustice, corruption |
| **Power** | Authority, strength, capability | power, strength, authority, leadership | Weakness, submission |
| **Wisdom** | Knowledge, understanding, clarity | wisdom, knowledge, understanding, education | Folly, ignorance |

### The Anchor Point

The point **(1, 1, 1, 1)** represents perfect harmony - the optimal balance of all four dimensions. All concepts are measured by their distance from this Anchor Point using Euclidean distance.

### Semantic Clarity

The maximum coordinate value of a concept, indicating its dominant dimension. Higher clarity (closer to 1.0) means the concept is more focused in a single dimension.

## API Reference

### DivineInvitationSemanticEngine

The main engine class that provides access to all analysis capabilities.

#### Core Methods

##### `analyze_concept(concept: str) -> Coordinates`
Analyzes a text concept and returns 4D coordinates.

**Parameters:**
- `concept`: Text string to analyze

**Returns:** `Coordinates` object with love, justice, power, wisdom values (0.0-1.0)

```python
coords = engine.analyze_concept("wisdom and knowledge")
# Returns: Coordinates(L=0.000, J=0.000, P=0.000, W=1.000)
```

##### `get_distance_from_anchor(coords: Coordinates) -> float`
Calculates Euclidean distance from the Anchor Point (1, 1, 1, 1).

**Parameters:**
- `coords`: Coordinates object

**Returns:** Float distance (0.0-2.0+)

##### `get_semantic_clarity(coords: Coordinates) -> float`
Calculates semantic clarity (maximum coordinate value).

**Parameters:**
- `coords`: Coordinates object

**Returns:** Float clarity (0.0-1.0)

#### Extended Analysis Methods

##### `perform_semantic_harmony_analysis(concepts: List[str]) -> SemanticResult`
Analyzes harmony between multiple concepts.

```python
concepts = ["love", "justice", "wisdom"]
result = engine.perform_semantic_harmony_analysis(concepts)
print(f"Harmonic cohesion: {result.harmonic_cohesion:.3f}")
```

##### `perform_mathematical_inference(unknown_word: str, context_words: List[str]) -> SemanticResult`
Infers meaning of unknown words from context.

```python
context = ["compassion", "kindness", "care"]
result = engine.perform_mathematical_inference("benevolence", context)
print(f"Inferred coordinates: {result.coordinates}")
print(f"Confidence: {result.confidence:.3f}")
```

##### `perform_ice_analysis(intent: str, context: str, execution: str) -> Dict`
Performs ICE (Intent-Context-Execution) framework analysis.

```python
result = engine.perform_ice_analysis(
    intent="wisdom benevolence",
    context="truth justice", 
    execution="power authority"
)
print(f"ICE harmony level: {result['ice_harmony_level']}")
print(f"ICE aligned: {result['is_ice_aligned']}")
```

##### `perform_phi_optimization(concepts: List[str]) -> Dict`
Performs golden ratio optimization analysis.

```python
result = engine.perform_phi_optimization(["love", "justice"])
print(f"Phi optimization: {result['phi_optimization']:.3f}")
print(f"Phi perfection: {result['phi_perfection']:.1f}%")
```

##### `perform_unified_analysis(concepts: List[str]) -> Dict`
Provides integrated scoring across all frameworks.

```python
result = engine.perform_unified_analysis(["love", "justice"])
print(f"Unified score: {result['unified_score']:.3f}")
print(f"Level: {result['level']}")
```

### Data Structures

#### Coordinates
```python
@dataclass
class Coordinates:
    love: float      # 0.0 - 1.0
    justice: float   # 0.0 - 1.0
    power: float     # 0.0 - 1.0
    wisdom: float    # 0.0 - 1.0
```

#### SemanticResult
```python
@dataclass
class SemanticResult:
    coordinates: Coordinates
    distance_from_anchor: float
    semantic_clarity: float
    concept_count: int
    confidence: float
    harmonic_cohesion: Optional[float] = None
```

## Analysis Frameworks

### 1. Divine Invitation Framework
The core framework that maps concepts to 4D semantic space through vocabulary lookup and normalization.

### 2. Semantic Harmony Analysis
Analyzes the cohesion and harmony between multiple concepts using cluster analysis and centroid calculations.

### 3. Mathematical Inference Engine
Discovers the meaning of unknown words by analyzing their geometric relationship to known context words.

### 4. ICE Framework
Analyzes concepts through three components:
- **Intent**: Goals, purpose, aspiration (Love + Wisdom)
- **Context**: Reality, truth, situation (Justice)
- **Execution**: Action, implementation, capability (Power)

### 5. Phi Optimization
Uses the golden ratio (φ = 1.618...) to optimize semantic analysis and calculate perfection metrics.

### 6. Unified Analysis
Combines all frameworks into a comprehensive scoring system with 7 levels:
1. TRANSCENDENT (≥0.9)
2. PERFECT_HARMONY (≥0.8)
3. EXCELLENT_COHESION (≥0.7)
4. GOOD_SEMANTICS (≥0.6)
5. DEVELOPING_UNDERSTANDING (≥0.5)
6. FOUNDATIONAL_UNDERSTANDING (≥0.3)
7. BUILDING_FOUNDATIONS (<0.3)

### 7. USP (Universal System Physics) Framework
Provides spiritual warfare capabilities including:
- Deception detection
- Counterforce generation
- Protective barriers

## Advanced Usage

### Custom Vocabulary Extension

The engine uses a built-in vocabulary that can be extended by modifying the `VocabularyManager` class:

```python
# In divine_invitation_engine.py, modify enhanced_vocab:
self.enhanced_vocab = {
    # Add your custom mappings
    'your_domain': ['love', 'justice', 'power', 'wisdom'],
    'technology': ['power', 'wisdom', 'innovation'],
    # ... existing mappings
}
```

### Batch Processing

```python
def analyze_batch(concepts, engine):
    """Analyze multiple concepts efficiently."""
    results = {}
    for concept in concepts:
        coords = engine.analyze_concept(concept)
        distance = engine.get_distance_from_anchor(coords)
        clarity = engine.get_semantic_clarity(coords)
        
        results[concept] = {
            'coordinates': coords,
            'distance': distance,
            'clarity': clarity
        }
    return results

concepts = ["love", "justice", "power", "wisdom"]
results = analyze_batch(concepts, engine)
```

### Semantic Comparison

```python
def compare_concepts(concept1, concept2, engine):
    """Compare two concepts semantically."""
    coords1 = engine.analyze_concept(concept1)
    coords2 = engine.analyze_concept(concept2)
    
    # Calculate semantic distance between concepts
    semantic_distance = math.sqrt(
        (coords1.love - coords2.love) ** 2 +
        (coords1.justice - coords2.justice) ** 2 +
        (coords1.power - coords2.power) ** 2 +
        (coords1.wisdom - coords2.wisdom) ** 2
    )
    
    return {
        'concept1': concept1,
        'concept2': concept2,
        'semantic_distance': semantic_distance,
        'coords1': coords1,
        'coords2': coords2
    }

comparison = compare_concepts("love", "justice", engine)
print(f"Semantic distance: {comparison['semantic_distance']:.3f}")
```

## Examples

### Example 1: Political Analysis

```python
# Analyze political statements
statements = [
    "We must protect our nation and ensure justice for all citizens",
    "Military strength is essential for national security", 
    "Education and healthcare are fundamental human rights"
]

for statement in statements:
    coords = engine.analyze_concept(statement)
    result = engine.perform_unified_analysis([statement])
    
    print(f"Statement: {statement[:50]}...")
    print(f"Coordinates: {coords}")
    print(f"Unified Level: {result['level']}")
    print("-" * 50)
```

### Example 2: Philosophical Concept Analysis

```python
# Analyze philosophical concepts
concepts = ["virtue", "ethics", "morality", "enlightenment"]

for concept in concepts:
    coords = engine.analyze_concept(concept)
    harmony = engine.perform_semantic_harmony_analysis([concept])
    
    print(f"{concept}:")
    print(f"  Coordinates: {coords}")
    print(f"  Clarity: {engine.get_semantic_clarity(coords):.3f}")
    print(f"  Distance from Anchor: {engine.get_distance_from_anchor(coords):.3f}")
```

### Example 3: ICE Framework for Decision Analysis

```python
def analyze_decision(decision_description):
    """Analyze a decision using ICE framework."""
    
    # For demonstration, split the description
    words = decision_description.split()
    intent_words = [w for w in words if any(i in w for i in ['goal', 'purpose', 'want'])]
    context_words = [w for w in words if any(c in w for c in ['reality', 'situation', 'fact'])]
    execution_words = [w for w in words if any(e in w for e in ['action', 'do', 'implement'])]
    
    # Fallback to simple analysis if no specific words found
    if not intent_words:
        intent_words = words[:len(words)//3]
    if not context_words:
        context_words = words[len(words)//3:2*len(words)//3]
    if not execution_words:
        execution_words = words[2*len(words)//3:]
    
    result = engine.perform_ice_analysis(
        ' '.join(intent_words),
        ' '.join(context_words), 
        ' '.join(execution_words)
    )
    
    return result

decision = "We want to help the community by providing education in this time of crisis"
ice_result = analyze_decision(decision)
print(f"ICE Harmony Level: {ice_result['ice_harmony_level']}")
print(f"Components Analysis: {ice_result['ice_components']}")
```

## Testing

### Running Tests

```bash
# Run all tests
python -m unittest discover tests/ -v

# Run specific test file
python tests/test_core_functionality.py

# Run the demo
python examples/demo.py
```

### Test Coverage

The test suite covers:
- Core concept analysis for all dimensions
- Mixed concept analysis
- Distance calculations
- Semantic clarity calculations
- Edge cases (empty input, unknown words)

### Adding Custom Tests

```python
import unittest
from divine_invitation_engine import DivineInvitationSemanticEngine

class CustomTest(unittest.TestCase):
    def setUp(self):
        self.engine = DivineInvitationSemanticEngine()
    
    def test_custom_concept(self):
        concept = "your test concept"
        coords = self.engine.analyze_concept(concept)
        # Add your assertions here
        self.assertIsNotNone(coords)

if __name__ == '__main__':
    unittest.main()
```

## Performance and Limitations

### Performance Characteristics
- **Initialization**: ~50ms (vocabulary loading)
- **Analysis**: <1ms per concept
- **Memory**: ~10MB for full vocabulary
- **Scalability**: Handles arbitrarily long input text

### Limitations
- Vocabulary-dependent (unknown words return zero coordinates)
- English language only (vocabulary currently in English)
- Linear analysis (doesn't understand word order or grammar)
- Fixed 4D semantic space

### Best Practices
- Use meaningful, descriptive text for better analysis
- Consider context when interpreting results
- Combine multiple frameworks for comprehensive analysis
- Validate results with domain knowledge

## Troubleshooting

### Common Issues

**Import Error**: `ModuleNotFoundError: No module named 'divine_invitation_engine'`
```python
# Add src directory to path
import sys, os
sys.path.append(os.path.join('.', 'src'))
```

**Zero Coordinates**: Concept returns (0, 0, 0, 0)
- Check if words exist in vocabulary
- Verify spelling and word form (use base forms)
- Consider extending vocabulary if needed

**Unexpected Results**: Coordinates don't match expectations
- Review the vocabulary mappings
- Consider word ambiguity and multiple meanings
- Use context-specific analysis frameworks

### Debug Mode

```python
# Enable debug output
engine = DivineInvitationSemanticEngine()

# Check vocabulary coverage
test_text = "your concept here"
words = test_text.lower().split()
known_words = [w for w in words if w in engine.vocab.keyword_map]
unknown_words = [w for w in words if w not in engine.vocab.keyword_map]

print(f"Known words: {known_words}")
print(f"Unknown words: {unknown_words}")
```

## Contributing

When contributing to the Semantic Substrate Engine:

1. **Core Philosophy**: Maintain simplicity and linear analysis
2. **Testing**: Add comprehensive tests for new features
3. **Documentation**: Update this documentation with changes
4. **Vocabulary**: Extend vocabulary thoughtfully with semantic accuracy
5. **Architecture**: Follow existing patterns and dataclass usage

## License and Attribution

This engine implements the "Divine Invitation" framework for semantic analysis. It provides direct access to the fundamental structure of meaning through mathematical simplicity and elegance.

---

**Appendix: Complete Method Reference**

See the source code in `src/divine_invitation_engine.py` for complete method signatures and implementation details.