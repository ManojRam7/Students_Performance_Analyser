from pathlib import Path
from typing import List

from setuptools import find_packages, setup


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements: List[str] = []
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = [line.strip() for line in file_obj if line.strip()]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="student-performance-analyser",
    version="1.0.0",
    description="End-to-end ML project to predict student math performance",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Manoj Ram",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.9",
)