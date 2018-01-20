import webbrowser

class Video(object):
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title,duration):
        self.title = title
        self.duration = duration

class TvShow(Video):
    def __init__(self,show_title, duration,season,episode,tv_station):
        Video.__init__(self,show_title,duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing():
        #do something
        print("something happens")
        
class Movie(Video):
    """ This class provides a way to store movie related information """
    def __init__(self, movie_title, duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self,movie_title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
