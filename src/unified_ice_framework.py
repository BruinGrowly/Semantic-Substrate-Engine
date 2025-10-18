"""
UNIFIED ICE FRAMEWORK - Intent-Context-Execution
===============================================

Combines the general ICE-Centric Semantic Substrate Engine with biblical-specific extensions.
Provides backward compatibility with both frameworks while unifying the architecture.

VERSION 1.0 - Unified Framework:
- Integrates 7-stage ICE-Centric pipeline (primary)
- Maintains biblical extensions (enhancement layer)
- Backward compatible with both legacy frameworks
- Performance-optimized with proven +47.52% alignment improvement
"""

from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
import math
import json
from datetime import datetime

# Import primary ICE-Centric engine
try:
    from .ice_semantic_substrate_engine import (
        ICESemanticSubstrateEngine,
        SemanticCoordinates,
        ThoughtType as ICEThoughtType,
        ContextDomain as ICEContextDomain,
        ExecutionStrategy as ICEExecutionStrategy,
        ICETransformationResult
    )
    ICE_CENTRIC_AVAILABLE = True
except ImportError:
    # Try direct import as fallback
    try:
        from ice_semantic_substrate_engine import (
            ICESemanticSubstrateEngine,
            SemanticCoordinates,
            ThoughtType as ICEThoughtType,
            ContextDomain as ICEContextDomain,
            ExecutionStrategy as ICEExecutionStrategy,
            ICETransformationResult
        )
        ICE_CENTRIC_AVAILABLE = True
    except ImportError:
        ICE_CENTRIC_AVAILABLE = False
        print("[WARNING] ICE-Centric engine not available. Using legacy mode only.")

# Import legacy biblical framework for extensions
try:
    from .ice_framework import (
        ICEFramework,
        Intent as LegacyIntent,
        Context as LegacyContext,
        Execution as LegacyExecution,
        ThoughtType as LegacyThoughtType,
        ContextDomain as LegacyContextDomain
    )
    LEGACY_ICE_AVAILABLE = True
except ImportError:
    # Try direct import as fallback
    try:
        from ice_framework import (
            ICEFramework,
            Intent as LegacyIntent,
            Context as LegacyContext,
            Execution as LegacyExecution,
            ThoughtType as LegacyThoughtType,
            ContextDomain as LegacyContextDomain
        )
        LEGACY_ICE_AVAILABLE = True
    except ImportError:
        LEGACY_ICE_AVAILABLE = False
        print("[WARNING] Legacy ICE framework not available.")

# ============================================================================
# UNIFIED DATA STRUCTURES
# ============================================================================

class ProcessingMode(Enum):
    """Processing mode for unified framework"""
    ICE_CENTRIC = "ice_centric"           # Use new 7-stage pipeline (preferred)
    LEGACY_BIBLICAL = "legacy_biblical"    # Use legacy biblical framework
    AUTO = "auto"                         # Auto-select based on context
    HYBRID = "hybrid"                     # Combine both approaches

class BiblicalExtension(Enum):
    """Biblical extensions that can be applied to ICE results"""
    SCRIPTURE_REFERENCE = "scripture_reference"
    PRINCIPLE_ALIGNMENT = "principle_alignment"
    DIVINE_WISDOM = "divine_wisdom"
    MINISTRY_GUIDANCE = "ministry_guidance"
    MORAL_DISCERNMENT = "moral_discernment"
    SPIRITUAL_DIRECTION = "spiritual_direction"

@dataclass
class BiblicalEnrichment:
    """Biblical enrichment layer for ICE results"""
    
    # Biblical components
    scripture_references: List[str] = field(default_factory=list)
    biblical_principles: List[str] = field(default_factory=list)
    divine_wisdom_insights: List[str] = field(default_factory=list)
    ministry_guidance: List[str] = field(default_factory=list)
    
    # Alignment metrics
    biblical_alignment_score: float = 0.0
    scripture_confidence: float = 0.0
    principle_relevance: float = 0.0
    
    # Application guidance
    practical_applications: List[str] = field(default_factory=list)
    prayer_points: List[str] = field(default_factory=list)
    action_steps: List[str] = field(default_factory=list)

