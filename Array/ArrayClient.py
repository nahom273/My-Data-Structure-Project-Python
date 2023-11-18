from Array import *

obj_arr = Array(4)
obj_arr.insert(99)
obj_arr.insert("foo")
obj_arr.insert("bar")

print("Array containig", len(obj_arr),"items")
obj_arr.traverse()

print("search",obj_arr.search(99))



obj_arr.delete("foo")
obj_arr.set(1,"hhhjsf")
obj_arr.traverse()