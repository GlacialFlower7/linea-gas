from web3 import Web3
import time
import winsound

GAS_THRESHOLD = 2.3
alarm = False
linea = Web3(Web3.HTTPProvider('https://rpc.linea.build'))

while True:
    assert linea.is_connected()
    gas_price = linea.eth.gas_price / 1e9
    print('current gas cost:\t', gas_price) 
    if gas_price < GAS_THRESHOLD:
        if not alarm: 
            alarm = True 
            i = 0
            while i < 3: # play the alarm three times
                winsound.Beep(440, 90)
                winsound.Beep(220, 90)
                winsound.Beep(220, 90)
                winsound.Beep(440, 90)
                winsound.Beep(440, 90)
                time.sleep(0.27)
                i+=1
    else: 
        alarm = False
    time.sleep(10) 
