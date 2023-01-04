from CnnDeepClassifier.utils import read_yaml_file, create_directories
from CnnDeepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from CnnDeepClassifier.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml_file(config_filepath)
        self.params = read_yaml_file(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file_dir=config.local_data_file_dir,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config