from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#ボートに接続
vehicle = connect('127.0.0.1:14550', wait_ready=True, timeout=60)

while not vehicle.is_armable:
    print("初期化を待っています")
    time.sleep(1)

vehicle.mode = VehicleMode("GUIDED")

vehicle.armed = True

while not vehicle.armed:
    print("アームを待っています")
    time.sleep(1)

#ボートゴールへ行く
aLocation = LocationGlobalRelative(35.513507, 138.755462, 0)

vehicle.simple_goto(aLocation)

