import os
import shutil


class ManageFilesFolders:
    def __init__(self, src, dst) -> None:
        self.src = src
        self.dst = dst

    def read_dir(self):
        entries = os.listdir(self.src)
        files = [entry for entry in entries if os.path.isdir(os.path.join(self.src, entry))]
        return files

    def read_file(self):
        entries = os.listdir(self.src)
        files = [entry for entry in entries if os.path.isfile(os.path.join(self.src, entry))]
        return files

    # Type name ex: '.exe'
    def read_file_type(self, type_name):
        entries = os.listdir(self.src)
        files = [
            entry
            for entry in entries
            if os.path.isfile(os.path.join(self.src, entry)) and entry.endswith(type_name)
        ]
        return files

    def get_target_type(self):
        temp_type = []
        set_type = ()
        files = self.read_file(self.src)
        for file in files:
            temp = file.split(".")
            temp_type.append(temp[-1])
            set_type = set(temp_type)
        return set_type

    def rename_folder(self, current_folder_path, new_folder_path):
        try:
            os.rename(current_folder_path, new_folder_path)
            print(
                f"Folder renamed from '{current_folder_path}' to '{new_folder_path}' successfully."
            )
        except Exception as e:
            print(f"An error occurred while renaming the folder: {e}")

    def move_file(self, src_file, dst_dir):
        try:
            # Check if the source file exists
            if not os.path.isfile(src_file):
                print(f"Source file '{src_file}' does not exist.")
                return

            # Check if the dstination directory exists, if not, create it
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

            # Construct the dstination file path
            dst_file = os.path.join(dst_dir, os.path.basename(src_file))

            # Move the file
            shutil.move(src_file, dst_file)
            print(f"File '{src_file}' moved to '{dst_file}' successfully.")

        except Exception as e:
            print(f"An error occurred while moving the file: {e}")

    def loop_move_file(self, files):
        for file in files:
            src_path = os.path.join(self.src, file)
            self.move_file(src_path, self.dst)
