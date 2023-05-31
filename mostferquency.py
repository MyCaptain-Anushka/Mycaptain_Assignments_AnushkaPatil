# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:45:32 2023

@author: anush
"""
#most frequent code

def most_frequent(string):
    # Create an empty dictionary to store the frequency of letters
    frequency = {}

    # Convert the string to lowercase
    string = string.lower()

    # Count the frequency of each letter in the string
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    # Sort the dictionary by values in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the letters and their frequencies
    for letter, count in sorted_frequency:
        print(f"{letter} = {count:02}")

# Example usage
most_frequent("Mississippi")
