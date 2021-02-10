# search_ipynb_files_for_string
Searches directory for Jupyter Notebook files for particular string


purpose: to search a directory recursively for any Jupyter Notebook files ('.ipynb')
If a Jupyter Notebook file is found:
1. it is converted to a text file and then;
2. searched for a string the user enters
3. returns a list of filepaths to the .ipynb file containing the search term

To use:

1. cd into directory which you would like to search
2. in command line: [ python search_notebook.py "string to search" ]
3. the search string must be surrounded by double quotes

