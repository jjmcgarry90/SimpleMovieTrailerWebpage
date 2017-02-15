import media
import fresh_tomatoes


# Create a list of movies to be passed to an HTML page maker
def create_movie_list():
    the_sixth_sense = media.Movie("The Sixth Sense", "A psychiatrist attempts "
                                  "to help a child who claims to see the dead",
                                  "https://www.youtube.com/watch?v=VG9AGf66tXM",  # NOQA
                                  "http://images6.fanpop.com/image/photos/36100000/The-Sixth-Sense-image-the-sixth-sense-36136397-1000-1500.jpg")  # NOQA

    finding_dory = media.Movie("Finding Dory", "The friendly but forgetful "
                               "blue fish begins a search for her parents.",
                               "https://www.youtube.com/watch?v=MKJA-VLpiCo",
                               "http://cdn.collider.com/wp-content/uploads/2015/11/finding-dory-poster.jpg")  # NOQA

    groundhog_day = media.Movie("Groundhog Day", "A weatherman finds himself "
                                "living the same day over and over",
                                "https://www.youtube.com/watch?v=tSVeDx9fk60",
                                "http://www.impawards.com/1993/posters/groundhog_day.jpg")  # NOQA
    # Create a movie list that can be accessed from outside this function
    global movies
    movies = [the_sixth_sense, finding_dory, groundhog_day]


create_movie_list()
# Pass our list to the magic page-maker
fresh_tomatoes.open_movies_page(movies)
