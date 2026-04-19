# ============================================
# @File    : day48_208.py
# @Date    : 2026-04-19 10:42
# @Author  : 帅宇昕
# ============================================
class Trie:

    def __init__(self):
        self.children= {}

        self.isEnd=False

    def insert(self, word: str) -> None:
        node=self
        for i in word:
            if i not in node.children:
                node.children[i]=Trie()
            node=node.children[i]
        node.isEnd=True



    def search(self, word: str) -> bool:
        node = self
        for i in word:
            if i not in node.children:
                return False
            else:
                node=node.children[i]

        return node.isEnd



    def startsWith(self, prefix: str) -> bool:
        node = self
        for i in prefix:
            if i not in node.children:
                return False
            else:
                node = node.children[i]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie =Trie()
trie.insert("apple")
print(trie.search("apple"))  # 返回 True
print(trie.search("app"))     # 返回 False
print(trie.startsWith("app")) # 返回 True
trie.insert("app")
print(trie.search("app"))     # 返回 True