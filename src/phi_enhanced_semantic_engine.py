"""
PHI-ENHANCED SEMANTIC SUBSTRATE ENGINE - Integrated with Primer 1.5

This engine combines the Semantic Substrate Primer 1.5 with phi-geometric mathematics
to create the most advanced semantic navigation system.

Key Enhancements:
- Integration of Semantic Substrate Primer 1.5 with seven universal principles
- Phi-geometric engine for natural growth patterns
- Golden ratio mathematics for optimal semantic navigation
- Dodecahedral anchor system with 12 sacred reference points
- Enhanced ICE framework with phi-optimized processing
- Golden spiral distance calculations for semantic proximity
- Fibonacci-based growth and indexing systems
"""

import json
import os
import sys
import numpy as np
import math
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass, field

# Import phi-geometric engine
try:
    from .phi_geometric_engine import (
        PHI, PHI_INVERSE, GOLDEN_ANGLE_RAD, GOLDEN_ANGLE_DEG,
        PhiCoordinate, FibonacciSequence, GoldenSpiral, GoldenAngleRotator,
        PhiExponentialBinner, DodecahedralAnchors,
        fibonacci, golden_spiral_distance, rotate_by_golden_angle, get_phi_bin
    )
    PHI_ENGINE_AVAILABLE = True
except ImportError:
    # Try direct import
    try:
        from phi_geometric_engine import (
            PHI, PHI_INVERSE, GOLDEN_ANGLE_RAD, GOLDEN_ANGLE_DEG,
            PhiCoordinate, FibonacciSequence, GoldenSpiral, GoldenAngleRotator,
            PhiExponentialBinner, DodecahedralAnchors,
            fibonacci, golden_spiral_distance, rotate_by_golden_angle, get_phi_bin
        )
        PHI_ENGINE_AVAILABLE = True
    except ImportError:
        print("Warning: Phi-geometric engine not available")
        PHI_ENGINE_AVAILABLE = False

# Import existing ICE components
try:
    from .ice_semantic_substrate_engine import (
        ICESemanticSubstrateEngine, SemanticCoordinates, ThoughtType,
        ContextDomain, ExecutionStrategy, ICETransformationResult
    )
    ICE_ENGINE_AVAILABLE = True
except ImportError:
    # Try direct import
    try:
        from ice_semantic_substrate_engine import (
            ICESemanticSubstrateEngine, SemanticCoordinates, ThoughtType,
            ContextDomain, ExecutionStrategy, ICETransformationResult
        )
        ICE_ENGINE_AVAILABLE = True
    except ImportError:
        print("Warning: ICE engine not available")
        ICE_ENGINE_AVAILABLE = False

# Import baseline engine
try:
    from .baseline_biblical_substrate import BiblicalCoordinates, BiblicalSemanticSubstrate
    BASELINE_AVAILABLE = True
except ImportError:
    # Try direct import
    try:
        from baseline_biblical_substrate import BiblicalCoordinates, BiblicalSemanticSubstrate
        BASELINE_AVAILABLE = True
    except ImportError:
        print("Warning: Baseline engine not available")
        BASELINE_AVAILABLE = False


