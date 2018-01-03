# -*- coding: utf-8 -*-
"""
Custom module for genreal IO.

Module Name : gsyIO

Author : 高斯羽 博士 (Dr. GAO, Siyu)

Version : 0.2.0

Last Modified : 2018-01-03

Change Log
----------------------
* **Notable changes:**

    + Version : 0.2.0
        - Added "data_time_now"
        - Added "prompt_msg"
        - Added "save_csv"
        - Added "save_csv_gui"
        - Added "save_image_gui"


List of functions
----------------------

* date_time_now_
* prompt_msg_
* save_csv_
* save_csv_gui_
* save_image_gui_
* save_txt_
* save_txt_on_event_
* search_file_and_start_

Function definitions
----------------------

"""

import tkinter as tk
import tkinter.messagebox as msgbox
import os
import glob
import csv
import time

from tkinter import filedialog
from time import gmtime, strftime, sleep

# default extensions for save as images
CONST_IMAGE_FILETER = [('Scalable Vector Graphics','*.svg *.svgz'),
                       ('Portable Network Graphics','*.png'),
                       ('Portable Document Format', '*.pdf'),
                       ('Encapsulated Poscript','*.eps'),
                       ('Joint Photographic Experts Group','*.jpeg *.jpg'),
                       ('PGF code for LaTex','*.pgf'),
                       ('Postscript','*.ps'),
                       ('Raw RGBA bitmap','*.raw *.rgba'),
                       ('Tagged Image File Format','*.tif *.tiff'),
                       ('all files','*.*')]

# =============================================================================
# <Function: get system time and date>
# =============================================================================
def date_time_now():
    """
    .. _date_time_now :
    
    Return the system date and time as a string.

    Return format: 'yyyy-mm-dd, HH:MM:SS:'

    Parameters
    ----------
        None

    Returns
    -------
    str_date_time : str
        Formatted system date time string in 'yyyy-mm-dd, HH:MM:SS:'. 
        The last colon is intended for printing to the console (or making logs).

    Examples
    --------
    >>> date_time_now()
    '2017-11-20, 15:14:42:'
    """

    str_date_time = strftime('%Y-%m-%d, %H:%M:%S:', gmtime())

    return str_date_time
# =============================================================================
# </Function: get system time and date>
# =============================================================================


# =============================================================================
# <Function: save the text as a txt file>
# =============================================================================
def save_txt(str_file_path, str_txt):
    
    """
    .. _save_txt :     
        
    This funciton saves the given string into the given file.
    
    Parameters
    ----------
    str_file_path : str
        The text file full path.
        
    str_txt : str
        The string to be write into the text file.

    Returns
    -------
    bool
        Returns True if read successful (no exception).
        Returns False on exception.

    Examples
    --------
    .. code:: python
    
        bool_success = save_txt(str_file_path, str_txt)
    """

    try:

        file = open(str_file_path, 'w')
        
        file.write(str_txt)
        
        file.close()
        
        return True
    
    except:
        
        return False
# =============================================================================
# </Function: save the text as a txt file>
# =============================================================================


# =============================================================================
# <Function: save the text as a txt file on event>
# =============================================================================
def save_txt_on_event(event, str_txt):

    """
    .. _save_txt_on_event :     

    This funciton calls the "save_txt" function to save the string into a text
    file.
    
    This function prompts file save dialogue to allow the user to interactively
    save the file.
    
    This function prompts messages to tell the user whether the save is successful
    or not.
    
    Reference for using "lambda" : https://goo.gl/zDmGPR

    Parameters
    ----------
    event : event
        The event that triggers this function.
        
    str_txt : str
        The string to be saved.

    Returns
    -------
    
    bool
        Returns True if read successful (no exception). 
        Returns False on exception.
    
    Examples
    --------
    .. code:: python
    
        button_save_help.on_clicked(lambda x: save_txt_on_event(x, CONST_STR_HELP))
        
    """
    
    bool_success = False
    
    try:
    
        locRoot = tk.Tk()
        
        locRoot.withdraw()
        
        str_file_path = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                                      title="Save as txt",
                                                      filetypes = (("Text files","*.txt"),
                                                                   ("all files","*.*")))
            
        locRoot.destroy()
        
        # if user cancelled, exit
        if len(str_file_path) == 0:
            
            return False
        
        else:
            
            pass
        
        if (str_file_path.endswith('.txt') == True) or (str_file_path.endswith('.TXT') == True):
            
            pass
        
        else:
            
            str_file_path = str_file_path + '.txt'
            
        bool_success = save_txt(str_file_path, str_txt)
    
        if bool_success == True:
            
            # prompt finish message
            locRoot = tk.Tk()
            
            locRoot.withdraw()
            
            msgbox.showinfo('Text file save finished', 
                            'Text file save finished.' + '\n' + '\n' + str_file_path)
            
            locRoot.destroy()
            
            return True
        
        else:
            
            # prompt fail message
            locRoot = tk.Tk()
            
            locRoot.withdraw()
            
            msgbox.showinfo('Text file save failed', 
                            'Text file save failed.')
            
            locRoot.destroy()
            
            return False
        
    except:
        
        # prompt fail message
        locRoot = tk.Tk()
        
        locRoot.withdraw()
        
        msgbox.showinfo('Text file save failed', 
                        'Text file save failed.')
        
        locRoot.destroy()
        
        return False        
