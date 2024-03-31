from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the file and returns a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", " ") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")


setup(
    name="student_marks_prediction_system",
    version="0.0.1",
    author="Sayam",
    author_email="sayamalvi07@gmail.com",
    description="A small package to predict student marks",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
