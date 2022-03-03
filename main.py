import json
import serial

serialPort = serial.Serial(port="/dev/ttyUSB0",
                           baudrate=9600,
                           bytesize=8,
                           timeout=2,
                           stopbits=serial.STOPBITS_ONE)


data = serialPort.readline()
data = str(data)
datalist = data.split(",")
second_data = datalist

second_dataframe = {
    'litreperminute': float(second_data[4]),
}

print(json.dumps(second_dataframe, indent=2))