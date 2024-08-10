import zipfile
import os


def zip_lambda_function(zip_filename, source_folder):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_folder))


if __name__ == "__main__":
    # Update these paths as needed
    zip_filename = 'lambda_function.zip'
    source_folder = r'XXXXXXXXXXXXXXXXXXXXXXX'   # Replace with your lambda_function.py file path which is in lambda_function directory in this project only

    zip_lambda_function(zip_filename, source_folder)
    print(f'Created zip file: {zip_filename}')