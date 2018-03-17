#!/usr/bin/python

# - * -coding: utf - 8 - * -
import webbrowser


class Video:

    # Parent class for common attributes

    def __init__(self, title):
        self.title = title


class Movie(Video):

    # Class called when a movie is given as input

    def __init__(
        self,
        title,
        moviestoryline,
        poster_image,
        trailer_youtube,
    ):
        Video.__init__(self, title)
        self.storyline = moviestoryline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def trailer(self):

    # Called to open trailer

    webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):

    # Class called when a TvShow is called

    def __init__(
        self,
        title,
        tv_station,
        poster_image,
        trailer_youtube_url,
    ):
        Video.__init__(self, title)
        self.tv_station = tv_station
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url


def trailer(self):

    # Called to open trailer

    webbrowser.open(self.trailer_youtube_url)
