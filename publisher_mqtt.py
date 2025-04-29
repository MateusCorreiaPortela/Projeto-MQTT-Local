import paho.mqtt.client as mqtt
import json
import time


mensagem_dispositivo = {
    "ID": "HA1U2E4OA",
    "data": "2025-04-24 11:57:03",
    "relogio": 2548,
    "vazao_instantanea": 2.14
    }

dispositivo = mqtt.Client(client_id='Dispositivo')
dispositivo.connect('localhost')
dispositivo.loop_start()
dispositivo.publish('topico1', json.dumps(mensagem_dispositivo))

time.sleep(10)
dispositivo.loop_stop()

