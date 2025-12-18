#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NLP Text Analysis for LJPW Measurement
Implements Part XI.3 of the LJPW Framework V7.0

Uses word dictionaries to analyze text and extract LJPW coordinates.
Applies φ-normalization for objective measurement.
"""

import re
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class NLPAnalysisResult:
    """Result of NLP text analysis"""
    L: float
    J: float
    P: float
    W: float
    total_words: int
    ljpw_word_count: int
    coverage: float  # Percentage of words that are LJPW-relevant

    def to_tuple(self) -> Tuple[float, float, float, float]:
        """Return LJPW coordinates as tuple"""
        return (self.L, self.J, self.P, self.W)

    def __str__(self) -> str:
        return f"LJPW({self.L:.3f}, {self.J:.3f}, {self.P:.3f}, {self.W:.3f}) | Coverage={self.coverage:.1%}"


class NLPLJPWAnalyzer:
    """
    NLP-based LJPW measurement using word dictionaries.

    Based on LJPW Framework V7.0, Part XI.3: NLP Text Analysis
    """

    def __init__(self):
        # Golden Ratio for normalization
        self.PHI = (math.sqrt(5) + 1) / 2  # φ = 1.618034

        # LJPW Word Dictionaries (from V7 Part XI.3)
        self.love_dictionary = {
            'connect', 'collaborate', 'partner', 'team', 'together', 'support',
            'trust', 'care', 'unity', 'family', 'bond', 'loyalty', 'empathy',
            'compassion', 'belonging', 'love', 'friendship', 'community',
            'cooperation', 'harmony', 'peace', 'kindness', 'mercy', 'agape'
        }

        self.justice_dictionary = {
            'comply', 'ethical', 'transparent', 'truth', 'honest', 'fair',
            'integrity', 'accountability', 'governance', 'audit', 'regulation',
            'disclosure', 'lawful', 'justice', 'fairness', 'righteousness',
            'rights', 'freedom', 'liberty', 'equality', 'legal', 'law',
            'balance', 'impartial', 'unbiased'
        }

        self.power_dictionary = {
            'grow', 'execute', 'compete', 'win', 'lead', 'revenue', 'profit',
            'expand', 'acquire', 'deliver', 'scale', 'strategic', 'accelerate',
            'momentum', 'power', 'strength', 'authority', 'sovereignty',
            'might', 'rule', 'govern', 'control', 'leadership', 'command',
            'military', 'force', 'capability', 'performance'
        }

        self.wisdom_dictionary = {
            'learn', 'innovate', 'understand', 'knowledge', 'insight',
            'research', 'develop', 'analyze', 'adapt', 'technology',
            'experience', 'expertise', 'creative', 'wisdom', 'understanding',
            'clarity', 'reason', 'logic', 'study', 'education', 'school',
            'university', 'science', 'mathematics', 'geometry', 'algorithms',
            'analysis', 'intelligence', 'thinking', 'reasoning'
        }

        # Build reverse lookup map
        self.word_to_dimension = {}
        for word in self.love_dictionary:
            self.word_to_dimension[word] = 'L'
        for word in self.justice_dictionary:
            self.word_to_dimension[word] = 'J'
        for word in self.power_dictionary:
            self.word_to_dimension[word] = 'P'
        for word in self.wisdom_dictionary:
            self.word_to_dimension[word] = 'W'

    def analyze_text(self, text: str) -> NLPAnalysisResult:
        """
        Analyze text and extract LJPW coordinates.

        Uses word dictionary matching with φ-normalization.

        Args:
            text: Input text to analyze

        Returns:
            NLPAnalysisResult with LJPW coordinates and metadata
        """
        # Tokenize text (extract words, lowercase, alphanumeric only)
        words = re.findall(r'\b[a-z]+\b', text.lower())
        total_words = len(words)

        if total_words == 0:
            return NLPAnalysisResult(0, 0, 0, 0, 0, 0, 0)

        # Count matches for each dimension
        counts = {'L': 0, 'J': 0, 'P': 0, 'W': 0}

        for word in words:
            if word in self.word_to_dimension:
                dimension = self.word_to_dimension[word]
                counts[dimension] += 1

        ljpw_word_count = sum(counts.values())
        coverage = ljpw_word_count / total_words if total_words > 0 else 0

        # Calculate raw frequencies
        if ljpw_word_count == 0:
            return NLPAnalysisResult(0, 0, 0, 0, total_words, 0, 0)

        raw_frequencies = {
            'L': counts['L'] / total_words,
            'J': counts['J'] / total_words,
            'P': counts['P'] / total_words,
            'W': counts['W'] / total_words
        }

        # Apply φ-normalization (V7 Part XI.3)
        L = self._phi_normalize(raw_frequencies['L'])
        J = self._phi_normalize(raw_frequencies['J'])
        P = self._phi_normalize(raw_frequencies['P'])
        W = self._phi_normalize(raw_frequencies['W'])

        return NLPAnalysisResult(
            L=L, J=J, P=P, W=W,
            total_words=total_words,
            ljpw_word_count=ljpw_word_count,
            coverage=coverage
        )

    def analyze_multiple_texts(self, texts: List[str]) -> NLPAnalysisResult:
        """
        Analyze multiple texts and aggregate results.

        Args:
            texts: List of text strings

        Returns:
            Aggregated NLPAnalysisResult
        """
        if not texts:
            return NLPAnalysisResult(0, 0, 0, 0, 0, 0, 0)

        # Analyze each text
        results = [self.analyze_text(text) for text in texts]

        # Aggregate using weighted average (by word count)
        total_words = sum(r.total_words for r in results)

        if total_words == 0:
            return NLPAnalysisResult(0, 0, 0, 0, 0, 0, 0)

        L = sum(r.L * r.total_words for r in results) / total_words
        J = sum(r.J * r.total_words for r in results) / total_words
        P = sum(r.P * r.total_words for r in results) / total_words
        W = sum(r.W * r.total_words for r in results) / total_words

        ljpw_word_count = sum(r.ljpw_word_count for r in results)
        coverage = ljpw_word_count / total_words

        return NLPAnalysisResult(
            L=L, J=J, P=P, W=W,
            total_words=total_words,
            ljpw_word_count=ljpw_word_count,
            coverage=coverage
        )

    def get_dimension_breakdown(self, text: str) -> Dict[str, Dict]:
        """
        Get detailed breakdown of dimension word matches.

        Args:
            text: Input text

        Returns:
            Dictionary with matched words for each dimension
        """
        words = re.findall(r'\b[a-z]+\b', text.lower())

        breakdown = {
            'L': {'matches': [], 'count': 0},
            'J': {'matches': [], 'count': 0},
            'P': {'matches': [], 'count': 0},
            'W': {'matches': [], 'count': 0}
        }

        for word in words:
            if word in self.word_to_dimension:
                dimension = self.word_to_dimension[word]
                breakdown[dimension]['matches'].append(word)
                breakdown[dimension]['count'] += 1

        return breakdown

    def _phi_normalize(self, frequency: float) -> float:
        """
        Apply φ-normalization to word frequency.

        Formula from V7 Part XI.3:
        dimension = φ × (dictionary_matches / total_words)^(1/φ)

        Args:
            frequency: Raw word frequency (0-1)

        Returns:
            φ-normalized value
        """
        if frequency <= 0:
            return 0

        return self.PHI * (frequency ** (1 / self.PHI))

    def calculate_harmony(self, result: NLPAnalysisResult) -> float:
        """
        Calculate Harmony Index from NLP result.

        H = 1 / (1 + distance_from_anchor)

        Args:
            result: NLPAnalysisResult

        Returns:
            Harmony value (0-1)
        """
        L, J, P, W = result.to_tuple()
        d = math.sqrt((1 - L)**2 + (1 - J)**2 + (1 - P)**2 + (1 - W)**2)
        return 1.0 / (1.0 + d)


def main():
    """Demonstration of NLP LJPW analysis"""
    print("=" * 80)
    print("NLP LJPW TEXT ANALYSIS")
    print("LJPW Framework V7.0 - Part XI.3 Implementation")
    print("=" * 80)

    analyzer = NLPLJPWAnalyzer()

    # Example 1: Love-dominant text
    print("\n=== EXAMPLE 1: LOVE-DOMINANT TEXT ===")
    love_text = """
    Our team collaborates together with trust and compassion. We support each other
    and build strong bonds of friendship and unity. The community thrives on
    empathy and care for one another.
    """

    result = analyzer.analyze_text(love_text)
    print(f"Text: {love_text.strip()}")
    print(f"\nResult: {result}")
    print(f"Harmony: {analyzer.calculate_harmony(result):.3f}")

    breakdown = analyzer.get_dimension_breakdown(love_text)
    print(f"\nDimension Breakdown:")
    for dim in ['L', 'J', 'P', 'W']:
        print(f"  {dim}: {breakdown[dim]['count']} matches - {breakdown[dim]['matches']}")

    # Example 2: Power-dominant text
    print("\n=== EXAMPLE 2: POWER-DOMINANT TEXT ===")
    power_text = """
    The company will execute strategic growth through strong leadership and command.
    We will compete to win, expand our revenue, and scale operations with
    accelerating momentum and force.
    """

    result = analyzer.analyze_text(power_text)
    print(f"Text: {power_text.strip()}")
    print(f"\nResult: {result}")
    print(f"Harmony: {analyzer.calculate_harmony(result):.3f}")

    breakdown = analyzer.get_dimension_breakdown(power_text)
    print(f"\nDimension Breakdown:")
    for dim in ['L', 'J', 'P', 'W']:
        print(f"  {dim}: {breakdown[dim]['count']} matches - {breakdown[dim]['matches']}")

    # Example 3: Balanced text
    print("\n=== EXAMPLE 3: BALANCED TEXT ===")
    balanced_text = """
    We will collaborate with integrity to execute innovative solutions.
    Our team combines wisdom and power with fair governance and compassionate
    leadership. Together we learn, grow, and maintain transparency.
    """

    result = analyzer.analyze_text(balanced_text)
    print(f"Text: {balanced_text.strip()}")
    print(f"\nResult: {result}")
    print(f"Harmony: {analyzer.calculate_harmony(result):.3f}")

    # Example 4: Corporate mission statement analysis
    print("\n=== EXAMPLE 4: CORPORATE MISSION STATEMENT ===")
    mission_texts = [
        "Drive innovation through research and learning",
        "Execute with power and strategic leadership",
        "Maintain ethical governance and transparency",
        "Build community through collaboration and trust"
    ]

    result = analyzer.analyze_multiple_texts(mission_texts)
    print(f"Texts analyzed: {len(mission_texts)}")
    for i, text in enumerate(mission_texts, 1):
        print(f"  {i}. {text}")
    print(f"\nAggregated Result: {result}")
    print(f"Harmony: {analyzer.calculate_harmony(result):.3f}")

    print("\n" + "=" * 80)
    print(f"NLP analyzer initialized with {len(analyzer.word_to_dimension)} total words")
    print("φ-normalization applied for objective measurement")
    print("=" * 80)


if __name__ == "__main__":
    main()
