class Solution:
    def reverseWords(self, s: str) -> str:
        list_words = s.split()
        reversed_words_list = []
        for i in list_words: 
            reversed_words_list.append(i[::-1])
        return ' '.join(reversed_words_list)