# =============================================================================
# </Function: save the text as a txt file on event>
# =============================================================================


# =============================================================================
# <Function: search the file according to the given filename 
# and start it with os default app>
# =============================================================================    
def search_file_and_start(str_pattern, str_filename):
    
    """
    .. _search_file_and_start :     
        
    This funciton searchs for the given file according to the given pattern. 
    If the given file is found, this function would try to start the file with
    os default application.
    
    The search is recursive. 
    
    This function uses "glob" for search.
        
    .. code :: python
    
        for item in glob.iglob(str_pattern, recursive=True):
            
            if item.endswith(os.path.join(os.sep , str_filename)):
                
                os.startfile(item)
                
                bool_found = True
                
                break
    
    Parameters
    ----------
    str_pattern : str
        The pattern for searching. E.g.  './\**/\*.html'
        
    str_filename : str
        The filename of the file to be started with os default application.

    Returns
    -------    
    bool
        Returns True if file found. 
        Returns False file not found or on exception.
    
    Examples
    --------
    .. code:: python
    
        bool_found = search_file_and_start(str_pattern, str_doct_filename)

    Reference
    ----------
    https://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
    """
    
    bool_found = False
    
    try:
                
        for item in glob.iglob(str_pattern, recursive=True):
            
            if item.endswith(os.path.join(os.sep , str_filename)):
                
                os.startfile(item)
                
                bool_found = True
                
                break
            
    except:
        
        bool_found = False
        
        pass
    
    return bool_found
# =============================================================================
# </Function: search the file according to the given filename
# and start it with os default app>
# =============================================================================


# =============================================================================
# <Function: save the data as a CSV file>
# =============================================================================
def save_csv(list_header, list_data, str_file_path):
    
    """
    .. _save_csv :     
        
    This function combines the given headers and the given data and then writes
    them into the given CSV file path.
        
    This function uses the "csv" module.
    
    Parameters
    ----------
    list_header : list
        The headers for the data sets.
        
    list_data : list
        The data sets. Each list element can be a 1-D list.
        
    str_file_path : str
        The str file full path.

    Returns
    -------    
    bool
        Returns True if file saved with no exception. 
        No return if exceptions. Instead, the exceptions would be raised.
        
    Raises
    -------
    ValueError
        If the number of headers is not the same as the number of data sets.
        
    ValueError
        If the lengths of all data sets are not the same.
        
    OSError
        If opening the CSV for writing fail or data write to the CSV file fail.
        
    
    Notes
    --------
    To transpose rows to columns, use the "zip" function.
    
    |  See: 
    |  https://goo.gl/SknzT8
    |  https://goo.gl/qqWV8b
        
    .. code:: python
        
        temp_data = list(zip(*list_data))
    
    Examples
    --------
    .. code:: python
    
        import numpy as np
        import csv

        from gsyIO import save_csv
        
        time = np.arange(0, 1, 0.05)

        data1 = np.arange(21, 20, -0.05)
        
        data2 = np.arange(38, 39, 0.05)
        
        headers = ['time', 'data1', 'data2']
        
        data_set = [time, data1, data2]
        
        str_file_path = 'c:/temp/test.csv'
        
        bool_saved = save_csv(headers, data_set, str_file_path)
    """
    
    # error messages----------------------------------------------------------#
    str_err_msg_header_mismatch = ('The number of data headers'
                                   + ' must match the number of data sets')
    
    str_err_msg_data_len_mismatch = ('The length of each data set'
                                     + ' must be all the same')
    
    # error check 1-----------------------------------------------------------#
    # raise ValueError if the number of headers 
    # is not the same as the number of data sets
    if len(list_header) != len(list_data):
        
        print('Error: Header mismatch.' 
              + '\n' + ' Length of header : ' + str(len(list_header)) 
              + '\n' + ' Length of data set : ' + str(len(list_data))
              + '\n' + 'Source : "save_csv"')

        raise ValueError(str_err_msg_header_mismatch)
        
    else:
        
        pass
    
    
    # error check 2-----------------------------------------------------------#
    # raise ValueError if the lenght of the data sets are not the same
    bool_data_len = all( len(x) == len(list_data[0]) for x in list_data )
    
    if bool_data_len == False:

        print('Error: Data length mismatch.'
              + '\n' + 'Source : "save_csv"')
        
        raise ValueError(str_err_msg_data_len_mismatch)
        
    else:
        
        pass
    
    # transpose columns to rows-----------------------------------------------#
    # ref : https://goo.gl/SknzT8
    # ref : https://goo.gl/qqWV8b
    temp_data = list(zip(*list_data))
    
    # add the header string to the first element
    temp_data.insert(0, list_header)
    
    
    # write to CSV file-------------------------------------------------------#
    try:
        
        with open(str_file_path, 'w', newline='') as csv_file:
            
            writer = csv.writer(csv_file)
            
            for item in temp_data:
                
                writer.writerow(item)
                
        return True
        
    except:

        print('Error : OSError.' + '\n' + 'Source "save_csv"')
            
        raise OSError('Error when trying to open/write CSV file ' + str_file_path)
