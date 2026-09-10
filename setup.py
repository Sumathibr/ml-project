from setuptools import setup
from typing import List



# declaring variables for setup function.
PROJECT_NAME= "housing predictor"
VERSION= "0.0.1"
AUTHER= "sumathi"
DESCRIPTION= "THIS IS MY 1ST MACHINE LEARNING PROJECT"
PACKAGES= ["housing"]
REQUIREMENTS_FILE_NAME= "requirements.txt"



def get_requirements_list()-> List[str]:
    """
    description: This function will return list of requirements from 
                requirements.txt file
    return: returns the list of libraries mentioned in requriments.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
name= PROJECT_NAME,
version= VERSION,
author= AUTHER,
description= DESCRIPTION,
packages=PACKAGES,
install_requires= get_requirements_list()

)