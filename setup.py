from setuptools import find_packages,setup
from typing import List
j = '-e .'
def get_requirements(file_path:str)->List[str]:
   requirements = []
   with open(file_path) as file_obj:
      requirements= file_obj.readlines()
      requirements=[req.replace('\n','') for req in requirements]
      if j in requirements:
         requirements.remove(j)
   return requirements


setup(
    name='MLproject',
    version='1',
    packages=find_packages(),
    install_requires = get_requirements('blah.txt')
)