## This file creates the whole ML pipeline into a package and it can be deployed 

from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:

    '''
    Returns all the packages needed in the project
    '''
    HYPHEN_E_DOT = '-e .'
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name = 'mlproject',
    version= '0.0.1',
    author= 'Divyanshu',
    author_email= 'anishtdevartrns@gmail.com',
    packages= find_packages(), 
    install_requires = get_requirements('requirements.txt')
)