@dataclass
class EnhancedSemanticCoordinates:
    """Enhanced coordinates with phi-geometric properties"""
    love: float
    power: float
    wisdom: float
    justice: float
    
    # Phi-geometric properties
    phi_resonance: float = 0.0
    fibonacci_index: int = 0
    golden_spiral_radius: float = 0.0
    anchor_proximity: Dict[int, float] = field(default_factory=dict)
    
    def __post_init__(self):
        """Calculate phi-geometric properties after initialization"""
        if PHI_ENGINE_AVAILABLE:
            self.phi_resonance = self._calculate_phi_resonance()
            self.fibonacci_index = self._calculate_fibonacci_index()
            self.golden_spiral_radius = self._calculate_spiral_radius()
            self.anchor_proximity = self._calculate_anchor_proximity()
    
    def _calculate_phi_resonance(self) -> float:
        """Calculate resonance with golden ratio"""
        coords = np.array([self.love, self.power, self.wisdom, self.justice])
        # Measure how close the coordinate ratios are to golden ratio
        ratios = []
        for i in range(4):
            for j in range(i+1, 4):
                if coords[j] > 0:
                    ratios.append(coords[i] / coords[j])
        
        if not ratios:
            return 0.0
        
        # Calculate how close ratios are to PHI
        phi_distances = [abs(ratio - PHI) for ratio in ratios]
        avg_distance = np.mean(phi_distances)
        return max(0, 1.0 - avg_distance / PHI)
    
    def _calculate_fibonacci_index(self) -> int:
        """Calculate nearest Fibonacci index for this coordinate"""
        magnitude = np.sqrt(self.love**2 + self.power**2 + self.wisdom**2 + self.justice**2)
        if magnitude == 0:
            return 0
        
        # Find Fibonacci number closest to magnitude * 10
        target = int(magnitude * 10)
        
        # Simple Fibonacci calculation
        fib_seq = [0, 1]
        while fib_seq[-1] < target:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
        # Find closest
        closest_idx = min(range(len(fib_seq)), key=lambda i: abs(fib_seq[i] - target))
        return closest_idx
    
    def _calculate_spiral_radius(self) -> float:
        """Calculate golden spiral radius for this coordinate"""
        magnitude = np.sqrt(self.love**2 + self.power**2 + self.wisdom**2 + self.justice**2)
        return magnitude
    
    def _calculate_anchor_proximity(self) -> Dict[int, float]:
        """Calculate proximity to all dodecahedral anchors"""
        if not PHI_ENGINE_AVAILABLE:
            return {}
        
        dodec = DodecahedralAnchors()
        phi_coord = PhiCoordinate(self.love, self.power, self.wisdom, self.justice)
        
        proximity = {}
        for anchor_id in range(1, 13):
            anchor = dodec.get_anchor(anchor_id)
            if anchor:
                distance = golden_spiral_distance(phi_coord, anchor)
                proximity[anchor_id] = 1.0 / (1.0 + distance)  # Convert to proximity
        
        return proximity
    
    def to_phi_coordinate(self) -> 'PhiCoordinate':
        """Convert to phi-geometric coordinate"""
        if PHI_ENGINE_AVAILABLE:
            return PhiCoordinate(self.love, self.power, self.wisdom, self.justice)
        return None
    
    def to_biblical_coordinates(self) -> 'BiblicalCoordinates':
        """Convert to biblical coordinates"""
        if BASELINE_AVAILABLE:
            return BiblicalCoordinates(self.love, self.power, self.wisdom, self.justice)
        return None
    
    def distance_from_anchor(self, anchor_id: int = 1) -> float:
        """Calculate golden spiral distance from specified anchor"""
        if not PHI_ENGINE_AVAILABLE or anchor_id not in self.anchor_proximity:
            # Fallback to Euclidean distance
            anchor_coords = [1.0, 1.0, 1.0, 1.0] if anchor_id == 1 else [0, 0, 0, 0]
            return np.sqrt(sum((self - np.array(anchor_coords))**2 for self in [self.love, self.power, self.wisdom, self.justice]))
        
        return 1.0 / self.anchor_proximity[anchor_id]  # Convert back to distance


