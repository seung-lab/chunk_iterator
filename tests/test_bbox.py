import bbox

bbox1 = [0,0,0,1025,1025,1025]
bbox2 = [1024,1024,1024,2048,2048,2048]

if bbox.overlap(bbox1, bbox2):
    print "overlaping"
else:
    print "not overlaping"

print bbox.intersection(bbox1,bbox2)
