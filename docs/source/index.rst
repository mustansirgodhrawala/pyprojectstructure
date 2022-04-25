Welcome to PyProjectStructure's documentation!
==============================================

Our repository and documentation mainly consist of best practices and the correct ways to use proper python package structure and generic tools such as tox, flake8 and mypy. Using these tools alongside github actions and such tools is getting more complicated and requires
an increasing number of config files and environments, we hope to make this less complicated and create a repo where people can gain insight from and learn how to write basic tests

Tech Stack:
- Tox: Runs pytest,mypy, and flake8
- Precommit: Runs black, trailing white spaces, check for large files
- Pytest: For checking code, 100% coverage is not needed.
- Codecov to get that cool badge on github.

Here' what we hope we can help with:
1. What goes inside pyproject.toml, setup.cfg, tox and what directories need to and don't need to exist.
2. How can I integrate CI/CD using open source and free tools like github actions.

Check out the :doc:`usage` section for further information, including
how to :ref:`install` the project.

``

.. note::

   This project is under active development.
