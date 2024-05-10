def default_value():
    return 5

import collections as c

l = [1,5,7,45,3,5,1,5,9]
counter = c.Counter('abcdeababdabdou')
counter_list = c.Counter(l)
print(counter)  # Counter({'a': 4, 'b': 4, 'd': 3, 'c': 1, 'e': 1, 'o': 1, 'u': 1})
print(counter_list) # Counter({5: 3, 1: 2, 7: 1, 45: 1, 3: 1, 9: 1})

deque = c.deque([2,3,4])
print(deque)
deque.append(5)            # [2,3,4,5]
deque.appendleft(1)        # [1,2,3,4,5]
deque.pop()                # removes 5
deque.popleft()            # removes 1
deque.extend([5,6])        # [2,3,4,5,6]
deque.extendleft([1,0])    # [0,1,2,3,4,5,6]
print(deque)

d = {1:1, 2: 4, 3: 9,4: 16}
d = c.OrderedDict(d)  # Keeps order of keys inserted
print(d)              # OrderedDict([(1, 1), (2, 4), (3, 9), (4, 16)])
print(d.get(2))       # 4
d.move_to_end(2)      # OrderedDict([(1, 1), (3, 9), (4, 16), (2, 4)])
d.popitem()           # Removes last inserted: OrderedDict([(1, 1), (3, 9), (4, 16)])

d = c.defaultdict(default_value)
print(d[1])        # default value returned from default_value function.

# UserList, UserDict, UserString to make different class similar to list/dict/str.

