import collections
print (map.__doc__)
# Make an iterator that computes the function using arguments from
# each of the iterables.  Stops when the shortest iterable is exhausted.

print(collections.__doc__)
# This module implements specialized container datatypes providing
# alternatives to Python's general purpose built-in containers, dict,
# list, set, and tuple.

# * namedtuple   factory function for creating tuple subclasses with named fields
# * deque        list-like container with fast appends and pops on either end
# * ChainMap     dict-like class for creating a single view of multiple mappings
# * Counter      dict subclass for counting hashable objects
# * OrderedDict  dict subclass that remembers the order entries were added
# * defaultdict  dict subclass that calls a factory function to supply missing values
# * UserDict     wrapper around dictionary objects for easier dict subclassing
# * UserList     wrapper around list objects for easier list subclassing
# * UserString   wrapper around string objects for easier string subclassing


#creating doc String of the code 
def myFunction(arg , arg1=None):
    """
     Description of my code
    """
    print(arg ,arg1)


def main():
    print(myFunction.__doc__)

if __name__ == "__main__":
    main()


