from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#コプターに接続
vehicle = connect('127.0.0.1:14570', wait_ready=True, timeout=60)

while not vehicle.is_armable:
    print("初期化を待っています")
    time.sleep(1)

vehicle.mode = VehicleMode("GUIDED")

vehicle.armed = True

while not vehicle.armed:
    print("アームを待っています")
    time.sleep(1)

targetAltitude=10

print("離陸します")

vehicle.simple_takeoff(targetAltitude)

while True:
    print("高度:", vehicle.location.global_relative_frame.alt)

    if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95:
        print("到達しました！")
        break

    time.sleep(1)

#コプターゴールへ行く
aLocation = LocationGlobalRelative(35.514063, 138.744247, 0)

vehicle.simple_goto(aLocation)

