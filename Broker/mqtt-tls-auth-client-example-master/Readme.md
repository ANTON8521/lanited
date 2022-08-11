
/PCB/CELL-01/UR3E-01/REGIN
<Tarea Robot (Int)> | <Inicia Tarea (Bool)> | <Permiso a Robot (Bool)> | <Confirmación (Bool)>

/PCB/CELL-01/UR3E-01/REGOUT
<Tarea Seleccionada (Int)> |  <Zona Robot (Int)> | <Permiso de Plc (Bool)> | <Confirmacion de Plc (Bool)>

/PCB/CELL-01/UR3E-01/REGSENSE


Requirements: python 3.8.x

python3 -m pip install -r requirements.txt

python3 auth-encript-mqtt-client-publish.py

python3 auth-encript-mqtt-client-subscribe.py