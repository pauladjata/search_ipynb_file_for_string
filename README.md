# search_ipynb_files_for_string

Searches directory for Jupyter Notebook files for particular string

Purpose: to search a directory recursively for any Jupyter Notebook files ('.ipynb')

If a Jupyter Notebook file is found:

1. it is converted to a text file and then;
2. searched for a string the user enters
3. returns a list of filepaths to the .ipynb file containing the search term

To use:

1. cd into directory which you would like to search
2. in command line: [ python search_notebook.py "string to search" ]
3. the search string must be surrounded by double quotes

The results are displayed in the command line.

OPTIONAL:

1. allows user to select directory (optional argument)
2. in command line: [ python search_notebook.py "string to search" --path "C:\Users\User\selected_directory"]
3. the directory path string must be surrounded by double quotes
