import urllib.request as request
import zipfile
from pathlib import Path
from src.annimated_picture import logger
from src.annimated_picture.entity.entity import DataingestionConfig
import os

from src.annimated_picture.utilis.common import get_size
class Dataingestion:
    def __init__(self,config:DataingestionConfig):
        self.config=config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(url=self.config.source_url,
                                                 filename=self.config.local_data_file)
            logger.info(f"downloded:{filename}")
        else:
            logger.info("file already exits")
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r')as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"extracted to :{unzip_path}")