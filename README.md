# easy_fastapi

## Venv (initial setup)
``` sh
user@DevTerm1:~/easy_fastapi $ python3 -m venv .venv
user@DevTerm1:~/easy_fastapi $ . ./.venv/bin/activate
(.venv) user@DevTerm1:~/easy_fastapi $
```

### venv (activate)
``` sh
(.venv) user@DevTerm1:~/easy_fastapi $ which pip
/home/user/easy_fastapi/.venv/bin/pip
```
## dependencies
``` sh
pip install pydantic  
pip install "uvicorn[standard]"
pip install fastapi
```






``` sh
 uvicorn --reload main:app  --host 0.0.0.0 --port
```
Simple example of using fastapi
Most of this was taken from fastapi 


## pre_reqs
pip install uvicorn fastapi
## Running 
``` sh
user@box:~/easy_fastapi$ python3 ./main.py
```

