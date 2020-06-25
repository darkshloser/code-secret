import smtplib
import


class Gml(object):
    def __init__(self):
        self.credentials = self.get_credentials
        if self.check_key_existence():
            pass

    @property
    def get_credentials(self):
        email = input("Enter email address: ")
        password = input("Password: ")
        email_subject = input("Subject: ")

    def check_key_existence(self):
        pass

    def get_existing_key(self):
        pass

    def store_created_key(self):
        pass
