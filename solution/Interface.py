from Database import Database
import argparse
import os
from LanguageModel import LanguageModel

def main():
    parser = argparse.ArgumentParser(description="CLI for updating document files with the latest data.")

    parser.add_argument("database_folder", type=str, help="Path to the database folder containing knowledge base files.")
    parser.add_argument("input_file", type=str, help="The document file that needs updating.")

    parser.add_argument("--model", type=str, default="deepseek-r1:8b", help="Name of the LLM model (default: deepseek-r1:8b).")

    args = parser.parse_args()

    if not os.path.isdir(args.database_folder):
        print(f"Error: The folder '{args.database_folder}' does not exist.")
        return

    full_input_path = os.path.join(args.database_folder, args.input_file)
    if not os.path.isfile(full_input_path):
        print(f"Error: The file '{full_input_path}' does not exist in '{args.database_folder}'.")
        return

    llm = LanguageModel(args.model)
    db = Database(data_folder=args.database_folder, language_model=llm)

    print(f"Updating '{args.input_file}' using model '{args.model}'...")
    db.update(args.input_file)

    print("Update process completed.")

if __name__ == "__main__":
    main()
