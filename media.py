import webbrowser
import fresh_tomatoes

"""This class holds infomation about movies"""


class Movie():
    def __init__(self, title, summary, trailer_youtube_url, poster_image_url):
        self.title = title
        self.summary = summary
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)
