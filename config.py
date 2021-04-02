# Change the following variables to fit your use case but remember: THE TRAILING '/' IS NEEDED (for the PATH, FOLDERS and IMG_FOLDER_PATH variables)

PATH: str = './college/' # base folder of your university/college material
FOLDERS: list[str] = ['subject1/', 'subject2/', 'subject3/'] # folder to process in the base folder
SUBJECTS_ACRONYMS: list[str] = ['SUBJ1', 'SUBJ2', 'SUBJ3'] # acronyms for the subject to process (must be in the same order as the respective folder)
IMG_FOLDER_PATH: str = 'pictures_flashcard/' # name of the folder containing the original and compressed pictures in each subject directory
ORIGINAL_IMGS_FOLDER_NAME: str = 'originals' # name of the original, uncompressed pictures in the picture folder of each subject directory
COMPRESSED_IMGS_FOLDER_NAME: str = 'compressed' # name of the compressed pictures in the picture folder of each subject directory
FLASHCARD_FILE_NAME_GENERATOR: str = 'flascard.md' # base name of the flashcard file (if too big the script will create name01.md, name02.md, ...)
QUALITY: int = 35  # 100 = original quality (gets processed anyway), 1 = max compression
BASEHEIGHT: int = 330 # will get scaled down to this height (keeps the original ratio)
LOG_LEVEL: str = 'CRITICAL'  # change to INFO or DEBUG if you want more output for debugging purposes
MAX_FLASHCARD_FILE_SIZE: int = 2097152 # max bytes for the flashcard file, certain cards apps have problems certains sizes. Default: 2097152 (2MB)