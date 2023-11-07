# https://github.com/MoldovanBrendon915/lftc2023-2024
# SortedST - Symbol Table (ST) Implementation

# Introduction:
# The SortedST class is an implementation of a symbol table (ST) data structure. A symbol table is a collection of key-value pairs
# with the primary operations of insertion, search, and deletion. In this implementation, the keys are stored in alphabetical order.


# Class Definition:
class SortedST:
    def __init__(self):
        """
        Initializes an empty symbol table.
        """
        self.table = []

    def insert(self, key, value):
        """
        Inserts a key-value pair into the symbol table while maintaining alphabetical order of the keys.

        Parameters:
        key (str): key
        value (any): value associated with the key.
        """
        self.table.append((key, value))
        self.table.sort(key=lambda item: item[0])

    def searchKey(self, key):
        """
        Searches for a key in the symbol table and returns the corresponding value if found.

        Parameters:
        key (str): key to search

        Returns:
        any: value associated with the key, or 'None'
        """
        for k, v in self.table:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Deletes a key and its associated value from the symbol table if the key exists.

        Parameters:
        key (str): The key to be deleted.
        """
        for i, (k, v) in enumerate(self.table):
            if k == key:
                del self.table[i]
                return

    def size(self):
        """
        Returns the number of key-value pairs in the symbol table.

        Returns:
        int: The number of key-value pairs in the symbol table.
        """
        return len(self.table)

    def keys(self):
        """
        Returns a list of all keys in the symbol table, sorted in alphabetical order.

        Returns:
        list of str: A list of all keys in alphabetical order.
        """
        return [k for k, _ in self.table]





if __name__ == '__main__':


    #example
    st = SortedST()

    #inserting elements
    st.insert('id1', 5)
    st.insert('id3', 3)
    st.insert('id2', 18)

    print(st.keys())

    #search key
    print(st.searchKey('id2'))
    print(st.searchKey('asdasd123'))

    # Deleting a key
    st.delete('id2')

    #list of keys
    print(st.keys())

    #length
    print(st.size())

