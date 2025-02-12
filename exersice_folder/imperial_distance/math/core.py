from typing import Tuple

def to_inches(feet: float, inches: float) -> float:
    """Convert feet and inches to total inches."""
    return feet * 12 + inches

def from_inches(total_inches: float) -> Tuple[float, float]:
    """Convert total inches back to feet and inches."""
    feet = total_inches // 12
    remainder = total_inches % 12
    return (feet, remainder)

def add(feet1: float, inches1: float, feet2: float, inches2: float) -> Tuple[float, float]:
    """Sum of two lengths in feet and inches."""
    total = to_inches(feet1, inches1) + to_inches(feet2, inches2)
    return from_inches(total)

def subtract(feet1: float, inches1: float, feet2: float, inches2: float) -> Tuple[float, float]:
    """Difference between two lengths (first minus second)."""
    total = to_inches(feet1, inches1) - to_inches(feet2, inches2)
    return from_inches(total)

def multiply(feet: float, inches: float, factor: float) -> Tuple[float, float]:
    """Multiply a length by a factor."""
    total = to_inches(feet, inches) * factor
    return from_inches(total)

def divide(feet: float, inches: float, parts: float) -> Tuple[float, float]:
    """Divide a length into equal parts."""
    if parts <= 0:
        raise ValueError("The number of parts must be positive.")
    total = to_inches(feet, inches)
    each_part = total / parts
    return from_inches(each_part)