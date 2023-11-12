import os.path
import sys
import tabulate
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import argparse
#from icecream import ic
import pprint
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)



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
            print(tmp_list)
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
    clean_word = word.strip(" ").strip(",").strip(".").strip("?").strip("!").strip('\n').strip('\t')
    if clean_word == '' or clean_word == '-' or clean_word == '+' or clean_word == '=':
        return None
    return clean_word.lower()

def dict_to_data(dictionary):

    data = pd.DataFrame({"Word": dictionary.keys(), "Count":dictionary.values()})
    #sort and extract RANGE most common words
    #check max, min etc.
    data = data.sort_values("Count", ascending=False)
    #range = int(input(f"Select range (default {RANGE}): "))
    #if range:
    #    return data.iloc[0:range]
    #else:
    return data.iloc[50:100]

def create_plot(data=TEST_DATA):
    x = data["Word"]
    y = data["Count"]

    fig, axes = plt.subplots(figsize=(6,4),dpi=300)
    axes.barh(x,y)
    #axes.title("Most commmon 50 words")
    #plt.show()
    axes.set_xlabel("Most common words")
    axes.set_ylabel("Count")

    return fig, axes

def plot_on_screen(fig):
    root = tk.Tk()
    root.geometry("600x600")
    canvas = tk.Canvas()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    quit_button = tk.Button(text="Quit", command=root.destroy)

    quit_button.pack(side=tk.BOTTOM)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    root.mainloop()




def main():
         
    parser = argparse.ArgumentParser()
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

        fig, axes = create_plot(common_words)
        fig.savefig('plot.png')

        showplot = input("Show plot on screen (y/n)? ")
        if showplot in ['y','Y','yes','Yes","YES']:
            plot_on_screen(fig)


if __name__ == "__main__": 
    main()


