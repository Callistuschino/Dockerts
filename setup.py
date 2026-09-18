from setuptools import setup, find_packages

setup(
    name="dockerts",
    version="0.1.0",
    description="A simple containerizable Python web service",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "flask>=2.2.0,<3.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "build>=0.10.0",
            "wheel>=0.38.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dockerts=dockerts.app:main",
        ],
    },
)
