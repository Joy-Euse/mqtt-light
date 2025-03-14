import paho.mqtt.client as mqtt

# MQTT broker details
broker = "broker.hivemq.com"  # Public broker
port = 1883
topic = "/student_group/light_control"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        client.subscribe(topic)
        print(f"📡 Subscribed to topic: {topic}")
    else:
        print(f"❌ Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    if payload == "ON":
        print("💡 Light is TURNED ON")
    elif payload == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"⚠️ Unknown command received: {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("🔌 Connecting to broker...")
client.connect(broker, port, 60)

client.loop_forever()
