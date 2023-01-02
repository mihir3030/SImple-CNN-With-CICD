import os
import yaml
import json
from ensure import ensure_annotations
# with help of ConfigBox we can get dictinory keys using dict.key - more refere trails.ipynb
from box import ConfigBox
from box.Exception import BoxValueError
from CnnDeepClassifier import logger

# ensure_annotation verifies that function output will be -> annotation type output 
# because we mention in annotation type -> ConfigBox type - more refere trails.ipynb
@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:  # so in annotation type we get ConfigBox dictinory
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path of input file
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} load  successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except  Exception as e:
        raise e