import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def extract_data(file_path):
    print("Loading data...")
    return pd.read_csv(file_path)

def transform_data(df):
    df = df.dropna()

    label_enc = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = label_enc.fit_transform(df[col])

    scaler = StandardScaler()
    num_cols = df.select_dtypes(include=['int64','float64']).columns
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df

def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print("Saved to:", output_path)

def run_pipeline(input_file, output_file):
    df = extract_data(input_file)
    df = transform_data(df)
    load_data(df, output_file)

if __name__ == "__main__":
    input_file = r"C:\Users\aruna\Downloads\play_tennis.csv"
    output_file = r"C:\Users\aruna\Downloads\processed_data.csv"

    run_pipeline(input_file, output_file)
