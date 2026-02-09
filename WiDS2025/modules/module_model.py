# Standard libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import functools

# Sklearn
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split

# MLFlow
import mlflow
from mlflow.models.signature import infer_signature

# External modules
from module_path import plots_data_path, mlruns_data_path, submission_data_path

def mlflow_logger(func):
    """Decorator to automatically start and close an mlflow run"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #create a new experiment if not in mlruns directory
        mlruns_path = mlruns_data_path()
        #mlflow.set_tracking_uri(mlruns_path)
        mlflow.set_tracking_uri('http://ec2-18-221-104-103.us-east-2.compute.amazonaws.com:5000')
        #print(mlflow.get_artifact_uri())
        experiment_name = 'WIDS2025'

        try:
            exp_id = mlflow.create_experiment(name=experiment_name)
        except Exception as e:
            exp_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

        with mlflow.start_run(experiment_id=exp_id):
            return func(*args, **kwargs)
    return wrapper


class ModelEvaluation:
    """
    Supports the evaluation of classification models (multinomial), collecting the results.
    """

    def __init__(self, X: pd.DataFrame, y: pd.Series, tag: str, test_size: float = 0.3, shuffle: bool = True, random_state: int = 42):
        """
        :param X: the inputs
        :param y: the prediction targets
        :param test_size: the fraction of the data to reserve for testing
        :param shuffle: whether to shuffle the data prior to splitting
        :param random_state: the random seed
        :param tag: target name for logging
        """

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y,
            random_state=random_state, test_size=test_size, shuffle=shuffle)
        
        self.tag = tag

    @mlflow_logger
    def evaluate_model(self, model) -> float:
        """
        :param model: the model to evaluate
        :return: the f1-score
        """
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        f1_score = metrics.f1_score(self.y_test, y_pred)
        print(f"{model}: f1_score={f1_score:.1f}")

        # log parameters and metrics in MLFlow
        mlflow.log_param("Model Type", type(model).__name__ + '_' + self.tag)
        for hyperparameter, value in model.get_params().items():
            mlflow.log_param(hyperparameter, value)
        mlflow.log_metric("f1_score", f1_score)
        signature = infer_signature(self.X_train, model.predict(self.X_train))
        mlflow.sklearn.log_model(model, "model", signature=signature)

        return f1_score
    
class ModelSubmission:

    """
    Supports the submission of a model using mlflow, using a dataset
    """

    def __init__(self, X: pd.DataFrame, version: int=1, threshold: float = 0.5):
        """
        :param X: the inputs of the test dataset
        :param version: version of the registered model
        :param threshold: threshold for predicting labels based on predicted probability
        """

        self.X = X
        self.version = version
        self.threshold = threshold

    def load_model(self):
        """
        :return: (tuple) The sklearn models registered in mlflow for sex_f and adhd, respectively
        """

        mlflow.set_tracking_uri(mlruns_data_path())

        model_sex_f = mlflow.sklearn.load_model(f"models:/Model_sex_f/{self.version}")
        model_adhd = mlflow.sklearn.load_model(f"models:/Model_adhd/{self.version}")

        return model_sex_f, model_adhd
    
    def predictions_proba(self):
        """
        :return: (tuple) Predicted probabilities for 1 class (sex_f, adhd)
        """
        
        model_sex_f, model_adhd = self.load_model()
        
        sex_proba = model_sex_f.predict_proba(self.X)
        adhd_proba = model_adhd.predict_proba(self.X)

        return sex_proba[:,1], adhd_proba[:,1]
    
    def predictions_labels(self):
        """
        :return: (tuple) Predicted probabilities for 1 class (sex_f, adhd)
        """
        
        model_sex_f, model_adhd = self.load_model()
        
        sex_labels = model_sex_f.predict(self.X)
        adhd_labels = model_adhd.predict(self.X)

        return sex_labels, adhd_labels
    
    def predictions_labels_from_proba(self):
        """
        :return: (tuple) Array of predicted classes for (sex_f, adhd)
        """

        sex_proba, adhd_proba = self.predictions_proba()

        sex_labels = np.where(sex_proba > self.threshold, 1, 0)
        adhd_labels = np.where(adhd_proba > self.threshold, 1, 0)

        return sex_labels, adhd_labels
    
    def to_submission(self, output_name: str):
        """
        Writes a csv file based on the submission form
        """

        sex_labels, adhd_labels = self.predictions_labels_from_proba()

        submission = pd.read_excel("../data/SAMPLE_SUBMISSION.xlsx")

        submission["ADHD_Outcome"] = adhd_labels
        submission["Sex_F"] = sex_labels

        submission.to_csv(os.path.join(submission_data_path(), output_name), index=False)
        
