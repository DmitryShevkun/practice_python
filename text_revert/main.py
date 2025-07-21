"""
program name:
description:
author:
created:
"""

import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():

    logging.info("program started")

    text_process('example.txt', 'output.txt')

    logging.info("program complete")


def text_process(input_file, output_file=None):

    logging.info("text_process started")

    if output_file is None: 
        output_file = input_file

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.rstrip('\n')[::-1] + '\n'

    with open(output_file, 'w') as file:
        file.writelines(lines)

    logging.info("text_process complete")


if __name__ == "__main__":
    main()