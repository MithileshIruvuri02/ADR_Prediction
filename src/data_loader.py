import pandas as pd
import os

def load_faers_data(directory):
    """Load FAERS data from TXT files into Pandas DataFrames."""
    files = {
        "demographics": "DEMO24Q4.txt",
        "drugs": "DRUG24Q4.txt",
        "reactions": "REAC24Q4.txt",
        "outcomes": "OUTC24Q4.txt"
    }
    
    data = {}
    for key, filename in files.items():
        path = f"{directory}/{filename}"
        data[key] = pd.read_csv(path, delimiter="$", low_memory=False)
    
    return data  # Returns a dictionary of DataFrames

# Example usage:
# faers_data = load_faers_data("data/faers_2024q1")



def load_sider_data():
    """Load SIDER dataset from TSV files into Pandas DataFrames."""
    project_path = r"M:\SEM 6 COURSES\BI\ADR_Prediction\ADR_Prediction"
    sider_path = os.path.join(project_path, "data", "sider")

    side_effects = pd.read_csv(os.path.join(sider_path, "meddra_all_se.tsv"), sep="\t", header=None)
    indications = pd.read_csv(os.path.join(sider_path, "meddra_all_indications.tsv"), sep="\t", header=None)

    return {"side_effects": side_effects, "indications": indications}

# Example usage:
sider_data = load_sider_data()
print(sider_data["side_effects"].head())  # Display first few rows of side effects data