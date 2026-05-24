import os
from box.exceptions import BoxValueError
import yaml
from src.annimated_picture import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import joblib

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """read yaml file and returns
    args:
      path_to_yaml: path like input
    raises:
      ValurError: if yaml file is empty
      e: empty file
    returns:
      ConfigBox:ConfigBox type
      """
    try:
        with open(path_to_yaml)as yaml_file:
            content= yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("yaml file is empty")
            logger.info(f"yaml file:{path_to_yaml}loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty:{e}")
    except Exception as e:
        raise e
@ensure_annotations
def create_directions(path_to_directories:list,verbose=True):
    """create list of directories
    Args:
      path_to_directories(list):list of directories
      ignore_log(bool,optional):ignore if multiple dirs is to be created.defaults to false"""
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")
@ensure_annotations
def save_json(path:Path,data:dict):
    """save json data
    Args:
      path(Path):path to json file
      data(dict):data to be saves in json file
    """
    with open(path,"w")as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at :{path}")
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """load json files data
    Args:
      path(Path):path to json file
    returns:
      ConfigBox:data as class attributes instead of dict"""
    with open(path)as f:
        content=json.load(f)
    logger.info(f"json file loaded successfully from:{path}")
    return ConfigBox(content)
@ensure_annotations
def save_bin(data:Any,path:Path):
    """save binary file
    Args:
      data(Any):data to be saves as binary
      path(Path): path to binary file
      """
    joblib.dump(vale=data,filename=path)
    logger.info(f"binary file saved at:{path}")
@ensure_annotations
def load_bin(path:Path)->Any:
    """load binary data
    Args:
      path(Path):path to binary file
    returns:
      ANY:object stored in the file
      """
    data=joblib.load(path)
    logger.info(f"binary file loaded from:{path}")
    return data
@ensure_annotations
def get_size(path:Path)->str:
    """get size in kb
    Args:
      path(Path):path to the file
    return:
    str:size in kb
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb}kb"
def decodeimage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,"wb")as f:
        f.write(imgdata)
        f.close()
def encodeimageintobase64(croppedimagepath):
    with open (croppedimagepath,"rb")as f:
        return base64.b64encode(f.read())