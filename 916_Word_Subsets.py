from typing import List


class Solution:
    def create_alphabet(self, word):
        alph = {}
        for letter in word:
            if letter not in alph:
                alph[letter] = 0
            alph[letter] += 1
        return alph

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        output = []
        word2 = {}

        for group in words2:
            for letter, count in self.create_alphabet(group).items():
                if letter not in word2:
                    word2[letter] = 0
                word2[letter] = max(word2[letter], count)

        count_unique = len(word2)

        for i, word in enumerate(words1):
            word = self.create_alphabet(word)
            count_same = 0

            for letter, count in word2.items():
                if (
                    letter in word and
                    count <= word[letter]
                ):
                    count_same += 1

            if count_same == count_unique:
                output.append(words1[i])
        
        return output
