import media
import fresh_tomatoes

def create_movie_list():
    the_sixth_sense = media.Movie("The Sixth Sense", "A psychiatrist attempts to "
                                  "help a child who claims to see the dead.",
                                  "https://www.youtube.com/watch?v=VG9AGf66tXM",
                                  "http://images6.fanpop.com/image/photos/36100000/The-Sixth-Sense-image-the-sixth-sense-36136397-1000-1500.jpg")  # NOQA

    finding_dory = media.Movie("Finding Dory", "The friendly but forgetful blue "
                               "tang fish begins a search for her long-lost parents.",
                               "https://www.youtube.com/watch?v=MKJA-VLpiCo",
                               "http://cdn.collider.com/wp-content/uploads/2015/11/finding-dory-poster.jpg")  # NOQA

    groundhog_day = media.Movie("Groundhog Day", "A weatherman finds himself "
                                "inexplicably living the same day over and over again.",
                                "https://www.youtube.com/watch?v=tSVeDx9fk60",
                                "http://www.impawards.com/1993/posters/groundhog_day.jpg")

    global movies
    movies = [the_sixth_sense, finding_dory, groundhog_day]


create_movie_list()
fresh_tomatoes.open_movies_page(movies)


