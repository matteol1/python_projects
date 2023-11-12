import argparse
import tabulate
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from constants import *

#Read file, check existence etc.
def check_file(filename=TEST_FILE):
    f = open(filename, "r")
    return f

def read_file(file=open(TEST_FILE, "r")):
    dictionary = dict()
    lines = file.readlines()
    for i,line in enumerate(lines):
        if line.startswith(COMMENT_SYMBOL):
            continue
        tmp_list = line.split(" ")
        if i%50==0:
            print(f"Reading line {i}")
        for word in tmp_list:
            clean_word = word_cleaner(word)
            if clean_word:
                if clean_word in dictionary:
                    dictionary[clean_word] +=1
                else:
                    dictionary[clean_word] = 1
    return dictionary

def word_cleaner(word):
    if word.startswith("\\"):
        return None
    clean_word = word
    for char in PUNCTUATION:
        clean_word = clean_word.strip(char)
    if clean_word == '' or clean_word == '-' or clean_word == '+' or clean_word == '=':
        return None
    return clean_word.lower()

def dict_to_data(dictionary):
    data = pd.DataFrame({"Word": dictionary.keys(), "Count":dictionary.values()})
    #sort and extract RANGE most common words
    data = data.sort_values("Count", ascending=False)
    return data.iloc[0:RANGE]

def print_table(common_words):
    table = zip(common_words["Word"], common_words["Count"])
    print(tabulate.tabulate(table, tablefmt="grid"))

def create_plot(data):
    x = data["Word"]
    y = data["Count"]

    fig, axes = plt.subplots(figsize=(6,4),dpi=300)
    axes.barh(x,y)
    #axes.title("Most commmon 50 words")
    #plt.show()
    axes.set_title(f"Count of the most common {RANGE} words")
    axes.set_xlabel("Most common words")
    axes.set_ylabel("Count")

    return fig, axes

def main():
         
    parser = argparse.ArgumentParser(description=PROGRAM_DESCRIPTION)
    parser.add_argument('file', type=str, help="File name (text file)")
    #optional args
    parser.add_argument('--verbose', action="store_true", help="Verbose mode")
    parse_args = parser.parse_args()
    #print(parse_args.verbose)

    filename = parse_args.file

    f = check_file(filename)
    if f:
        print(f"File {filename} opened successfully. Reading...")
        words = read_file(f)
        print("File imported correctly")
        common_words = dict_to_data(words)
        print("Dictionary created successfully")

        view_on_screen = input("Show results (y/n)? ")
        if view_on_screen in ['y','Y','yes','Yes","YES']:
                print_table(common_words)
        fig, axes = create_plot(common_words)
        saveplot = input("Save plot to file (y/n)? ")
        if saveplot in ['y','Y','yes','Yes","YES']:
            fig.savefig(IMAGE_FILE)
            print(f"File {IMAGE_FILE} saved successfully")
    f.close()

if __name__ == "__main__": 
    main()


