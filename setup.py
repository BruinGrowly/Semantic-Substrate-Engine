"""
Semantic Substrate Engine - Setup Configuration
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file, 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
else:
    requirements = [
        'numpy>=1.21.0',
        'scipy>=1.7.0',
        'sympy>=1.9',
        'matplotlib>=3.4.0',
    ]

setup(
    name="semantic-substrate-engine",
    version="3.0.0",
    author="BruinGrowly",
    author_email="",
    description="A sophisticated semantic processing system combining mathematical precision with value-aligned computation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BruinGrowly/Semantic-Substrate-Engine",
    project_urls={
        "Bug Tracker": "https://github.com/BruinGrowly/Semantic-Substrate-Engine/issues",
        "Documentation": "https://github.com/BruinGrowly/Semantic-Substrate-Engine/tree/main/docs",
        "Source Code": "https://github.com/BruinGrowly/Semantic-Substrate-Engine",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*", "research", "research.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'pylint>=2.12.0',
            'black>=22.0.0',
            'mypy>=0.950',
        ],
        'viz': [
            'matplotlib>=3.4.0',
        ],
    },
    keywords=[
        'semantic-analysis',
        'nlp',
        'artificial-intelligence',
        'machine-learning',
        'computational-semantics',
        'value-alignment',
        'ethics',
        'ai-safety',
    ],
    license="MIT",
    include_package_data=True,
    zip_safe=False,
)
