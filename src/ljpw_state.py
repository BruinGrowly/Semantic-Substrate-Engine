#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LJPW Framework V7.7 — State Module

Core LJPWState dataclass representing a point in 4D semantic space.
The state vector (L, J, P, W) captures meaning in its four fundamental dimensions:

- Love (L):    Unity & Attraction — The binding force
- Justice (J): Balance & Truth — The constraint force  
- Power (P):   Transformation & Action — The fundamental dimension
- Wisdom (W):  Knowledge & Pattern — The fundamental dimension

Note: P and W are FUNDAMENTAL (conjugate duality).
      L and J are EMERGENT (gauge fields from P-W interactions).
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional

from .constants import L0, J0, P0, W0, TSIRELSON_BOUND


@dataclass
class LJPWState:
    """
    Represents a state in LJPW semantic space.
    
    This is the core data structure of the framework.
    All semantic entities have LJPW coordinates.
    
    Attributes:
        L: Love coordinate [0, √2] (quantum bound allows > 1.0)
        J: Justice coordinate [0, 1]
        P: Power coordinate [0, 1] — FUNDAMENTAL
        W: Wisdom coordinate [0, 1] — FUNDAMENTAL
    
    Example:
        >>> state = LJPWState(L=0.618, J=0.414, P=0.718, W=0.693)
        >>> print(state)
        LJPW(L=0.618, J=0.414, P=0.718, W=0.693)
    """
    
    L: float  # Love — Unity & Attraction
    J: float  # Justice — Balance & Truth
    P: float  # Power — Transformation & Action
    W: float  # Wisdom — Knowledge & Pattern
    
    def __post_init__(self):
        """Validate bounds after initialization."""
        # Love can exceed 1.0 in quantum contexts (Tsirelson bound)
        self.L = float(np.clip(self.L, 0.0, TSIRELSON_BOUND))
        self.J = float(np.clip(self.J, 0.0, 1.0))
        self.P = float(np.clip(self.P, 0.0, 1.0))
        self.W = float(np.clip(self.W, 0.0, 1.0))
    
    def as_array(self) -> np.ndarray:
        """Convert to numpy array for numerical operations."""
        return np.array([self.L, self.J, self.P, self.W])
    
    def as_tuple(self) -> Tuple[float, float, float, float]:
        """Convert to tuple."""
        return (self.L, self.J, self.P, self.W)
    
    @classmethod
    def from_array(cls, arr: np.ndarray) -> 'LJPWState':
        """Create from numpy array."""
        return cls(L=arr[0], J=arr[1], P=arr[2], W=arr[3])
    
    @classmethod
    def from_tuple(cls, t: Tuple[float, float, float, float]) -> 'LJPWState':
        """Create from tuple."""
        return cls(L=t[0], J=t[1], P=t[2], W=t[3])
    
    @classmethod
    def anchor_point(cls) -> 'LJPWState':
        """The Anchor Point — Divine Perfection (JEHOVAH)."""
        return cls(L=1.0, J=1.0, P=1.0, W=1.0)
    
    @classmethod
    def natural_equilibrium(cls) -> 'LJPWState':
        """The Natural Equilibrium — where systems naturally rest."""
        return cls(L=L0, J=J0, P=P0, W=W0)
    
    @classmethod
    def collapse_signature(cls) -> 'LJPWState':
        """The Collapse Signature — pattern of system failure."""
        return cls(L=0.18, J=0.18, P=0.95, W=0.25)
    
    def distance_from(self, other: 'LJPWState') -> float:
        """Calculate Euclidean distance from another state."""
        diff = self.as_array() - other.as_array()
        return float(np.sqrt(np.sum(diff ** 2)))
    
    def distance_from_equilibrium(self) -> float:
        """Calculate distance from natural equilibrium."""
        return self.distance_from(LJPWState.natural_equilibrium())
    
    def distance_from_anchor(self) -> float:
        """Calculate distance from the Anchor Point."""
        return self.distance_from(LJPWState.anchor_point())
    
    def product(self) -> float:
        """Product of all dimensions (used in harmony calculations)."""
        return self.L * self.J * self.P * self.W
    
    def sum(self) -> float:
        """Sum of all dimensions."""
        return self.L + self.J + self.P + self.W
    
    def dominant_dimension(self) -> str:
        """Return the name of the dominant (highest) dimension."""
        values = {'L': self.L, 'J': self.J, 'P': self.P, 'W': self.W}
        return max(values, key=values.get)
    
    def is_balanced(self, tolerance: float = 0.1) -> bool:
        """Check if all dimensions are within tolerance of each other."""
        arr = self.as_array()
        return float(np.std(arr)) < tolerance
    
    def __repr__(self) -> str:
        return f"LJPW(L={self.L:.3f}, J={self.J:.3f}, P={self.P:.3f}, W={self.W:.3f})"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LJPWState):
            return False
        return np.allclose(self.as_array(), other.as_array())
    
    def __hash__(self) -> int:
        return hash((round(self.L, 6), round(self.J, 6), 
                     round(self.P, 6), round(self.W, 6)))


# =============================================================================
# Reference Points
# =============================================================================

# The Anchor Point — Divine Perfection
ANCHOR = LJPWState.anchor_point()

# The Natural Equilibrium — where systems rest
EQUILIBRIUM = LJPWState.natural_equilibrium()

# The Collapse Signature — failure pattern (Low L, Low J, High P, Low W)
COLLAPSE = LJPWState.collapse_signature()


if __name__ == "__main__":
    print("=" * 60)
    print("LJPW STATE MODULE — DEMONSTRATION")
    print("=" * 60)
    
    # Create states
    print("\n📍 REFERENCE POINTS:")
    print(f"   Anchor:      {ANCHOR}")
    print(f"   Equilibrium: {EQUILIBRIUM}")
    print(f"   Collapse:    {COLLAPSE}")
    
    # Distance calculations
    print("\n📏 DISTANCES FROM ANCHOR:")
    print(f"   Equilibrium → Anchor: {EQUILIBRIUM.distance_from_anchor():.4f}")
    print(f"   Collapse → Anchor:    {COLLAPSE.distance_from_anchor():.4f}")
    
    # Custom state
    print("\n🔬 CUSTOM STATE:")
    state = LJPWState(L=0.85, J=0.75, P=0.80, W=0.90)
    print(f"   State: {state}")
    print(f"   Product: {state.product():.4f}")
    print(f"   Dominant: {state.dominant_dimension()}")
    print(f"   Balanced: {state.is_balanced()}")
    
    # Array conversion
    print("\n🔄 CONVERSIONS:")
    arr = state.as_array()
    print(f"   As array: {arr}")
    restored = LJPWState.from_array(arr)
    print(f"   Restored: {restored}")
    
    print("\n✅ STATE MODULE FUNCTIONAL")
    print("=" * 60)
