import message
class Email(message.Message):
    def __init__(self, sender_address, recipent_address,subject, message):
        super().set_message(message)
        self.sender_address=sender_address
        self.recipent_address=recipent_address
        self.subject=subject
    def send(self):
        print(f"Sending Email...\nFrom:\t{self.sender_address}\nTo:\t{self.recipent_address}\nSubject: {self.subject}\n"+self.message)

email=Email('gocha@123.pl','emilier@123.pl','impreska','kupilam martini')
email.send()