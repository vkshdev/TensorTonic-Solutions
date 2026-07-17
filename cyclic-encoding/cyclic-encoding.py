import math

def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here

    if period <= 0:
        raise ValueError("period must be > 0")
    result = []
    for v in values:
        angle = (2 * math.pi * v) / period
        sin_val = math.sin(angle)
        cos_val = math.cos(angle)
        result.append([sin_val, cos_val])
    return result