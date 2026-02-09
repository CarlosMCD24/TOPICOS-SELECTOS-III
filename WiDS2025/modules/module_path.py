from pathlib import Path


def train_data_path() -> Path:
    """
    Returns the location of train data directory, allowing for script executions in subfolders without worrying about the
    relative location of the data

    :return: the path to the train data directory
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "data/TRAIN_OLD"
        if data_folder.exists() and data_folder.is_dir():
            print("Train data directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Data not found")
        
def test_data_path() -> Path:
    """
    Returns the location of test data directory, allowing for script executions in subfolders without worrying about the
    relative location of the data

    :return: the path to the test data directory
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "data/TEST"
        if data_folder.exists() and data_folder.is_dir():
            print("Test data directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Data not found")
        
        
def plots_data_path() -> Path:
    """
    Returns the location of the Plots directory, allowing for script executions in subfolders without worrying about the
    relative location of the data

    :return: the path to the plots directory
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "plots"
        if data_folder.exists() and data_folder.is_dir():
            print("Plots directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Plots directory not found")
        
def mlruns_data_path() -> Path:
    """
    Returns the location of the mlruns directory, allowing for script executions in subfolders without worrying about the
    relative location of the data

    :return: the path to the plots directory
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "mlruns"
        if data_folder.exists() and data_folder.is_dir():
            print("Mlruns directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Mlruns directory not found")
        
def submission_data_path() -> Path:
    """
    Returns the location of the submission directory, allowing for script executions in subfolders without worrying about the
    relative location of the data

    :return: the path to the plots directory
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "submission"
        if data_folder.exists() and data_folder.is_dir():
            print("Submission directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Submission directory not found")