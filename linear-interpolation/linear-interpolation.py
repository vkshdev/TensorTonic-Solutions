def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here

    result = values[:]
    n = len(values)
    i = 0
    
    while i < n:
        if result[i] is None:
            left = i - 1
            v_left = result[left]
            right = i
            while right < n and result[right] is None:
                right += 1
            v_right = result[right]
            
            gap = right - left
            for j in range(left + 1, right):
                frac = (j - left) / gap
                result[j] = v_left + frac * (v_right - v_left)

            i = right
        else:
            i += 1
    return result    