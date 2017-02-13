import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)



theSS1 = Movie("The Sixth Sense",
              "A psychiatrist attempts to help a child who claims to see the dead.",
              "https://www.youtube.com/watch?v=VG9AGf66tXM",
              "http://images6.fanpop.com/image/photos/36100000/The-Sixth-Sense-image-the-sixth-sense-36136397-1000-1500.jpg")

theSS2 = Movie("The Sixth Sense",
              "A psychiatrist attempts to help a child who claims to see the dead.",
              "https://www.youtube.com/watch?v=VG9AGf66tXM",
              "http://images6.fanpop.com/image/photos/36100000/The-Sixth-Sense-image-the-sixth-sense-36136397-1000-1500.jpg")

theSS3 = Movie("The Sixth Sense",
              "A psychiatrist attempts to help a child who claims to see the dead.",
              "https://www.youtube.com/watch?v=VG9AGf66tXM",
              "http://images6.fanpop.com/image/photos/36100000/The-Sixth-Sense-image-the-sixth-sense-36136397-1000-1500.jpg")

movies = [theSS1, theSS2, theSS3]


fresh_tomatoes.open_movies_page(movies)
