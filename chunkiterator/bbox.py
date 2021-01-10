def overlap_1d(x1min, x1max, x2min, x2max):
    if x1max <= x2min:
        return False
    if x2max <= x1min:
        return False
    return True

def overlap(bbox1, bbox2):
    for i in range(3):
        if not overlap_1d(bbox1[i], bbox1[i+3], bbox2[i], bbox2[i+3]):
            return False
    return True

def intersection(bbox1, bbox2):
    if overlap(bbox1, bbox2):
        return [max(bbox1[0],bbox2[0]), max(bbox1[1],bbox2[1]),max(bbox1[2],bbox2[2]),min(bbox1[3],bbox2[3]),min(bbox1[4],bbox2[4]), min(bbox1[5],bbox2[5])]
    else:
        return [0,0,0,0,0,0]