# =============================================================================
# </Function: save the data as a CSV file>
# =============================================================================


# =============================================================================
# <Function: gui for saving the data as a CSV file>
# =============================================================================
def save_csv_gui(list_header, list_data):

    """
    .. _save_csv_gui :     
        
    This function is a gui wrapper for "save_csv".
        
    This function prompts a file save dialogue to allow the user to select the 
    directory and filename.

    This function would then return the full path to "save_csv" to allow saving CSV.
    
    Parameters
    ----------
    list_header : list
        The headers for the data sets.
        
    list_data : list
        The data sets. Each list element can be a 1-D list.
    
    Returns
    -------    
    bool
        Returns True if file saved with no exception. Returns False if exceptions.
    
    Examples
    --------
    .. code:: python
    
        import numpy as np
        import csv
        
        time = np.arange(0, 1, 0.05)

        data1 = np.arange(21, 20, -0.05)
        
        data2 = np.arange(38, 39, 0.05)
        
        headers = ['time', 'data1', 'data2']
        
        data_set = [time, data1, data2]
        
        save_csv_gui(headers, data_set)
        
    """

    bool_success = False

    try:
    
        locRoot = tk.Tk()
        
        locRoot.withdraw()
        
        # prompt dialogue-----------------------------------------------------#
        # you need to set the "defaulttextension" otherwise the returned string 
        # would not have any extension
        str_file_path = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                                      title="Save as CSV",
                                                      defaultextension='.csv',
                                                      filetypes = (("CSV file","*.csv"),
                                                                   ("all files","*.*")))
            
        locRoot.destroy()
        
        # if user cancelled, exit---------------------------------------------#
        if len(str_file_path) == 0:
            
            return False
        
        else:
            
            pass
        
        # extension check-----------------------------------------------------#
        # if the last four letter (case insensitive) is ".csv" then pass,
        # if not, add ".csv"
        if str_file_path[-4:].casefold() == '.csv'.casefold():
            
            pass
        
        else:
            
            str_file_path = str_file_path + '.csv'

        # print(str_file_path)
            
        bool_success = save_csv(list_header, list_data, str_file_path)
    
        if bool_success == True:

            # print('Cmd call successful.')
            
            # prompt finish message
            locRoot = tk.Tk()
            
            locRoot.withdraw()
            
            msgbox.showinfo('CSV file save finished', 
                            'CSV file save finished.' + '\n' + '\n' + str_file_path)
            
            locRoot.destroy()
            
            return True
        
        else:

            # print('Cmd call fail.')
            
            # prompt fail message
            locRoot = tk.Tk()
            
            locRoot.withdraw()
            
            msgbox.showinfo('CSV file save failed', 
                            'CSV file save failed.')
            
            locRoot.destroy()
            
            return False
        
    except:
        
        print('Exception: Source : "save_csv_gui"')

        # prompt fail message
        locRoot = tk.Tk()
        
        locRoot.withdraw()
        
        msgbox.showinfo('CSV file save failed', 
                        'CSV file save failed.')
        
        locRoot.destroy()
        
        return False
