import pandas as pd
import sys

def clean_data(file_path):
    try:
        df = pd.read_csv(file_path)
        original_rows = len(df)

        # Remove duplicates
        df = df.drop_duplicates()
        duplicates_removed = original_rows - len(df)

        # Remove rows with missing values
        df = df.dropna()
        missing_removed = original_rows - duplicates_removed - len(df)

        # Save cleaned file
        cleaned_path = file_path.replace('.csv', '_cleaned.csv')
        df.to_csv(cleaned_path, index=False)

        print(f"✅ Cleaned file saved as: {cleaned_path}")
        print(f"Original rows: {original_rows}")
        print(f"Duplicates removed: {duplicates_removed}")
        print(f"Rows with missing values removed: {missing_removed}")
        print(f"Final rows: {len(df)}")

        return cleaned_path

    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_data.py your_file.csv")
    else:
        clean_data(sys.argv[1])
