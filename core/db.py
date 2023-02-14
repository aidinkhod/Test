from typing import Dict


class Database:
    posts = [
        {
            'pk': 1,
            'year': 2002,
            'amount': 6000,
            'car': 'Mercedes Benz',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/e/ee/2002_Mercedes-Benz_E320%2C_Front_Left%2C_10-27-2021.jpg',
            'description': 'The 2002 Mercedes-Benz A-class is a small car with the heart of an S-class luxury sedan. The expensive-looking façade helps it look right at home among the rest of the Benz lineup, and its modern, tech-filled cabin delivers much the same experience as pricier models.',
            'contacts': 'Please contact by email benz@mercedes.com or phone +1 90 2323 909 22 '
        },
        {
            'pk': 2,
            'year': 2006,
            'amount': 8000,
            'car': 'Toyota',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/7/7d/2004-2006_Toyota_Camry.jpg',
            'description': 'The Toyota Camry is an excellent vehicle. It runs well, very reliable, comfortable, high quality, low maintenance, stylish, and a great value. The features are very nice and easy to access',
            'contacts': 'Please contact by email camry@toyota.com or phone +123 321 75 85'
        },
        {
            'pk': 3,
            'year': 2004,
            'amount': 6500,
            'car': 'Subaru',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/8/86/04-05_Subaru_WRX_STi_2.jpg',
            'description': 'The Impreza Base, Premium, and Limited versions all deliver estimated highway fuel mileage ratings of 36 miles per gallon. The Impreza Sport and most of the Legacy lineup also come in with estimated highway fuel mileage ratings in the neighborhood of 35 miles per gallon.',
            'contacts': 'Please contact by email impreza@subaru.com +123 456 78 90'
        }
        ]
    sum = list()
    for i in posts:
        sum.append(i.get('amount'))

    @classmethod
    def get_post_by_pk(cls, pk: int) -> Dict[str, int | str]:
        result = list(filter(lambda p: p.get("pk") == pk, cls.posts))
        return result[0] if result else None

    @staticmethod
    def get_list():
        return Database.posts

    @staticmethod
    def sum_amount(total_amount):
        return sum(total_amount)
