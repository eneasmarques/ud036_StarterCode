# Fresh Tomatoes Movie Trailers

## Índice
* [Descrição](#descrição)
* [Instruções](#instruções)
* [Contribuindo](#contribuindo)

## Descrição

### Versão
Python 2.7.15

### Instalar

[GitHub.com](https://github.com/eneasmarques/ud036_StarterCode) - (branch master) - executar arquivo entertainment_center.py

[GitHub.io](https://eneasmarques.github.io/ud036_StarterCode/fresh_tomatoes.html)

## Instruções

### Arquivos e pastas

Pastas do Projeto:
* **css** - para o arquivo `style.css`.
* **js** - para o arquivo `main.js`.

### Código de trabalho

Ao executar o arquivo `entertainment_center.py` será importada uma lista de filmes disponíveis em `https://api.themoviedb.org` por meio da classe `MovieApi()` e do método `getPopularMovies(self)` que retornará um array para variável `movies`.

Por meio de um loop iresmo instanciar objetos da classe `Movie` em um novo array que será enviado para `fresh_tomatoes.py` por meio do método `open_movies_page(movies)`.

O método `open_movies_page(movies)` por sua vez passará o array para o método `create_movie_tiles_content(movies)` que irá gerar o conteúdo com a lista de Filmes atribuindo os valores(movie_title,poster_image_url e trailer_youtube_id) e retornará esse conteúdo.

Após retornar a lista será gerada nossa página no arquivo `fresh_tomatoes.html`.

## Contribuindo

Depois de aprovado pela **Udacity** qualquer contribuiçaõ será bem vinda.
