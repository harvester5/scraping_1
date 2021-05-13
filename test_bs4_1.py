from bs4 import BeautifulSoup
import sqlite3 as lite
# эта версия для MAMBA

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

with open("E:/Python/sites/mamba.html", encoding="utf-8") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    divs = soup.findAll("div",{"class":"sc-1pkcrix-16 eheMUG"})
    for divx in divs:
#        print(divx)
        tempStr = str(divx)
        l_url = tempStr[140:tempStr.find("sc-1pkcrix-11")-14]
        l_name = tempStr[tempStr.find("img alt") + 9 :tempStr.find("sc-1pkcrix-13") - 9]
        l_age = tempStr[tempStr.find("item-title-age") + 16 : tempStr.find("sc-1pkcrix-18") - 22]
#        print(tempStr.find("Хочет"))
        print(tempStr)
        print(l_name)
        print(l_url)
        print(l_age)
#            posylka = l_name.split(',')
#            #сейчас найдем страничку таинственного незнакомца
#            l_site = tempStr[tempStr.find('a class="user-card__link app" href=')+36:tempStr.find('rel="profile-view"')-2]
# #           saveData(posylka[0],posylka[1], posylka[2], "e:/test.bmp")
#            print(tempStr)