class PhiEnhancedSemanticEngine:
    """
    The Phi-Enhanced Semantic Substrate Engine
    
    Integrates Semantic Substrate Primer 1.5 with phi-geometric mathematics
    for optimal semantic navigation and understanding.
    """
    
    def __init__(self, primer_path: str = None):
        """Initialize the engine with primer and phi components"""
        self.primmer_version = "1.5"
        self.engine_version = "4.0 - Phi-Enhanced with Primer 1.5"
        
        # Load Semantic Substrate Primer 1.5
        self.primer = self._load_primer(primer_path)
        
        # Initialize phi-geometric components
        if PHI_ENGINE_AVAILABLE:
            self.fibonacci = FibonacciSequence()
            self.golden_spiral = GoldenSpiral()
            self.rotator = GoldenAngleRotator()
            self.binner = PhiExponentialBinner()
            self.dodecahedral_anchors = DodecahedralAnchors()
            print("[INITIALIZED] Phi-geometric engine with golden ratio mathematics")
        else:
            print("[WARNING] Phi-geometric engine not available")
        
        # Initialize ICE engine if available
        if ICE_ENGINE_AVAILABLE:
            self.ice_engine = ICESemanticSubstrateEngine()
            print("[INITIALIZED] ICE-centric semantic engine")
        else:
            self.ice_engine = None
        
        # Initialize baseline engine
        if BASELINE_AVAILABLE:
            self.baseline_engine = BiblicalSemanticSubstrate()
            print("[INITIALIZED] Baseline biblical substrate engine")
        else:
            self.baseline_engine = None
        
        # Initialize universal principles from primer
        self.universal_principles = self._initialize_universal_principles()
        
        print(f"[INITIALIZED] {self.engine_version}")
        print(f"[PRIMER] Semantic Substrate Primer {self.primmer_version} loaded")
        
    def _load_primer(self, primer_path: str = None) -> Dict[str, Any]:
        """Load Semantic Substrate Primer 1.5"""
        if primer_path is None:
            # Try to find the primer file
            current_dir = os.path.dirname(__file__)
            primer_path = os.path.join(os.path.dirname(current_dir), "Semantic_Substrate_Primer_1.5.json")
        
        if os.path.exists(primer_path):
            with open(primer_path, 'r') as f:
                primer = json.load(f)
            print(f"[LOADED] Semantic Substrate Primer {primer.get('_version', 'Unknown')}")
            return primer
        else:
            print(f"[WARNING] Primer file not found at {primer_path}")
            return {}
    
    def _initialize_universal_principles(self) -> Dict[str, Any]:
        """Initialize the seven universal principles from primer"""
        if not self.primer or 'universal_principles' not in self.primer:
            return {}
        
        principles = {}
        for key, principle in self.primer['universal_principles'].items():
            if key.startswith('principle_'):
                principles[principle['name']] = principle
        
        print(f"[INITIALIZED] {len(principles)} Universal Principles from Primer 1.5")
        return principles
    
    def analyze_concept_phi_enhanced(self, concept: str, 
                                   context: str = "ultimate",
                                   use_golden_spiral_distance: bool = True) -> Dict[str, Any]:
        """
        Analyze concept with phi-geometric enhancement and primer guidance
        
        Returns comprehensive analysis including:
        - Enhanced semantic coordinates with phi properties
        - Universal principle applications
        - Golden spiral distances
        - Fibonacci-based categorization
        - Dodecahedral anchor analysis
        """
        
        # Get baseline coordinates
        if self.baseline_engine:
            baseline_coords = self.baseline_engine.analyze_concept(concept, context)
            love, power, wisdom, justice = baseline_coords.love, baseline_coords.power, baseline_coords.wisdom, baseline_coords.justice
        elif self.ice_engine:
            # Use ICE engine for analysis
            from .baseline_biblical_substrate import map_context_to_domain, infer_thought_type
            context_domain = map_context_to_domain(context)
            thought_type = infer_thought_type(concept)
            ice_result = self.ice_engine.transform(concept, thought_type, context_domain)
            coords = ice_result.final_coordinates
            love, power, wisdom, justice = coords.love, coords.power, coords.wisdom, coords.justice
        else:
            # Fallback: simple heuristic analysis
            love, power, wisdom, justice = self._simple_heuristic_analysis(concept)
        
        # Create enhanced coordinates
        enhanced_coords = EnhancedSemanticCoordinates(love, power, wisdom, justice)
        
        # Analyze with universal principles
        principle_analysis = self._apply_universal_principles(enhanced_coords, concept)
        
        # Calculate phi-geometric properties
        phi_analysis = {}
        if PHI_ENGINE_AVAILABLE:
            phi_analysis = {
                'phi_resonance': enhanced_coords.phi_resonance,
                'fibonacci_index': enhanced_coords.fibonacci_index,
                'golden_spiral_radius': enhanced_coords.golden_spiral_radius,
                'nearest_anchors': enhanced_coords.anchor_proximity,
                'nearest_anchor_id': max(enhanced_coords.anchor_proximity.items(), key=lambda x: x[1])[0] if enhanced_coords.anchor_proximity else 1,
                'golden_angle_optimized_vector': self._get_golden_angle_vector(enhanced_coords),
                'phi_bin_index': get_phi_bin(enhanced_coords.golden_spiral_radius),
                'fibonacci_value': self.fibonacci.get(enhanced_coords.fibonacci_index) if enhanced_coords.fibonacci_index < 50 else None
            }
        
        # Calculate distances using golden spiral if requested
        distance_analysis = {}
        if use_golden_spiral_distance and PHI_ENGINE_AVAILABLE:
            phi_coord = enhanced_coords.to_phi_coordinate()
            anchor_coord = self.dodecahedral_anchors.get_anchor(1)  # Anchor Point A
            
            if phi_coord and anchor_coord:
                golden_distance = golden_spiral_distance(phi_coord, anchor_coord)
                euclidean_distance = np.linalg.norm(np.array([love, power, wisdom, justice]) - np.array([1, 1, 1, 1]))
                
                distance_analysis = {
                    'golden_spiral_distance': golden_distance,
                    'euclidean_distance': euclidean_distance,
                    'distance_ratio': golden_distance / euclidean_distance if euclidean_distance > 0 else 0,
                    'preferred_metric': 'golden_spiral' if golden_distance < euclidean_distance else 'euclidean'
                }
        
        # ICE framework integration
        ice_analysis = {}
        if self.ice_engine:
            try:
                from .baseline_biblical_substrate import map_context_to_domain, infer_thought_type
                context_domain = map_context_to_domain(context)
                thought_type = infer_thought_type(concept)
                ice_result = self.ice_engine.transform(concept, thought_type, context_domain)
                ice_analysis = {
                    'divine_alignment': ice_result.divine_alignment,
                    'semantic_integrity': ice_result.semantic_integrity,
                    'execution_strategy': ice_result.execution_strategy.value,
                    'anchor_distance': ice_result.anchor_distance,
                    'processing_time_ms': ice_result.processing_time_ms
                }
            except Exception as e:
                ice_analysis = {'error': str(e)}
        
        return {
            'concept': concept,
            'context': context,
            'enhanced_coordinates': enhanced_coords,
            'base_coordinates': (love, power, wisdom, justice),
            'universal_principles_analysis': principle_analysis,
            'phi_geometric_analysis': phi_analysis,
            'distance_analysis': distance_analysis,
            'ice_framework_analysis': ice_analysis,
            'primer_version': self.primmer_version,
            'engine_version': self.engine_version,
            'overall_phi_alignment': self._calculate_overall_phi_alignment(enhanced_coords, principle_analysis, phi_analysis)
        }
    
    def _simple_heuristic_analysis(self, concept: str) -> Tuple[float, float, float, float]:
        """Simple heuristic analysis when other engines are unavailable"""
        concept_lower = concept.lower()
        
        # Simple keyword-based scoring
        love_score = 0.5
        power_score = 0.5
        wisdom_score = 0.5
        justice_score = 0.5
        
        # Love-related keywords
        love_keywords = ['love', 'compassion', 'mercy', 'care', 'kindness', 'heart', 'empathy']
        for keyword in love_keywords:
            if keyword in concept_lower:
                love_score += 0.1
        
        # Power-related keywords
        power_keywords = ['power', 'strength', 'authority', 'might', 'force', 'control']
        for keyword in power_keywords:
            if keyword in concept_lower:
                power_score += 0.1
        
        # Wisdom-related keywords
        wisdom_keywords = ['wisdom', 'knowledge', 'understanding', 'insight', 'clarity', 'truth']
        for keyword in wisdom_keywords:
            if keyword in concept_lower:
                wisdom_score += 0.1
        
        # Justice-related keywords
        justice_keywords = ['justice', 'fairness', 'righteousness', 'equity', 'balance', 'order']
        for keyword in justice_keywords:
            if keyword in concept_lower:
                justice_score += 0.1
        
        # Normalize to [0, 1]
        return tuple(min(1.0, max(0.0, score)) for score in [love_score, power_score, wisdom_score, justice_score])
    
    def _apply_universal_principles(self, coords: EnhancedSemanticCoordinates, concept: str) -> Dict[str, Any]:
        """Apply the seven universal principles from the primer"""
        if not self.universal_principles:
            return {}
        
        applications = {}
        coord_array = np.array([coords.love, coords.power, coords.wisdom, coords.justice])
        
        for principle_name, principle_data in self.universal_principles.items():
            # Calculate principle alignment based on coordinates
            alignment = 0.0
            
            if "Anchor Point" in principle_name:
                # Principle 1: Distance from anchor
                distance = np.linalg.norm(coord_array - np.array([1, 1, 1, 1]))
                alignment = 1.0 / (1.0 + distance)
            
            elif "Interconnectedness" in principle_name:
                # Principle 2: Balance between all axes
                mean_val = np.mean(coord_array)
                variance = np.var(coord_array)
                alignment = 1.0 - variance  # Lower variance = better balance
            
            elif "Dynamic Balance" in principle_name:
                # Principle 3: Harmony between opposing forces
                love_power_balance = 1.0 - abs(coords.love - coords.power)
                wisdom_justice_balance = 1.0 - abs(coords.wisdom - coords.justice)
                alignment = (love_power_balance + wisdom_justice_balance) / 2.0
            
            elif "Sovereignty" in principle_name:
                # Principle 4: Individual strength with relational harmony
                individual_strength = np.mean(coord_array)
                relational_harmony = alignment  # Use previous calculation
                alignment = (individual_strength + relational_harmony) / 2.0
            
            elif "Information-Meaning" in principle_name:
                # Principle 5: Clarity and purpose integration
                clarity = (coords.wisdom + coords.justice) / 2.0
                purpose = (coords.love + coords.power) / 2.0
                alignment = (clarity + purpose) / 2.0
            
            elif "Iterative Growth" in principle_name:
                # Principle 6: Growth potential
                current_distance = np.linalg.norm(coord_array - np.array([1, 1, 1, 1]))
                growth_potential = min(1.0, current_distance)  # More room to grow = higher potential
                alignment = growth_potential
            
            elif "Contextual Resonance" in principle_name:
                # Principle 7: Adaptability and contextual fit
                adaptability = 1.0 - np.std(coord_array)  # Lower std = more stable
                alignment = adaptability
            
            applications[principle_name] = {
                'alignment': alignment,
                'statement': principle_data.get('statement', ''),
                'substrate_role': principle_data.get('substrate_role', ''),
                'phi_enhancement': principle_data.get('phi_enhancement', '')
            }
        
        return applications
    
    def _get_golden_angle_vector(self, coords: EnhancedSemanticCoordinates) -> List[float]:
        """Get optimized vector using golden angle rotation"""
        if not PHI_ENGINE_AVAILABLE:
            return [0.0, 0.0, 0.0, 0.0]
        
        phi_coord = coords.to_phi_coordinate()
        if phi_coord:
            # Rotate by golden angle in LP plane for optimization
            rotated = rotate_by_golden_angle(phi_coord, n=1, plane="LP")
            return [rotated.love, rotated.power, rotated.wisdom, rotated.justice]
        return [0.0, 0.0, 0.0, 0.0]
    
    def _calculate_overall_phi_alignment(self, coords: EnhancedSemanticCoordinates, 
                                       principle_analysis: Dict, phi_analysis: Dict) -> float:
        """Calculate overall alignment with phi-enhanced principles"""
        if not principle_analysis or not phi_analysis:
            return 0.5  # Default moderate alignment
        
        # Principle alignment average
        principle_alignment = np.mean([app['alignment'] for app in principle_analysis.values()])
        
        # Phi resonance
        phi_resonance = phi_analysis.get('phi_resonance', 0.5)
        
        # Anchor proximity (use nearest anchor)
        anchor_proximity = max(phi_analysis.get('nearest_anchors', {1: 0.5}).values())
        
        # Weighted combination
        overall = (principle_alignment * 0.4 + phi_resonance * 0.3 + anchor_proximity * 0.3)
        return min(1.0, max(0.0, overall))
    
    def navigate_phi_optimized_path(self, start_concept: str, 
                                   target_concept: str,
                                   optimization_strategy: str = "golden_spiral") -> Dict[str, Any]:
        """
        Navigate between concepts using phi-optimized paths
        
        Strategies:
        - golden_spiral: Follow golden spiral trajectory
        - fibonacci_stepping: Use Fibonacci-scaled steps
        - anchor_hopping: Navigate via dodecahedral anchors
        - golden_angle: Use golden angle rotations for direction
        """
        
        # Analyze both concepts
        start_analysis = self.analyze_concept_phi_enhanced(start_concept)
        target_analysis = self.analyze_concept_phi_enhanced(target_concept)
        
        if not PHI_ENGINE_AVAILABLE:
            return {
                'error': 'Phi-geometric engine not available',
                'start_concept': start_concept,
                'target_concept': target_concept
            }
        
        start_coords = start_analysis['enhanced_coordinates']
        target_coords = target_analysis['enhanced_coordinates']
        
        # Generate navigation path based on strategy
        if optimization_strategy == "golden_spiral":
            path = self._generate_spiral_path(start_coords, target_coords)
        elif optimization_strategy == "fibonacci_stepping":
            path = self._generate_fibonacci_path(start_coords, target_coords)
        elif optimization_strategy == "anchor_hopping":
            path = self._generate_anchor_path(start_coords, target_coords)
        elif optimization_strategy == "golden_angle":
            path = self._generate_golden_angle_path(start_coords, target_coords)
        else:
            path = self._generate_linear_path(start_coords, target_coords)
        
        return {
            'start_concept': start_concept,
            'target_concept': target_concept,
            'optimization_strategy': optimization_strategy,
            'path': path,
            'path_length': len(path),
            'total_distance': self._calculate_path_distance(path),
            'phi_efficiency': self._calculate_phi_efficiency(path),
            'start_analysis': start_analysis,
            'target_analysis': target_analysis
        }
    
    def _generate_spiral_path(self, start: EnhancedSemanticCoordinates, 
                            target: EnhancedSemanticCoordinates, 
                            num_points: int = 10) -> List[EnhancedSemanticCoordinates]:
        """Generate golden spiral path between two points"""
        path = [start]
        
        start_phi = start.to_phi_coordinate()
        target_phi = target.to_phi_coordinate()
        
        if not start_phi or not target_phi:
            return [start, target]
        
        # Calculate spiral parameters
        for i in range(1, num_points - 1):
            t = i / (num_points - 1)
            
            # Interpolate with golden spiral influence
            love = start.love + t * (target.love - start.love)
            power = start.power + t * (target.power - start.power)
            wisdom = start.wisdom + t * (target.wisdom - start.wisdom)
            justice = start.justice + t * (target.justice - start.justice)
            
            # Apply golden spiral rotation
            phi_coord = PhiCoordinate(love, power, wisdom, justice)
            rotated = rotate_by_golden_angle(phi_coord, n=i, plane="LP")
            
            # Blend with interpolation
            spiral_weight = 0.1 * math.sin(t * math.pi)
            love = love * (1 - spiral_weight) + rotated.love * spiral_weight
            power = power * (1 - spiral_weight) + rotated.power * spiral_weight
            wisdom = wisdom * (1 - spiral_weight) + rotated.wisdom * spiral_weight
            justice = justice * (1 - spiral_weight) + rotated.justice * spiral_weight
            
            path.append(EnhancedSemanticCoordinates(love, power, wisdom, justice))
        
        path.append(target)
        return path
    
    def _generate_fibonacci_path(self, start: EnhancedSemanticCoordinates, 
                               target: EnhancedSemanticCoordinates) -> List[EnhancedSemanticCoordinates]:
        """Generate Fibonacci-stepped path"""
        path = [start]
        
        # Use Fibonacci sequence for step sizes
        fib_steps = [1, 1, 2, 3, 5, 8, 13][:5]  # Use first 5 Fibonacci numbers
        total_steps = sum(fib_steps)
        
        current = start
        for step_size in fib_steps[:-1]:  # Exclude last step to reach target
            t = step_size / total_steps
            
            love = current.love + t * (target.love - start.love)
            power = current.power + t * (target.power - start.power)
            wisdom = current.wisdom + t * (target.wisdom - start.wisdom)
            justice = current.justice + t * (target.justice - start.justice)
            
            current = EnhancedSemanticCoordinates(love, power, wisdom, justice)
            path.append(current)
        
        path.append(target)
        return path
    
    def _generate_anchor_path(self, start: EnhancedSemanticCoordinates, 
                            target: EnhancedSemanticCoordinates) -> List[EnhancedSemanticCoordinates]:
        """Generate path via dodecahedral anchors"""
        path = [start]
        
        # Find nearest anchors to start and target
        start_nearest = max(start.anchor_proximity.items(), key=lambda x: x[1])[0] if start.anchor_proximity else 1
        target_nearest = max(target.anchor_proximity.items(), key=lambda x: x[1])[0] if target.anchor_proximity else 1
        
        if start_nearest != target_nearest:
            # Add intermediate anchor
            intermediate_anchor = self.dodecahedral_anchors.get_anchor((start_nearest + target_nearest) // 2)
            if intermediate_anchor:
                path.append(EnhancedSemanticCoordinates(
                    intermediate_anchor.love, intermediate_anchor.power,
                    intermediate_anchor.wisdom, intermediate_anchor.justice
                ))
        
        path.append(target)
        return path
    
    def _generate_golden_angle_path(self, start: EnhancedSemanticCoordinates, 
                                  target: EnhancedSemanticCoordinates) -> List[EnhancedSemanticCoordinates]:
        """Generate path using golden angle rotations"""
        path = [start]
        
        for i in range(1, 5):  # 4 intermediate steps
            t = i / 5.0
            
            # Linear interpolation with golden angle rotation
            love = start.love + t * (target.love - start.love)
            power = start.power + t * (target.power - start.power)
            wisdom = start.wisdom + t * (target.wisdom - start.wisdom)
            justice = start.justice + t * (target.justice - start.justice)
            
            # Apply golden angle rotation
            phi_coord = PhiCoordinate(love, power, wisdom, justice)
            rotated = rotate_by_golden_angle(phi_coord, n=i, plane="LW")
            
            path.append(EnhancedSemanticCoordinates(
                rotated.love, rotated.power, rotated.wisdom, rotated.justice
            ))
        
        path.append(target)
        return path
    
    def _generate_linear_path(self, start: EnhancedSemanticCoordinates, 
                            target: EnhancedSemanticCoordinates) -> List[EnhancedSemanticCoordinates]:
        """Generate simple linear path as fallback"""
        return [start, target]
    
    def _calculate_path_distance(self, path: List[EnhancedSemanticCoordinates]) -> float:
        """Calculate total path distance using golden spiral metric"""
        if not PHI_ENGINE_AVAILABLE or len(path) < 2:
            return 0.0
        
        total_distance = 0.0
        for i in range(len(path) - 1):
            phi1 = path[i].to_phi_coordinate()
            phi2 = path[i + 1].to_phi_coordinate()
            if phi1 and phi2:
                total_distance += golden_spiral_distance(phi1, phi2)
        
        return total_distance
    
    def _calculate_phi_efficiency(self, path: List[EnhancedSemanticCoordinates]) -> float:
        """Calculate how phi-efficient the path is"""
        if not path:
            return 0.0
        
        # Average phi resonance along path
        avg_phi_resonance = np.mean([coord.phi_resonance for coord in path])
        
        # Anchor proximity efficiency
        if path[0].anchor_proximity and path[-1].anchor_proximity:
            start_anchor_proximity = max(path[0].anchor_proximity.values())
            end_anchor_proximity = max(path[-1].anchor_proximity.values())
            anchor_efficiency = (start_anchor_proximity + end_anchor_proximity) / 2.0
        else:
            anchor_efficiency = 0.5
        
        # Overall efficiency
        efficiency = (avg_phi_resonance + anchor_efficiency) / 2.0
        return min(1.0, max(0.0, efficiency))
    
    def get_engine_status(self) -> Dict[str, Any]:
        """Get comprehensive engine status"""
        status = {
            'engine_version': self.engine_version,
            'primer_version': self.primmer_version,
            'phi_engine_available': PHI_ENGINE_AVAILABLE,
            'ice_engine_available': ICE_ENGINE_AVAILABLE,
            'baseline_engine_available': BASELINE_AVAILABLE,
            'universal_principles_count': len(self.universal_principles),
        }
        
        if PHI_ENGINE_AVAILABLE:
            status.update({
                'phi_constants': {
                    'PHI': PHI,
                    'PHI_INVERSE': PHI_INVERSE,
                    'GOLDEN_ANGLE_DEG': GOLDEN_ANGLE_DEG
                },
                'dodecahedral_anchors': 12,
                'fibonacci_sequence_length': len(self.fibonacci.sequence) if hasattr(self, 'fibonacci') else 0
            })
        
        return status


# Demonstration function
def demonstrate_phi_enhanced_engine():
    """Demonstrate the phi-enhanced semantic engine"""
    
    print("=" * 80)
    print("PHI-ENHANCED SEMANTIC SUBSTRATE ENGINE")
    print("Integrated with Primer 1.5 and Golden Ratio Mathematics")
    print("=" * 80)
    
    # Initialize engine
    engine = PhiEnhancedSemanticEngine()
    
    # Show status
    status = engine.get_engine_status()
    print(f"Engine Version: {status['engine_version']}")
    print(f"Primer Version: {status['primer_version']}")
    print(f"Phi Engine: {'Available' if status['phi_engine_available'] else 'Unavailable'}")
    print(f"ICE Engine: {'Available' if status['ice_engine_available'] else 'Unavailable'}")
    print(f"Universal Principles: {status['universal_principles_count']}")
    
    if 'phi_constants' in status:
        print(f"PHI: {status['phi_constants']['PHI']:.10f}")
        print(f"Golden Angle: {status['phi_constants']['GOLDEN_ANGLE_DEG']:.6f}°")
    
    # Test concept analysis
    print(f"\n[PHI-ENHANCED CONCEPT ANALYSIS]")
    print("-" * 50)
    
    test_concepts = [
        "divine wisdom and eternal love",
        "sacred geometry and golden ratio",
        "justice and mercy in harmony",
        "spiritual transformation"
    ]
    
    for concept in test_concepts:
        analysis = engine.analyze_concept_phi_enhanced(concept)
        print(f"\nConcept: {concept}")
        print(f"  Overall Phi Alignment: {analysis['overall_phi_alignment']:.3f}")
        print(f"  Phi Resonance: {analysis['phi_geometric_analysis'].get('phi_resonance', 0):.3f}")
        print(f"  Fibonacci Index: {analysis['phi_geometric_analysis'].get('fibonacci_index', 0)}")
        print(f"  Nearest Anchor: #{analysis['phi_geometric_analysis'].get('nearest_anchor_id', 1)}")
        
        if 'distance_analysis' in analysis:
            print(f"  Golden Spiral Distance: {analysis['distance_analysis'].get('golden_spiral_distance', 0):.4f}")
            print(f"  Preferred Metric: {analysis['distance_analysis'].get('preferred_metric', 'unknown')}")
    
    # Test navigation
    print(f"\n[PHI-OPTIMIZED NAVIGATION]")
    print("-" * 50)
    
    start_concept = "confusion and chaos"
    target_concept = "divine order and wisdom"
    
    strategies = ["golden_spiral", "fibonacci_stepping", "anchor_hopping", "golden_angle"]
    
    for strategy in strategies:
        navigation = engine.navigate_phi_optimized_path(start_concept, target_concept, strategy)
        print(f"\nStrategy: {strategy}")
        print(f"  Path Length: {navigation['path_length']} points")
        print(f"  Total Distance: {navigation['total_distance']:.4f}")
        print(f"  Phi Efficiency: {navigation['phi_efficiency']:.3f}")
    
    print(f"\n" + "=" * 80)
    print("PHI-ENHANCED SEMANTIC ENGINE - FULLY OPERATIONAL")
    print("Bridging Semantic Substrate Primer 1.5 with Golden Ratio Mathematics")
    print("=" * 80)
    
    return engine


if __name__ == "__main__":
    engine = demonstrate_phi_enhanced_engine()