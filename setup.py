"""
Setup configuration for Advanced Calculator package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="advanced-calculator",
    version="1.0.0",
    author="Abdulvehhab Erol",
    author_email="7abdist2@gmail.com",
    description="A professional advanced calculator with comprehensive math operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/falepone/my-python-project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "pylint>=2.16.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
        ],
    },
)
