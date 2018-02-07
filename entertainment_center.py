"""generates the content of the Movie trailers website"""
import fresh_tomatoes
import media

def main():
    """Initializes movie objects in an array and passes to fresh_tomatoes"""    

    the_matrix = media.Movie("The Matrix", "1 hour",
                             "A computer hacker learns from mysterious rebels "
                             "about the true nature of his reality and his "
                             "role in the war against its controllers.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=m8e-FF8MsqU") 

    interstellar = media.Movie("Interstellar", "1 hour",
                               "A team of explorers travel through a wormhole"
                               "in space in an attempt to ensure humanity's"
                               "survival.",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=2LqzF5WauAw")

    dumb_and_dumber = media.Movie("Dumb and Dumber", "1 hour",
                                  "The cross-country adventures of two "
                                  "good-hearted but incredibly stupid friends",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BZDQwMjNiMTQtY2UwYy00NjhiLTk0ZWEtZWM5ZWMzNGFjNTVkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR0,0,182,268_AL_.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=MSu25pQ4iFw")  # NOQA

    rick_roll = media.Movie("Infinity War", "1 hour",
                            "The Avengers and their allies must be willing to"
                            " sacrifice all in an attempt to defeat the "
                            "powerful Thanos before his blitz of devastation"
                            " and ruin puts an end to the universe.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0MjA1OTMxOV5BMl5BanBnXkFtZTgwMzM1NDcyNDM@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    the_equalizer = media.Movie("The Equalizer", "1 hour",
                                "A man believes he has put his mysterious"
                                "past behind him and has dedicated himself to"
                                " beginning a new, quiet life. But when he"
                                " meets a young girl under the control of "
                                "ultra-violent Russian gangsters, he can't "
                                "stand idly by - he has to help her.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MzE2NTk0NF5BMl5BanBnXkFtZTgwOTM3NTk1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=VjctHUEmutw")

    shawshank_redemption = media.Movie("Shawshank Redemption", "1 hour",
                                       "Two imprisoned men bond over a number"
                                       " of years, finding solace and eventua"
                                       "l redemption through acts of common d"
                                       "ecency.",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")  # NOQA

    movies = [rick_roll, dumb_and_dumber, interstellar,
              the_equalizer, shawshank_redemption, the_matrix]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
