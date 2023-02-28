from distutils.core import setup

import numpy
from Cython.Build import cythonize

setup(
    name='core',
    version='0.0.1',
    ext_modules=cythonize(
        module_list=[
            "core.pyx",
        ]),
    include_dirs=[numpy.get_include()],
    compiler_directives={'language_level': "3"},
    extra_compile_args=["-O3", "-ffast-math"],
)
