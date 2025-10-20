class MySet:
    def __init__(self, elements=None):
        # Initialize an empty dictionary
        self.dictionary = {}
        
        # If a list of elements is given, add each to the dictionary
        if elements:
            for element in elements:
                self.dictionary[element] = True

    def add(self, element):
        # Add element as a key in dictionary
        self.dictionary[element] = True

    def delete(self, element):
        # Safely remove element if it exists
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        # Check if element exists in dictionary
        return element in self.dictionary

    def size(self):
        # Return number of elements
        return len(self.dictionary)

    def __repr__(self):
        return f"MySet({list(self.dictionary.keys())})"
