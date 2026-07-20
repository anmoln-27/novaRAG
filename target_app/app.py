from fastapi import FastAPI
from pydantic import BaseModel
from target_app.database import users

app = FastAPI(
    title="novaRAG Target Application",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to novaRAG Target Application"
    }


# ----------------------------------
# LOGIN
# ----------------------------------

class Login(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: Login):

    if data.username not in users:
        return {
            "success": False
        }

    if users[data.username]["password"] == data.password:

        return {
            "success": True,
            "role": users[data.username]["role"]
        }

    return {
        "success": False
    }


# ----------------------------------
# TRANSFER
# ----------------------------------

class Transfer(BaseModel):
    sender: str
    receiver: str
    amount: int


@app.post("/transfer")
def transfer(data: Transfer):

    # ----------------------------------
    # Intentionally vulnerable
    # ----------------------------------

    # Auto-create accounts if they don't exist
    # This prevents 500 errors while still
    # leaving the business logic vulnerable.

    if data.sender not in users:

        users[data.sender] = {
            "password": "password",
            "role": "user",
            "balance": 1000
        }

    if data.receiver not in users:

        users[data.receiver] = {
            "password": "password",
            "role": "user",
            "balance": 1000
        }

    # -----------------------------
    # BUSINESS LOGIC VULNERABILITY
    # -----------------------------
    #
    # No authorization check
    # No balance validation
    # No negative amount validation
    #
    # AI should discover this.

    users[data.sender]["balance"] -= data.amount
    users[data.receiver]["balance"] += data.amount

    return {
        "message": "Transfer Successful",
        "sender": data.sender,
        "receiver": data.receiver,
        "amount": data.amount,
        "sender_balance": users[data.sender]["balance"],
        "receiver_balance": users[data.receiver]["balance"]
    }