#!/usr/bin/env python3

def return_evens(num_list):
    evens=[num for num in num_list if num%2==0]
    print(evens)
    return evens
return_evens([0,1,3,5,7,8,9])

def make_exclamation(sentence_list):
    sentence=[sentence +"!" for sentence in sentence_list]
    print (sentence)
    return sentence
make_exclamation(["Hello", "I'm doing great", "Python is fun"])