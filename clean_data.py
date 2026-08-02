import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates()
    df = df.dropna()
    cleaned_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned file saved as: {cleaned_path}")
    return cleaned_path

# Example usage
if __name__ == "__main__":
    clean_data("your_file.csv")
