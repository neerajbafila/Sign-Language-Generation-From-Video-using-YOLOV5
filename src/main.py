
import mlflow
import argparse
import os
import logging



STAGE = "MAIN" ## stage name


def main():
    with mlflow.start_run() as run:
        mlflow.run(".", "get_data", use_conda=False)
        mlflow.run(".", "base_model_creation", use_conda=False)
        mlflow.run(".", "prepare_callbacks", use_conda=False)
        mlflow.run(".", "model_training", use_conda=False)


if __name__ == "__main__":

    # logging.info("\n************************************")
    
    try:
        logging.info("\n************************************")
        logging.info(f">>>>>>>>>>{STAGE} STARTED<<<<<<<<<<")
        main()
        logging.info(f">>>>>>>>>>{STAGE} COMPLETED SUCCESSFULLY<<<<<<<<<<")
    except Exception as e:
        logging.exception(e)
        raise e



