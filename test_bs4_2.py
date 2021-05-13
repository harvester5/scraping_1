from bs4 import BeautifulSoup
import sqlite3 as lite
import locale
# эта версия для HOTLINE

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


def saveDataNotebook(l_name, l_age, l_town, l_foto):
    con = lite.connect('notebooks.db')
    cur = con.cursor()

    # data = readImage(l_foto)
    # binary = lite.Binary(data)

    cur.execute('SELECT * FROM notebooks')
    idx = len(cur.fetchall())
    cur.execute('INSERT INTO notebooks(id, name, price, info) VALUES(?, ?, ?, ?)', (idx, l_name, l_age, l_town))
    con.commit()
    con.close()

locale.setlocale(locale.LC_ALL,"Russian_Russia.1251")
with open("D:/Python/sites/hotline.html", encoding="utf-8") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
#    divs = soup.findAll("li",{"class":"product-item"})
#    divs = soup.findAll("div",{"class":"item-info"})
    divs = soup.findAll("p",{"class":"h4"})

    i=0
    for divx in divs:
#        print(divx)
        i+=1
        if (i==1) : continue

        # if tempStr.find("Смартфон") < 0 : continue
#        tempStr=divx[divx.find(">",15):divx.find(" </a>")]
        divz = divx.findAll("span class") #,{'class':'"value"'})
        print(divz)
        divy = str(divx)
        tempStr2 = divy[divy.find(">",15):divy.find(" </a>")]
        print("---------------------------------------------------------------------------------------------")
        print(tempStr2)
#        posylka = tempStr.split(chr(13))
#        print(posylka[1])
#            #сейчас найдем страничку таинственного незнакомца
#            l_site = tempStr[tempStr.find('a class="user-card__link app" href=')+36:tempStr.find('rel="profile-view"')-2]
# #           saveData(posylka[0],posylka[1], posylka[2], "e:/test.bmp")
#            print(tempStr)

