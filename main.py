from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import sys
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline


# def test_exception():
#     try:
#         x=1/0
#     except Exception as e:
#         raise SensorException(e,sys)

if __name__ == '__main__': 

    # to check data ingestion.  
    # import entire collection m from mongo db as DF and save in feature stor dir as a csv file.
    # split the data into train and test and save them as csv in "ingested " dir 
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()

    # to check data ingestion configuration
    # training_pipeline_config = TrainingPipelineConfig()
    # data_ingestion_config = DataIngestionConfig(training_pipeline_config = training_pipeline_config)
    # print(data_ingestion_config.__dict__)
    
    #to check custom exception handling
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)

    #to check mongo db connection
    # mongo_db_connection = MongoDBClient()
    # print("collection_names = ",mongo_db_connection.database.list_collection_names())
