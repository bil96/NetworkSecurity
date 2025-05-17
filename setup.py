from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function returns a list of requirements.
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt") as f:
            lines = f.readlines()
            for line in lines:
                requirement= line.strip()
                if requirement and requirement != '-e':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Bilal Qwider",
    author_email="bilalqwider@yahoo.com",
    packages=find_packages(),
)