# =============================================================================
# <Function: gui for saving the data as a CSV file>
# =============================================================================


# =============================================================================
# <Function: gui for saving images>
# =============================================================================
def save_image_gui(list_filetypes=CONST_IMAGE_FILETER):

    """
    .. _save_image_gui :     
        
    This function is a gui wrapper for getting the image full path. The actual
    implementation of image saving is up to you.
        
    This function prompts a file save dialogue to allow the user to select the 
    directory and filename.
    
    Parameters
    ----------
    list_filetypes : list
        The list for image filetype filters.

        The default list is :

        .. code :: python

            CONST_IMAGE_FILETER = [('Scalable Vector Graphics','*.svg *.svgz'),
                      ('Portable Network Graphics','*.png'),
                      ('Portable Document Format', '*.pdf'),
                      ('Encapsulated Poscript','*.eps'),
                      ('Joint Photographic Experts Group','*.jpeg *.jpg'),
                      ('PGF code for LaTex','*.pgf'),
                      ('Postscript','*.ps'),
                      ('Raw RGBA bitmap','*.raw *.rgba'),
                      ('Tagged Image File Format','*.tif *.tiff'),
                      ('all files','*.*')]

       

    Returns
    -------    
    str_file_path : str
        The full path of the image file.
    
    Examples
    --------
    .. code:: python
    
        import numpy as np
        import csv
        
        time = np.arange(0, 1, 0.05)

        data1 = np.arange(21, 20, -0.05)
        
        data2 = np.arange(38, 39, 0.05)
        
        headers = ['time', 'data1', 'data2']
        
        data_set = [time, data1, data2]
        
        str_filename = save_csv_gui(headers, data_set)

        print(str_filename)
    """

    str_ini_dir = os.getcwd()

    str_title = 'Save as image'

    try:
    
        locRoot = tk.Tk()
        
        locRoot.withdraw()

        # print('just above')
        
        # prompt dialogue-----------------------------------------------------#
        str_file_path = filedialog.asksaveasfilename(initialdir=str_ini_dir,
                                                      title=str_title,
                                                      defaultextension='.png',
                                                      filetypes = list_filetypes)
            
        locRoot.destroy()

        return str_file_path

    except:

        # print('exception img')

        return ''
# =============================================================================
# </Function: gui for saving images>
# =============================================================================


# =============================================================================
# <Function: prompt different types of messages>
# =============================================================================
def prompt_msg(str_title, str_msg, str_type='info'):

    """
    .. _prompt_msg :     
        
    This function is a wrapper for tk's three different message boxes.
        
    This function prompts a message box with the message given.
    
    Parameters
    ----------
    str_title : str
        Title of the message box.

    str_msg : str
        The message to be shown.

    str_type : str, default = "info"
        Type of the message box.

        * "info" = information message box. This is the default value.
        * "err" = error message box
        * "warn" = warning message box


    Returns
    -------    
    None
    
    Examples
    --------
    .. code:: python
    
        import tkinter as tk
        import tkinter.messagebox as msgbox

        import gsyIO

        gsyIO.prompt_msg('message title', 'message body', 'err')
    """
    # make tk main window-----------------------------------------------------#
    root = tk.Tk()

    # hide tk main window-----------------------------------------------------#
    root.withdraw()

    # prompt info msg---------------------------------------------------------#
    if str_type == 'info':

        msgbox.showinfo(str_title, str_msg)

    # prompt error msg--------------------------------------------------------#
    elif str_type == 'err':

        msgbox.showerror(str_title, str_msg)

    # prompt warning msg------------------------------------------------------#
    elif str_type == 'warn':

        msgbox.showwarning(str_title, str_msg)

    # default, prompt info msg------------------------------------------------#
    else:
        
        msgbox.showinfo(str_title, str_msg)

    # destroy tk main window--------------------------------------------------#
    root.destroy()
# =============================================================================
# </Function: prompt different types of messages>
# =============================================================================