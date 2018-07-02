
import re


def clean_sent(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)#sub is used to replace
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)#\ it is escape seq we are removing '
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"let's", "let us", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:&<>{}+=~*|%.?$,\'!\[\]]", "", text)#here removing spec sym 	
    text=re.sub('^[0-9]+', '', text) 
    temp=[]
    for i in text.split():
        if len(i)>12:
            continue
        else:
            i=re.sub("[^a-zA-Z]","", i)
            temp.append(i)
    text=' '.join(temp)    
    return text
