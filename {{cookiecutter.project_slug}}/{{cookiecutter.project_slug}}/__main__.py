"""
Band service skeleton
(c) Dmitry Rodin 2018
---------------------
"""
from band import settings, start_server

def main():
    start_server(**settings)

if __name__ == '__main__':
    main()
