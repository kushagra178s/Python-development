a = True
i = 1 
with open('log.txt') as f:
    while a:
        a  = f.readline()

        if "python" in a.lower():
            print(a)
            print("present")
            print(i)
        i+=1