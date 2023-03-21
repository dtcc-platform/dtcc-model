# Development

To (re)build all classes from the definition `src/proto/dtcc.proto`, run
the command

    bin/build-classes

This repo uses `setuptools.build_meta` as the build backend rather
than `scikit_build_core.build` since we are not using pybind.
