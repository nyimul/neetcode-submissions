public class TrieNode {
    // Two features to track:
    public bool endOfWord = false;
    //public Dictionary<TrieNode, List<TrieNode>> childrenMap = new(); // could do hashmap version
    public TrieNode[] childrenArray = new TrieNode[26]; // array version when we know size - 26 lowercase letters
    // A TrieNode never holds a character: The letter is represented by which slot a child sits in.
}

public class PrefixTree {
    // Every tree needs a root that will be branched from
    private TrieNode root;

    public PrefixTree() {
        root = new TrieNode();
    }
    
    public void Insert(string word) {
        // Simple: just insert each char throughout tree iff that line doesnt exist
        TrieNode currentNode = root;
        foreach(char ch in word) {
            int idx = ch - 'a';
            if (currentNode.childrenArray[idx] == null) {
                currentNode.childrenArray[idx] = new TrieNode();
            }
            //currentNode.childrenArray[idx] = ch; // this line is WRONG
            // i dont understand this line:
            currentNode = currentNode.childrenArray[idx]; // updates node we are on for this step
        }
        currentNode.endOfWord = true;
    }
    
    public bool Search(string word) {
        // Just go through each character and trace through the tree. True only if exact match
        TrieNode currentNode = root;
        foreach (char ch in word) {
            int idx = ch - 'a';
            if (currentNode.childrenArray[idx] == null) {
                // no match in this step, so return false
                return false;
            }
            currentNode = currentNode.childrenArray[idx];
        }
        //return true; // this isnt right either apparently
        // I didnt understand how the endOfWord boolean is used. It is used to signify legitimate words:
        return currentNode.endOfWord; // app only valid if app is added, not apple
    }
    
    public bool StartsWith(string prefix) {
        TrieNode currentNode = root;
        foreach (char ch in prefix) {
            int idx = ch - 'a';
            if (currentNode.childrenArray[idx] == null) {
                return false;
            }
            currentNode = currentNode.childrenArray[idx];
        }
        return true;
    }
}
