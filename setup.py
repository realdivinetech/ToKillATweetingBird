from setuptools import setup, find_packages

setup(
    name="realdivinetech",          # package name
    version="0.1.0",                # version number
    packages=find_packages(where="."),  # auto-discover packages
    install_requires=[
        "selenium>=4.8.0",
        "pandas",
        "dynaconf",
        "psycopg2-binary",
        "lxml",
        "fake-useragent~=1.2.1",
        "beautifulsoup4",
    ],
    python_requires=">=3.8",        # adjust if needed
)
