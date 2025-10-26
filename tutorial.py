from src.baseline_biblical_substrate import BiblicalSemanticSubstrate

# 1. Initialize the engine
engine = BiblicalSemanticSubstrate()

# 2. Define the concept to analyze
concept_text = "divine wisdom"

# 3. Analyze the concept
coordinates = engine.analyze_concept(concept_text, context="theological")

# 4. Print the results
print(f"Analysis of: '{concept_text}'")
print(f"Coordinates (L, J, P, W): {coordinates}")

print(f"Dominant Attribute: {coordinates.get_dominant_attribute()}")
print(f"Deficient Attributes: {coordinates.get_deficient_attributes()}")

# Calculate divine alignment metrics
divine_resonance = coordinates.divine_resonance()
distance_from_anchor = coordinates.distance_from_jehovah()

print(f"Divine Resonance: {divine_resonance:.2f}")
print(f"Distance from Universal Anchor: {distance_from_anchor:.2f}")
