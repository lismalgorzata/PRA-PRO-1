import random
class thermometer():
    
    def __init__(self):
        self.is_on=False
        self.patient_temp=0
        
    def turn_on(self):
        self.is_on=True
        print('Thermometer is on.')
    def turn_off(self):
        self.is_on=False
        print('Thermometer is off.')
        
    def measure(self):
        self.patient_temp=random.uniform(34.0,42.0)
        self.patient_temp=float('{:.1f}'.format(self.patient_temp))
    
    def display(self):
        print('Temperature: ',self.patient_temp)
        if self.patient_temp>=37.0 and self.patient_temp<41.0:
            print('Fever')
        elif self.patient_temp>=41.0:
            print('CRITICAL TEMPERATURE!!@!11!21!!')
        else:
            print('Alles gut')
            
t=thermometer()
t.turn_on()
t.measure()
t.display()
t.turn_off()