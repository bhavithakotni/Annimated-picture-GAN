from src.annimated_picture.constant import *
from src.annimated_picture.utilis.common import read_yaml,create_directions
from src.annimated_picture.entity.entity import DataingestionConfig
class ConfigurationManager:
    def __init__(self,config_filepath=config_file_path,params_filepath=params_file_path):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        create_directions([self.config.artifacts_root])
    def get_dataingestion_config(self)->DataingestionConfig:
        config=self.config.data_ingestion
        create_directions([config.root_dir])
        dataingestion_config=DataingestionConfig(root_dir=config.root_dir,local_data_file=config.local_data_file,
                                                 source_url=config.source_url,
                                                 unzip_dir=config.unzip_dir)
        return dataingestion_config
    