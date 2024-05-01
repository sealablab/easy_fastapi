from fastapi import FastAPI
from pydantic import BaseModel, Field
from loguru import logger
import serial  # This is the "pyserial" package

app = FastAPI()

class GlobalOptArgs(BaseModel):
    uart_p: str
    baudrate: int = 115200


def loop_forever(S):
    cnt=0
    while (True):
        cnt = cnt + 1
        ln = S.readline()
        print("%d: %s" % (cnt, ln))

        
if __name__ == '__main__':
    logger.info("Main")
    S = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    logger.info(f"--- Serial:{S}")
    S = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
 
