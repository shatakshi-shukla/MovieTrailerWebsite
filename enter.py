#!/usr/bin/python

# - * -coding: utf - 8 - * -

import given
import media

# Movies/TvShow to be displayed

TOY_STORY = media.Movie('TOY STORY', 'A STORY OF A BOY AND HIS TOYS',
                        'http://tny.im/cHZ',
                        'https://www.youtube.com/watch?v=rNk1Wi8SvNc')

COCKTAIL = media.Movie('COCKTAIL', 'Friend circle movie',
                       'http://tny.im/cID',
                       'https://www.youtube.com/watch?v=3nA1hmKCRpE')

PLL = media.TvShow('PLL', 'SET MAX',
                   'http://tny.im/cIE',
                   'https://www.youtube.com/watch?v=xZJwm3pfwPg')

HELLO_KITTY = media.Movie('HELLO KITTY', 'about kitty',
                          'http://tny.im/cIF',
                          'https://www.youtube.com/watch?v=LiaYDPRedWQ')

THIS_IS_US = media.TvShow('THIS IS US', 'comedy central',
                          'http://tny.im/cII',
                          'https://www.youtube.com/watch?v=QJI8o54tn8g')

MODERN_FAMILY = media.TvShow('MODERN FAMILY', 'SONY',
                             'http://tny.im/cIH',
                             'http://tny.im/cIH')

Friends = media.TvShow('Friends', 'comedy central',
                       'http://tny.im/cHV',
                       'https://www.youtube.com/watch?v=FxAG_11PzCk')

# Movies/TvShows to be displayed are passed through a list

movies = [
    TOY_STORY,
    COCKTAIL,
    PLL,
    HELLO_KITTY,
    THIS_IS_US,
    MODERN_FAMILY,
    Friends
]
given.open_movies_page(movies)
