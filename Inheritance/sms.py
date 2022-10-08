import message
class SMS(message.Message):
    def __init__(self, sender_number, recipent_number, message):
        super().set_message(message)
        self.sender_number=sender_number
        self.recipent_number=recipent_number
    def send(self):
        print(f"Sending SMS...\nFrom:\t{self.sender_number}\nTo:\t{self.recipent_number}\n"+self.message)
        
sms=SMS(123456789,987654321,"johnny metal")

sms.send()