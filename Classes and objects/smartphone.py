import contact
import contacts_list

smartphone=contacts_list.Contact_List()

contact_1=contact.Contact('John Brown','brown@onet.pl','555234000')
contact_2=contact.Contact('Anna May', 'am@o2.pl', '232000199')
contact_3=contact.Contact('George Small', 'smallg@google.pl', '222999100')
contact_4=contact.Contact('Paola Big', 'bigpaola@poczta.pl', '100200300')

smartphone.add_new_contact(contact_1)
smartphone.add_new_contact(contact_2)
smartphone.add_new_contact(contact_3)
smartphone.add_new_contact(contact_4)
smartphone.display_contact_list()
