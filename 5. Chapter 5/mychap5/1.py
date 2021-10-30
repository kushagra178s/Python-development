mydict = {
    "fast" : "quick",
    "ksx"  : "coder",
    "marks": [1,2,5],
    "anotherdict" : {'ksx' : 'player'}
}
#print(mydict.values())
#print(list(mydict.keys()))
updatedict = {
    "yoyo" : "friend"
} 
mydict.update(updatedict)
print(mydict)