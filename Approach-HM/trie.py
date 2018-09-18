class Trie:

    # Write Trie Class Here if you choose to implement the Trie
    # Parents
    def __init__(self, value=""):
        self.value = value
        self.children = []  # list of Trie [Trie("c"), Trie("d"), ...]

    def get_children(self):
        return self.children

    def insert(self, str):
        if len(str) == 0:
            return
        for child_trie in self.children:
            # iterate through
            if child_trie.get_value() == str[0]:
                child_trie.insert(str[1:])
                return
        # new Trie
        newTrie = Trie(str[0])
        newTrie.insert(str[1:])
        self.children.append(newTrie)

    def get_value(self):
        return self.value

    def print_trie(self):
        if len(self.children) == 0:
            print(self.get_value(), end="")
            print()
        for child in self.children:
            print(self.get_value(), end="")
            child.print_trie()

    def list_trie(self, user_input, lst, acmstr):
        if len(self.children) == 0:
            lst.append(acmstr + self.get_value())
            return
        if user_input == "":
            for child in self.children:
                child.list_trie(user_input, lst, acmstr + self.get_value())
            return
        for child in self.children:
            if user_input[0] == child.get_value():
                child.list_trie(user_input[1:], lst, acmstr + self.get_value())

    def user_food_type(self, user_input):
        retlst = []
        self.list_trie(user_input, retlst, "")
        return retlst

