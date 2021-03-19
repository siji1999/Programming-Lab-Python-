word=input("enter the word")
end=word[-3:]
if end=='ing':
    word=word+'ly'
else:
    word=word+'ing'
print(word)
