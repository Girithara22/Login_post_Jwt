from fastapi import FastAPI,HTTPException
from datetime import datetime,timedelta
from jose import jwt,JWTError
import uvicorn

Alogorthm = "HS256"
Access_scode_time =5
Secret_code="gl23"

app = FastAPI()

def create_token(uname:str):
  expire = datetime.utcnow()+timedelta(minutes=Access_scode_time)
  payload={"username":uname,"expire":expire} 
  return jwt.encode(payload,Secret_code,Alogorthm)
  

def verify_token(token:str): 
  try:
    payload=jwt.decode(token,Secret_code,algorithms={Alogorthm})
    return payload["username"]
  except JWTError:
    raise HTTPException(status_code=400,detail="invalid token")
  pass

@app.post('/login')
def login(uname:str,password:str):
   if uname=="admin" and password=="123g":
    token=create_token(uname)
    return {"acess token":token} 
   return HTTPException(status_code=400,detail="invalid")

@app.get('/secure_data')
def set_data(token:str):
  uname=verify_token(token)
  return{"message":f"hello{uname},this is encrypted"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
