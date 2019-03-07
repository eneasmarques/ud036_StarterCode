import requests


class MovieApi():
    """ Trara lista de Filmes de API """

    # chave para acessar API
    API_KEY = "api_key=c21742cf254973b3db2aca79f0f2a960"

    # variavel para armazenar links
    URL = {
        'popular_movies': "https://api.themoviedb.org/3/movie/popular",
        'images': "https://image.tmdb.org/t/p/w500/",
        'movies': "https://api.themoviedb.org/3/movie/"
    }

    def getPopularMovies(self):
        """ Funcao que retornara array de filmes populares de uma API """
        resp = requests.get(
            self.URL['popular_movies'] +
            '?' +
            self.API_KEY).json()

        movies = []
        for movie in resp['results']:
            if not(movie['poster_path'] is None):
                filter = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'poster_image_url':
                        self.URL['images'] + movie['poster_path'],
                    'trailer_youtube_url': self.getKeyMovie(movie['id'])
                }

                movies.append(filter)

        return movies

    def getKeyMovie(self, movie_id):
        """ Funcao que retornara array de filmes populares de uma API """
        getURL = self.URL['movies'] + str(movie_id) + '/videos?' + self.API_KEY
        getURL += '&language=en-US'
        resp = requests.get(getURL).json()
        return resp['results'][0]['key']
