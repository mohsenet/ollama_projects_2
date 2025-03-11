from django.test import TestCase
from app_1.pickle_tools import PickleTools


def save_object(file_name, status, data=''):
    p = PickleTools('/home/mohsen/Desktop/' + file_name)

    if status == 'save':
        # Save
        p.dump(data)
        return 0

    if status == 'load':
        # Load
        data = p.load()
        return data
