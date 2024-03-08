alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
word = input()
sentence = ""

for i in alphabet:
    try:
        sentence += str(word.index(i)) + " "
    except:
        sentence += "-1 "
        
print(sentence)