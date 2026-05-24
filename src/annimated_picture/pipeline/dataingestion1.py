from src.annimated_picture.config.configuration import ConfigurationManager
from src.annimated_picture.components.dataingestion import Dataingestion
from src import logger

stage_name=" dataingestion"

class DataingestionPipeline:
    def __init__(self):
        pass
    def main(self):    
        config=ConfigurationManager()
        data_ingestion_config= config.get_dataingestion_config()
        data_ingestion= Dataingestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>stage{stage_name}started<<<<<<")
        obj = DataingestionPipeline()
        obj.main()
        logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e