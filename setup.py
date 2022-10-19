#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import sys

pkg_name = "workflow_facemap"
here = path.abspath(path.dirname(__file__))

long_description = """"
# Workflow for tracking facial features in video recordings with SVD analysis using Facemap

Build a complete imaging workflow using the DataJoint elements
+ [elements-lab](https://github.com/datajoint/element-lab)
+ [elements-animal](https://github.com/datajoint/element-animal)
+ [elements-session](https://github.com/datajoint/element-session)
+ [element-facemap](https://github.com/datajoint/element-facemap)
"""

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

with open(path.join(here, pkg_name, "version.py")) as f:
    exec(f.read())

setup(
    name="workflow-facemap",
    version=__version__,
    description="Facemap workflow using the DataJoint elements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DataJoint",
    author_email="info@datajoint.com",
    license="MIT",
    url="https://github.com/datajoint/workflow-facemap",
    keywords="neuroscience datajoint facemap",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=requirements,
)
