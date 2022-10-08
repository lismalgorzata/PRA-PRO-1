class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no= 1
        self.channels_list=[]
        self.volume_level=0
    
    def turn_on(self):
        self.is_on=True
        
    def turn_off(self):
        self.is_on=False
        
    def show_status(self):
        if self.is_on:
            if self.channel_no< len(self.channels_list):
                print('tv is on, channel', self.channel_no,'(', self.channels_list[self.channel_no-1], ')', '|', 'volume:',self.volume_level,)
            else:
                print('tv is on, channel', self.channel_no, 'not found', 'volume:',self.volume_level)
        else: print('tv is off')
    
    def set_channel(self, new_channel_no):
        self.new_channel_no=new_channel_no
        self.channel_no=new_channel_no
         
    def set_channels(self, channels_list):
        self.channels_list=channels_list
    
    def show_channels(self):
        print('channels list:', '\n', end='')
        for i in range(0,len(self.channels_list)):
            print(i+1, self.channels_list[i], sep='. ')
    
    def increase_volume(self):
        while self.volume_level < 10 :
            self.volume_level+=1
            break
        
    def decrease_volume(self):
        while self.volume_level > 0:
            self.volume_level-=1
            break

t1=TV()
t1.show_status()
t1.turn_on()
t1.show_status()
t1.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'TVP Kultura', 'TV Puls', 'Eska TV'])
t1.show_channels()
t1.set_channel(2)
t1.show_status()
t1.increase_volume()
t1.increase_volume()
t1.increase_volume()
t1.increase_volume()
t1.show_status()
t1.set_channel(4)
t1.show_status()
t1.decrease_volume()
t1.decrease_volume()
t1.show_status()