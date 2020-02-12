class ContactBook:
    contact_list = [ ]

    def __init__(self, surname, name, patronymic, post_adr, emails, phone_numb, messengers):
        self.surname - surname
        self.name = name
        self.patronymic = patronymic
        self.post_adr = post_adr
        self.emails = emails
        self.phone_numb = phone_numb
        self.messengers = messengers
        global reg_num
        reg_num += 1
        self.id = reg_num

        def __str__(self):
            return 
