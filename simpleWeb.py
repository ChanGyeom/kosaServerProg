from flask import Flask, request, render_template, jsonify, _app_ctx_stack
import sqlite3

'''
CREATE TABLE appdata (
    id INTEGER AUTO_INCREMENT,
    time datetime DEFAULT current_timestamp,
    kor INTEGER,
    math INTEGER,
    PRIMARY KEY(id)
)
'''

DATABASE = 'data.db'


app = Flask(__name__, static_folder='static', template_folder='template')

# 데이터베이스 열기
def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(DATABASE)
    return top.sqlite_db


# 데이터베이스 정리
@app.teardown_appcontext
def close_connection(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

@app.route('/reset' , methods=['POST'])
def reset():
    if request.is_json:
        data = request.get_json()
        pwd = data['API_KEY']
        if pwd == 'abc123':
            try:
                cur = get_db().cursor()
                cur.execute('DROP TABLE IF EXISTS appdata')
                cur.execute('CREATE TABLE appdata (id INTEGER AUTO_INCREMENT,time datetime DEFAULT current_timestamp,kor INTEGER, math INTEGER,PRIMARY KEY(id))')
                get_db().commit()
            except:
                get_db().rollback()
            return "Successfully reset"
        else :
            return "Fale reset"
    else:
        return "Fale request"


@app.route('/insert' , methods=['POST'])
def insert():
    if request.is_json:
        data = request.get_json()
        try:
            #if (data.get('kor'), data.get('math')):
                kor = data['kor']
                math = data['math']
                print(kor, math)
                
                cur = get_db().cursor()
                cur.execute('INSERT INTO appdata (kor, math) VALUES (?, ?)', (kor, math))
                get_db().commit()
                return jsonify(code=0)
            
        except:
            get_db().rollback()
            return jsonify(code=1)
    else:
        return "plz jason"

# 데이터베이스 처리 결과를 딕셔너리 형태로 반환
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/select')
def select():
    result = []
    try:
        get_db().row_factory = dict_factory
        cur = get_db().cursor()
        cur.execute('SELECT time, kor, math FROM appdata')
        result = cur.fetchall()
    except:
        get_db().rollback()
    return render_template('select.html', data = result)    

    
@app.route('/')
def hello():
    return 'Hello'

@app.route('/sample')
def sample():
    return render_template('sample.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    a = 0
    b = 0
    if request.method == 'GET':
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
    if request.method == 'POST':
        data = request.get_json()
        a = int(data['a'])
        b = int(data['b'])
        
    return str(a+b)
if __name__ == '__main__':
    app.run(
    host="127.0.0.1",
    port=7070,
    debug=True)
    


