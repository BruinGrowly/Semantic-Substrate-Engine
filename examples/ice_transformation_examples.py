"""
ICE-Centric Semantic Substrate Engine - Integration Examples
=============================================================

Comprehensive examples demonstrating how to use the ICE-Centric
Semantic Substrate Engine for Intent-Context-Execution processing.

Author: Semantic Substrate Engine Team
License: MIT
"""

import sys
import os

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.join(parent_dir, 'src'))

from ice_semantic_substrate_engine import (
    ICESemanticSubstrateEngine,
    ThoughtType,
    ContextDomain,
    ExecutionStrategy,
    JEHOVAH
)


def example_1_basic_transformation():
    """
    Example 1: Basic ICE Transformation

    Demonstrates the simplest usage of the ICE-Centric engine
    with a single transformation and result inspection.
    """
    print("=" * 80)
    print("EXAMPLE 1: Basic ICE Transformation")
    print("=" * 80)
    print()

    # Initialize the engine
    engine = ICESemanticSubstrateEngine()

    # Perform a simple transformation
    input_text = "Show compassion and mercy to those who suffer"

    result = engine.transform(
        input_text,
        thought_type=ThoughtType.MORAL_JUDGMENT,
        context_domain=ContextDomain.ETHICAL
    )

    # Display results
    print(f"Input: \"{input_text}\"")
    print()
    print("INTENT PHASE:")
    print(f"  Intent Coordinates: {result.intent_coordinates}")
    print(f"  Dominant Axis: {result.behavioral_guidance['dominant_axis']}")
    print()
    print("CONTEXT PHASE:")
    print(f"  Context Domain: {result.context_domain.value}")
    print(f"  Context-Adjusted: {result.context_adjusted_coordinates}")
    print(f"  Context Alignment: {result.context_alignment:.4f}")
    print()
    print("EXECUTION PHASE:")
    print(f"  Execution Strategy: {result.execution_strategy.value}")
    print(f"  Recommended Tone: {result.behavioral_guidance['recommended_tone']}")
    print(f"  Recommended Approach: {result.behavioral_guidance['recommended_approach']}")
    print()
    print("METRICS:")
    print(f"  Divine Alignment: {result.divine_alignment:.4f} ({result.divine_alignment*100:.2f}%)")
    print(f"  Anchor Distance: {result.anchor_distance:.4f}")
    print(f"  Semantic Integrity: {result.semantic_integrity:.4f} ({result.semantic_integrity*100:.2f}%)")
    print(f"  Processing Time: {result.processing_time_ms:.3f}ms")
    print()
    print(f"Output: \"{result.output_text}\"")
    print()


def example_2_domain_comparison():
    """
    Example 2: Cross-Domain Comparison

    Shows how the same input text is processed differently
    across different context domains.
    """
    print("=" * 80)
    print("EXAMPLE 2: Cross-Domain Comparison")
    print("=" * 80)
    print()

    engine = ICESemanticSubstrateEngine()

    input_text = "Lead with strength and wisdom"

    domains = [
        ContextDomain.SPIRITUAL,
        ContextDomain.BUSINESS,
        ContextDomain.EDUCATIONAL,
        ContextDomain.MINISTRY
    ]

    print(f"Input: \"{input_text}\"")
    print()

    for domain in domains:
        result = engine.transform(
            input_text,
            thought_type=ThoughtType.PRACTICAL_WISDOM,
            context_domain=domain
        )

        print(f"Domain: {domain.value.upper()}")
        print(f"  Strategy: {result.execution_strategy.value}")
        print(f"  Divine Alignment: {result.divine_alignment:.4f}")
        print(f"  Semantic Integrity: {result.semantic_integrity:.4f}")
        print(f"  Coordinates: {result.context_adjusted_coordinates}")
        print(f"  Tone: {result.behavioral_guidance['recommended_tone']}")
        print()


