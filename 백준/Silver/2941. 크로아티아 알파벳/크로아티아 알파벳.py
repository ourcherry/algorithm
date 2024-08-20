arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0
userinput = input()
word = userinput

for spell in arr:
    exception = 0
    if(spell == "z="):
        exception = userinput.count("dz=")
    cnt += userinput.count(spell) - exception
    word = word.replace(spell, "/")
    
cnt += len(word.replace("/", ""))
print(cnt)
