import ctypes as C

CLIB = C.CDLL('./libgeometry.so')
CLIB.add_float.argtypes = C.c_float
CLIB.add_float.restype = C.c_float





