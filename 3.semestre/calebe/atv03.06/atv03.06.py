from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'root', 
    'password': '',
    'database': 'localiza'
}

def get_db():
    return mysql.connector.connect(**db_config)


@app.route('/reservar', methods=['POST'])
def reservar():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    
    query = "INSERT INTO reservas (id_cliente, id_veiculo, data_reserva) VALUES (%s, %s, %s)"
    cursor.execute(query, (data['id_cliente'], data['id_veiculo'], data['data_reserva']))
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Veículo reservado com sucesso!"}), 201

@app.route('/veiculos', methods=['GET'])
def listar_veiculos():
    conn = get_db()
    cursor = conn.cursor(dictionary=True) # dictionary=True ajuda a formatar como JSON
    cursor.execute("SELECT * FROM veiculos")
    veiculos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(veiculos)


@app.route('/cancelar/<int:id_veiculo>', methods=['DELETE'])
def cancelar(id_veiculo):
    conn = get_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM reservas WHERE id_veiculo = %s"
    cursor.execute(query, (id_veiculo,))
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Reserva cancelada e veículo liberado!"}), 200

if __name__ == '__main__':
    app.run(debug=True)