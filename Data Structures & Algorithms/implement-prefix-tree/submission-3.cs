public class TrieNode {
    public bool endOfWord = false;
    public Dictionary<char, TrieNode> children = new();
}

public class PrefixTree {
    private TrieNode root;
    public PrefixTree() {
        root = new TrieNode();
    }
    
    public void Insert(string word) {
        TrieNode cur = root;
        foreach (char c in word) {
            if (!cur.children.TryGetValue(c, out var next)) {
                // Create new instance
                next = new TrieNode();
                cur.children[c] = next;
            }
            cur = next;
        }
        // End of word
        cur.endOfWord = true;
    }
    
    public bool Search(string word) {
        TrieNode cur = root;
        foreach (char c in word) {
            if (!cur.children.TryGetValue(c, out var next)) {
                // Then this isnt a word
                return false;
            }
            cur = next;
        }
        return cur.endOfWord;
    }
    
    public bool StartsWith(string prefix) {
        TrieNode cur = root;
        foreach (char c in prefix) {
            if (!cur.children.TryGetValue(c, out var next)) {
                return false;
            }
            cur = next;
        }
        return true;
    }
}
