from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) ->List[str]:
    """this funcion will return the list of all libraries inside the requirements file

    Args:
        file_path (str): requirements.txt file path

    Returns:
        List[str]: list of all listed libraries inside the requirements file 
    """

    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt'),
    author='Vipin',
    author_email='vipinpal7060@gmail.com',

)