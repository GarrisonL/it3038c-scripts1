File Organizer

The purpose of this python script is to allow a user to specify a destination on there system
in which they would want or wouldn't mind having re-organized. 
This script is a continuation/upgrade of the previous file organizer script I wrote for project 2.

In the previous script, the user had to mamually go into the script code and enter the path of the directory to be organized. 
Of the several additions, the most crucial is the ability to run the script and answer a prompt instead of changing the code .

 Additons being:

 1. Organization log
    -After running the script, any organization changes to the directory are automatically logged to a newly created txt file in the directory.

 2. Improved file extension matching
    -Similar files are grouped with eachother . Organization completely depends on the availability of files but separate folders are still created. Meaning... when the script is finished running a folder for images, documents, etc are made, but will be empty if no files of those types exist in the specified directory.

 3. File Age Organization
    - files older than whatever date the user specifies in the code (default 10 days) will be moved to an "Archive" folder.

INSTRUCTIONS:

Simply run the script and specify the path to the directory in which you would like to be organized.
-For example if you want your downloads folder to be organized "cd C:\Users\Username\Downloads"

If you have a few text documents, and images in the directory they will be organized.
