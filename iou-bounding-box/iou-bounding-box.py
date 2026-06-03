import numpy as np
def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here

    box_a = np.asarray(box_a, dtype=float)
    box_b = np.asarray(box_b, dtype=float)

    x_left   = max(box_a[0], box_b[0])
    y_top    = max(box_a[1], box_b[1])
    x_right  = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    inter_w = max(0.0, x_right - x_left)
    inter_h = max(0.0, y_bottom - y_top)
    inter_area = inter_w * inter_h
    area_a = max(0.0, (box_a[2] - box_a[0]) * (box_a[3] - box_a[1]))
    area_b = max(0.0, (box_b[2] - box_b[0]) * (box_b[3] - box_b[1]))
    union = area_a + area_b - inter_area
    if union <= 0.0:
        return 0.0

    return float(inter_area / union)
    pass