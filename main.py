import datetime
import sys
import requests
from pprint import pprint
from PyQt5 import QtWidgets
from translate import Translator
from weath import Ui_MainWindow


class Weather(QtWidgets.QMainWindow):
    def __init__(self):
        super(Weather, self).__init__()
        self.weath = Ui_MainWindow()
        self.weath.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.weath.pushButton.clicked.connect(self.getWeather)

    def getWeather(self):
        city = self.weath.lineEdit.text()
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=67e5d475c1b83b139ca15616b1855968&units=metric'.format(city)
            res = requests.get(url)
            data = res.json()
            now = datetime.datetime.now()

            pprint(data)

            temp = str(round(data['main']['temp'])) + '°'
            temp_feels = str(round(data['main']['feels_like'])) + '°'
            wind_speed = str(round(data['wind']['speed'])) + ' м/с'
            humidity = str(round(data['main']['humidity'])) + '%'
            weather = str(translator.translate(data['weather'][0]['description']).capitalize())
            d = str(day_week[now.weekday()]) + ', ' + str(now.day) + ' ' + str(month[now.month])

            self.weath.label_city.setText(city)
            self.weath.label_temp.setText(temp)
            self.weath.label_feels.setText(temp_feels)
            self.weath.label_humidity.setText(humidity)
            self.weath.label_one.setText('Ощущается:')
            self.weath.label_two.setText('Скорость ветра:')
            self.weath.label_three.setText('Влажность:')
            self.weath.label_weather.setText((data['weather'][0]['description']).capitalize())
            self.weath.label_wind_speed.setText(wind_speed)
            self.weath.label_time.setText(now.strftime("%H:%M"))
            self.weath.label_date.setText(d)

            print(data['weather'][0]['description'] + ' - ' + weather)
        except:
            self.weath.label_city.setText('Ошибка')


app = QtWidgets.QApplication([])
application = Weather()
application.show()

translator = Translator(from_lang="English", to_lang="Russian")

day_week = {0: 'ПН', 1: 'ВТ', 2: 'СР', 3: 'ЧТ', 4: 'ПТ', 5: 'СБ', 6: 'ВС'}
month = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа",
         9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}

sys.exit(app.exec())
