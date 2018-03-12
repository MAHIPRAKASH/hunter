name="Prakash"
def reverse_words(sentence):        
     return " ".join((lambda x : [i[::-1] for i in x])(name.split(" ")))
print(reverse_words(name))
