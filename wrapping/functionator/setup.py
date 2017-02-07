from distutils.core import setup, Extension
from Cython.Build import cythonize

lds = Extension(name="func_p",
                sources=["func_p.pyx", "func_c.c"])

setup(ext_modules=cythonize([lds]))