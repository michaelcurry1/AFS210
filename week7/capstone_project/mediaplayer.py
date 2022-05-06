
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

 
# class Node:
#     # A doubly-linked node.
#     def __init__(self,title,artist):
#         self.title = title
#         self.artist = artist
#         self.next = None
#         self.prev = None


#     def getTitle(self):
#         return self.title 

#     def getArtist(self):
#         return self.artist 

#     def setTitle(self,title):
#          self.title = title

#     def setArtist(self,artist):
#         self.artist = artist

#     def fullTitle(self):

class Playlist:
    def __init__(self):
        
        self.currentSong = None
        self.end = None
        self.count = 0
  
    def addLast(self,title,artist):
        newSong = Song(title, artist)
        # Add a node at the end of the list
        # node4 = Node (data)
        if self.count == 0:
           
            self.currentSong = newSong
            self.end = self.currentSong
        else:

            self.end.next = newSong
            newSong.prev = self.end
            self.end = newSong
            self.currentSong.prev = self.end
            self.end.next = self.currentSong
        self.count += 1 

        print("Song Has Been Added" , newSong.__str__())

    def size()


    def iter(self):
        # Iterate through the list.
        current = self.currentSong
        count = 0
        playlist = self.size()
       
        while count < playlist:
            # title = current.data.title
            # artist = current.data.artist
            print(current.__str__())
            current = current.next
            count += 1
            # yield val



        


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

playlist = Playlist()
playlist.addLast("American Girl","Tom Petty")
playlist.addLast("Dead Flowers","Rolling Stones")
playlist.addLast("The Breeze","Lynrd Skynrd")
playlist.addLast("Sweet Home Alabama","Lynrd Skynrd")
playlist.addLast("Love Song","The Outlaws")
playlist.addLast("Folsom Prison","Johnny Cash")


while True:
    menu()
    choice = int(input())

   
    
    # playlist = ["Sweet Home Alabama", "American Girl", "Dead Flowers"]
    # playlist.append("Gimme Back My Bullets")
    # print(playlist)

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        songtitle = input("Please Enter Song Title ")
        artist = input("Please Enter Artist Name ")
      


        # Add song to playlist
        playlist.addLast(songtitle, artist)
        playlist.iter()
       
        
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        playlist = ["Sweet Home Alabama", "American Girl", "Dead Flowers"]
        playlist.remove("Dead Flowers")
        print(playlist)

        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        
        print("\nSong list:\n")
        playlist.iter()
    elif choice == 0:
        print("Goodbye.")
        break

            
