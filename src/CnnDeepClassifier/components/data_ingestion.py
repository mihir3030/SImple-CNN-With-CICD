import os
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path
from CnnDeepClassifier.entity import DataIngestionConfig
from CnnDeepClassifier import logger
from CnnDeepClassifier.utils import get_size
from tqdm import tqdm  # giving progressbar in terminal

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self, ):
        logger.info("trying to download files...")
        if not os.path.exists(self.config.local_data_file_dir):
            logger.info("download started")
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file_dir
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file_dir))}")

    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            logger.info(f"removeing file: {target_filepath} of size zero: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    def unzip_and_clean(self):
        logger.info(f"unziping file and removing unwanted files")
        with ZipFile(file=self.config.local_data_file_dir, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)
