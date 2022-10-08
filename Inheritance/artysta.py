class song():
    def __init__(self,artist, track_title, album, year):
        self.artist=artist
        self.track_title=track_title
        self.album=album
        self.year=year
    
    def __str__(self):
        dane='Artist: '+str(self.artist) +'\n' +'Title track: '+str(self.track_title) + '\n' + 'Album: '+str(self.album) + '\n' + 'Year: '+str(self.year) 
        return dane
    
x=song('mitski','washing machine heart','be the cowboy','2018')
print(x)