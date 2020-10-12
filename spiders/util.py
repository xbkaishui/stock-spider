# -*- coding: utf-8 -*-
import os
import datetime
import sys

def is_cached(file_path):
    '''
    Checks if the file cached is still valid
    '''
    if not os.path.exists(file_path):
        return False

    file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
    current_time = datetime.datetime.now()
    file_age = (current_time - file_time).total_seconds()

    if file_age > 86400:
        return False
    else:
        return True