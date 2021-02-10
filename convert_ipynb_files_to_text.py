#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['ipython', 'nbconvert', '--to', 'script', fname], cwd=d)


# In[92]:


os_path = r'C:\Users\Paul\backup_1Nov19\python_stock_APIs\convert_ipynb_files_to_text.ipynb'

# save_path = 

d, fname = os.path.split(os_path)

check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)


# In[ ]:


def convert_ipynb_file_to_py_file(os_path):
    
    d, fname = os.path.split(os_path)

check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)


# In[27]:


import os.path, time 

last_mod_time = time.ctime(os.path.getmtime(os_path))

print(last_mod_time)

# print("last modified: %s" % time.ctime(os.path.getmtime(os_path)))

# print("created: %s" % time.ctime(os.path.getctime(os_path)))


# In[31]:


string_test_1 = 'Mon Apr  6 17:56:58 2020'
string_test_2 = 'Sat Feb  8 17:33:13 2020'
string_test_3 = 'Thu Jun 25 11:10:23 2020'


# In[30]:


regex_YEAR = r"[0-9]{4}$"
regex_MONTH = r"\b([a-z]{3})\s+[0-9]{1,2}\b"
regex_DAY = r"\b[a-z]{3}\s+([0-9]{1,2})\b"


# In[60]:


STRING_TO_TEST = string_test_3

# find YEAR
YEAR = re.findall(regex_YEAR, STRING_TO_TEST)[0]

# find MONTH
matches = re.finditer(regex_MONTH, STRING_TO_TEST, re.I)

for matchNum, match in enumerate(matches, start=1):
    
    MONTH = match.group(1)


# find DAY
matches = re.finditer(regex_DAY, STRING_TO_TEST, re.I)

for matchNum, match in enumerate(matches, start=1):
    
    DAY = match.group(1)

DATE = str(DAY) + r'-' + str(MONTH) + r'-' + str(YEAR)

print(DATE)


# In[86]:


def return_date_of_file(date_of_file):
    
    STRING_TO_TEST = date_of_file

    # find YEAR
    YEAR = re.findall(regex_YEAR, STRING_TO_TEST)[0]

    # find MONTH
    matches = re.finditer(regex_MONTH, STRING_TO_TEST, re.I)

    for matchNum, match in enumerate(matches, start=1):

        MONTH = match.group(1)


    # find DAY
    matches = re.finditer(regex_DAY, STRING_TO_TEST, re.I)

    for matchNum, match in enumerate(matches, start=1):

        DAY = match.group(1)

    DATE = str(DAY) + r'-' + str(MONTH) + r'-' + str(YEAR)

    return DATE


# In[89]:


date_of_file = return_date_of_file(string_test_3)


# In[91]:


return_TRUE_FALSE_date_of_file_is_greater_than_test_date(date_of_file, '25-Jun-2018')


# In[88]:


def return_TRUE_FALSE_date_of_file_is_greater_than_test_date(date_of_file, test_date):
    
    from datetime import datetime

    DATE_OF_FILE = datetime.strptime(date_of_file, '%d-%b-%Y')

    DATE_OF_TEST_DATE = datetime.strptime(test_date, '%d-%b-%Y')

    if DATE_OF_FILE > DATE_OF_TEST_DATE:
        
        return True
    
    else:
        
        return False


# In[85]:


from datetime import datetime

date_time_str = DATE

DATE_OF_FILE = datetime.strptime(date_time_str, '%d-%b-%Y')

print ("The date is", DATE_OF_FILE)

now_time = datetime.now()

now_time < DATE_OF_FILE


# In[119]:


def return_Windows_path_of_py_and_txt_files(os_path):

    from pathlib import Path
    p = Path(os_path)

    py_path_and_name = Path(p.parent.as_posix() + '/' + p.stem + '.py')
    txt_path_and_name = Path(p.parent.as_posix() + '/' + p.stem + '.txt')

    return py_path_and_name, txt_path_and_name


# In[121]:


return_Windows_path_of_py_and_txt_files(os_path)[0]


# In[ ]:


from pathlib import Path
p = Path(os_path)

py_path_and_name = Path(p.parent.as_posix() + '/' + p.stem + '.py')
txt_path_and_name = Path(p.parent.as_posix() + '/' + p.stem + '.txt')

py_path_and_name, txt_path_and_name


# In[115]:


os.rename(py_path_and_name, txt_path_and_name)

