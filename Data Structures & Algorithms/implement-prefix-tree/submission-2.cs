//Hashmap implementation
public class TrieNode {
    public bool endOfWord = false;
    public Dictionary<char, TrieNode> children = new(); // NOT A LIST of TrieNodes
}

public class PrefixTree {
    // Every tree has a root
    private TrieNode root;

    public PrefixTree() {
        root = new TrieNode();
    }
    
    public void Insert(string word) {
        TrieNode cur = root;
        foreach (char c in word) {
            // use map instead of idx for array
            if (!cur.children.TryGetValue(c, out var next)) {
                // No match, create a new node (NOT LIST):
                next = new TrieNode();
                cur.children[c] = next;
            }
            // either way we progress
            //cur.children[c].Add() // dont need to store char!!!
            cur = next; // Do I need to try get value here?
        }
        cur.endOfWord = true;
    }
    
    public bool Search(string word) {
        // Simple. Just go char by char
        TrieNode cur = root;
        foreach (char c in word) {
            if (!cur.children.TryGetValue(c, out var next)) {
                // No match
                return false;
            }
            cur = next;
        }
        return cur.endOfWord;
    }
    
    public bool StartsWith(string prefix) {
        // Simple. Just go char by char
        TrieNode cur = root;
        foreach (char c in prefix) {
            if (!cur.children.TryGetValue(c, out var next)) {
                // No match
                return false;
            }
            cur = next;
        }
        return true;
    }
}
