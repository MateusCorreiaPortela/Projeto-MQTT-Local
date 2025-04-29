import pika
import json
from pymongo import MongoClient


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila1')
channel.exchange_declare(exchange='exchange1')

channel.queue_bind(exchange='exchange1', queue='fila1', routing_key='chave1')

client = MongoClient("mongodb://localhost:27017")
db = client["banco"]
colecao = db["mensagens"]


def callback(ch,method,properties,body):
    try:
        mensagem = json.loads(body)
        colecao.insert_one(mensagem)
        connection.close

    except:
        print('Erro')
    

channel.basic_consume(queue='fila1', on_message_callback=callback, auto_ack=True)

try:
    channel.start_consuming()
    print('Consumo feito com sucesso!')

except:
    print('Consumo Interrompido')
    connection.close