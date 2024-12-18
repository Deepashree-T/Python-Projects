# Task1 Define songs playlist dictionary 

songs = {
    "Gerua": {
        "artist": "Arijit Singh, Antara Mitra",
        "genre": "Romantic"
    },
    "Tujh Mein Rab Dikhta Hai": {
        "artist": "Roopkumar Rathod",
        "genre": "Romantic/Ballad"
    },
    "Kal Ho Naa Ho": {
        "artist": "Sonu Nigam",
        "genre": "Emotional/Inspirational"
    },
    "Chaiyya Chaiyya": {
        "artist": "Sukhwinder Singh, Sapna Awasthi",
        "genre": "Folk Fusion"
    },
    "Tumhi Dekho Na": {
        "artist": "Shreya Ghoshal, Sonu Nigam",
        "genre": "Romantic/Ballad"
    },
    "Suraj Hua Maddham": {
        "artist": "Sonu Nigam, Alka Yagnik",
        "genre": "Romantic/Ballad"
    },
    "Lungi Dance": {
        "artist": "Yo Yo Honey Singh",
        "genre": "Party/Pop"
    },
    "Mitwa": {
        "artist": "Shafqat Amanat Ali",
        "genre": "Sufi/Romantic"
    },
    "Bholi Si Surat": {
        "artist": "Udit Narayan, Lata Mangeshkar",
        "genre": "Romantic"
    },
    "Main Hoon Na": {
        "artist": "Sonu Nigam",
        "genre": "Inspirational/Pop"
    }
}

# Check details of a specific song
print("Details of 'Gerua':")
print(songs["Gerua"], "\n")


# Function to add songs to the playlist
def add_song(songs, title, artist, genre):
    
    if title in songs:
        print(f"The song '{title}' already exists in the playlist.")
    else:
        songs[title] = {
            "artist": artist,
            "genre": genre
        }
        print(f"Song '{title}' added successfully!")


# Adding a new song
add_song(songs, "Zaalima", "Arijit Singh, Harshdeep Kaur", "Romantic")

# Print the updated dictionary
print("\nPlaylist after adding a new song:")
print(songs)

# Function to view all songs in the playlist
def view_playlist(songs):

    if not songs:
        print("The playlist is empty.")
    else:
        print("Songs in the Playlist:")
        for title, details in songs.items():
            print(f"Title: {title}")
            print(f"  Artist(s): {details['artist']}")
            print(f"  Genre: {details['genre']}\n")


# View the playlist
view_playlist(songs)


# Updating song information
def update_song(songs, title, new_artist=None, new_genre=None):
    
    if title not in songs:
        print(f"The song '{title}' does not exist in the playlist.")
    else:
        if new_artist:
            songs[title]["artist"] = new_artist
            print(f"Artist for '{title}' updated to '{new_artist}'.")
        if new_genre:
            songs[title]["genre"] = new_genre
            print(f"Genre for '{title}' updated to '{new_genre}'.")
        if not new_artist and not new_genre:
            print("No updates were made as no new artist or genre was provided.")

# View the updated playlist
print("\nUpdated Playlist:")
view_playlist(songs)

#Function to delete a song from the playlist
def delete_song(songs, title):
    if title in songs:
        del songs[title]
        print(f"Song '{title}' has been removed from the playlist.")
    else:
        print(f"The song '{title}' does not exist in the playlist.")

# To chck if the song is deleted
delete_song(songs,"Gerua")

# To check: Delete a song that does not exist
delete_song(songs, "Rang")

#View the updated playlist
print("\nUpdated Playlist")

