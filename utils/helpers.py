def clamp(value, low=0, high=100):
    return max(low, min(high, int(value)))