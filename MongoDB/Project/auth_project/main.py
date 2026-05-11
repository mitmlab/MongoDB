from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from models import RegisterModel, LoginModel, ForgotPasswordModel
from auth import register_user, login_user, forgot_password

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

security = HTTPBearer()

# Home Route
@app.get("/")
def home():
    return {"message": "FastAPI MongoDB Auth Project"}

# Register API
@app.post("/register")
def register(data: RegisterModel):
    return register_user(data)

# Login API
@app.post("/login")
def login(data: LoginModel):
    return login_user(data)

# Forgot Password API
@app.put("/forgot-password")
def reset_password(data: ForgotPasswordModel):
    return forgot_password(data)

# Protected Route
@app.get("/profile")
def profile(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")

        return {
            "message": "Protected Route Accessed",
            "user": email
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
