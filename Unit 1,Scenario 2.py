# Movie Collection Management System
class Movie:
    # Class Variable
    cinema_name = "Galaxy Multiplex"

    # Constructor
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    # Class Method
    @classmethod
    def change_cinema(cls, new_name):
        cls.cinema_name = new_name

    # Static Method
    @staticmethod
    def movie_category(rating):
        if rating >= 8.0:
            return "Hit"
        elif rating >= 5.0:
            return "Average"
        else:
            return "Flop"

    # Magic Method
    def __str__(self):
        return (
            f"Movie Name   : {self.movie_name}\n"
            f"Rating       : {self.rating}/10\n"
            f"Ticket Price : ₹{self.ticket_price}\n"
            f"Category     : {Movie.movie_category(self.rating)}"
        )


class Cinema:
    def __init__(self):
        self.movies = []

    # Add Movie
    def add_movie(self, movie):
        self.movies.append(movie)

    # Display Movies
    def display_movies(self):
        print("=" * 50)
        print(f"        {Movie.cinema_name}")
        print("      MOVIE COLLECTION SYSTEM")
        print("=" * 50)

        for i, movie in enumerate(self.movies, start=1):
            print(f"\nMovie {i}")
            print("-" * 50)
            print(movie)

        print("\n" + "=" * 50)
        print("Total Movies :", len(self.movies))
        print("=" * 50)

# Main Program
cinema = Cinema()

movie1 = Movie("Avengers: Endgame", 9.2, 350)
movie2 = Movie("The Flash", 6.5, 250)
movie3 = Movie("Random Movie", 4.3, 180)

cinema.add_movie(movie1)
cinema.add_movie(movie2)
cinema.add_movie(movie3)

cinema.display_movies()

print("\nUpdating Cinema Name...\n")

Movie.change_cinema("CineWorld Multiplex")

cinema.display_movies()
Comment:-
        Galaxy Multiplex
      MOVIE COLLECTION SYSTEM
Movie 1

Movie Name   : Avengers: Endgame
Rating       : 9.2/10
Ticket Price : ₹350
Category     : Hit

Movie 2

Movie Name   : The Flash
Rating       : 6.5/10
Ticket Price : ₹250
Category     : Average

Movie 3

Movie Name   : Random Movie
Rating       : 4.3/10
Ticket Price : ₹180
Category     : Flop


Total Movies : 3


Updating Cinema Name:

        CineWorld Multiplex
      MOVIE COLLECTION SYSTEM

Movie 1

Movie Name   : Avengers: Endgame
Rating       : 9.2/10
Ticket Price : ₹350
Category     : Hit

Movie 2

Movie Name   : The Flash
Rating       : 6.5/10
Ticket Price : ₹250
Category     : Average

Movie 3

Movie Name   : Random Movie
Rating       : 4.3/10
Ticket Price : ₹180
Category     : Flop

Total Movies : 3
