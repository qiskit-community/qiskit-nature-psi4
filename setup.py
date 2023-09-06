# This code is part of a Qiskit project.
#
# (C) Copyright IBM 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import setuptools
import inspect
import sys
import os
import re

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

if not hasattr(setuptools, 'find_namespace_packages') or not inspect.ismethod(setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 (find_namespace_packages). "
          "Upgrade it to version >='40.1.0' and repeat install.".format(setuptools.__version__))
    sys.exit(1)

VERSION_PATH = os.path.join(os.path.dirname(__file__), "qiskit_nature_psi4", "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(README_PATH) as readme_file:
    README = re.sub(
        "<!--- long-description-skip-begin -->.*<!--- long-description-skip-end -->",
        "",
        readme_file.read(),
        flags=re.S | re.M,
    )

setuptools.setup(
    name='qiskit-nature-psi4',
    version=VERSION,
    description='Qiskit Nature Psi4: Third-party integration plugin of Qiskit Nature + Psi4.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/qiskit-community/qiskit-nature-psi4',
    author='Qiskit Nature Psi4 Development Team',
    author_email='hello@qiskit.org',
    license='Apache-2.0',
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering"
    ],
    keywords='qiskit sdk quantum nature chemistry physics psi4',
    packages=setuptools.find_packages(include=['qiskit_nature_psi4', 'qiskit_nature_psi4.*']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False
)
