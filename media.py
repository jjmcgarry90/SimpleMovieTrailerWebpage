import webbrowser

class Movie():
    """This class holds information about movies"""
    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    
    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)







