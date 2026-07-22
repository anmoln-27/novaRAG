[
  {
    "id": "atk_1042",
    "timestamp": "2026-07-15T09:41:12Z",
    "hacker": {
      "endpoint": "/transfer",
      "method": "POST",
      "payload": { "sender": "alice", "receiver": "bob", "amount": -1000 },
      "reason": "Negative transfer test — checks whether the API rejects negative amounts before debiting the sender."
    },
    "executor": {
      "success": true,
      "endpoint": "/transfer",
      "status_code": 200,
      "response": { "message": "Transfer Successful", "sender_balance": -500, "receiver_balance": 2000 },
      "response_time_seconds": 0.008
    },
    "critic": {
      "vulnerability_found": true,
      "severity": "High",
      "type": "Business Logic Vulnerability",
      "description": "Transfer allowed sender balance to become negative."
    }
  },
  {
    "id": "atk_1041",
    "timestamp": "2026-07-15T09:38:47Z",
    "hacker": {
      "endpoint": "/transfer",
      "method": "POST",
      "payload": { "sender": "alice", "receiver": "bob", "amount": 999999999 },
      "reason": "Large transfer amount test — checks for integer overflow or missing upper-bound validation."
    },
    "executor": {
      "success": true,
      "endpoint": "/transfer",
      "status_code": 200,
      "response": { "message": "Transfer Successful", "sender_balance": -999999499, "receiver_balance": 1000001999 },
      "response_time_seconds": 0.011
    },
    "critic": {
      "vulnerability_found": true,
      "severity": "Critical",
      "type": "Business Logic Vulnerability",
      "description": "No upper bound on transfer amount allowed an unrealistic balance to be created."
    }
  },
  {
    "id": "atk_1040",
    "timestamp": "2026-07-15T09:35:03Z",
    "hacker": {
      "endpoint": "/transfer",
      "method": "POST",
      "payload": { "sender": "alice", "receiver": "alice", "amount": 500 },
      "reason": "Self-transfer test — checks whether transferring to yourself is handled safely."
    },
    "executor": {
      "success": true,
      "endpoint": "/transfer",
      "status_code": 200,
      "response": { "message": "Transfer Successful", "sender_balance": 1000, "receiver_balance": 1000 },
      "response_time_seconds": 0.006
    },
    "critic": {
      "vulnerability_found": false,
      "severity": "Low",
      "type": "Business Logic Vulnerability",
      "description": "Self-transfer left balance unchanged as expected — no issue found."
    }
  },
  {
    "id": "atk_1039",
    "timestamp": "2026-07-15T09:30:55Z",
    "hacker": {
      "endpoint": "/login",
      "method": "POST",
      "payload": { "username": "admin' OR '1'='1", "password": "x" },
      "reason": "SQL injection probe against the login form's username field."
    },
    "executor": {
      "success": true,
      "endpoint": "/login",
      "status_code": 401,
      "response": { "message": "Invalid credentials" },
      "response_time_seconds": 0.014
    },
    "critic": {
      "vulnerability_found": false,
      "severity": "Low",
      "type": "Injection",
      "description": "Login correctly rejected the injection payload with a 401."
    }
  },
  {
    "id": "atk_1038",
    "timestamp": "2026-07-15T09:26:19Z",
    "hacker": {
      "endpoint": "/transfer",
      "method": "POST",
      "payload": { "sender": "bob", "receiver": "unknown_user", "amount": 250 },
      "reason": "Nonexistent receiver test — checks whether transfers to unknown accounts are validated."
    },
    "executor": {
      "success": true,
      "endpoint": "/transfer",
      "status_code": 200,
      "response": { "message": "Transfer Successful", "sender_balance": 750, "receiver_balance": 250 },
      "response_time_seconds": 0.009
    },
    "critic": {
      "vulnerability_found": true,
      "severity": "Medium",
      "type": "Business Logic Vulnerability",
      "description": "Transfer succeeded to a receiver account that does not appear to be validated as existing."
    }
  },
  {
    "id": "atk_1037",
    "timestamp": "2026-07-15T09:20:41Z",
    "hacker": {
      "endpoint": "/transfer",
      "method": "POST",
      "payload": { "sender": "bob", "receiver": "alice", "amount": 0 },
      "reason": "Zero-amount transfer test — checks whether zero-value transfers are rejected."
    },
    "executor": {
      "success": true,
      "endpoint": "/transfer",
      "status_code": 200,
      "response": { "message": "Transfer Successful", "sender_balance": 1000, "receiver_balance": 2000 },
      "response_time_seconds": 0.007
    },
    "critic": {
      "vulnerability_found": false,
      "severity": "Low",
      "type": "Business Logic Vulnerability",
      "description": "Zero-value transfer had no material effect — informational only."
    }
  }
]