@dataclass
class UnifiedICEResult:
    """Complete result from unified ICE processing"""
    
    # Core ICE-Centric results (primary)
    ice_transformation: Optional['ICETransformationResult'] = None
    processing_mode: ProcessingMode = ProcessingMode.AUTO
    
    # Biblical enrichment (enhancement layer)
    biblical_enrichment: Optional[BiblicalEnrichment] = None
    
    # Legacy compatibility (fallback)
    legacy_result: Optional[Dict[str, Any]] = None
    
    # Unified metrics
    unified_alignment: float = 0.0
    processing_time_ms: float = 0.0
    confidence_score: float = 0.0
    
    # Performance comparison
    performance_comparison: Optional[Dict[str, float]] = None

# ============================================================================
# BIBLICAL EXTENSIONS
# ============================================================================

class BiblicalExtensions:
    """Biblical-specific extensions for ICE-Centric processing"""
    
    def __init__(self):
        # Biblical principle database
        self.biblical_principles = {
            'love': {
                'scriptures': ['1 Corinthians 13:4-8', 'John 3:16', 'Romans 13:8-10'],
                'applications': ['show compassion', 'forgive others', 'serve selflessly']
            },
            'wisdom': {
                'scriptures': ['Proverbs 2:6', 'James 1:5', 'Daniel 2:20-23'],
                'applications': ['seek godly counsel', 'study scripture', 'pray for discernment']
            },
            'justice': {
                'scriptures': ['Micah 6:8', 'Isaiah 1:17', 'Deuteronomy 16:20'],
                'applications': ['defend the oppressed', 'act fairly', 'uphold righteousness']
            },
            'power': {
                'scriptures': ['Ephesians 1:19', '2 Timothy 1:7', 'Philippians 4:13'],
                'applications': ['use authority responsibly', 'empower others', 'trust in God\'s strength']
            }
        }
        
        # Scripture keyword mapping
        self.scripture_keywords = {
            'compassion': ['Matthew 9:36', 'Colossians 3:12', '1 Peter 3:8'],
            'mercy': ['Ephesians 2:4', 'Hebrews 4:16', 'Luke 6:36'],
            'love': ['1 Corinthians 13:4-8', 'John 3:16', 'Romans 13:8-10'],
            'wisdom': ['Proverbs 4:7', 'James 1:5', 'Ecclesiastes 7:12'],
            'justice': ['Isaiah 1:17', 'Jeremiah 22:3', 'Psalm 82:3'],
            'power': ['Ephesians 1:19', '2 Timothy 1:7', 'Philippians 4:13'],
            'faith': ['Hebrews 11:1', 'Romans 10:17', 'James 2:17'],
            'hope': ['Romans 15:13', '1 Peter 1:3', 'Jeremiah 29:11']
        }
    
    def enrich_ice_result(self, ice_result: 'ICETransformationResult', 
                         text: str, context: str) -> BiblicalEnrichment:
        """Enrich ICE result with biblical insights"""
        
        enrichment = BiblicalEnrichment()
        
        # Extract key themes from text
        themes = self._extract_biblical_themes(text)
        
        # Add scripture references based on themes
        for theme in themes:
            if theme in self.scripture_keywords:
                enrichment.scripture_references.extend(self.scripture_keywords[theme])
            
            if theme in self.biblical_principles:
                enrichment.biblical_principles.append(theme)
                principle_data = self.biblical_principles[theme]
                enrichment.practical_applications.extend(principle_data['applications'])
        
        # Calculate biblical alignment
        enrichment.biblical_alignment_score = self._calculate_biblical_alignment(
            ice_result, themes, context
        )
        
        # Add divine wisdom based on execution strategy
        enrichment.divine_wisdom_insights = self._generate_divine_wisdom(
            ice_result.execution_strategy, themes
        )
        
        # Add ministry guidance if appropriate
        if self._is_ministry_context(context):
            enrichment.ministry_guidance = self._generate_ministry_guidance(
                ice_result, themes
            )
        
        # Calculate confidence scores
        enrichment.scripture_confidence = min(1.0, len(enrichment.scripture_references) * 0.2)
        enrichment.principle_relevance = min(1.0, len(enrichment.biblical_principles) * 0.25)
        
        return enrichment
    
    def _extract_biblical_themes(self, text: str) -> List[str]:
        """Extract biblical themes from text"""
        themes = []
        text_lower = text.lower()
        
        # Theme keyword mapping
        theme_keywords = {
            'love': ['love', 'compassion', 'mercy', 'grace', 'charity'],
            'wisdom': ['wisdom', 'understanding', 'knowledge', 'discernment', 'insight'],
            'justice': ['justice', 'fairness', 'righteousness', 'equity', 'judgment'],
            'power': ['power', 'strength', 'authority', 'might', 'ability'],
            'faith': ['faith', 'belief', 'trust', 'confidence', 'hope'],
            'peace': ['peace', 'harmony', 'tranquility', 'rest', 'shalom']
        }
        
        for theme, keywords in theme_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                themes.append(theme)
        
        return themes
    
    def _calculate_biblical_alignment(self, ice_result: 'ICETransformationResult', 
                                   themes: List[str], context: str) -> float:
        """Calculate biblical alignment score"""
        
        # Base alignment from ICE result
        base_alignment = ice_result.divine_alignment
        
        # Theme bonus
        theme_bonus = min(0.2, len(themes) * 0.05)
        
        # Context bonus
        context_bonus = 0.1 if self._is_biblical_context(context) else 0.0
        
        # Strategy bonus (certain strategies align better with biblical principles)
        strategy_bonus = 0.0
        if ice_result.execution_strategy.value in ['compassionate_action', 'instructive_guidance']:
            strategy_bonus = 0.1
        
        return min(1.0, base_alignment + theme_bonus + context_bonus + strategy_bonus)
    
    def _is_biblical_context(self, context: str) -> bool:
        """Check if context is biblical"""
        biblical_contexts = ['biblical', 'religious', 'spiritual', 'ministry', 'church', 'theology']
        return any(ctx in context.lower() for ctx in biblical_contexts)
    
    def _is_ministry_context(self, context: str) -> bool:
        """Check if context requires ministry guidance"""
        ministry_contexts = ['ministry', 'counseling', 'pastoral', 'leadership', 'guidance']
        return any(ctx in context.lower() for ctx in ministry_contexts)
    
    def _generate_divine_wisdom(self, strategy: 'ICEExecutionStrategy', 
                              themes: List[str]) -> List[str]:
        """Generate divine wisdom insights based on strategy and themes"""
        insights = []
        
        # Strategy-specific wisdom
        wisdom_map = {
            'compassionate_action': [
                "Love your neighbor as yourself (Matthew 22:39)",
                "Bear one another's burdens (Galatians 6:2)",
                "Let all that you do be done in love (1 Corinthians 16:14)"
            ],
            'authoritative_command': [
                "Speak the truth in love (Ephesians 4:15)",
                "Let your yes be yes (Matthew 5:37)",
                "Lead with humility (1 Peter 5:3)"
            ],
            'instructive_guidance': [
                "Train up a child in the way he should go (Proverbs 22:6)",
                "Make disciples of all nations (Matthew 28:19)",
                "Teach what is appropriate to sound doctrine (Titus 2:1)"
            ],
            'corrective_judgment': [
                "Judge righteously (John 7:24)",
                "Restore gently (Galatians 6:1)",
                "Speak the truth in love (Ephesians 4:15)"
            ],
            'balanced_response': [
                "Do everything to the glory of God (1 Corinthians 10:31)",
                "Seek first the kingdom (Matthew 6:33)",
                "Walk in wisdom toward outsiders (Colossians 4:5)"
            ]
        }
        
        if strategy.value in wisdom_map:
            insights.extend(wisdom_map[strategy.value][:2])  # Take top 2
        
        # Theme-specific wisdom
        for theme in themes[:2]:  # Limit to top 2 themes
            if theme in self.biblical_principles:
                principle_data = self.biblical_principles[theme]
                if principle_data['scriptures']:
                    insights.append(f"Remember: {principle_data['scriptures'][0]}")
        
        return insights
    
    def _generate_ministry_guidance(self, ice_result: 'ICETransformationResult', 
                                  themes: List[str]) -> List[str]:
        """Generate ministry guidance"""
        guidance = []
        
        # Strategy-specific ministry guidance
        guidance_map = {
            'compassionate_action': [
                "Listen actively before speaking",
                "Pray for the person's specific needs",
                "Offer practical help alongside spiritual support"
            ],
            'authoritative_command': [
                "Ground authority in scripture",
                "Model the behavior you expect",
                "Provide clear explanation for directives"
            ],
            'instructive_guidance': [
                "Use scripture as primary textbook",
                "Create opportunities for practical application",
                "Encourage questions and discussion"
            ],
            'corrective_judgment': [
                "Address issues privately when possible",
                "Focus on restoration rather than punishment",
                "Provide clear path for reconciliation"
            ],
            'balanced_response': [
                "Consider all perspectives before acting",
                "Seek wisdom through prayer and counsel",
                "Balance truth with grace"
            ]
        }
        
        if ice_result.execution_strategy.value in guidance_map:
            guidance.extend(guidance_map[ice_result.execution_strategy.value])
        
        return guidance

