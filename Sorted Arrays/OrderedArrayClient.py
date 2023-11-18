from OrderedArray import * 
max=2000
Ordarr=OrderedArray(max)

Ordarr.insert(34)
Ordarr.insert(34)
Ordarr.insert(5454)
Ordarr.insert(34234)
Ordarr.insert(342)
Ordarr.traverse()


print("lenght",len(Ordarr))
print(Ordarr)
print("find(23)", Ordarr.find(23))
print("find(34)", Ordarr.find(5454))
print("this is delet", Ordarr.delete(34))



