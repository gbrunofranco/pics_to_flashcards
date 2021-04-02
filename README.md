## Overview

This is a script to create markdown flashcards based on pictures for applying the active recall and spaced repetition techniques. The style of flashcards is based on Obisdian (on desktop environments) but the real goal is to make it readable by Neuracache on mobile.


## Requirements

python 3.9 is needed to run the script and git for cloning the repo


## Installation
Clone this repo with:

    git clone https://github.com/gbrunofranco/pics_to_flashcards.git

Install the required libraries (be sure that you're using pip 3.9!), you can also create a virtual environment first:

    cd pics_to_flashcards

    pip install -r requirements.txt

Change the config.py according to your needs

Simply run the script (be sure that you're using python 3.9!):
    
    python create_flashcards.py


## Folders Structure
The script expects something like this:

    college
    ├── subject1
    │   └── pictures_flashcard
    │       ├── originals
    |       |   ├── pic1.png
    |       |   ├── pic2.png
    |       |   └── ...
    │       └── compressed
    ├── subject2
    │   └── pictures_flashcard
    │       ├── originals
    |       |   ├── pic1.png
    |       |   ├── pic2.png
    |       |   └── ...
    │       └── compressed
    └── ...

The program will search in the college folder for every subject folders you have selected in the config.py file, then it will check inside the subject directories for a folder named 'pictures_flashcard' there should be two subfolders inside this one: one containing every picture you want to convert into a flashcard and another one will contain the compressed pictures created by the script (it should be empty if you didn't create any flashcards yet).

You can change the folder names (and structure!) in the config.py file

## The config.py file

* **PATH**: this is the relative path to the 'college' directory from the folder you're running the script in

* **FOLDERS**: these are the subject directories inside the **PATH** directory

* **SUBJECTS_ACRONYMS**: there are the subject acronyms for each subject, be aware that they are assigned with the same order as the **FOLDER** variable

    e.g.: if **FOLDERS** is: ['subject1/', 'subject2/', 'subject3/'] and **SUBJECTS_ACRONYMS** is: ['SUBJ1', 'SUBJ2', 'SUBJ3'], then 'subject1' will have the acronym SUBJ1, subject2 will have the acronym SUBJ2 etc...
    
    The acronyms are used in Neuracache to distinguish between different subjects, if you don't use Neuracache you still need to put a list of strings with at least as many entries as the **FOLDERS** list

* **IMG_FOLDER_PATH**: this is the name of the folder inside each direectory in **FOLDERS**, containing the original and compressed pictures that we want to create flashcards from

* **ORIGINAL_IMGS_FOLDER_NAME** and **COMPRESSED_IMGS_FOLDER_NAME**: the name of the originals and compressed folder inside the **IMG_FOLDER_PATH** folder

* **FLASHCARD_FILE_NAME_GENERATOR**: this is the basename of the markdown file containing the flashcards, this will be created inside each folder in **FOLDERS**, when its size is greater than **MAX_FLASHCARD_FILE_SIZE** a second file named **FLASHCARD_FILE_NAME_GENERATOR**02.md will be created (the same applies for **FLASHCARD_FILE_NAME_GENERATOR**02.md, **FLASHCARD_FILE_NAME_GENERATOR**03.md etc...)

* **QUALITY**: integer number between 0 and 100, this is the quality of the compression, a number between 25 and 50 should be fine

* **BASEHEIGHT**: this is the height to which each picture will be scaled down to during compression in order to avoid vertical scrolling during review in Neuracache. On my phone 330 works fine, experiment with it and see what works for you. Bigger phones should be able go higher than that whereas smaller phones may need to go down.

* **LOG_LEVEL**: this is the log level you want from my program, if you're having trouble making it work and you want to try to debug it yourself then change this to 'INFO' or 'DEBUG' (try INFO first, DEBUG outputs A LOT of stuff)

* **MAX_FLASHCARD_FILE_SIZE**: this is the maximum size in bytes that each flashcard files can have, I've had problems with Neuracache and big files so this prevents that by splitting the markdown files in multiple parts
