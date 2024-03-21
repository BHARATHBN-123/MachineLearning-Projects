from  setuptools import setup , find_packages
from typing import List

''' "-e ." in Requirements.txt file  will connect setup.py file to requirements.txt file to create package
of this project so that it can be re used as package'''

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    
    ''' This function will return a list of requirements'''

    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.replace("\n","") for req in file_obj.readlines() if not HYPEN_E_DOT]
    return requirements

#Setting up the project details
setup(
    name="MLPROJECT",
    version='1.0',
    author="Bharath B N",
    author_email="bharathbn17498@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("Requirements.txt")


)