# PDF-Merge-and-Split-software
Using python makes PDF Merge and Split software with GUI


*How to use:*
Add -- adding PDF file to the program for merge to one file or split files to multiple single page PDF file. 
Clean -- To remove all added file in the program.

Merge -- Starting merge added files and display output file location.
Save as -- Defining the merge file as location and file name. Without define output file location, the program will using default output location which is the same as exe file. 

Split -- Starting to split all file in the list to single page PDF files and display the file path and name. 
Save path -- Defining the output file paht for split function. Without defining, the program will use default path.

Quit -- End the program.


[PDF_merge.py is the source file for the exe programe.] 



Using pyinstaller to generate exe file for Windows OS.

```
pip install pyinstaller
pyinstaller --onefile -w --icon=a.ico PDF_merge.py
```

