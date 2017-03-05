import media
import fresh_tomatoes

#this function will create movie objects and then a list that contains them
def create_movie_list():
    the_sixth_sense = media.Movie("The Sixth Sense", "A psychiatrist attempts "
                                  "to help a child who claims to see the dead.",
                                  "https://www.youtube.com/watch?v=VG9AGf66tXM",
                                  "http://images6.fanpop.com/image/photos/36100000/The-Sixth-Sense-image-the-sixth-sense-36136397-1000-1500.jpg")  # NOQA

    men_in_black = media.Movie("Men in Black", "A police officer joins a secret "
                               "organization that polices and monitors "
                               "extraterrestrial interactions on Earth.",
                               "https://www.youtube.com/watch?v=HYUd7AOw_lk",
                               "http://assets.flicks.co.nz/images/movies/poster/c9/c96c08f8bb7960e11a1239352a479053_500x735.jpg")  # NOQA

    groundhog_day = media.Movie("Groundhog Day", "A weatherman finds himself "
                                "inexplicably living the same day over and over"
                                "again.",
                                "https://www.youtube.com/watch?v=tSVeDx9fk60",
                                "http://www.impawards.com/1993/posters/groundhog_day.jpg")
    # Create a movie list that can be accessed from outside this function
    global movies
    movies = [the_sixth_sense, men_in_black, groundhog_day]


create_movie_list()
# This function call passes the movie list to an html page maker.
fresh_tomatoes.open_movies_page(movies)


