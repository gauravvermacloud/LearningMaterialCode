from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_word = []
    for line in story:
        line_word = line.split()
        for word in line_word:
            story_word.append(word)

print(story_word)