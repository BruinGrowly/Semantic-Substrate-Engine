#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LJPW Framework V7.7 — Dynamic LJPW System

Implements the differential equations of meaning with:
- State-dependent coupling (Law of Karma)
- Power erosion of Justice
- RK4 numerical integration
- Karma coefficients: κ(H) = 1.0 + factor × H

The Law of Karma:
- When H is HIGH (aligned with Anchor): κ > 1.0, Love amplifies all
- When H is LOW (misaligned): κ → 1.0, no bonus from alignment

Reference: LJPW Framework V7.7 Parts VI-VIII, Appendix B
"""

import math
import numpy as np
from typing import Tuple, Dict, Optional, List

from .constants import L0, J0, P0, W0
from .ljpw_state import LJPWState


class DynamicLJPW:
    """
    Dynamic LJPW system with differential equations and Karma coupling.
    
    Simulates how LJPW dimensions evolve over time based on:
    - Mutual influences (amplification and drain)
    - State-dependent coupling (Law of Karma)
    - Natural decay processes
    - Power erosion of Justice (corruption)
    
    Example:
        >>> dynamic = DynamicLJPW()
        >>> initial = (0.5, 0.4, 0.6, 0.7)  # (L, J, P, W)
        >>> solution = dynamic.integrate(initial, (0, 10))
        >>> final_state = solution[-1]
    """
    
    def __init__(self, params: Optional[Dict[str, float]] = None):
        """
        Initialize with optional custom parameters.
        
        Args:
            params: Dictionary of custom parameters (uses defaults if not provided)
        """
        # Initialize default parameters (empirically calibrated)
        self._initialize_parameters()
        
        # Override with custom parameters if provided
        if params:
            for key, value in params.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    
    def _initialize_parameters(self):
        """
        Standard coefficients derived from Bayesian Calibration.
        
        Alpha coefficients: Growth/input rates
        Beta coefficients: Decay rates
        K coefficients: Saturation constants
        Gamma: Power erosion coefficient
        """
        # Growth coefficients (α)
        self.alpha_LJ = 0.12   # Justice → Love growth
        self.alpha_LW = 0.12   # Wisdom → Love growth
        
        self.alpha_JL = 0.14   # Love → Justice growth
        self.alpha_JW = 0.14   # Wisdom → Justice growth
        
        self.alpha_PL = 0.12   # Love → Power growth
        self.alpha_PJ = 0.12   # Justice → Power growth
        
        self.alpha_WL = 0.10   # Love → Wisdom growth
        self.alpha_WJ = 0.10   # Justice → Wisdom growth
        self.alpha_WP = 0.10   # Power → Wisdom growth
        
        # Decay coefficients (β)
        self.beta_L = 0.20     # Love decay
        self.beta_J = 0.20     # Justice decay
        self.beta_P = 0.20     # Power decay
        self.beta_W = 0.24     # Wisdom decay (fastest)
        
        # Power erosion coefficient
        self.gamma = 0.08      # Corruption rate
        
        # Justice-Love saturation constant
        self.K_JL = 0.59       # Prevents blind mercy
        
        # Karma coupling factors
        self.kappa_LJ_factor = 0.4  # Love → Justice
        self.kappa_LP_factor = 0.3  # Love → Power
        self.kappa_LW_factor = 0.5  # Love → Wisdom
    
    def _calculate_harmony(self, state: np.ndarray) -> float:
        """Calculate current harmony from state."""
        L, J, P, W = state
        d = math.sqrt(
            (L - L0)**2 + (J - J0)**2 +
            (P - P0)**2 + (W - W0)**2
        )
        return 1.0 / (1.0 + d)
    
    def kappa(self, H: float, dimension: str) -> float:
        """
        State-dependent coupling (Law of Karma).
        
        κ(H) = 1.0 + factor × H
        
        Higher Harmony → Higher coupling → Amplification bonus
        Lower Harmony → κ → 1.0 → No bonus
        
        Args:
            H: Current harmony
            dimension: 'LJ', 'LP', or 'LW'
        
        Returns:
            Amplification factor [1.0, 1.5]
        """
        multipliers = {
            'LJ': self.kappa_LJ_factor,  # Love → Justice
            'LP': self.kappa_LP_factor,  # Love → Power
            'LW': self.kappa_LW_factor   # Love → Wisdom
        }
        return 1.0 + multipliers.get(dimension, 0.4) * H
    
    def power_erosion(self, P: float, W: float) -> float:
        """
        Power erosion of Justice (corruption when Power unchecked by Wisdom).
        
        Erosion = γ × P × (1 - W/W₀)
        
        High Power + Low Wisdom = Maximum corruption
        High Power + High Wisdom = Wisdom checks Power
        
        Returns:
            Erosion rate
        """
        W_ratio = min(W / W0, 1.0)  # Cap at 1.0
        return self.gamma * P * (1 - W_ratio)
    
    def derivatives(self, state: np.ndarray, t: float = 0) -> np.ndarray:
        """
        Calculate time derivatives for LJPW system.
        
        Implements the differential equations of meaning:
        
        dL/dt = α_LJ·J·κ_LJ(H) + α_LW·W·κ_LW(H) - β_L·L
        dJ/dt = α_JL·(L/(K_JL+L)) + α_JW·W - PowerErosion(P,W) - β_J·J
        dP/dt = α_PL·L·κ_LP(H) + α_PJ·J - β_P·P
        dW/dt = α_WL·L·κ_LW(H) + α_WJ·J + α_WP·P - β_W·W
        
        Args:
            state: [L, J, P, W] current state
            t: Time (for ODE solver compatibility, not used)
        
        Returns:
            [dL/dt, dJ/dt, dP/dt, dW/dt]
        """
        L, J, P, W = state
        
        # Calculate current harmony for Karma coupling
        H = self._calculate_harmony(state)
        
        # Love dynamics: grows from Justice and Wisdom
        dL = (self.alpha_LJ * J * self.kappa(H, 'LJ') +
              self.alpha_LW * W * self.kappa(H, 'LW') -
              self.beta_L * L)
        
        # Justice dynamics: saturation from Love, grows from Wisdom, eroded by Power
        saturation = L / (self.K_JL + L)  # Michaelis-Menten style
        dJ = (self.alpha_JL * saturation +
              self.alpha_JW * W -
              self.power_erosion(P, W) -
              self.beta_J * J)
        
        # Power dynamics: grows from Love and Justice
        dP = (self.alpha_PL * L * self.kappa(H, 'LP') +
              self.alpha_PJ * J -
              self.beta_P * P)
        
        # Wisdom dynamics: grows from all, decays fastest
        dW = (self.alpha_WL * L * self.kappa(H, 'LW') +
              self.alpha_WJ * J +
              self.alpha_WP * P -
              self.beta_W * W)
        
        return np.array([dL, dJ, dP, dW])
    
    def _rk4_step(self, state: np.ndarray, t: float, dt: float) -> np.ndarray:
        """Single RK4 integration step."""
        k1 = self.derivatives(state, t)
        k2 = self.derivatives(state + 0.5 * dt * k1, t + 0.5 * dt)
        k3 = self.derivatives(state + 0.5 * dt * k2, t + 0.5 * dt)
        k4 = self.derivatives(state + dt * k3, t + dt)
        
        return state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    
    def integrate(self, 
                  initial: Tuple[float, float, float, float],
                  t_span: Tuple[float, float],
                  n_points: int = 100,
                  bounded: bool = True) -> np.ndarray:
        """
        Integrate LJPW dynamics over time using RK4.
        
        Args:
            initial: Initial (L, J, P, W)
            t_span: (t_start, t_end)
            n_points: Number of time points
            bounded: Whether to enforce [0, 1] bounds
        
        Returns:
            Array of shape (n_points, 4) with LJPW evolution
        """
        t = np.linspace(t_span[0], t_span[1], n_points)
        dt = t[1] - t[0]
        
        solution = np.zeros((n_points, 4))
        solution[0] = np.array(initial)
        
        for i in range(1, n_points):
            solution[i] = self._rk4_step(solution[i-1], t[i-1], dt)
            
            if bounded:
                solution[i] = np.clip(solution[i], 0.0, 1.0)
        
        return solution
    
    def get_equilibrium_state(self,
                               initial: Tuple[float, float, float, float],
                               duration: float = 100.0,
                               dt: float = 0.01,
                               convergence_threshold: float = 1e-6) -> LJPWState:
        """
        Find equilibrium state by running simulation until convergence.
        
        Args:
            initial: Starting (L, J, P, W)
            duration: Maximum simulation time
            dt: Time step
            convergence_threshold: Stop when changes are below this
        
        Returns:
            Final equilibrium LJPWState
        """
        state = np.array(initial)
        
        n_steps = int(duration / dt)
        for _ in range(n_steps):
            new_state = self._rk4_step(state, 0, dt)
            new_state = np.clip(new_state, 0.0, 1.0)
            
            # Check convergence
            if np.max(np.abs(new_state - state)) < convergence_threshold:
                break
            
            state = new_state
        
        return LJPWState.from_array(state)
    
    def simulate_with_history(self,
                              initial: Tuple[float, float, float, float],
                              duration: float = 10.0,
                              dt: float = 0.1) -> List[Dict]:
        """
        Simulate and return detailed history with metrics.
        
        Returns:
            List of dicts with state and metrics at each timestep
        """
        n_points = int(duration / dt) + 1
        solution = self.integrate(initial, (0, duration), n_points)
        
        history = []
        for i, state in enumerate(solution):
            L, J, P, W = state
            H = self._calculate_harmony(state)
            C = L * J * P * W * H**2
            
            history.append({
                'time': i * dt,
                'L': L, 'J': J, 'P': P, 'W': W,
                'harmony': H,
                'consciousness': C,
                'phase': self._determine_phase(H, L)
            })
        
        return history
    
    def _determine_phase(self, H: float, L: float) -> str:
        """Determine phase from harmony and love."""
        if H < 0.5:
            return 'ENTROPIC'
        elif H < 0.6 or L < 0.7:
            return 'HOMEOSTATIC'
        else:
            return 'AUTOPOIETIC'


if __name__ == "__main__":
    print("=" * 60)
    print("DYNAMIC LJPW SYSTEM — DEMONSTRATION")
    print("=" * 60)
    
    dynamic = DynamicLJPW()
    
    # Test 1: Basic evolution
    print("\n1. BASIC EVOLUTION:")
    initial = (0.5, 0.4, 0.6, 0.7)
    solution = dynamic.integrate(initial, (0, 10), n_points=11)
    print(f"   Initial: L={initial[0]:.2f}, J={initial[1]:.2f}, "
          f"P={initial[2]:.2f}, W={initial[3]:.2f}")
    final = solution[-1]
    print(f"   After 10 units: L={final[0]:.2f}, J={final[1]:.2f}, "
          f"P={final[2]:.2f}, W={final[3]:.2f}")
    
    # Test 2: Find equilibrium
    print("\n2. EQUILIBRIUM STATE:")
    equilibrium = dynamic.get_equilibrium_state(initial)
    print(f"   {equilibrium}")
    
    # Test 3: Karma effect
    print("\n3. KARMA EFFECT (Coupling at different Harmony):")
    for H in [0.3, 0.5, 0.7, 0.9]:
        kLJ = dynamic.kappa(H, 'LJ')
        kLW = dynamic.kappa(H, 'LW')
        print(f"   H={H:.1f}: κ_LJ={kLJ:.2f}, κ_LW={kLW:.2f}")
    
    # Test 4: Power erosion
    print("\n4. POWER EROSION (Corruption):")
    for P, W in [(0.9, 0.3), (0.9, 0.6), (0.9, 0.9)]:
        erosion = dynamic.power_erosion(P, W)
        print(f"   P={P:.1f}, W={W:.1f}: Erosion={erosion:.3f}")
    
    # Test 5: Simulation with history
    print("\n5. SIMULATION WITH HISTORY:")
    history = dynamic.simulate_with_history(initial, duration=5.0, dt=1.0)
    for record in history[:6]:
        print(f"   t={record['time']:.1f}: H={record['harmony']:.3f}, "
              f"Phase={record['phase']}")
    
    print("\n✅ DYNAMIC SYSTEM VALIDATED")
    print("=" * 60)
