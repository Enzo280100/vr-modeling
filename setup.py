from setuptools import setup, find_packages

# Read dependencies from the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Configuration of setup.py
setup(
    name="master_project",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    description="Library for the project",
    author="Alejandro Delgado, Enzo Infantes, Viktoria Gagua | DSDM 24-25",
    author_email="alejandro.delgado@bse.eu, enzo.infantes@bse.eu, viktoria.gagua@bse.eu",
    url="https://github.com/Enzo280100/VR",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
