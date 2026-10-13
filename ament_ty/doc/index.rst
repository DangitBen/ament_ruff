ament_ruff
==================

Type check python files using the `ty <https://github.com/astral-sh/ty>`_ tool.

How to run the check from the command line?
-------------------------------------------

.. code:: sh

    usage: ament_ty [-h] [--config path] [--reformat] [--xunit-file XUNIT_FILE] [paths ...]

    Type check python code using ty

    positional arguments:
      paths                 The files or directories to check

    options:
      -h, --help            show this help message and exit
      --config path         The path to a pyproject.toml or ty.toml config file.
      --xunit-file XUNIT_FILE
                            Generate a xunit compliant XML file


How to run the check from within a CMake ament package as part of the tests?
----------------------------------------------------------------------------

The CMake integration is provided by the package `ament_cmake_ty
<https://github.com/swri-robotics/ament_ruff/tree/main/ament_cmake_ty>`_.