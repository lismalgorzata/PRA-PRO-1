class Phone():
    def __init__(self):
        self.is_on=False
        self.is_locked=True
        self.is_onAriplaneMode=False
        
    def turn_on(self):
        self.is_on=True
        print('HELLO')
        
    def turn_off(self):
        self.is_off=False
        print('GOODBYE')
    
    def unlock(self):
        print('Insert your PIN to unlock.')
    
    def insert_pin(self,pin):
        self.pin=pin
        if self.pin == 1009:
            self.is_locked=False
            print('Welcome')
        else:
            print('Incorrect. Try again')
    def lock(self):
        self.is_locked=True
        print('Phone locked')
    
    def airplane_mode_on(self):
        self.is_onAriplaneMode=True
        print("\tAirplane mode on. \nYou'll be unable to make or receive calls, \nsend or receive messages or browse the internet.")
    def airplane_mode_off(self):
        self.is_onAriplaneMode=False
        print("\tAirplane mode off. \nYou're able to make and receive calls, \nsend and receive messages and browse the internet.")

phone1=Phone()
phone1.turn_on()
phone1.unlock()
phone1.insert_pin(2345)
phone1.insert_pin(1009)
phone1.lock()
phone1.turn_off()
print('\n----------\n')
phone2=Phone()
phone2.unlock()
phone2.insert_pin(1009)
phone2.airplane_mode_on()
phone2.airplane_mode_off()
phone2.lock()

            
    
    
        
    