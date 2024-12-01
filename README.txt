Created: 2024-11-30

#####################################
#Python Robotic Enterprise Framework#
#####################################

CONTENTS
--------
1. Purpose
2. Structure
2.1. The Data folder
2.2. The Framework folder
3. Function 
--------

1. Purpose:
--------
This project is intended to mirror the structure and capability of the Robotic Enterprise Framework found in UiPath. A project based on the framework should be able to process large quantities of data in an orderly and controlled manner, making the framework an effective tool for data processing. 
The code itself is extensively documented internally and as such should be legible to anyone with a working understanding of programming and the UiPath REF.
--------

2. Structure:
--------
The basic file structure of the project is the same as the UiPath REF; the project root folder contains one Main file and two subfolders (in addition to this README, of course):
 - Main.py
 - Data
 - Framework

Any additional subroutines developed for specific projects can be placed either directly in the root project folder or in a folder dedicated to contain those subroutines. Subroutines sharing or working in the same systems should ideally be placed in the same subfolders in the root project folder. If subroutines are given their own subfolders, these must include an empty __init__.py file in order for that folder to be available to the project as a module.
--------

2.1. The Data folder:
--------
The Data folder contains an empty __init__.py file necessary to make the folder a python module available to the 
project and one config file in the json format. The config file, similarly to the REF config file in UiPath, contains project specific information used in processing such as folder paths, urls and more.
In addition, the Data folder contains two subfolders:
 - Input 
 - Output

These two subfolders are intended to contain any input and output data the specific project may require and/or produce. Note: by default, the project logger outputs a log to the output folder. The location of the project log can be changed in the logger module. For more info about the project logger, see below. 
--------

2.2. The Framework folder:
--------
The Framework folder contains an empty __init__.py file like the Data folder necessary to make the Framework folder
a module available to the project. In addition, the folder contains eight subroutines used by the Main file; 
six of these are to be considered as core modules necessary for and intended to mirror the role of the framework workflows (and in some sense the state machine states) in the UiPath REF:
 - Initialization
 - InitApps	
 - GetTransactionData		
 - Proces	
 - SetTransactionStatus
 - End

In addition to the six core modules listed above, the Framework folder also contains two other modules which are not critical to the core function of the PyREF as such, but provide important utility in terms of the capability of the UiPath REF: 
 - Logger			
 - ClassBRE

For more details on the function of the various modules, see below. 
--------

3. Function:
--------
Each subroutine manages the tasks of the workflows and and in some sense mirrors the four states of the UiPath REF. The core funcionality of the framework is handled by the first six subroutines listed above:

 - Initialization: 		this subroutine initializes anything necessary for the specific project to run

 - InitApps:			this subroutine found in Initialization initializes any third party software 						necessary for the specific project

 - GetTransactionData:		this subroutine retrieves the data the specific project should process as well as 					each single item to be processed in that data

 - Proces:			this subroutine processes each single item in the data bulk

 - SetTransactionStatus:	this subroutine updates the status of each single processed item according to its 					result; success, Business Rule Exception or Exception. This subroutine also controls 					which item should be processed next

 - End:				this subroutine handles any final actions before the framework ends

In addition, the following two modules provide important utility in terms of the capability of the UiPath REF:

 - Logger:			this subroutine defines a central logger used throughout the default framework to log 				deatils about the processing of the individual items. By default, the module outputs 				a log file to the output subfolder in the Data folder

 - ClassBRE:			this subroutine defines a custom exception class called Business Rule Exception used 				in the Proces module and passed to the SetTransactionStatus module in case the data 				requires a custom exception to be raised if for some reason any data in the data bulk 				cannot or should not be processed, but either set aside or handled differently

The logic between the subroutines - such as managing exceptions and controlling when/how each subroutine is triggered - is handled by the transaction logic of Main file.
As mentioned above, in addition to this README, the code itself is extensively internally documented such that hovering the mouse cursor over any function will show a tooltip containing info about any I/O arguments as well as a short description of the function. Finally, almost all modules as well as the Main file contain comments documenting each step of the process. 

#####################################
#Python Robotic Enterprise Framework#
#####################################
