import paho.mqtt.client as mqtt
import time

broker = "broker.hivemq.com"
port = 1883
topic = "dispensador/medicamento"

client = mqtt.Client()
client.connect(broker, port, 60)

print("Publicador conectado...")

while True:
    mensaje = "medicamento_dispensado"
    client.publish(topic, mensaje)
    print("Enviado:", mensaje)
    time.sleep(5)
