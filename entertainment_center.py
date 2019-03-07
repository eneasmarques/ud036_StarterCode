import fresh_tomatoes
import media
import movies_api

movie_api = movies_api.MovieApi()
movies = movie_api.getPopularMovies()

listaMovies = []
for movie in movies:
    listaMovies.append(media.Movie(movie['title'],
                                   movie['poster_image_url'],
                                   movie['trailer_youtube_url']))
fresh_tomatoes.open_movies_page(listaMovies)
