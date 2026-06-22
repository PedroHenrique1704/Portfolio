from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="phcf1704",
        database="bdcrud"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT nome_produto, valor FROM vendas')
    vendas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', vendas=vendas)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome_produto = request.form['nome_produto']
        valor = request.form['valor']
        conn = get_db_connection()
        cursor = conn.cursor()
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
        cursor.execute(comando)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<string:nome_produto>', methods=['GET', 'POST'])
def update(nome_produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        novo_valor = request.form['valor']
        comando = f'UPDATE vendas SET valor = {novo_valor} WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conn.commit()
        print(f"Updated: {comando}")
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute(f'SELECT nome_produto, valor FROM vendas WHERE nome_produto = "{nome_produto}"')
    venda = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update.html', venda=venda)

@app.route('/update_name/<string:nome_produto>', methods=['GET', 'POST'])
def update_name(nome_produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        novo_nome = request.form['nome_produto']
        comando = f'UPDATE vendas SET nome_produto = "{novo_nome}" WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conn.commit()
        print(f"Updated name: {comando}")
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute(f'SELECT nome_produto, valor FROM vendas WHERE nome_produto = "{nome_produto}"')
    venda = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_name.html', venda=venda)

@app.route('/delete/<string:nome_produto>')
def delete(nome_produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conn.commit()
    print(f"Deleted: {comando}")
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
