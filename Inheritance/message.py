class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        new_message = ''
        is_first=True
        
        for letter in message:
            if is_first:
                new_message += letter.upper()
                is_first=False
            else:
                new_message += letter.lower()
        new_message += ', BYE.'
        self.message=new_message
        