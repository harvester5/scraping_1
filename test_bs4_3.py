from bs4 import BeautifulSoup
import sqlite3 as lite
# эта версия для BADOO

# Функция открытия изображения в бинарном режиме
def readImage(filename):
    try:
        fin = open(filename, "rb")
        img = fin.read()
        return img

    except IOError as e:
        # В случае ошибки, выводим ее текст
        print( "Error %d: %s" % (e.args[0], e.args[1]) )
        sys.exit(1)
    finally:
        if fin:
            fin.close()


def saveData(l_name, l_age, l_town, l_foto):
    con = lite.connect('lovers.db')
    cur = con.cursor()

    data = readImage(l_foto)
    # Конвертируем данные
    binary = lite.Binary(data)

    cur.execute('SELECT * FROM lovers')
    idx = len(cur.fetchall())
    cur.execute('INSERT INTO lovers(id, name, age, town, foto) VALUES(?, ?, ?, ?, ?)', (idx, l_name, l_age, l_town, binary))
    con.commit()
    con.close()

with open("E:/Python/sites/Badoo.html", encoding="utf-8") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

#    print(soup.h2)
#    print(soup.head)
#    print(soup.li)
    divs =  soup.find_all("div", {"class" : "users-list__cell"})
#    divs = soup.findAll('div')
    for divx in divs:
           tempStr = str(divx)
           l_name = tempStr[132:tempStr.find(" - ")]
#           print(tempStr.find("Хочет"))
           print(l_name)
           posylka = l_name.split(',')
           #сейчас найдем страничку таинственного незнакомца
           l_site = tempStr[tempStr.find('a class="user-card__link app" href=')+36:tempStr.find('rel="profile-view"')-2]
#           saveData(posylka[0],posylka[1], posylka[2], "e:/test.bmp")
           print(tempStr)
