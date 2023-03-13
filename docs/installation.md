# Installation

DTCC Model can be easily installed using [`pip`](https://pypi.org/project/pip/).

To install from the Python Package Index (PyPI):

    pip install dtcc-model

To install from the source directory:

    pip install .

---
**NOTE**

Sometimes `pip` and `python` may be out of sync which means that `pip` will
install a package in a location where it will not be found by `python`. It is
therefore safer to replace the `pip` command by `python -m pip`:

    python -m pip install [dtcc-model or .]
---

DTCC Model also provides a C++ library containing the C++ version of the data
model. The C++ library can be easily installed from source via CMake:

    mkdir build
    cd build
    cmake ..
    make -j
    make install
