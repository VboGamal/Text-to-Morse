from morse3 import Morse
import time


header = """
  __  __                            _____                                _              
 |  \/  |                          / ____|                              | |             
 | \  / |  ___   _ __  ___   ___  | |      ___   _ __ __   __ ___  _ __ | |_  ___  _ __ 
 | |\/| | / _ \ | '__|/ __| / _ \ | |     / _ \ | '_ \\ \ / // _ \| '__|| __|/ _ \| '__|
 | |  | || (_) || |   \__ \|  __/ | |____| (_) || | | |\ V /|  __/| |   | |_|  __/| |   
 |_|  |_| \___/ |_|   |___/ \___|  \_____|\___/ |_| |_| \_/  \___||_|    \__|\___||_|   
                                                                                        
"""
print(header)

text = input("Please Enter a Text to Encode: ")

morse_code = Morse(text).stringToMorse()

time.sleep(1)
print("[+] Converting ....")
time.sleep(1)
print("[+] Sending ....")
time.sleep(1)
print("[+] Done")
print(f"your Morse code is :{morse_code}")
