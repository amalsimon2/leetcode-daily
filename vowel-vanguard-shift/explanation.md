# Explanation

The algorithm first iterates through the character array to collect the indices and characters of all vowels. If no vowels are found, it returns the original array. Otherwise, it performs a right cyclic shift on the collected vowel characters (moving the last vowel to the front). Finally, it places the shifted vowels back into their original indices in a new list and returns it.

## Time Complexity

O(N) where N is the length of the character array

## Space Complexity

O(N) to store the vowel tracking lists and the result array
