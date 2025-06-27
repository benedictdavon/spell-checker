class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordTrie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word:str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def load_words(self, filepath:str):
        with open(filepath, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    self.insert(word)   