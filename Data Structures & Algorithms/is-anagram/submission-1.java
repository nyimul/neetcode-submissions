class Solution {
    public boolean isAnagram(String s, String t) {
        //Instead, we can just use a hashmap to keep track of letter: occurences pairs

        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (mapS.containsKey(s.charAt(i))) {
                // increment the existing value
                int prev = mapS.get(s.charAt(i));
                prev++;
                mapS.put(s.charAt(i), prev);
                //System.out.println(mapS.get(s[i]));
            } else {
                mapS.put(s.charAt(i), 1);
            }
        }
        System.out.println(mapS);

        for (int i = 0; i < t.length(); i++) {
            if (mapT.containsKey(t.charAt(i))) {
                // increment the existing value
                int prev = mapT.get(t.charAt(i));
                prev++;
                mapT.put(t.charAt(i), prev);
            } else {
                mapT.put(t.charAt(i), 1);
            }
        }
        System.out.println(mapT);

        return (mapT.equals(mapS));

    }
}
