n=int(input("enter  number of words to be stored:"))
longest=0
for i in range(n):
    word=input("enter a word:")
    length=len(word)
    if length>longest:
        longest=length
print("length of longest word:",longest)
