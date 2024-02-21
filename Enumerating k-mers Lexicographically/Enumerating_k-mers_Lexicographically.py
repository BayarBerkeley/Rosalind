letter = input("Enter your symbols:")
numb = input("Enter your k-mer:")

try:
    numb = int(numb)
    print(f" your symbols are {letter} and k-mer {numb}")
except:
    print("Please enter a valid integer")


ls_letter = letter.split(" ")

def enum_k_mer(ls_letter,numb, text, file):
    if len(text) == numb:
        file.write(text + '\n')
        return None
    
    for i in ls_letter:
        enum_k_mer(ls_letter, numb, text + i, file)
with open('result.txt', 'w') as file:
    enum_k_mer(ls_letter, numb, "", file)