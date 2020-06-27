from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def home():
    is_started = True
    car = {'name': 'ВАЗ-2110'}
    user = {'name': 'Бычков Алексей Андреевич'}
    return render_template('home.html', car=car, is_started=is_started, user=user)


@app.route('/parametrs')
def parametrs():
    parms = [{'name': 'Температура охлаждающей жидкости (°С)', 'value': '25'},
             {'name': 'Напряжение борт. сети (V)', 'value': '14.1'},
             {'name': 'Частота враащения кол. вала (об/мин)', 'value': '910'},
             {'name': 'Текущая скорость', 'value': '0'},
             {'name': 'Мгновенный расход (л/ч)', 'value': '0.8'},
             {'name': 'Мгновенный расход (л/км)', 'value': '0'},
             {'name': 'Средний расход (л/км)', 'value': '9.2'}]
    car = {'name': 'ВАЗ-2110'}
    user = {'name': 'Бычков Алексей Андреевич'}
    return render_template('parametrs.html', car=car, parms=parms, user=user)


@app.route('/errors')
def errors():
    is_started = True
    errors = [{'code': 'P1901', 'name': 'Ошибка электроцепи питания', 'date': '24.06.20202'},
              {'code': 'P1902', 'name': 'Не заводится', 'date': '25.06.20202'}]
    car = {'name': 'ВАЗ-2110'}
    user = {'name': 'Бычков Алексей Андреевич'}
    return render_template('errors.html', car=car, errors=errors, user=user)


@app.route('/car/<id>', methods=['GET', 'POST'])
def car(id):
    if request.method == 'GET':
        pass
    else:
        # Найти нужную машину по ID car = Car.query.filter_by(id=id).first()
        #                              таблица в бд         в бд    переменная
        data = request.data  # помещаем данные из запроса
        data = request.get_json()
        var = data['модель']  # обращение к json


@app.route('/stop-engine', methods=['GET', 'POST'])
def stop_engine():
    if request.method == 'GET':
        data = request.values
        return 'Я ПОССАЛ'
    else:
        return 'Я ОБОСРАЛСЯ'


@app.route('/start-engine', methods=['GET', 'POST'])
def start_engine():
    if request.method == 'GET':
        data = request.values
        return 'Я ПОССАЛ'
    else:
        return 'Я ОБОСРАЛСЯ'
