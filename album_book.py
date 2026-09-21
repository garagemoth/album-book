from pathlib import Path
import json
import os

album_dict = {
    "Taylor Swift": ["Lover", "folklore", "evermore", "Midnights"],
    "Ariana Grande": ["sweetener", "thank u, next", "positions", "eternal sunshine"],
    "Billie Eilish": ["WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?", "Happier Than Ever", "HIT ME HARD AND SOFT"],
    "Charli xcx": ["how i\'m feeling now", "CRASH", "BRAT", "Music, Fashion, Film"],
    "underscores": ["fishmonger", "Wallsocket", "U"],
    "SOPHIE": ["PRODUCT", "OIL OF EVERY PEARL\'S UN-INSIDES", "SOPHIE"],
    "100 gecs": ["1000 gecs", "10,000 gecs"],
    "Porter Robinson": ["Worlds", "Nurture", "SMILE! :D"],
    "Kero Kero Bonito": ["Intro Bonito", "Bonito Generation", "Time \'n\' Place"]
}

album_database = Path(__file__).resolve().parent / 'album_database.json'

if not album_database.exists():
    album_database.touch()

    with open(album_database, 'w') as file:
        json.dump(album_dict, file, indent=4)

with open(album_database, 'r') as file:
    artists_file = json.load(file)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_data():
    with open(album_database, 'w') as file:
        json.dump(artists_file, file, indent=4)

def add_artist():
    artist = input("Who would you like to add?: > ")
    if artist in artists_file:
        print("That artist is already in the database.")
    else:
        print(f"{artist} has been added to the artist list.")
        artists_file[artist] = []
        save_data()

def remove_artist():
    artist = input("Who would you like to remove?: > ")
    if artist not in artists_file:
        print("That artist is not found in the database.")
    else:
        print(f"{artist} has been removed to the artist list.")
        del artists_file[artist]
        save_data()

def add_album():
    album = input("What album would you like to add?: > ")
    artist = input("What artist does the album belong to?: > ")
    if artist in artists_file:
        if album not in artists_file[artist]:
            artists_file[artist].append(album)
            save_data()
            print(f"The album \"{album}\" has been added to the database.")
        else:
            print("This album is already in the artist's database.")
    else:
        add_artist = input(f"This artist does not seem to be in your database. Do you want to add {artist}? [Y/N]: > ")
        if add_artist.lower() == 'y':
            artists_file[artist] = [album]
            save_data()
            print(f"{artist} has been added to the artist list.")
            print(f"{album} has been added to the artist's database.")
        elif add_artist.lower() != 'n':
            print("Input invalid.")

def remove_album():
    artist = input("What artist does the album belong to?: > ")
    if artist in artists_file:
        album = input("What album would you like to remove?: > ")
        if album in artists_file[artist]:
            artists_file[artist].remove(album)
            save_data()
            print(f"The album \"{album}\" has been removed from the database.")
        else:
            print("This album is not in the artist's database")
    else:
        print("This artist is not in the database, fix your spelling or capitalization.")

def main():
    while True:
        clear_terminal()
        print("-----------------------------------------")
        print("\tWelcome to the Album Book!")
        print("-----------------------------------------\n")

        print("Actions:")
        print("[1] Search Artist")
        print("[2] Search Album")
        print("[3] Artists Selection")
        print("[4] Album Modification")
        print("[5] Quit")

        action = input("What would you like to do?: > ")
        clear_terminal()
        match action:
            case '1': # Artists Search
                artist_search = input("\nSearch for an artist to see their albums or enter \'q\' to go back: > ")

                if artist_search == 'q':
                    pass

                elif artist_search in artists_file:
                    print(f"\n{artist_search}'s albums:")
                    print()
                    if artists_file[artist_search] == []:
                        print("This artist has no albums in the database.")
                    else:
                        for i in artists_file[artist_search]:
                            print("-", i)
                    input("Press enter to continue.")
                    clear_terminal()
                else:
                    print("Artist not found - check your spelling or capitalization")
                    append_artist = input(f"If artist is not in database, would you like to add {artist_search}? [Y/N]: > ")

                    if append_artist.lower() == 'y':
                        artists_file[artist_search] = []
                        save_data()
                    elif append_artist.lower() == 'n':
                        print("Input invalid.")
                    input("Press enter to continue.")
                    clear_terminal()

            case '2': # Album Search
                album_search = input("Search for an album to see the artist who made it or enter \'q\' to quit: > ")
                albums_matched = {}

                if album_search == 'q':
                    pass

                else:
                    for artist, albums in artists_file.items():
                        for album in albums:
                            if album == album_search:
                                albums_matched[artist] = album
                                continue

                    if albums_matched == {}:
                        print("This album is not in the database.")
                    else:
                        for artist, album in albums_matched.items():
                            print(f"{artist} - {album}")
                    input("\nPress enter to continue.")
                    clear_terminal()


            case '3': # Artists Selection
                print("Actions:")
                print("[1] View Artists List")
                print("[2] Add Artist")
                print("[3] Remove Artist")
                print("[4] Go Back")

                artist_action = input("What would you like to do?: > ")
                clear_terminal()

                match artist_action:
                    case '1': # View Artists List
                        print("Artists List")
                        for i in artists_file:
                            print('-', i)

                    case '2': # Add Artist
                        add_artist()

                    case '3': # Remove Artist
                        remove_artist()

                    case '4': # Go Back
                        pass

                    case _:
                        print("Your input is invalid.")
                input("Press enter to go back to menu.")

            case '4': # Album Modification
                print("Actions:")
                print("[1] Add an Album")
                print("[2] Remove an Album")
                print("[3] Go back")
                ans = input("What would you like to do?: > ")
                clear_terminal()

                match ans:
                    case '1': # Add an Album
                        add_album()
                        
                    case '2':
                        remove_album()

                    case '3': # Go Back
                        pass

                    case _:
                        print("Your input is invalid.")
                input("Press enter to continue.")
                clear_terminal()

            case '5': # Quit
                break

            case _: # Invalid Input
                input("Invalid input, press enter to try again.")

if __name__ == "__main__":
    main()