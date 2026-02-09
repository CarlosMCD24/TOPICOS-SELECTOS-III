# Standard libraries
import pandas as pd
import os

# Sklearn libraries
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer

# External libraries
from module_path import train_data_path, test_data_path

COL_EHQ_EHQ_TOTAL = "EHQ_EHQ_Total"
COL_COLORVISION_CV_SCORE = "ColorVision_CV_Score"
COL_APQ_P_APQ_P_CP = "APQ_P_APQ_P_CP"
COL_APQ_P_APQ_P_ID = "APQ_P_APQ_P_ID"
COL_APQ_P_APQ_P_INV = "APQ_P_APQ_P_INV"
COL_APQ_P_APQ_P_OPD = "APQ_P_APQ_P_OPD"
COL_APQ_P_APQ_P_PM = "APQ_P_APQ_P_PM"
COL_APQ_P_APQ_P_PP = "APQ_P_APQ_P_PP"
COL_SDQ_SDQ_CONDUCT_PROBLEMS = "SDQ_SDQ_Conduct_Problems"
COL_SDQ_SDQ_DIFFICULTIES_TOTAL = "SDQ_SDQ_Difficulties_Total"
COL_SDQ_SDQ_EMOTIONAL_PROBLEMS = "SDQ_SDQ_Emotional_Problems"
COL_SDQ_SDQ_EXTERNALIZING = "SDQ_SDQ_Externalizing"
COL_SDQ_SDQ_GENERATING_IMPACT = "SDQ_SDQ_Generating_Impact"
COL_SDQ_SDQ_HYPERACTIVITY = "SDQ_SDQ_Hyperactivity"
COL_SDQ_SDQ_INTERNALIZING = "SDQ_SDQ_Internalizing"
COL_SDQ_SDQ_PEER_PROBLEMS = "SDQ_SDQ_Peer_Problems"
COL_SDQ_SDQ_PROSOCIAL = "SDQ_SDQ_Prosocial"
COL_MRI_TRACK_AGE_AT_SCAN = "MRI_Track_Age_at_Scan"
COL_BASIC_DEMOS_ENROLL_YEAR = "Basic_Demos_Enroll_Year"
COL_BASIC_DEMOS_STUDY_SITE = "Basic_Demos_Study_Site"
COL_PREINT_DEMOS_FAM_CHILD_ETHNICITY = "PreInt_Demos_Fam_Child_Ethnicity"
COL_PREINT_DEMOS_FAM_CHILD_RACE = "PreInt_Demos_Fam_Child_Race"
COL_MRI_TRACK_SCAN_LOCATION = "MRI_Track_Scan_Location"
COL_BARRATT_BARRATT_P1_EDU = "Barratt_Barratt_P1_Edu"
COL_BARRATT_BARRATT_P1_OCC = "Barratt_Barratt_P1_Occ"
COL_BARRATT_BARRATT_P2_EDU = "Barratt_Barratt_P2_Edu"
COL_BARRATT_BARRATT_P2_OCC = "Barratt_Barratt_P2_Occ"


class Dataset:

    def __init__(self, num_samples: int = None, random_seed: int = 42):
        """
        :param num_samples: the number of samples to draw from the data frame; if None, use all samples
        :param random_seed: the random seed to use when sampling data points
        """

        self.num_samples = num_samples
        self.random_seed = random_seed
    
    def load_data_frame(self) -> pd.DataFrame:
        """
        :return: the full data frame for this dataset for train features, test features, and training labels

        Note: Null values are dropped and invoice date variable type is changed to timestamp
        """

        train_path = train_data_path()
        test_path = test_data_path()
        
        train_q = pd.read_excel(os.path.join(train_path,"TRAIN_QUANTITATIVE_METADATA.xlsx"))
        train_c = pd.read_excel(os.path.join(train_path,"TRAIN_CATEGORICAL_METADATA.xlsx"))
        test_q = pd.read_excel(os.path.join(test_path,"TEST_QUANTITATIVE_METADATA.xlsx"))
        test_c = pd.read_excel(os.path.join(test_path,"TEST_CATEGORICAL.xlsx"))

        train_combined = pd.merge(train_q, train_c, on="participant_id", how="left").set_index("participant_id")
        test_combined = pd.merge(test_q, test_c, on="participant_id", how="left").set_index("participant_id")

        labels = pd.read_excel(os.path.join(train_path,"TRAINING_SOLUTIONS.xlsx")).set_index("participant_id")
        assert all(train_combined.index == labels.index), "Label IDs don't match train IDs"

        # drop columns (cause missing values)
        drop_cols = [COL_MRI_TRACK_AGE_AT_SCAN, COL_PREINT_DEMOS_FAM_CHILD_ETHNICITY]
        train_combined.drop(drop_cols, axis=1, inplace=True)
        test_combined.drop(drop_cols, axis=1, inplace=True)

        # impute missing values
        test_combined.fillna(test_combined.median(numeric_only=True), inplace=True)

        # Sample
        if self.num_samples is not None:
            train_combined = train_combined.sample(self.num_samples, random_state=self.random_seed)   

        return train_combined, test_combined, labels
    
