# Lesson 5

import urllib

def read_text():
    quotes = open("./ud036/lesson5/movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()

def check_curse_word(line):
    # http://www.wdylike.appspot.com/?q=
    page = urllib.urlopen("http://www.wdylike.appspot.com/?q={}".format(line))
    result = page.read()
    page.close()
    return result

read_text()
print("Line: {} | Answer: {}".format("shot", check_curse_word("shot")))
print("Line: {} | Answer: {}".format("shit", check_curse_word("shit")))