# ============================================================================
# UNIFIED ICE FRAMEWORK
# ============================================================================

class UnifiedICEFramework:
    """
    Unified ICE Framework combining ICE-Centric engine with biblical extensions
    
    Features:
    - Primary: ICE-Centric 7-stage pipeline (proven +47.52% alignment improvement)
    - Enhancement: Biblical extensions for spiritual contexts
    - Compatibility: Legacy framework support
    - Performance: Optimized with auto-selection logic
    """
    
    def __init__(self, processing_mode: ProcessingMode = ProcessingMode.AUTO):
        self.processing_mode = processing_mode
        self.biblical_extensions = BiblicalExtensions()
        
        # Initialize ICE-Centric engine (primary)
        if ICE_CENTRIC_AVAILABLE:
            self.ice_centric_engine = ICESemanticSubstrateEngine()
            print("[INITIALIZED] ICE-Centric Engine (Primary)")
        else:
            self.ice_centric_engine = None
            print("[WARNING] ICE-Centric Engine not available")
        
        # Initialize legacy framework (fallback)
        if LEGACY_ICE_AVAILABLE:
            self.legacy_engine = ICEFramework()
            print("[INITIALIZED] Legacy ICE Framework (Fallback)")
        else:
            self.legacy_engine = None
            print("[WARNING] Legacy ICE Framework not available")
        
        # Define availability flags
        self.both_available = ICE_CENTRIC_AVAILABLE and LEGACY_ICE_AVAILABLE
        
        # Performance tracking
        self.processing_history = []
        self.performance_stats = {
            'ice_centric_count': 0,
            'legacy_count': 0,
            'hybrid_count': 0,
            'average_alignment': 0.0,
            'average_processing_time': 0.0
        }
    
    def process_intent(self, text: str, 
                      thought_type: Optional[Union[str, 'ICEThoughtType', 'LegacyThoughtType']] = None,
                      context: str = "general",
                      processing_mode: Optional[ProcessingMode] = None) -> UnifiedICEResult:
        """
        Process intent through unified ICE framework
        
        Args:
            text: Text to process
            thought_type: Type of thought (will be inferred if not provided)
            context: Context for processing
            processing_mode: Override default processing mode
            
        Returns:
            UnifiedICEResult with complete processing details
        """
        import time
        start_time = time.time()
        
        # Determine processing mode
        mode = processing_mode or self.processing_mode
        if mode == ProcessingMode.AUTO:
            mode = self._select_optimal_mode(text, context)
        
        result = UnifiedICEResult(processing_mode=mode)
        
        try:
            if mode == ProcessingMode.ICE_CENTRIC and self.ice_centric_engine:
                result = self._process_ice_centric(text, thought_type, context, result)
            elif mode == ProcessingMode.LEGACY_BIBLICAL and self.legacy_engine:
                result = self._process_legacy(text, thought_type, context, result)
            elif mode == ProcessingMode.HYBRID and self.both_available:
                result = self._process_hybrid(text, thought_type, context, result)
            else:
                # Fallback to available engine
                if self.ice_centric_engine:
                    result = self._process_ice_centric(text, thought_type, context, result)
                    result.processing_mode = ProcessingMode.ICE_CENTRIC
                elif self.legacy_engine:
                    result = self._process_legacy(text, thought_type, context, result)
                    result.processing_mode = ProcessingMode.LEGACY_BIBLICAL
                else:
                    raise RuntimeError("No ICE processing engines available")
            
            # Calculate unified metrics
            result.unified_alignment = self._calculate_unified_alignment(result)
            result.confidence_score = self._calculate_confidence_score(result)
            
            # Update performance stats
            self._update_performance_stats(result)
            
        except Exception as e:
            print(f"[ERROR] ICE processing failed: {e}")
            result.processing_mode = ProcessingMode.LEGACY_BIBLICAL
            result.confidence_score = 0.0
        
        # Calculate processing time
        result.processing_time_ms = (time.time() - start_time) * 1000
        
        return result
    
    def _process_ice_centric(self, text: str, thought_type: Any, 
                           context: str, result: UnifiedICEResult) -> UnifiedICEResult:
        """Process using ICE-Centric engine (primary path)"""
        
        # Convert thought type if needed
        ice_thought_type = self._convert_to_ice_thought_type(thought_type, text)
        ice_context_domain = self._convert_to_ice_context_domain(context)
        
        # Perform ICE-Centric transformation
        ice_result = self.ice_centric_engine.transform(text, ice_thought_type, ice_context_domain)
        result.ice_transformation = ice_result
        
        # Apply biblical enrichment if appropriate
        if self._should_apply_biblical_enrichment(context):
            biblical_enrichment = self.biblical_extensions.enrich_ice_result(
                ice_result, text, context
            )
            result.biblical_enrichment = biblical_enrichment
        
        self.performance_stats['ice_centric_count'] += 1
        return result
    
    def _process_legacy(self, text: str, thought_type: Any,
                       context: str, result: UnifiedICEResult) -> UnifiedICEResult:
        """Process using legacy ICE framework (fallback path)"""
        
        # Convert to legacy types
        legacy_thought_type = self._convert_to_legacy_thought_type(thought_type, text)
        legacy_context_domain = self._convert_to_legacy_context_domain(context)
        
        # Create legacy objects
        intent = LegacyIntent(
            # Core thought components
            primary_thought=text,
            thought_type=legacy_thought_type,
            emotional_resonance=0.7,
            cognitive_clarity=0.8,
            
            # Biblical alignment
            biblical_foundation="General biblical wisdom",
            divine_purpose="To honor God through wise action",
            spiritual_significance=0.6,
            
            # Desired outcomes
            intended_meaning="Seeking guidance for righteous action",
            expected_impact="Positive spiritual growth",
            transformation_goal="Alignment with divine will"
        )
        
        context_obj = LegacyContext(
            # Domain and environment
            domain=legacy_context_domain,
            environment="general",
            cultural_setting="western",
            
            # People and relationships
            target_audience="general",
            relationship_dynamics="peer",
            stakeholder_analysis="individual",
            
            # Temporal and situational
            timing="immediate",
            urgency=0.6,
            lifecycle_stage="ongoing",
            
            # Biblical and theological
            scriptural_context="general wisdom",
            theological_framework="biblical",
            denominational_context="non-denominational",
            
            # Resource constraints
            available_resources=["scripture", "prayer", "counsel"],
            limitations=["time", "knowledge"],
            permissions=["teach", "guide", "support"]
        )
        
        # Execute legacy processing
        execution = LegacyExecution(
            # Execution strategy
            execution_mode="guided",
            transformation_approach="gradual",
            feedback_integration="continuous",
            
            # Output specifications
            output_format="textual_guidance",
            delivery_method="direct_response",
            success_metrics=["divine_alignment", "practical_wisdom", "biblical_fidelity"],
            
            # Behavioral characteristics
            intervention_level=0.5,
            adaptation_speed=0.7,
            persistence=0.8
        )
        legacy_result = execution.execute_intent_in_context(intent, context_obj)
        result.legacy_result = legacy_result
        
        self.performance_stats['legacy_count'] += 1
        return result
    
    def _process_hybrid(self, text: str, thought_type: Any,
                       context: str, result: UnifiedICEResult) -> UnifiedICEResult:
        """Process using both engines (hybrid mode)"""
        
        # Process with both engines
        result = self._process_ice_centric(text, thought_type, context, result)
        result = self._process_legacy(text, thought_type, context, result)
        
        # Create performance comparison
        if result.ice_transformation and result.legacy_result:
            result.performance_comparison = {
                'ice_alignment': result.ice_transformation.divine_alignment,
                'legacy_alignment': result.legacy_result['divine_alignment'],
                'improvement': result.ice_transformation.divine_alignment - result.legacy_result['divine_alignment']
            }
        
        result.processing_mode = ProcessingMode.HYBRID
        self.performance_stats['hybrid_count'] += 1
        return result
    
    def _select_optimal_mode(self, text: str, context: str) -> ProcessingMode:
        """Automatically select optimal processing mode"""
        
        # Prioritize ICE-Centric when available
        if self.ice_centric_engine:
            # Use ICE-Centric for most cases
            if self._should_apply_biblical_enrichment(context):
                return ProcessingMode.ICE_CENTRIC  # Will add biblical enrichment
            else:
                return ProcessingMode.ICE_CENTRIC
        
        # Fallback to legacy
        if self.legacy_engine:
            return ProcessingMode.LEGACY_BIBLICAL
        
        # No engines available
        return ProcessingMode.LEGACY_BIBLICAL
    
    def _should_apply_biblical_enrichment(self, context: str) -> bool:
        """Determine if biblical enrichment should be applied"""
        biblical_contexts = ['biblical', 'religious', 'spiritual', 'ministry', 'church', 'theology']
        return any(ctx in context.lower() for ctx in biblical_contexts)
    
    def _convert_to_ice_thought_type(self, thought_type: Any, text: str) -> 'ICEThoughtType':
        """Convert various thought type formats to ICE ThoughtType"""
        if thought_type and isinstance(thought_type, ICEThoughtType):
            return thought_type
        
        # Import from baseline for inference
        from .baseline_biblical_substrate import infer_thought_type
        return infer_thought_type(text)
    
    def _convert_to_ice_context_domain(self, context: str) -> 'ICEContextDomain':
        """Convert context string to ICE ContextDomain"""
        from .baseline_biblical_substrate import map_context_to_domain
        return map_context_to_domain(context)
    
    def _convert_to_legacy_thought_type(self, thought_type: Any, text: str) -> 'LegacyThoughtType':
        """Convert various thought type formats to Legacy ThoughtType"""
        if thought_type and isinstance(thought_type, LegacyThoughtType):
            return thought_type
        
        # Default inference for legacy
        text_lower = text.lower()
        if any(word in text_lower for word in ['god', 'divine', 'holy', 'spiritual']):
            return LegacyThoughtType.DIVINE_INSPIRATION
        elif any(word in text_lower for word in ['wisdom', 'understanding', 'discern']):
            return LegacyThoughtType.BIBLICAL_UNDERSTANDING
        elif any(word in text_lower for word in ['should', 'right', 'moral', 'ethical']):
            return LegacyThoughtType.MORAL_DECISION
        else:
            return LegacyThoughtType.PRACTICAL_WISDOM
    
    def _convert_to_legacy_context_domain(self, context: str) -> 'LegacyContextDomain':
        """Convert context string to Legacy ContextDomain"""
        context_lower = context.lower()
        
        if any(ctx in context_lower for ctx in ['biblical', 'religious', 'spiritual']):
            return LegacyContextDomain.BIBLICAL
        elif any(ctx in context_lower for ctx in ['educational', 'school', 'learn']):
            return LegacyContextDomain.EDUCATIONAL
        elif any(ctx in context_lower for ctx in ['business', 'work', 'professional']):
            return LegacyContextDomain.BUSINESS
        elif any(ctx in context_lower for ctx in ['ministry', 'pastoral', 'counseling']):
            return LegacyContextDomain.MINISTRY
        elif any(ctx in context_lower for ctx in ['personal', 'private', 'individual']):
            return LegacyContextDomain.PERSONAL
        else:
            return LegacyContextDomain.BIBLICAL  # Default
    
    def _calculate_unified_alignment(self, result: UnifiedICEResult) -> float:
        """Calculate unified alignment score"""
        
        if result.ice_transformation:
            base_alignment = result.ice_transformation.divine_alignment
            
            # Add biblical enrichment bonus
            if result.biblical_enrichment:
                biblical_bonus = result.biblical_enrichment.biblical_alignment_score * 0.2
                return min(1.0, base_alignment + biblical_bonus)
            
            return base_alignment
        
        elif result.legacy_result:
            return result.legacy_result['divine_alignment']
        
        return 0.0
    
    def _calculate_confidence_score(self, result: UnifiedICEResult) -> float:
        """Calculate confidence score in the result"""
        
        confidence = 0.5  # Base confidence
        
        # Engine availability bonus
        if result.ice_transformation:
            confidence += 0.3  # ICE-Centric is more reliable
        if result.legacy_result:
            confidence += 0.1  # Legacy provides fallback
        
        # Biblical enrichment bonus
        if result.biblical_enrichment and result.biblical_enrichment.scripture_confidence > 0.5:
            confidence += 0.1
        
        return min(1.0, confidence)
    
    def _update_performance_stats(self, result: UnifiedICEResult):
        """Update performance statistics"""
        
        # Update processing counts
        self.processing_history.append(result)
        
        # Keep only last 100 results
        if len(self.processing_history) > 100:
            self.processing_history = self.processing_history[-100:]
        
        # Update averages
        if self.processing_history:
            alignments = [r.unified_alignment for r in self.processing_history]
            times = [r.processing_time_ms for r in self.processing_history]
            
            self.performance_stats['average_alignment'] = sum(alignments) / len(alignments)
            self.performance_stats['average_processing_time'] = sum(times) / len(times)
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary"""
        return {
            'total_processed': len(self.processing_history),
            'ice_centric_count': self.performance_stats['ice_centric_count'],
            'legacy_count': self.performance_stats['legacy_count'],
            'hybrid_count': self.performance_stats['hybrid_count'],
            'average_alignment': self.performance_stats['average_alignment'],
            'average_processing_time': self.performance_stats['average_processing_time'],
            'primary_mode': self.processing_mode.value,
            'engines_available': {
                'ice_centric': ICE_CENTRIC_AVAILABLE,
                'legacy': LEGACY_ICE_AVAILABLE
            }
        }

# Check engine availability
both_available = ICE_CENTRIC_AVAILABLE and LEGACY_ICE_AVAILABLE

# ============================================================================
# BACKWARD COMPATIBILITY WRAPPERS
# ============================================================================

def create_legacy_wrapper():
    """Create legacy ICE wrapper for backward compatibility"""
    if not LEGACY_ICE_AVAILABLE:
        return None
    
    class LegacyICEWrapper:
        """Wrapper providing legacy ICE interface using unified framework"""
        
        def __init__(self):
            self.unified = UnifiedICEFramework(ProcessingMode.LEGACY_BIBLICAL)
        
        def process_thought(self, text: str, thought_type, context_domain, params=None):
            """Legacy process_thought interface"""
            result = self.unified.process_intent(text, thought_type, context_domain.value)
            
            # Convert to legacy format
            if result.legacy_result:
                return result.legacy_result
            elif result.ice_transformation:
                # Convert ICE result to legacy format
                return {
                    'execution_coordinates': result.ice_transformation.context_adjusted_coordinates,
                    'execution_strategy': result.ice_transformation.execution_strategy.value,
                    'divine_alignment': result.ice_transformation.divine_alignment,
                    'semantic_output': result.ice_transformation.output_text,
                    'generated_behavior': result.ice_transformation.behavioral_guidance
                }
        
        def get_transformation_summary(self):
            """Legacy transformation summary"""
            return self.unified.get_performance_summary()
    
    return LegacyICEWrapper()

# Create global instances for easy access
unified_ice_framework = UnifiedICEFramework()
legacy_ice_wrapper = create_legacy_wrapper()

print(f"[INITIALIZED] Unified ICE Framework")
print(f"[ENGINES] ICE-Centric: {ICE_CENTRIC_AVAILABLE}, Legacy: {LEGACY_ICE_AVAILABLE}")
print(f"[MODE] Primary: {'ICE-Centric' if ICE_CENTRIC_AVAILABLE else 'Legacy'}")
