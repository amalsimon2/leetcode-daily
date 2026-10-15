# Explanation

First, we iterate through the string to collect all vowels. We then reverse this list of vowels. Next, we iterate through the string a second time, and whenever we encounter a vowel position, we replace it with the next vowel from our reversed list.

## Time Complexity

O(N) where N is the length of the string

## Space Complexity

O(N) to store the character list and extracted vowels
