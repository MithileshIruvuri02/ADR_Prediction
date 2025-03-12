import pandas as pd
import os

# Define project paths
PROJECT_PATH = r"M:\SEM 6 COURSES\BI\ADR_Prediction\ADR_Prediction"
FAERS_PATH = os.path.join(PROJECT_PATH, "data", "faers_24q4")

def preprocess_faers():
    """Load and preprocess FAERS data."""
    
    # Define file paths
    files = {
        "demographics": "DEMO24Q4.txt",
        "drugs": "DRUG24Q4.txt",
        "reactions": "REAC24Q4.txt"
    }
    
    # Load datasets
    demographics = pd.read_csv(os.path.join(FAERS_PATH, files["demographics"]), delimiter="$", low_memory=False)
    drugs = pd.read_csv(os.path.join(FAERS_PATH, files["drugs"]), delimiter="$", low_memory=False)
    reactions = pd.read_csv(os.path.join(FAERS_PATH, files["reactions"]), delimiter="$", low_memory=False)

    # Standardizing column names
    demographics.columns = demographics.columns.str.lower().str.strip()
    drugs.columns = drugs.columns.str.lower().str.strip()
    reactions.columns = reactions.columns.str.lower().str.strip()

    # Select relevant columns
    demographics = demographics[["primaryid", "caseid", "age", "sex", "wt", "reporter_country"]]
    drugs = drugs[["primaryid", "caseid", "drugname", "route", "dose_amt", "dose_freq"]]
    reactions = reactions[["primaryid", "caseid", "pt"]]  # PT = Preferred Term (reaction)

    # Merge datasets on 'primaryid' and 'caseid'
    merged_df = demographics.merge(drugs, on=["primaryid", "caseid"]).merge(reactions, on=["primaryid", "caseid"])

    # Handle missing values
    merged_df.fillna({"age": merged_df["age"].median(), "wt": merged_df["wt"].median(), "sex": "UNKNOWN"}, inplace=True)

    # Save preprocessed data
    output_path = os.path.join(PROJECT_PATH, "data", "processed_faers.csv")
    merged_df.to_csv(output_path, index=False)
    
    print(f"Preprocessed FAERS data saved to {output_path}")
    
    
def preprocess_sider():
    """Load and preprocess SIDER dataset."""
    SIDER_PATH = os.path.join(PROJECT_PATH, "data", "sider")

    # Load SIDER side effects dataset
    side_effects = pd.read_csv(os.path.join(SIDER_PATH, "meddra_all_se.tsv"), sep="\t", header=None)
    side_effects.columns = ["drug_id", "stitch_id", "umls_id", "type", "umls_id_version", "side_effect"]
    side_effects = side_effects[["drug_id", "side_effect"]]
    side_effects.to_csv(os.path.join(SIDER_PATH, "processed_side_effects.csv"), index=False)
    
    print("✅ SIDER side effects processed successfully!")

    # Load SIDER indications dataset
    indications_file = os.path.join(SIDER_PATH, "meddra_all_indications.tsv")
    
    if os.path.exists(indications_file):
        indications = pd.read_csv(indications_file, sep="\t", header=None)

        # Print the number of columns detected
        print(f"Indications dataset has {indications.shape[1]} columns.")

        # Define the correct column names
        indications.columns = ["stitch_id", "umls_id", "concept_name", "meddra_concept_type", "meddra_id", "indication", "extra_column"]

        # Keep only relevant columns
        indications = indications[["stitch_id", "indication"]]

        # Save the processed indications
        indications.to_csv(os.path.join(SIDER_PATH, "processed_indications.csv"), index=False)
        
        print("✅ SIDER indications processed successfully!")
    else:
        print("⚠️ Indications file not found! Skipping...")




# Run preprocessing
if __name__ == "__main__":
    preprocess_sider()
    preprocess_faers()

    print("Preprocessing completed.")
