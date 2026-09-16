# Explanation

The problem asks us to reverse only the vowels in a string while leaving the consonants untouched. We can achieve this by first iterating through the string and collecting all characters that are vowels ('a', 'e', 'i', 'o', 'u'). We then reverse this collection of vowels. Finally, we build the resulting string by iterating through the original string again, replacing each vowel encountered with the next vowel from our reversed list, and keeping consonants as they are.

## Time Complexity

O(N) where N is the length of the string, as we traverse the string a constant number of times.

## Space Complexity

O(N) to store the extracted vowels and the resulting string characters.
