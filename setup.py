# Library imports
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    # Create an empty list to store libraries from requirements.txt
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        # Replace the \n from requirements.txt with blanks
        requirements = [req.replace("\n", "") for req in requirements]

        # Condition to remove the '-e .' from this list
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'MLProject',
    version = '0.0.1',
    author = 'sank0de',
    author_email = 'c0design277@gmail.com',
    packages = find_packages(),
    ##install_requires = ['pandas', 'numpy', 'seaborn']
    # Instead of doing the above, the following can be done
    install_requires = get_requirements('requirements.txt')
)