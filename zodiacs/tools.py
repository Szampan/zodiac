from datetime import datetime     

import logging

class ZodiacSign:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y/%m/%d').date()
        self.end_date = datetime.strptime(end_date, '%Y/%m/%d').date()

    def is_me(self, date):
        if date.month == 1 and date.day < 20:
            date = date.replace(year=1901)
        else:
            date = date.replace(year=1900)
        return self.start_date < date < self.end_date

ZODIAC_SIGNS = [
    ZodiacSign('Wodnik', '1900/1/20', '1900/2/18'),
    ZodiacSign('Ryby', '1900/2/19', '1900/3/20'),
    ZodiacSign('Baran', '1900/3/21', '1900/4/19'),
    ZodiacSign('Byk', '1900/4/20', '1900/5/20'),
    ZodiacSign('Bliźnięta', '1900/5/21', '1900/6/21'),
    ZodiacSign('Rak', '1900/6/22', '1900/7/22'),
    ZodiacSign('Lew', '1900/7/23', '1900/8/22'),
    ZodiacSign('Panna', '1900/8/23', '1900/9/22'),
    ZodiacSign('Waga', '1900/9/23', '1900/10/22'),
    ZodiacSign('Skorpion', '1900/10/23', '1900/11/21'),
    ZodiacSign('Strzelec', '1900/11/22', '1900/12/21'),
    ZodiacSign('Koziorożec', '1900/12/22', '1901/1/19'),
]    


def get_sign(input):
    date = input
    for sign in ZODIAC_SIGNS:
        if sign.is_me(date):
            return sign.name


def print(x=None):
    if x:
        return logging.debug(f'▬▬▬ {x} ▬▬▬')
    return ('')
    