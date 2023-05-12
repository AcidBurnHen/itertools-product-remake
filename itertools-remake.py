
import itertools

def combine(*args, repeat=1):
    # Repeat each input iterable as needed
    pools = [tuple(iterable) * repeat for iterable in args]
    # print("pools:" ,pools)
    
    # Initialize indices for each input iterable
    indices = [0] * len(args)
    # print("indices: ", indices)
    
    # Calculate lengths of input iterables
    lengths = [len(iterable) for iterable in args]
    # print("lenghts: ", lengths)
    
    while True:
        for i in range(len(args)):
            yield tuple(pools[i][indices[i]])
        yield tuple(pools[i][indices[i]] for i in range(len(args)))
        # for i in range(len(args)):
            # print("pools[i]: ", pools[i])
            # print("indices[i]:", indices[i])
            # print("pool indices i: ", pools[i][indices[i]])
            # print("----------")
            
        # Update indices for next iteration
        for i in range(len(args) - 1, -1, -1):
            # print("i:", i)
            if indices[i] == lengths[i] * repeat - 1:
                # Roll over to next item in the iterable
                indices[i] = 0
            else:
                # Move to next item in the iterable
                indices[i] += 1
                break
        else:
            # All indices have rolled over, stop iteration
            break

        # print(indices)

list1 = [{"a", "b", "c"}, {"d", "f", "g"}, {"h", "j", "k"}]
list2 = [{1, 2, 3}, {4, 5, 6, 7, 8}]
list3 = [{"l": "m"}, {"o": 10}]

combine(list1, list2, list3) 
test = combine(list1, list2, list3) 
for item in test:
    print(item)

print("____________________________________________")
test2 = itertools.product(list1, list2, list3)
for item in test2:
    print(item)

