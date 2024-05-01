from fastapi import FastAPI
from pydantic import BaseModel, Field
from loguru import logger
import serial  # This is the "pyserial" package

app = FastAPI()

class GlobalOptArgs(BaseModel):
    uart_p: str = '/dev/ttyACM0'
    baudrate: int = 115200
    uart_timeout: int = 1


def loop_forever(S):
    cnt=0
    logger.info(S)
    while (True):
        cnt = cnt + 1
        ln = S.readline()
        print("%d: %s" % (cnt, ln))

        
if __name__ == '__main__':
    logger.info("Main")
    Args = GlobalOptArgs()
    logger.info(Args)
    S = serial.Serial(Args.uart_p, Args.baudrate, timeout=Args.uart_timeout)
    loop_forever(S)
    #S = serial.Serial(Args.uart_p, Args.baudrate, Args.uart_timeout)
    #S = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
 
