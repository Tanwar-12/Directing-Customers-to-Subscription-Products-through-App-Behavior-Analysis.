import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_hard_to_guess_string'

config = Config()
