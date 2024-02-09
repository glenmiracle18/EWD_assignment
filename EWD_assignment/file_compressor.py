import os
import zipfile
import tarfile
import datetime

def compress_files():
    folder_to_compress = input("Enter the path to the folder you want to compress: ")
    available_types = [".zip", ".tar", ".tgz"]
    print("Available compressed file types:")
    for i, type in enumerate(available_types):
        print(f"{i + 1}. {type}")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    compress_type = available_types[choice - 1]

    try:
        if compress_type == ".tgz":
            today = datetime.date.today().strftime("%Y_%m_%d")
            archive_name = f"{os.path.basename(folder_to_compress)}_{today}{compress_type}"
            with tarfile.open(archive_name, "w:gz") as tar:
                tar.add(folder_to_compress, arcname=os.path.basename(folder_to_compress))
        else:
            archive_name = f"{os.path.basename(folder_to_compress)}{compress_type}"
            if compress_type == ".zip":
                with zipfile.ZipFile(archive_name, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                    for root, _, files in os.walk(folder_to_compress):
                        for file in files:
                            zipf.write(os.path.join(root, file))
            else:
                with tarfile.open(archive_name, "w") as tar:
                    tar.add(folder_to_compress, arcname=os.path.basename(folder_to_compress))

        print(f"Compression successful! Archive created: {archive_name}")
    except Exception as e:
        print(f"Compression failed: {e}")

if __name__ == "__main__":
    compress_files()

