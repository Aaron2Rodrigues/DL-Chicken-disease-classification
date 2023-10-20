import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format= '[%(ascitime)s]: %(message)s:')

project_name = "cnnClassifier"

file_list= [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__innit__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirement.txt",
    "setup.py",
    "reserch/trials.ipynb",
    "templates/index.html"
]


for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
     
   
    if filedir !="":
       os.makedirs(filedir, exist_ok=True)
       logging.info(f"creating directory; {filedir} for the file:{filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize == 0):
       with open (filepath,"w") as f:
          pass
          logging.info(f"creatuing a filepath{filepath}")

    else:
       logging.info(f"{filepath} alredy exists")