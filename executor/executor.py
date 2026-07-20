import requests
import json
import time
import os

BASE_URL = "http://127.0.0.1:8080"


def execute_attack(attack):

    endpoint = attack["endpoint"]
    method = attack["method"].upper()
    payload = attack.get("payload", {})

    url = BASE_URL + endpoint

    start_time = time.time()

    try:

        if method == "POST":
            response = requests.post(
                url,
                json=payload,
                timeout=10
            )

        elif method == "GET":
            response = requests.get(
                url,
                params=payload,
                timeout=10
            )

        elif method == "PUT":
            response = requests.put(
                url,
                json=payload,
                timeout=10
            )

        elif method == "DELETE":
            response = requests.delete(
                url,
                json=payload,
                timeout=10
            )

        else:

            return {
                "success": False,
                "endpoint": endpoint,
                "method": method,
                "payload": payload,
                "error": f"Unsupported HTTP method: {method}"
            }

        end_time = time.time()

        try:
            response_data = response.json()
        except Exception:
            response_data = response.text

        result = {
            "success": True,
            "endpoint": endpoint,
            "method": method,
            "payload": payload,
            "status_code": response.status_code,
            "response": response_data,
            "response_time_seconds": round(
                end_time - start_time,
                4
            )
        }

    except Exception as e:

        result = {
            "success": False,
            "endpoint": endpoint,
            "method": method,
            "payload": payload,
            "error": str(e)
        }

    # ------------------------------------
    # Save Execution Log
    # ------------------------------------

    os.makedirs("logs", exist_ok=True)

    with open(
        "logs/attack_log.json",
        "a"
    ) as file:

        json.dump(
            result,
            file,
            indent=4
        )

        file.write("\n\n")

    return result