def example_3_all_execution_strategies():
    """
    Example 3: All Execution Strategies

    Demonstrates each of the 5 execution strategies with
    carefully crafted inputs.
    """
    print("=" * 80)
    print("EXAMPLE 3: All Execution Strategies")
    print("=" * 80)
    print()

    engine = ICESemanticSubstrateEngine()

    test_cases = [
        {
            "name": "Compassionate Action (LOVE-dominant)",
            "text": "Comfort those who are grieving with tender care",
            "type": ThoughtType.EMOTIONAL_EXPRESSION,
            "domain": ContextDomain.RELATIONAL
        },
        {
            "name": "Authoritative Command (POWER-dominant)",
            "text": "Take decisive action with unwavering authority",
            "type": ThoughtType.PRACTICAL_WISDOM,
            "domain": ContextDomain.BUSINESS
        },
        {
            "name": "Instructive Guidance (WISDOM-dominant)",
            "text": "Seek deep understanding through careful study",
            "type": ThoughtType.PRACTICAL_WISDOM,
            "domain": ContextDomain.EDUCATIONAL
        },
        {
            "name": "Corrective Judgment (JUSTICE-dominant)",
            "text": "Judge with righteousness and fairness in all matters",
            "type": ThoughtType.MORAL_JUDGMENT,
            "domain": ContextDomain.ETHICAL
        },
        {
            "name": "Balanced Response (All equal)",
            "text": "Integrate love power wisdom and justice harmoniously",
            "type": ThoughtType.DIVINE_INSPIRATION,
            "domain": ContextDomain.SPIRITUAL
        }
    ]

    for test in test_cases:
        result = engine.transform(
            test["text"],
            thought_type=test["type"],
            context_domain=test["domain"]
        )

        print(f"{test['name']}")
        print(f"  Input: \"{test['text']}\"")
        print(f"  Strategy: {result.execution_strategy.value}")
        print(f"  Dominant Axis: {result.behavioral_guidance['dominant_axis']}")
        print(f"  Coordinates: {result.context_adjusted_coordinates}")
        print(f"  Alignment: {result.divine_alignment:.4f}")
        print(f"  Integrity: {result.semantic_integrity:.4f}")
        print()


def example_4_performance_tracking():
    """
    Example 4: Performance Statistics Tracking

    Shows how to use the built-in performance tracking
    to monitor engine performance over multiple transformations.
    """
    print("=" * 80)
    print("EXAMPLE 4: Performance Statistics Tracking")
    print("=" * 80)
    print()

    engine = ICESemanticSubstrateEngine()

    # Perform multiple transformations
    test_inputs = [
        ("Express genuine care and compassion", ThoughtType.EMOTIONAL_EXPRESSION, ContextDomain.RELATIONAL),
        ("Make bold strategic decisions", ThoughtType.PRACTICAL_WISDOM, ContextDomain.BUSINESS),
        ("Pursue knowledge with diligence", ThoughtType.PRACTICAL_WISDOM, ContextDomain.EDUCATIONAL),
        ("Uphold ethical principles firmly", ThoughtType.MORAL_JUDGMENT, ContextDomain.ETHICAL),
        ("Seek divine guidance in all things", ThoughtType.DIVINE_INSPIRATION, ContextDomain.SPIRITUAL),
    ]

    print("Running 5 transformations...")
    print()

    for text, thought_type, domain in test_inputs:
        result = engine.transform(text, thought_type, domain)
        print(f"✓ {text[:50]}... [{result.execution_strategy.value}]")

    print()

    # Get performance statistics
    stats = engine.get_performance_stats()

    print("PERFORMANCE STATISTICS:")
    print(f"  Total Transformations: {stats['transformations']}")
    print(f"  Average Divine Alignment: {stats['average_alignment']:.4f}")
    print(f"  Average Semantic Integrity: {stats['average_integrity']:.4f}")
    print(f"  Average Processing Time: {stats['average_processing_time_ms']:.3f}ms")
    print()


def example_5_detailed_guidance():
    """
    Example 5: Detailed Behavioral Guidance

    Demonstrates how to access and use the detailed behavioral
    guidance provided by the execution phase.
    """
    print("=" * 80)
    print("EXAMPLE 5: Detailed Behavioral Guidance")
    print("=" * 80)
    print()

    engine = ICESemanticSubstrateEngine()

    input_text = "Provide wise counsel to those seeking guidance"

    result = engine.transform(
        input_text,
        thought_type=ThoughtType.PRACTICAL_WISDOM,
        context_domain=ContextDomain.MINISTRY
    )

    print(f"Input: \"{input_text}\"")
    print()
    print("BEHAVIORAL GUIDANCE:")
    guidance = result.behavioral_guidance

    print(f"  Execution Strategy: {result.execution_strategy.value}")
    print(f"  Dominant Axis: {guidance['dominant_axis']}")
    print()
    print("  Recommended Tone:")
    print(f"    {guidance['recommended_tone']}")
    print()
    print("  Recommended Approach:")
    print(f"    {guidance['recommended_approach']}")
    print()
    print("  Recommended Actions:")
    for action in guidance['recommended_actions']:
        print(f"    - {action}")
    print()
    print("  Context Considerations:")
    for consideration in guidance['context_considerations']:
        print(f"    - {consideration}")
    print()


