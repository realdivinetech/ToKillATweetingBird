from setuptools import setup, find_packages

setup(
    name="ToKillATweetingBird",   # The package name
    version="0.1.0",              # Any version number you choose
    packages=find_packages(),     # Automatically find all subpackages
    install_requires=[            # Optional: dependencies
        "beautifulsoup4",
        "lxml"
    ],
)
