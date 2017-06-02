# a HashTable has:
# - values: the list of values
# - size: the size of the table
class HashTable:
    def __init__(self, vals = None):
        self.values = [None]*8
        #if vals is not None: TODO: finish this
        self.size = 0
    def __eq__(self, other):
        return type(other) == HashTable and self.values == other.values
    def __repr__(self):
        st = ""
        for i in range(self.size-1):
            st += "{}, ".format(self.values[i])
        st += "{}, ".format(self.values[self.size-1])
        return st


# returns an empty has table of size 8
#   -> HashTable
def empty_hash_table():
    return HashTable()