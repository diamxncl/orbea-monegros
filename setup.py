from setuptools import setup, find_packages

setup(
    name="PEC4_PCD_ALVAROSALASROBLEDILLO",
    version="1.0.0",
    description="PEC 4 Ánalisis de orbea monegros.",
    author="Álvaro Salas Robledillo",
    author_email="asalrob@uoc.edu",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=2.2.3",
        "matplotlib>=3.9.0",
        "faker>=33.3.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
