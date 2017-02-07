from distutils.core import setup
from Cython.Build import cythonize

setup(name="cython_len_extern",
      ext_modules = cythonize("len_extern.pyx")
)

