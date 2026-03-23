import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "dispensador/medicamento"

def on_message(client, userdata, message):
    print("Recibido:", message.payload.decode())

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, port, 60)
client.subscribe(topic)

print("Suscriptor esperando mensajes...")

client.loop_forever()
