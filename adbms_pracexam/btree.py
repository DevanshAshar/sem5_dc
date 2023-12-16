from BTrees.IIBTree import IIBTree
import time

t = IIBTree()
insertion_start_time = time.time()
for i in range(100000):
    t.update({i: 2 * i + 10})
insertion_end_time = time.time()
print(
    f"Insertion time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds"
)
key = int(input("enter key: "))
search_start_time = time.time()
if t.has_key(key):
    print(t[key])
search_end_time = time.time()
print(
    f"Search time: {round((search_end_time-search_start_time)*1000,3)} milliseconds"
)
