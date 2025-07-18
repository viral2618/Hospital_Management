words=input("enter a word:")
char_count=dict()
for char in words:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
for char,count in char_count.items():
    print(char+":",count)