import random 
engmovies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Godfather Part II", "12 Angry Men", "Schindler's List", "The Lord of the Rings: The Return of the King", "Pulp Fiction", "The Lord of the Rings: The Fellowship of the Ring", "The Good, the Bad and the Ugly", "Forrest Gump", "Fight Club", "Inception", "The Lord of the Rings: The Two Towers", "Star Wars: Episode V – The Empire Strikes Back", "The Matrix", "Goodfellas", "One Flew Over the Cuckoo's Nest", "Se7en", "Interstellar", "Seven Samurai", "It's a Wonderful Life", "The Silence of the Lambs", "Saving Private Ryan", "City of God", "Life Is Beautiful", "Spirited Away", "The Green Mile", "Parasite", "Terminator 2: Judgment Day", "Back to the Future", "Whiplash", "Gladiator", "The Prestige", "The Departed", "The Pianist", "The Lion King", "American History X", "The Usual Suspects", "Casablanca", "Psycho", "The Intouchables", "Modern Times", "Once Upon a Time in the West", "Rear Window", "Alien", "Apocalypse Now", "Memento", "Raiders of the Lost Ark", "Django Unchained", "WALL·E", "The Shining", "Avengers: Infinity War", "Oldboy", "Witness for the Prosecution", "Princess Mononoke", "Joker", "Dr. Strangelove", "The Lives of Others", "Cinema Paradiso", "Grave of the Fireflies", "Aliens", "Sunset Boulevard", "Paths of Glory", "The Great Dictator", "Your Name", "Spider-Man: Into the Spider-Verse", "The Truman Show", "The Hunt", "The Wolf of Wall Street", "Inglourious Basterds", "The Sixth Sense", "A Beautiful Mind", "Toy Story", "Braveheart", "Amélie", "Léon: The Professional", "2001: A Space Odyssey", "Reservoir Dogs", "The Sting", "North by Northwest", "Requiem for a Dream", "Vertigo", "The Apartment", "Full Metal Jacket", "Lawrence of Arabia", "Eternal Sunshine of the Spotless Mind", "Die Hard", "The Treasure of the Sierra Madre", "Chinatown", "No Country for Old Men", "The Thing", "The Grand Budapest Hotel", "Heat", "The Great Escape", "Blade Runner", "Mad Max: Fury Road", "Gone Girl", "Coco", "Green Book"]
movie = random.choice(engmovies).lower()
# print(movie)
hp=7
life=2
guessed_letters =[]
won=True

while hp > 0 and life > 0:
    for i in movie :
        if i != " " and i not in guessed_letters:
            won=False
        elif won :
            print("congradulations")
            break
    for i in movie :
        if (i==" "):
            print(" ",end=" ")
        elif i in guessed_letters:
            print(i, end=" ")
        else:
            print('_',end=" ")
    print()

    choice = input("guess or movieguess: ").lower()

    if choice == "guess":
        guess = input("Enter a letter: ").lower()
        if len(guess)!=1:
            print(" you can only enter one letter")
        if guess in guessed_letters:
            print("already guessed")
        elif guess in movie:
            guessed_letters.append(guess)
            print("correct")
        else:
              print("wrong")
              hp=hp-1
              print(hp)
        

    elif choice == "movieguess":
        movieguess = input("Enter the movie: ").lower()

        if movieguess == movie:
            print("congratulations")
            break
        else:
            life=life-1
            print(" you have one remaining life ")
            print(life)

    if hp == 0 or life == 0 :
        print("game over ")
        print("The movie was ",movie)
