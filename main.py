import os
import sys

import pandas as pd
from pypdf import PdfReader


def visitor_text(
    text, currentTransformationMatrix, textMatrix, fontDictionary, fontSize
):
    if len(text) <= 0:
        return
    print(f"text: {text} | {currentTransformationMatrix} | {textMatrix}")


def main():
    # Get the path to the PDF file from the command line argument
    if len(sys.argv) < 2:
        print("Please provide pdf file or files as program arguments.")
        return
    for i in range(len(sys.argv)):
        if i == 0:
            continue

        pdfPath = sys.argv[i]

        if not os.path.isfile(pdfPath):
            print(f"There is no file at path:", pdfPath)
            continue

        pdfReader = PdfReader(pdfPath)
        pdfReader.pages[0].extract_text(visitor_text=visitor_text)


if __name__ == "__main__":
    main()
