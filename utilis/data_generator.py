import random
import string #для айди понадобится библиотека

import fake
from faker import Faker

faker_instance = Faker()

class DataGenerator:
    """""
    
    Фейкер для генерации рандомных данных/значений
    
    """""
    @staticmethod
    def fake_project_id():
        first_letter = faker_instance.random.choice(string.ascii_letters)
        rest_characters = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits + "_", k=10))
        project_id = first_letter + rest_characters
        return project_id

    @staticmethod
    def fake_name():
        return faker_instance.word()


    @staticmethod
    def fake_build_id():
        first_letter_build = faker_instance.random.choice(string.ascii_letters)
        rest_characters_build = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits, k=10))
        build_id = first_letter_build + rest_characters_build
        return build_id


    @staticmethod
    def fake_emaiL():
        first_letter_email = faker_instance.random.choice(string.ascii_letters)
        first_part_email = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits + "_" + ".", k=9))
        second_part_email = ''.join(faker_instance.random.choices(string.ascii_letters, k=4))
        third_part_email = ''.join(faker_instance.random.choices(string.ascii_letters, k=3))
        generated_email = f"{first_letter_email}{first_part_email}@{second_part_email}.{third_part_email}"
        return generated_email


    @staticmethod
    #Строка, которая начинается не с латинской буквы + содержит спецсимволы
    def incorrect_id_1():
        special_symbol = faker_instance.random.choice('@#$%^&*')
        first_part_symbols = ''.join(faker_instance.random.choices(string.digits + special_symbol, k=4))
        second_part_symbols = ''.join(faker_instance.random.choices(string.ascii_letters, k=7))
        incorrect_id_1 = f"{first_part_symbols}{second_part_symbols}"
        return incorrect_id_1

    @staticmethod
    #В строке есть пробел
    def incorrect_id_2():
        string_part = ''.join(faker_instance.random.choices(string.ascii_letters, k=4))
        numbers_part = ''.join(faker_instance.random.choices(string.digits, k=3))
        result_1 = f"{string_part} {numbers_part}"
        return result_1

    @staticmethod
    #Строка содержит буквы русского алфавита
    def incorrect_id_3():
        non_latin = random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        string_part = ''.join(faker_instance.random.choices(string.digits, k=7))
        result_id = f"{non_latin}{string_part}"
        return result_id




