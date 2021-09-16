import time

angle2 = 115
speed_L = 900
speed_R = 900


def remap_range(
    val: float,
    old_min: float,
    old_max: float,
    new_min: float,
    new_max: float,
) -> float:

    old_span: float = old_max - old_min
    new_span: float = new_max - new_min
    new_val: float = new_min + new_span * (float(val - old_min) / float(old_span))

    return new_val


def angle(x_dif):
    global angle2

    if x_dif > 50:
        angle2 += 5
    elif x_dif < -50:
        angle2 -= 5
    return angle2


def motor(angle):
    global speed_L, speed_R
    speed_L = 900
    speed_R = 900

    if angle > 90:
        speed_L = remap_range(angle2, 90, 140, 900, 1000)
    else:
        speed_R = remap_range(angle2, 40, 90, 1000, 900)

time.sleep(5)

for i in range(23):
    print("===== Surveillance Mode =====")
    time.sleep(0.8)

print("===== Person is Detected =====")
time.sleep(2.67)
print("Latitude = 36.613878 & Longitude = 126.384706")

# ==========
print("===== Tracking Mode =====")
x_dif = 267
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 186
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 14
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -67
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -107
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -316
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -367
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -394
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -386
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -274
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -302
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -245
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -168
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -66
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -33
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 26
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 132
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 242
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 183
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 55
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 15
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 77
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -39
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -53
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 96
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 39
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -16
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -49
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -66
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -5
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 83
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 99
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -51
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 36
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -56
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -103
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -54
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 39
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 53
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -96
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = 109
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -94
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

print("===== Tracking Mode =====")
x_dif = -93
print("x_dif: " + str(x_dif))
print("angle: " + str(angle(x_dif)))
print("speed_L: " + str(speed_L) + " & speed_R: " + str(speed_R))
time.sleep(0.69)
motor(angle2)

# ==========

print("===== Person is Touched =====")
time.sleep(2.67)
print("Latitude = 36.613899 & Longitude = 126.384607")
print("coming home...")
time.sleep(24)
print("===== Boat is at home =====")

for i in range(25):
    print("===== Surveillance Mode =====")
    time.sleep(0.8)