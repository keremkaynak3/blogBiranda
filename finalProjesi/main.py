import sqlite3 as sql
from flask import Flask, render_template

import uPdates

app = Flask(__name__)
#try blocklarına göm mutlaka.
# SQLite veritabanı bağlantısı

db = sql.connect(r"C:\Users\MR. CAPH\Desktop\blog.db")
cursor = db.cursor()

# Ana ekranda görünecek olan ülkeleri veritabanından çekiyorum.
cursor.execute("SELECT ulke_adi, linkler, baskent, kodu, nufus, para_birimi, yerler, fotolar FROM ulkeler")
countries = cursor.fetchall()

# index.html ve country.html dosyalarımı main dosyamda çağırıyorum.
@app.route('/')
def index():
    return render_template('index.html', countries=countries)


@app.route('/country/<int:country_id>')
def country(country_id):
    # Seçilen ülkenin bilgilerini alıyorum.
    country_info = countries[country_id - 1] if 0 < country_id <= len(countries) else None

    # Eğer ülke bulunamazsa veya veri yoksa, hata mesajı gösteriyorum.
    if not country_info:
        return "Ülke bulunamadı!"

    return render_template('country.html', country=country_info)

print("Evet için 1: \nHayır için 2:")
secim = int(input("Yeni bir veri girecek misin?:"))

if secim==1:
    a = uPdates.uPdates()
    a.add_Country()
    a.add_Country()

if secim==2:
    print("İşte Web sitesi:")

if __name__ == '__main__':
    app.run(debug=True)

db.close()



