from phones_numbers import book_phones
from engine import get_data, make_action

r = True
while r:
    r = make_action(get_data(), book_phones)
    print(r)
