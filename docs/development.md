# Development

You must currently run the `build.sh` script in the repo root after
making changes to the .proto file before commiting your updates

This repo uses `setuptools.build_meta` as the build backend rather
than `scikit_build_core.build` since we are not using pybind.
