from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    is_started = True
    leha = {'name': 'Пидор'}
    return render_template('home.html', leha=leha, is_started=is_started)


@app.route('/car/<id>', methods=['GET', 'POST'])
def car(id):
    if request.method == 'GET':
        pass
    else:
        # Найти нужную машину по ID car = Car.query.filter_by(id=id).first()
        #                              таблица в бд         в бд    переменная
        data = request.data()  # помещаем данные из запроса
        data = request.get_json()
        data['модель']  # обращение к json

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        data = request.values
        return 'Я ПОССАЛ', 200
    else:
        return 'Я ОБОСРАЛСЯ'