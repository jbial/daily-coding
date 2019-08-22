"""
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple
lines such that each line has a length of k or less. You must break
it up so that words don't break across lines. Each line has to have
the maximum possible amount of words. If there's no way to break the
text up, then return null.

You can assume that there are no spaces at the ends of the string and
that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog"
and k = 10, you should return: ["the quick", "brown fox", "jumps over",
"the lazy", "dog"]. No string in the list has a length of more than 10.

Solution:
Use a greedy algorithm to determine how many words/line based on word len
"""


def wordLength(wordlist):
    """Helper function to compute sum of lengths of words
    """
    return sum(len(word) for word in wordlist)


def makeWordList(sentence):
    """Helper to make test case from sentence
    """
    return sentence.split(" ")


def format_text(words, k):
    """Formats the words in the sentence into a sentence array
    """
    wordList, sentence = [], []
    for i, word in enumerate(words):
        if len(wordList) == 0:
            wordList.append(word)
            continue

        # greedily fill the word list until maximum width is reached
        spacesBtwn = len(wordList) - 1
        if wordLength(wordList) + spacesBtwn + len(word) >= k:
            sentence.append(wordList)
            wordList = []

        # add next word to the wordlist
        wordList.append(word)

        # handle the last line
        if i == len(words) - 1:
            sentence.append(wordList)
            wordList = []
    return sentence
    

def format_spaces(sentenceList, k):
    """Formats the spaces needed between words in a sentence list
    """

    def calculate_spaces(spaces, bins):
        """Returns list of spaces evenly distributed
        """
        space_dist = [spaces // bins for _ in range(bins)]
        for i in range(spaces % bins):
            space_dist[i] += 1
        return space_dist

    spacesList = []
    for sentence in sentenceList:
        # available spaces to fill
        spacesFree = k - wordLength(sentence)
        if len(sentence) == 1:
            spacesList.append([spacesFree])
        else:
            spacesList.append(calculate_spaces(spacesFree, len(sentence) - 1))
    return spacesList


def justify(words, k):
    """Fully justifies a given list of words from a sentence
    """
    sentences = format_text(words, k)
    spaces = format_spaces(sentences, k)
    
    # stitch together the sentences and spaces
    return [''.join([i + j * " " for i, j in zip(s, space)]) + s[-1] 
            for s, space in zip(sentences, spaces)]


def main():
    
    tests = (
        (makeWordList("the quick brown fox jumps over the lazy dog"), 16),
        (makeWordList("this is a stupid and hard daily coding problem"), 10),
        (makeWordList("this problem was asked by the Palantir data gods"), 20)
    )

    for i in justify(*tests[2]):
        print(i)

if __name__ == '__main__':
    main()
