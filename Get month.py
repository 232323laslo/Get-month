def get_month(language, number):
    lng_ua = ['січень', 'лютий', 'березень', 'квітень', 'травень', 'червень', 'липень', 'серпень', 'вересень', 'жовтень', 'листопад',
              'грудень']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']

    if lan == 'ua':
        return lng_ua[num - 1]
    elif lan == 'en':
        return lng_en[num - 1]

lan = input('Language en/ua: ')
num = int(input('Month number: '))
print(get_month(lan, num))
