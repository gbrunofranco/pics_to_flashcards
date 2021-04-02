# Creator: Gabriele Bruno Franco
# Source code: https://github.com/gbrunofranco/
# Version 1.0


from os import listdir, path
from config import *
import logging
import base64
from PIL import Image


def generate_flashcard_file_name(folder: str) -> str:
    logging.debug('In generate_flashcard_file_name(), generating flashcards file name now...')

    flashcard_file_name: str = FLASHCARD_FILE_NAME_GENERATOR
    logging.debug('Checking if flashcard file already exist...')

    if path.isfile(PATH+folder+flashcard_file_name):

        logging.info('Flashcard file already exists, starting while loop...')
        count: int = 1

        try:
            logging.info(f'Checking if: {PATH+folder+flashcard_file_name} is bigger than 2 MBs...')

            logging.info(f'Found size: {path.getsize(PATH+folder+flashcard_file_name)}')

            while (path.getsize(PATH+folder+flashcard_file_name) > MAX_FLASHCARD_FILE_SIZE):
                count += 1
                flashcard_file_name = FLASHCARD_FILE_NAME_GENERATOR[:-3] + str(count) + FLASHCARD_FILE_NAME_GENERATOR[-3:]
            logging.info(f'Final flashcard name: {flashcard_file_name}')

        except OSError:
            print(f'\n{colored(255, 0, 0, "Error")} reading: {PATH+folder+flashcard_file_name}\nSkipping...\n')

    return flashcard_file_name


def process_pictures(original_files: list[str], compressed_files: list[str], folder: str, subject, flashcard_file_name: str):

    logging.debug(f'Opening flashcard file at: {PATH+folder+flashcard_file_name}...')
    logging.debug(f'Starting the picture processing loop...')

    for picture_name in original_files:
        if f'compressed_{picture_name}' in compressed_files:
            logging.debug(f'{picture_name} already compressed, skipping...')
            continue

        with open(PATH+folder+flashcard_file_name, 'a') as fc_file:
            logging.debug(f'{picture_name} not compressed, processing...')
            with open(PATH+folder+IMG_FOLDER_PATH+'originals/'+picture_name, 'rb') as img_file:
                pic: Image.Image = Image.open(img_file)
                hpercent: float = (BASEHEIGHT / float(pic.size[1]))
                wsize: int = int((float(pic.size[0]) * hpercent))
                pic = pic.resize((wsize, BASEHEIGHT), Image.ANTIALIAS)
                pic.save(PATH+folder+IMG_FOLDER_PATH+'compressed/'+"compressed_"+picture_name, optimize=True, quality=QUALITY)

            logging.debug(f'{picture_name} compressed and saved at {PATH+folder+IMG_FOLDER_PATH+"compressed/"+"compressed_"+picture_name}...')

            logging.debug(f'Creating card for {picture_name}...')

            with open(PATH+folder+IMG_FOLDER_PATH+'compressed/'+"compressed_"+picture_name, 'rb') as img_file:
                question: str = picture_name[:-4]  # assumes png or jpg
                print(f'{question} #flashcard #{subject}\n', file=fc_file)
                encoded_img = base64.b64encode(img_file.read())
                print('![](data:image/png;base64,'+encoded_img.decode('utf-8')+')', file=fc_file)
                print('\n---', file=fc_file)

            logging.debug(f'{picture_name} card created and saved in {PATH+folder+IMG_FOLDER_PATH+"compressed/"+"compressed_"+picture_name}...')

            flashcard_file_name = generate_flashcard_file_name(folder)

    print(f'{colored(0, 128, 0, subject)} correctly processed...')


def read_prepare_pictures(folder: str, flashcard_file_name: str, subject: str):

    logging.info(f'Opening {PATH+folder+flashcard_file_name}...')

    try:
        logging.info(f'Reading the original pictures at {PATH+folder+IMG_FOLDER_PATH+ORIGINAL_IMGS_FOLDER_NAME}...')
        original_files: list[str] = listdir(PATH+folder+IMG_FOLDER_PATH+ORIGINAL_IMGS_FOLDER_NAME)

    except FileNotFoundError:
        print(f'\nError reading: {PATH+folder+IMG_FOLDER_PATH+ORIGINAL_IMGS_FOLDER_NAME}')
        print(f"{colored(255, 0, 0, subject)} skipped...", end='\n\n')
        return

    try:
        logging.info(f'Reading the already compressed pictures at {PATH+folder+IMG_FOLDER_PATH+COMPRESSED_IMGS_FOLDER_NAME}...')
        compressed_files: list[str] = listdir(PATH+folder+IMG_FOLDER_PATH+COMPRESSED_IMGS_FOLDER_NAME)
        logging.info(f'{len(compressed_files)} compressed pictures found...')

    except FileNotFoundError:
        print(f'\n{colored(255, 0, 0, "Error")} reading: {PATH+folder+IMG_FOLDER_PATH+COMPRESSED_IMGS_FOLDER_NAME}')
        print(f"{colored(255, 0, 0, subject)} skipped...", end='\n\n')

    process_pictures(original_files, compressed_files, folder, subject, flashcard_file_name)


# from L D at https://stackoverflow.com/a/61960902
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def main():

    logging.basicConfig(encoding='utf-8', level=LOG_LEVEL, format='%(levelname)s: %(message)s')

    for idx, folder in enumerate(FOLDERS):
        logging.info(f'In main() function, calling generate_flashcard_file_name() at {folder} now...')
        print(f'\nStarting creation of flashcards at: {PATH+folder}')
        read_prepare_pictures(folder, generate_flashcard_file_name(folder), SUBJECTS_ACRONYMS[idx])


if __name__ == '__main__':
    main()
