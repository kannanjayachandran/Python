import time
import pyotp as ptp

# setting a key
key = "ThisIsSecret"

# generating OTP from key
totp= ptp.TOTP(key)

print(f'The OTP is : {totp.now()}')

input_code = input("Enter 2 factor authentication code: ")

# checking if correct otp is entered or not
print(totp.verify(input_code))