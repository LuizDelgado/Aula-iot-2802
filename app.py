#O objetivo dessa aplicação é fazer a requisição de data e hora e exibir na tela

#Importar as bibliotecas
from flask import Flask, render_template #Funcionalidades do flask
from datetime import datetime #Requisição de dia e hora do sistema

#Criar o nosso aplicativo Flask
app = Flask(__name__)

#Rota de consulta da api - NOMEDOSITE.COM/
@app.route('/')
def main():
    #Lógica de captura de data e hora
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    return render_template('index.html', time=current_time)

#Funcionalidade
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)