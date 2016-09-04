# Lesson 6

import webbrowser
import lesson6_fresh_tomatoes

class Movie(object):

    def __init__(self, title=None, storyline=None, poster=None, trailer=None):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def __str__(self):
        return "{} [{}]".format(self.title, self.storyline)

    def show_trailer(self):
        webbrowser.open(self.trailer)

        return False

toy_story1 = Movie("Toy Story",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
    "http://ia.media-imdb.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story2 = Movie("Toy Story 2",
    "When Woody is stolen by a toy collector, Buzz and his friends vow to rescue him, but Woody finds the idea of immortality in a museum tempting.",
    "http://ia.media-imdb.com/images/M/MV5BMTQ0OTU0NTcyNl5BMl5BanBnXkFtZTcwOTk5Mjc4OA@@._V1_.jpg",
    "https://www.youtube.com/watch?v=Lu0sotERXhI")

toy_story3 = Movie("Toy Story 3",
    "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
    "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SY1000_CR0,0,707,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg")

movies = [toy_story1, toy_story2, toy_story3]

for movie in movies:
    print(movie)

lesson6_fresh_tomatoes.open_movies_page(movies)
