from setuptools import setup, find_packages

setup(
    name="zamunda-api",
    version="0.2.1",  # Update this with your versioning
    description="A Python API for interacting with Zamunda",
    long_description="",
    long_description_content_type="text/markdown",
    author="murrou-cell",
    author_email="",
    url="https://github.com/murrou-cell/zamunda-api",
    packages=find_packages(),  # Automatically find all sub-packages
    install_requires=[
        "beautifulsoup4==4.12.3",
        "fastapi==0.115.5",
        "Requests==2.32.4",
        "uvicorn==0.32.1",
        "torrentool==1.0.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)