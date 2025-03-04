from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not strings:
            raise TypeError(
                f"Illegal argument for findLongestCommonWord: strings = {strings} must be a non-empty list"
            )

        for index, string in enumerate(strings):
            if not isinstance(string, str):
                raise TypeError(
                    f"Illegal argument for findLongestCommonWord: string = {string} must be string format"
                )
            trie.put(string, index)

        current = self.root
        min_word = min(strings, key=len)
        longest_prefix = []

        for char in min_word:
            if char in current.children and len(current.children) == 1:
                longest_prefix.append(char)
                current = current.children[char]

        return "".join(longest_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
