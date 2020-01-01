# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 11:02:35 2018

@author: Jamiu
"""
# In[]

filename = 'AbrahamLincoln.txt'

def read_text(filename):
    """ This function reads a text and returns a string 
    	This function is adapted from the HarvardX course - using python for research
    """
    with open(filename, "r", encoding = "utf-8") as txt_file:
        text = txt_file.read()
        text = text.replace("\n"," ").replace("\r","")
    return(text)
        
text = read_text(filename)

# In[]

def count_words(text):
    """A function to count the number of times each word occurs in a text. All punctuation marks are skipped.
    The function returns a dictionary object whose keys are the unique words and values are word counts
    This function is adapted from the HarvardX course - using python for research
    """
    text = text.lower()
    skips = [".", ",", ";",":","?","'",'"', '-', '_', '&', '*', '(', ')']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return(word_counts)

# In[]

words = list((count_words(text)).keys())
num_letters = list(range(1, (max([len(words[ind]) for ind in range(len(words))]))+1))

def ch_counter(words):
    """This function calculates the number of characters 
    in each word contained in an input textfile"""   
    Num_Char =[]    
    for num in num_letters:
        num_ch = 0
        for word in words:
            if len(word) == num:
                num_ch +=1
        Num_Char.append(num_ch)
    return(Num_Char)

num_char = ch_counter(words)

cum_num_char = 0
Cum_Num_Char = []
for j in range(len(num_char)):
    cum_num_char +=num_char[j]/sum(num_char)
    Cum_Num_Char.append(cum_num_char)

# In[]

def viz():            
    import matplotlib.pyplot as plt
    plt.ion()
              
    #plt.bar(num_letters, num_char)
    #plt.plot(num_letters, Cum_Num_Char, 'r-', lw = 2)
    
    """You will notice that the cumulative curve is too low and 
    will be better as a secondary axis. To do that, we can redefine 
    the plot as follows"""
    
    #plt.close('all')
    
    fig = plt.figure(figsize=(8,7))
    ax1 = fig.add_subplot(111)
    ax1.bar(num_letters, num_char, label = "Num_Char")
    ax1.set_xlabel('Number of Characters', fontsize=14)
    ax1.set_ylabel('Number of Words', fontsize=14)
    plt.axis([0, max(num_letters)+1, 0, max(num_char)+2])
    ax1.set_title("Distribution of the Words by Number of Characters", fontsize=15)
    ax1.legend(loc = 'center left', fontsize=14)
    ax1.tick_params(axis='both', which='major', labelsize=13)
    ax2 = ax1.twinx()
    
    ax2.plot(num_letters, Cum_Num_Char, 'r-', lw = 2, label = "Cum_Num_Char")
    ax2.set_ylabel('Normalized Cum Number of Words', fontsize=14)
    ax2.axis([0, max(num_letters)+1, 0, 1.005])
    ax2.tick_params(axis='both', which='major', labelsize=13)
    ax2.legend(loc = 'center right', fontsize=14)
    return(fig)
	
viz()
