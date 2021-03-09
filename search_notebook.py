'''
Created on February 10, 2021
Function to convert Jupyter Notebook files ('.ipynb') to text files
and then search for a string
Returns a list of file paths of .ipynb files containing the string
@author: pauladjata
'''

# import site-packages and modules
import os
import shutil


def main(string_to_search, selected_path):

    def save_ipynb_file_as_txt_file(filename):

        import re

        regex = r".ipynb$"

        subst = "_copy.ipynb"

        # 1. make copy of ipynb file

        orig_ipynb_file = filename

        # new_ipynb_file = filename.replace('.ipynb', '_copy.ipynb')

        new_ipynb_file = re.sub(regex, subst, filename, 0, re.MULTILINE)

        shutil.copy2(orig_ipynb_file, new_ipynb_file)

        # 2. change extension of new file from .ipynb to .txt

        subst = ".txt"

        ipynb_fname = new_ipynb_file
        # txt_fname = new_ipynb_file.replace('.ipynb', '.txt')

        txt_fname = re.sub(regex, subst, ipynb_fname, 0, re.MULTILINE)

        os.rename(ipynb_fname, txt_fname)

        return txt_fname

    def search_text_file_for_string(filename_to_search):

        with open(filename_to_search, encoding="utf8") as f:
            datafile = f.readlines()

            for line in datafile:
                if string_to_search.lower() in line.lower():

                    return True

            return False

    # This is the path where you want to search
    if not selected_path:

        selected_path = os.getcwd()

    if not os.path.isdir(selected_path):

        print("THE DIRECTORY GIVEN DOES NOT EXIST")

        return None

    # this is the extension you want to detect
    extension = ".ipynb"

    filepath_list = []

    file_info_dict = {}
    key = 0

    for root, dirs_list, files_list in os.walk(selected_path):
        for file_name in files_list:
            if os.path.splitext(file_name)[-1] == extension:
                file_name_path = os.path.join(root, file_name)

                if file_name_path not in filepath_list:

                    file_info_dict.setdefault(key, [])

                    file_info_dict[key] = {
                        'root': root,
                        'filename': file_name,
                        'file_name_path': file_name_path
                    }

                    filepath_list.append(file_name_path)

                    key += 1

    found_search_string_in_ipynb_file_list = []

    for k, v in file_info_dict.items():

        # print(k, v)

        txt_file_name = save_ipynb_file_as_txt_file(v['file_name_path'])

        if search_text_file_for_string(txt_file_name):

            if ".ipynb_checkpoints" not in txt_file_name:

                found_search_string_in_ipynb_file_list.append(
                    txt_file_name.replace('_copy.txt', '.ipynb'))

        os.remove(txt_file_name)

    if len(found_search_string_in_ipynb_file_list) == 0:

        print('__ NO FILE FOUND CONTAINING THE SEARCH STRING',
              string_to_search, ' __')

    for i, j in enumerate(found_search_string_in_ipynb_file_list):

        print(i, j)


if __name__ == "__main__":

    import argparse

    ap = argparse.ArgumentParser()

    # Add the arguments to the parser

    # Required positional argument
    ap.add_argument('search_string', type=str,
                    help="A required string positional argument. Format 'string to search' Must be surrounded by double quotes")

    ap.add_argument("--path", type=str, required=False, default=None,
                    help=r"An optional string positional argument. Used to set the root path from which to search. Format 'C:\Users' Must be surrounded by double quotes")

    args = ap.parse_args()

    if (args.search_string == None or len(args.search_string) == 0):
        ap.print_help()
    else:
        main(string_to_search=args.search_string, selected_path=args.path)
