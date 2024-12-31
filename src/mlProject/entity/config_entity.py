
#    from the workflow we are creating and Updating the entity

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:    #data_ingestion
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

    
@dataclass(frozen=True)
class DataValidationConfig:   #data_validation
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:    #data_transformation
    root_dir: Path
    data_path: Path



@dataclass(frozen=True)
class ModelTrainerConfig:      #model_trainer
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str



@dataclass(frozen=True)   
class ModelEvaluationConfig:    #model_evaluation
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str

