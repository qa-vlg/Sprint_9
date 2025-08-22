import random
import string
from pathlib import Path

class UserRandomData:

    @staticmethod
    def create_user_data():
        first_name = UserRandomData.user_first_name()
        last_name = UserRandomData.user_last_name()
        user_name = UserRandomData.user_name()
        email = UserRandomData.user_email()
        password = UserRandomData.user_pwd()
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "user_name": user_name
        }
        return user_data
    
    @staticmethod
    def user_first_name():
        return ''.join(random.choices(string.ascii_letters, k = random.choice(range(5, 7))))

    @staticmethod
    def user_last_name():
        return ''.join(random.choices(string.ascii_letters, k = random.choice(range(8, 12))))

    @staticmethod
    def user_name():
        return ''.join(random.choices(string.ascii_letters + string.digits, k = random.choice(range(7, 10))))

    @staticmethod
    def user_email():
        domain = 'qa.com'
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k = random.choice(range(15, 25))))
        return f'{prefix}@{domain}'
    
    @staticmethod
    def user_pwd():
        return ''.join(random.choices(string.ascii_letters + string.digits, k = random.choice(range(8, 10))))


class FilePath:

    @staticmethod
    def get_file_path(file_name):
        project_dir = Path(__file__).parent
        file_path = project_dir / 'assets' / file_name
        return str(file_path)