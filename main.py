import random
from openpyxl import Workbook
from openpyxl import *

x = 10
a = 0
r = 1
Col_Phrase = int(input("Какая последняя цифра вашей таблицы?: "))

c = random.randint(3, Col_Phrase)

list = load_workbook('Phrase.xlsx')

sheet = list.get_sheet_by_name('Лист1')

while a != x:
    a = a + 1
    print(str(r) + ". " + str(sheet["C" + str(c)].value))
    r += 1
    c = random.randint(3, Col_Phrase)