"""
This module contains utility functions for the phi_geometric_engine.
"""

from src.phi_geometric_engine import (
    FibonacciSequence,
    GoldenSpiral,
    GoldenAngleRotator,
    PhiExponentialBinner,
    PhiCoordinate
)


def fibonacci(n: int) -> int:
    """Quick access to nth Fibonacci number"""
    fib = FibonacciSequence()
    return fib.get(n)


def golden_spiral_distance(p1: PhiCoordinate, p2: PhiCoordinate,
                          center: PhiCoordinate | None = None) -> float:
    """Quick access to golden spiral distance"""
    spiral = GoldenSpiral()
    return spiral.distance_4d(p1, p2, center)


def rotate_by_golden_angle(coord: PhiCoordinate, n: int = 1,
                          plane: str = "LP") -> PhiCoordinate:
    """Quick access to golden angle rotation"""
    rotator = GoldenAngleRotator()
    return rotator.rotate_4d(coord, n, plane)


def get_phi_bin(value: float) -> int:
    """Quick access to phi exponential bin"""
    binner = PhiExponentialBinner()
    return binner.get_bin(value)