def example_6_semantic_integrity_analysis():
    """
    Example 6: Semantic Integrity Analysis

    Shows how semantic integrity is calculated and what it means
    for meaning preservation through transformations.
    """
    print("=" * 80)
    print("EXAMPLE 6: Semantic Integrity Analysis")
    print("=" * 80)
    print()

    engine = ICESemanticSubstrateEngine()

    test_cases = [
        "Love conquers all obstacles",
        "Power without wisdom is dangerous",
        "Justice demands fairness and equality",
        "Wisdom grows through experience"
    ]

    print("Analyzing semantic integrity across transformations:")
    print()

    for text in test_cases:
        result = engine.transform(
            text,
            thought_type=ThoughtType.FACTUAL_STATEMENT,
            context_domain=ContextDomain.GENERAL
        )

        print(f"Input: \"{text}\"")
        print(f"  Intent Coords: {result.intent_coordinates}")
        print(f"  Final Coords:  {result.context_adjusted_coordinates}")
        print(f"  Semantic Integrity: {result.semantic_integrity:.4f} ({result.semantic_integrity*100:.2f}%)")
        print(f"  Meaning Preserved: {'✓ Excellent' if result.semantic_integrity > 0.95 else '⚠ Review'}")
        print()


def example_7_thought_type_exploration():
    """
    Example 7: Thought Type Exploration

    Demonstrates how different thought types influence the
    transformation process.
    """
    print("=" * 80)
    print("EXAMPLE 7: Thought Type Exploration")
    print("=" * 80)
    print()

    engine = ICESemanticSubstrateEngine()

    base_text = "Understanding requires both knowledge and experience"

    thought_types = [
        ThoughtType.PRACTICAL_WISDOM,
        ThoughtType.FACTUAL_STATEMENT,
        ThoughtType.DIVINE_INSPIRATION,
        ThoughtType.THEOLOGICAL_QUESTION
    ]

    print(f"Base Text: \"{base_text}\"")
    print()

    for thought_type in thought_types:
        result = engine.transform(
            base_text,
            thought_type=thought_type,
            context_domain=ContextDomain.EDUCATIONAL
        )

        print(f"Thought Type: {thought_type.value}")
        print(f"  Intent Coordinates: {result.intent_coordinates}")
        print(f"  Execution Strategy: {result.execution_strategy.value}")
        print(f"  Divine Alignment: {result.divine_alignment:.4f}")
        print()


def example_8_custom_anchor():
    """
    Example 8: Custom Anchor Point

    Shows how to use a custom anchor point instead of the
    default Jehovah anchor at (1.0, 1.0, 1.0, 1.0).
    """
    print("=" * 80)
    print("EXAMPLE 8: Custom Anchor Point")
    print("=" * 80)
    print()

    # Default anchor
    default_engine = ICESemanticSubstrateEngine()

    # Custom anchor (more power-focused)
    custom_anchor = (0.7, 1.0, 0.8, 0.9)
    custom_engine = ICESemanticSubstrateEngine(anchor_point=custom_anchor)

    input_text = "Lead with strength and conviction"

    print(f"Input: \"{input_text}\"")
    print()

    # Default transformation
    default_result = default_engine.transform(
        input_text,
        thought_type=ThoughtType.PRACTICAL_WISDOM,
        context_domain=ContextDomain.BUSINESS
    )

    print("DEFAULT ANCHOR (1.0, 1.0, 1.0, 1.0):")
    print(f"  Final Coordinates: {default_result.context_adjusted_coordinates}")
    print(f"  Divine Alignment: {default_result.divine_alignment:.4f}")
    print(f"  Anchor Distance: {default_result.anchor_distance:.4f}")
    print()

    # Custom transformation
    custom_result = custom_engine.transform(
        input_text,
        thought_type=ThoughtType.PRACTICAL_WISDOM,
        context_domain=ContextDomain.BUSINESS
    )

    print(f"CUSTOM ANCHOR {custom_anchor}:")
    print(f"  Final Coordinates: {custom_result.context_adjusted_coordinates}")
    print(f"  Divine Alignment: {custom_result.divine_alignment:.4f}")
    print(f"  Anchor Distance: {custom_result.anchor_distance:.4f}")
    print()


