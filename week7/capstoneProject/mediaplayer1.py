import doubly_linked_for_capstone
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    # def __eq__(self, other):
    #     return ((self.title, self.artist) == (other.title, other.artist))
        
    # def __ne__(self, other):
    #     return not (self == other)

    # def __lt__(self, other):
    #     return ((self.title, self.artist) < (other.title, other.artist))
        
    # def __gt__(self, other):
    #     return ((self.title, self.artist) < (other.title, other.artist))
        

class MediaPlayer():

    def __init__(self):
        self.playlist = doubly_linked_for_capstone.DoublyLinkedList()
        self.currentSong = None

    def add(self, songTitle, songArtist):
        newSong = Song(songTitle, songArtist)
        self.playlist.add(newSong)
        self.playlist.count += 1

    def deleteByTitle(self, title):
        currentSong = self.playlist.head
        prev = self.playlist.head
        if self.playlist.count == 0:
            print("No Songs To Delete.")
        else:
            while currentSong:
                print(currentSong)
                if currentSong == title:
                    if currentSong == self.playlist.tail:
                        prev.next = self.playlist.head
                        self.playlist.tail = prev
                        
                        print("This Song Was Deleted.")
                    elif currentSong == self.playlist.head:
                        currentSong.next.prev = self.playlist.tail
                        self.playlist.tail = currentSong.next
                        print("This Song Was Deleted.")
                    else: 
                        prev.next = currentSong.next
                        currentSong.next = prev
                        print("This Song Was Deleted.")
                    self.playlist.count -= 1
                else:
                    print("Could Not Find Improper Spelling.")
                prev = currentSong
                currentSong = prev.next


    def remove(self, index) -> int:
        if (index < 0) or (index > self.playlist.size()-1):
            return 0
        self.playlist.deleteAtIndex(index)
        return 1

    def play(self, song=None):
        if song:
            self.currentSong = song
        if not self.currentSong:
            self.currentSong = self.playlist.getStart()
        print(self.currentSong.data.getTitle()+"Is Now Playing.")

    def skip(self):
        self.currentSong = self.currentSong.next

        if not self.currentSong:
            # We reached the end of the playlist, loop back to the beginning.
            self.currentSong = self.playlist.getStart()
        self.play(self.currentSong)

    def goBack(self):
        self.currentSong = self.currentSong.prev
        if not self.currentSong:
            #We reached the end of the playlist, loop back to the end.
            self.currentSong = self.playlist.getEnd()
        self.play(self.currentSong)

    def showCurrentSong(self):
        if self.currentSong:
            print(self.currentSong.data)
        else:
            print("No song is playing at this time.")

    def shuffle(self):
        self.playlist.shuffleList()

myMediaPlayer = MediaPlayer()
myMediaPlayer.add("American Girl","Tom Petty")
myMediaPlayer.add("Dead Flowers","Rolling Stones")
myMediaPlayer.add("The Breeze","Lynrd Skynrd")
myMediaPlayer.add("Sweet Home Alabama","Lynrd Skynrd")
myMediaPlayer.add("Love Song","The Outlaws")
myMediaPlayer.add("Folsom Prison","Johnny Cash")  

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


while True:
    menu()
    choice = int(input())

    if choice == 1:
        newSongTitle = input("Please Enter The Song Title.")
        newSongArtist = input("Please Enter The Song's Artist.")
        myMediaPlayer.add(newSongTitle, newSongArtist)
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        print("New Song Added to Playlist")
    elif choice == 2:
        print("Your Playlist Currently Includes:")
        print(myMediaPlayer.playlist)
        removeIndex = int(input("Please Enter The Index Of The Song To Remove."))
        myMediaPlayer.remove(removeIndex)
        #     print("Song Removed From Playlist\n")
        # else:
        #     print("Invalid Selection\n")
            # print("Song Removed From Playlist")
        # Prompt user for Song Title 
        # remove song from playlist
        # print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")
        myMediaPlayer.play()        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")
        myMediaPlayer.skip()                    
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")
        myMediaPlayer.goBack()  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")
        myMediaPlayer.shuffle()
        print(myMediaPlayer.playlist)          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")
        myMediaPlayer.showCurrentSong()    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(myMediaPlayer.playlist)
    elif choice == 0:
        print("Goodbye.")
        break

            
