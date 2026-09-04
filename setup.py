#find_package check which folder has "__init__.py" file it consider that folder a a package.
from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    """This function return list of requirements"""

    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #Reads liness from file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e.
                if requirement and requirement !='-e .':
                  requirement_lst.append(requirement)

    except FileNotFoundError:
       print("requirements.txt file is not found")
    return requirement_lst

setup(
    name="Ai",    #project name
    version="0.0.1",
    author="Sudhanshu Kumar",
    author_email="sudhanshukumar03089@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement()
)