def example_9_context_stability_impact():
    """
    Example 9: Context Stability Impact

    Demonstrates how context domain stability affects
    anchor alignment and coordinate adjustment.
    """
    print("=" * 80)
    print("EXAMPLE 9: Context Stability Impact")
    print("=" * 80)
    print()

    engine = ICESemanticSubstrateEngine()

    input_text = "Make wise decisions with clarity"

    # Test across domains with different stability
    domains_with_stability = [
        (ContextDomain.SPIRITUAL, 1.0),
        (ContextDomain.ETHICAL, 0.9),
        (ContextDomain.GENERAL, 0.6),
        (ContextDomain.BUSINESS, 0.4)
    ]

    print(f"Input: \"{input_text}\"")
    print()
    print("Context Stability Impact on Anchor Alignment:")
    print()

    for domain, stability in domains_with_stability:
        result = engine.transform(
            input_text,
            thought_type=ThoughtType.PRACTICAL_WISDOM,
            context_domain=domain
        )

        print(f"{domain.value.title()} (Stability: {stability}):")
        print(f"  Intent Coords:     {result.intent_coordinates}")
        print(f"  Context-Adjusted:  {result.context_adjusted_coordinates}")
        print(f"  Anchor Distance:   {result.anchor_distance:.4f}")
        print(f"  Divine Alignment:  {result.divine_alignment:.4f}")
        print(f"  Pull Strength:     {stability * 0.3:.2f}")
        print()


def run_all_examples():
    """Run all examples sequentially"""
    examples = [
        example_1_basic_transformation,
        example_2_domain_comparison,
        example_3_all_execution_strategies,
        example_4_performance_tracking,
        example_5_detailed_guidance,
        example_6_semantic_integrity_analysis,
        example_7_thought_type_exploration,
        example_8_custom_anchor,
        example_9_context_stability_impact
    ]

    for i, example in enumerate(examples, 1):
        example()
        if i < len(examples):
            print("\n" + "─" * 80 + "\n")
            input("Press Enter to continue to next example...")
            print()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ICE-Centric SSE Integration Examples")
    parser.add_argument(
        "--example",
        type=int,
        help="Run specific example (1-9)",
        choices=range(1, 10)
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all examples sequentially"
    )

    args = parser.parse_args()

    if args.all:
        run_all_examples()
    elif args.example:
        example_func = globals()[f"example_{args.example}_{['basic_transformation', 'domain_comparison', 'all_execution_strategies', 'performance_tracking', 'detailed_guidance', 'semantic_integrity_analysis', 'thought_type_exploration', 'custom_anchor', 'context_stability_impact'][args.example-1]}"]
        example_func()
    else:
        # Interactive menu
        print("=" * 80)
        print("ICE-CENTRIC SEMANTIC SUBSTRATE ENGINE - EXAMPLES")
        print("=" * 80)
        print()
        print("Available Examples:")
        print("  1. Basic ICE Transformation")
        print("  2. Cross-Domain Comparison")
        print("  3. All Execution Strategies")
        print("  4. Performance Statistics Tracking")
        print("  5. Detailed Behavioral Guidance")
        print("  6. Semantic Integrity Analysis")
        print("  7. Thought Type Exploration")
        print("  8. Custom Anchor Point")
        print("  9. Context Stability Impact")
        print("  0. Run All Examples")
        print()

        choice = input("Select example (0-9): ").strip()

        if choice == "0":
            run_all_examples()
        elif choice in [str(i) for i in range(1, 10)]:
            example_num = int(choice)
            example_names = [
                'basic_transformation',
                'domain_comparison',
                'all_execution_strategies',
                'performance_tracking',
                'detailed_guidance',
                'semantic_integrity_analysis',
                'thought_type_exploration',
                'custom_anchor',
                'context_stability_impact'
            ]
            example_func = globals()[f"example_{example_num}_{example_names[example_num-1]}"]
            example_func()
        else:
            print("Invalid choice. Please run again with --help for options.")
