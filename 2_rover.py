from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#ローバーに接続
vehicle = connect('127.0.0.1:14560', wait_ready=True, timeout=60)

while not vehicle.is_armable:
    print("初期化を待っています")
    time.sleep(1)

vehicle.mode = VehicleMode("GUIDED")

vehicle.armed = True

while not vehicle.armed:
    print("アームを待っています")
    time.sleep(1)

#ローバーゴールへ行く
aLocation = LocationGlobalRelative(35.511500, 138.753830, 0)

vehicle.simple_goto(aLocation)

