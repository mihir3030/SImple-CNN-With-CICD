from CnnDeepClassifier.config import ConfigurationManager
from CnnDeepClassifier.components import DataIngestion
from CnnDeepClassifier import logger

STAGE_NAME = "Data Ingestion Stage"
def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>{STAGE_NAME} started")
        main()
        logger.info(f">>>>>>>>>>{STAGE_NAME} compleated successfully\n\n X==========================X\n\n")
    except Exception as e:
        logger.exception(e)
        raise e