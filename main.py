from src import logger
from src.annimated_picture.pipeline.dataingestion1 import DataingestionPipeline

stage_name= "dataingestion "

try:
    logger.info(f">>>>>>stage{stage_name}started<<<<<<")
    obj = DataingestionPipeline()
    obj.main()
    logger.info(f">>>>>>stage{stage_name} completed<<<")
except Exception as e:
    logger.exception(e)
    raise e  