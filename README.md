# Xandobe [PRE-ALPHA]
This is an application that will allow you to patch any Adobe creative suite product up to 2018. This tool does not physically crack the applications, moreso just patches the licensing to avoid any issues.
# What will it do?
## **1. Windows Host Files**
  - This tool will give you the ability to add custom entries to your Windows hosts file. Entries can be single, or multiple        through importing your own .txt file containing the entries. 

## **2. Services**
  - It will disable the respective services to do with Adobe (including creative cloud, with or without) and prevent them from starting up again.

## **3. Firewall**
  - The tool will create rules for inbound/outbound connections to do with only the installed Adobe Applications as a fallback just incase for any reason your services enable again

## **4. Complete patch**
  - It has the option to completely patch everything for you rather than isolating certain functions and using only the hosts editor

## Requirements
  - python-hosts
  - pywin32
  - setuptools
  - win-inet-pton
  __________________
# Development Usage 
## **Functions**

1. hosts_file.py
	**Class: Entries**
	- *prompt_entry*()
    This function launches the menu for deciding on custom host entry (singular at the moment) or import a .txt file.
    
  - *add_custom_entry*()
		This will allow the user to enter a single entry with the format `127.0.0.1 hostname` 
    
	- *import_file_entry*()
		Controls the import process of windows hosts file. 
		**Args**
		- file_path > full path to hosts file including file itself: **C:\Windows\System32\drivers\etc**
    
	- *get_hosts*()
		Function will determine the path of the system host file via python_hosts module determine_hosts_path() function
    
	- *remove_duplicate_entries*()
		Function will remove all duplcate entries with a given (readable) file.
		**Args**
		- input_file
			The file that you want to remove duplicate string entries from
		- output_file
			The file you want the function to output after removing duplicates (it's this way for safety over files)
	
