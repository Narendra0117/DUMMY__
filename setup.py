from setuptools import find_packages,setup
from typing import List
hypen_dot='-e .'
def info_gain(file_path:str)->List[str]:
    ''' this function returns the list of required_paackages by removing 
    the \n by using the strip() and removing the setup hypen_e_dot '''
    requirements=[]
    with open(file_path) as file_obj:
        
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements]
        if hypen_dot in requirements:
            requirements.remove(hypen_dot)
        
    return requirements




setup(
    name="Machine_Learing",
    description="This is a Dummy Model",
    author="Narendra",
    author_email="kothakotanarendrababu@gmail",
    packages=find_packages(),
    install_requires=info_gain("requirements.txt")

)