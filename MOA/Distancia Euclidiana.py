import numpy
import numpy as np

ver1 = np.array((4307, 2322))
ver2 = numpy.array((675,  1006))

dist = np.linalg.norm(ver1 - ver2)

print(round(dist, 2))

