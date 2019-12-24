import media
import fresh_tomatoes

Joker = media.Movie("Joker", "a failed stand-up comedian who turns to a life of crime and chaos in Gotham City","https://upload.wikimedia.org/wikipedia/en/e/e1/Joker_%282019_film%29_poster.jpg", "https://www.youtube.com/watch?v=t433PEQGErc")
Once_upon_a_time_in_Hollywood = media.Movie("Once upon a time in Hollywood", "the film follows an actor and his stunt double as they navigate the changing film industry, and features multiple storylines in a modern fairy tale tribute to the final moments of Hollywood's golden age","https://upload.wikimedia.org/wikipedia/en/a/a6/Once_Upon_a_Time_in_Hollywood_poster.png","https://www.youtube.com/watch?v=ELeMaP8EPAA")
Rocketman = media.Movie("Rocketman", "The film follows John in his early days as a prodigy at the Royal Academy of Music through his musical partnership with Taupin", "https://upload.wikimedia.org/wikipedia/en/0/0f/Rocketman_%28film%29.png", "https://www.youtube.com/watch?v=S3vO8E2e6G0")
Booksmart = media.Movie("Booksmart", "Story of a girl who studies a lot", "https://upload.wikimedia.org/wikipedia/en/0/09/Booksmart_%282019_film_poster%29.png","https://www.youtube.com/watch?v=vmz0-sBOEgo")
Parasite = media.Movie("Parasite","follows a young man from a poor family who begins to tutor a rich family's daughter, and slowly starts to infiltrate their personal lives","https://upload.wikimedia.org/wikipedia/en/0/00/Parasite_%282019_film%29.jpg","https://www.youtube.com/watch?v=isOGD_7hNIY")
Midsommer = media.Movie("Midsommer", "It follows a group of friends who travel to Sweden for a festival that occurs once every ninety years and find themselves in the clutches of a pagan cult.", "https://upload.wikimedia.org/wikipedia/en/4/47/Midsommar_%282019_film_poster%29.png","https://www.youtube.com/watch?v=1Vnghdsjmd0")

movies = [Joker, Once_upon_a_time_in_Hollywood, Rocketman, Booksmart, Parasite, Midsommer]

fresh_tomatoes.open_movies_page(movies)