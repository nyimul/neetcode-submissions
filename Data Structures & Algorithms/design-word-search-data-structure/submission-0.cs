/*
1. There is the naive, brute force solution.

2. There is then a trie implementation with Depth First Search.

3. Then there is recursive implementation with Trie - I do not know if it is the same as doing depth first search.

Apparently:
Depth-First Search (DFS) - Used to traverse the Trie when encountering wildcard characters
Recursion - The DFS approach uses recursive calls to explore all possible character matches for wildcards
// Is this the same concept as the "recursive stack" method used in DFS? Cant we do either recursive stack or the data type?
*/

public class TrieNode {
    public bool endOfWord = false;
    // Array or hashmap? Doesnt matter!
    public TrieNode[] children = new TrieNode[26]; // holds 26 lowercase letters
}

public class WordDictionary {
    private TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }
    
    /*
    * We need to: add word. What if there are wild cards?
    * Wild cards only matter in search.
    */
    public void AddWord(string word) {
        TrieNode cur = root;
        foreach (char c in word) {
            int i = c - 'a';
            if (cur.children[i] == null) {
                cur.children[i] = new TrieNode();
            }
            cur = cur.children[i];
        }
        cur.endOfWord = true;
    }
    
    public bool Search(string word) {
        // Implement a depth first search algorithm via recursive stack
        // Recursive calls using searchHelper - which takes in two new params. Lets see if I can figure it out.
        return SearchHelper(word, 0, root);
    }
    // Custom helper, takes in two new params:
    // 1) an index that defines the start of the remaining substring that needs to be searched. we pass in an index instead because passing in the substring itreself would necessitate creating that substring, which would take linear time for each recursive call.
    // 2) The TrieNode we are on, so that we arent always starting from our Trie's root node.
    private bool SearchHelper(string word, int i, TrieNode cur) {
        // foreach or regular for? well we have an index being passed through, so:
        for (; i < word.Length; i++) {
            // char could be '.' so we want to be careful here. '.' - 'a' is like -51
            char c = word[i];
            int j = c - 'a';
            if (c == '.') {
                // if c == '.', then we have to traverse EVERY child from current node.
                foreach (TrieNode child in cur.children) {
                    // IF a match is found, return true.
                    if (child != null && SearchHelper(word, i + 1, child)) {
                        return true;
                    }
                }
                // I do not understand why we need a return false here.
                return false;
            } else if (cur.children[j] == null) {
                return false;
            } else {
                // match for c in children, for sure
                // regular old logic of traversing
                cur = cur.children[j];
            }
        }
        return cur.endOfWord;
    }
}
