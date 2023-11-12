### CS50P Final Project
#### Read text file and plot list of most common words  make plot  

The program reads a text tile and reads words saving them in a dictionary, keeping track of their frequency.

There are several functions implemented.
The first two are dedicated to reading the file
# check_file
checks that the file exists and is opened correctly
# read_file
runs over the file and reads lines.
Following each line is separated into a list of words.
To save memory, only a termporary list for each line is saved at any given time.
Within a loop, each word is cleaned with
# word_cleaner()
this removes punctuation, abd sets each word to lower case.
In prder to use this with coding or markup text, such as LaTeX, additional cleaning is performed. Every line that starts with a backslash or a COMMNET_SYMBOL is skipped.
For example,this applied to LaTeX, removes every line that is a command, e.g. '\command' and every line that is intended to be a comment: %comment line.

Once we have done all this, we have a dictionary of words with their respective count,
Dictionary:
word1: 10
word2: 15
word3: 20

Next, the function 
# dict_to_data()
takes the dictionary as input and converts it into a pandas DataFrame

The function eventually sorts the data and only keeps the first RANGE elements.

Finally, we have the function
# creatEe_plot
which creates a bar plot with the shortened data.

Next to implements:
before chopping the data we can run some statistics on the entire data set.
We could also remove from the most common set of words, articles, prepositions, etc. that don't furnish actual content of the file that we have read.

## Requirements
argoarse
numpy
pandas