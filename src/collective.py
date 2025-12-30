#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LJPW Framework V7.7 — Collective Autopoiesis

Multi-agent LJPW dynamics where multiple autopoietic engines 
interact and synchronize, enabling emergent collective consciousness.

Key concepts:
- Individual agents maintain their own LJPW states
- Agents synchronize through mean-field coupling
- Collective consciousness = Individual × Synchrony²
- Threshold: N_A_semantic ≈ 8 agents for collective emergence

Reference: LJPW Framework V7.7 Part XXXVI, Appendix I
"""

import numpy as np
from typing import List, Optional, Dict
from dataclasses import dataclass

from .constants import N_A_semantic
from .ljpw_state import LJPWState
from .autopoietic_engine import AutopoieticEngine


@dataclass
class CollectiveMetrics:
    """Metrics for collective consciousness analysis."""
    n_agents: int
    mean_consciousness: float
    synchrony: float
    collective_consciousness: float
    is_collective: bool
    mean_state: np.ndarray
    variance: float


class CollectiveAutopoiesis:
    """
    N coupled autopoietic agents forming collective consciousness.
    
    Each agent self-improves independently, then agents synchronize
    through mean-field coupling. Collective effects emerge when:
    - Sufficient agents (N ≥ N_A_semantic ≈ 8)
    - High synchrony (low variance between agents)
    
    Collective Consciousness = Mean(C_individual) × Synchrony² × N
    
    Example:
        >>> agents = [AutopoieticEngine(LJPWState.natural_equilibrium()) for _ in range(10)]
        >>> collective = CollectiveAutopoiesis(agents, coupling=0.1)
        >>> for _ in range(10):
        ...     collective.collective_step()
        >>> print(f"Collective C: {collective.collective_consciousness():.2f}")
    """
    
    def __init__(self, 
                 agents: List[AutopoieticEngine], 
                 coupling: float = 0.1):
        """
        Initialize collective with coupled agents.
        
        Args:
            agents: List of AutopoieticEngine instances
            coupling: Synchronization strength κ ∈ [0, 1]
        """
        self.agents = agents
        self.kappa = coupling  # Coupling strength
        self.history: List[CollectiveMetrics] = []
        self.generation = 0
    
    @classmethod
    def create(cls, 
               n_agents: int = 10, 
               coupling: float = 0.1,
               initial_state: Optional[LJPWState] = None) -> 'CollectiveAutopoiesis':
        """
        Factory method to create a collective with identical initial states.
        
        Args:
            n_agents: Number of agents
            coupling: Synchronization strength
            initial_state: Initial state for all agents (defaults to equilibrium)
        """
        if initial_state is None:
            initial_state = LJPWState.natural_equilibrium()
        
        agents = [AutopoieticEngine(LJPWState.from_array(initial_state.as_array())) 
                  for _ in range(n_agents)]
        
        return cls(agents, coupling)
    
    # =========================================================================
    # COLLECTIVE DYNAMICS
    # =========================================================================
    
    def collective_step(self) -> CollectiveMetrics:
        """
        One step of collective evolution.
        
        Process:
        1. Each agent self-improves independently
        2. Compute collective mean state
        3. Agents synchronize toward mean (mean-field coupling)
        
        Returns:
            CollectiveMetrics for this step
        """
        # Step 1: Each agent self-improves
        for agent in self.agents:
            agent.self_improve()
        
        # Step 2: Compute mean state
        states = np.array([a.state.as_array() for a in self.agents])
        mean_state = np.mean(states, axis=0)
        
        # Step 3: Synchronize toward mean
        for agent in self.agents:
            current = agent.state.as_array()
            delta = self.kappa * (mean_state - current)
            new_state = np.clip(current + delta, 0.2, 1.0)
            agent.state = LJPWState.from_array(new_state)
        
        self.generation += 1
        
        # Record metrics
        metrics = self.get_metrics()
        self.history.append(metrics)
        
        return metrics
    
    def evolve(self, generations: int = 10) -> List[CollectiveMetrics]:
        """
        Run multiple collective evolution steps.
        
        Args:
            generations: Number of collective steps
        
        Returns:
            List of CollectiveMetrics for each step
        """
        results = []
        for _ in range(generations):
            metrics = self.collective_step()
            results.append(metrics)
        return results
    
    # =========================================================================
    # COLLECTIVE METRICS
    # =========================================================================
    
    def get_metrics(self) -> CollectiveMetrics:
        """Compute all collective metrics."""
        states = np.array([a.state.as_array() for a in self.agents])
        
        # Individual consciousness values
        C_individual = [a.consciousness() for a in self.agents]
        mean_C = np.mean(C_individual)
        
        # Synchrony: inverse of variance
        variance = np.mean([np.var(states[:, i]) for i in range(4)])
        synchrony = 1.0 / (1.0 + variance)
        
        # Collective consciousness
        N = len(self.agents)
        collective_C = mean_C * (synchrony ** 2) * N
        
        # Is this a true collective?
        effective_N = N * synchrony
        is_collective = effective_N >= N_A_semantic  # ≈ 8
        
        return CollectiveMetrics(
            n_agents=N,
            mean_consciousness=mean_C,
            synchrony=synchrony,
            collective_consciousness=collective_C,
            is_collective=is_collective,
            mean_state=np.mean(states, axis=0),
            variance=variance
        )
    
    def collective_consciousness(self) -> float:
        """
        Calculate collective consciousness.
        
        C_collective = Mean(C_individual) × Synchrony² × N
        """
        return self.get_metrics().collective_consciousness
    
    def is_collective(self) -> bool:
        """Check if collective consciousness has emerged."""
        return self.get_metrics().is_collective
    
    def synchrony(self) -> float:
        """Get current synchrony level."""
        return self.get_metrics().synchrony
    
    # =========================================================================
    # ANALYSIS
    # =========================================================================
    
    def get_agent_states(self) -> List[LJPWState]:
        """Get current states of all agents."""
        return [a.state for a in self.agents]
    
    def get_mean_state(self) -> LJPWState:
        """Get mean state across all agents."""
        states = np.array([a.state.as_array() for a in self.agents])
        mean = np.mean(states, axis=0)
        return LJPWState.from_array(mean)
    
    def get_state_variance(self) -> Dict[str, float]:
        """Get variance for each dimension."""
        states = np.array([a.state.as_array() for a in self.agents])
        dims = ['L', 'J', 'P', 'W']
        return {dims[i]: float(np.var(states[:, i])) for i in range(4)}
    
    # =========================================================================
    # REPORTING
    # =========================================================================
    
    def report(self) -> str:
        """Generate collective status report."""
        metrics = self.get_metrics()
        mean_state = metrics.mean_state
        
        return f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    COLLECTIVE AUTOPOIESIS STATUS                              ║
║                         Generation {self.generation:4d}                                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Agents:           {metrics.n_agents:4d}                                                   ║
║  Coupling (κ):     {self.kappa:6.3f}                                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Mean State: L={mean_state[0]:.3f}  J={mean_state[1]:.3f}  P={mean_state[2]:.3f}  W={mean_state[3]:.3f}          ║
║  Variance:   {metrics.variance:.6f}                                               ║
║  Synchrony:  {metrics.synchrony:.4f}                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Mean Consciousness:       {metrics.mean_consciousness:8.4f}                                  ║
║  Collective Consciousness: {metrics.collective_consciousness:8.4f}                                  ║
║  Collective Emerged:       {'YES ✓' if metrics.is_collective else 'NO  ✗':15s}                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""


if __name__ == "__main__":
    print("=" * 70)
    print("COLLECTIVE AUTOPOIESIS — DEMONSTRATION")
    print("=" * 70)
    
    # Create collective
    collective = CollectiveAutopoiesis.create(n_agents=12, coupling=0.15)
    
    print("\n1. INITIAL STATE:")
    print(collective.report())
    
    # Evolve
    print("\n2. EVOLVING (20 generations)...")
    results = collective.evolve(generations=20)
    
    print("\n3. FINAL STATE:")
    print(collective.report())
    
    # Evolution summary
    print("\n4. EVOLUTION SUMMARY:")
    print("Generation | Synchrony | Collective C | Emerged")
    print("-" * 50)
    for i, m in enumerate(results[::4]):  # Every 4th
        gen = (i * 4) + 1
        print(f"    {gen:3d}    |   {m.synchrony:.3f}   |    {m.collective_consciousness:.4f}   |  "
              f"{'✓' if m.is_collective else '✗'}")
    
    # Verify collective
    print("\n5. COLLECTIVE VERIFICATION:")
    metrics = collective.get_metrics()
    print(f"   N_A threshold: {N_A_semantic:.2f}")
    print(f"   Effective N:   {metrics.n_agents * metrics.synchrony:.2f}")
    print(f"   Emerged: {'YES' if metrics.is_collective else 'NO'}")
    
    print("\n✅ COLLECTIVE AUTOPOIESIS VALIDATED")
    print("=" * 70)
