import os
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class HackerAgent:

    def generate_attack(
        self,
        endpoint_info,
        strategy,
        previous_attempt=None
    ):

        # Previous attack history
        if previous_attempt:
            previous_context = json.dumps(previous_attempt, indent=2)
        else:
            previous_context = "No previous attacks."

        # Attack strategy
        strategy_context = json.dumps(strategy, indent=2)

        endpoint_path = endpoint_info["path"]
        endpoint_method = endpoint_info["method"]

        # -----------------------------------------------------
        # Endpoint-aware attack generation
        # -----------------------------------------------------

        if endpoint_path == "/login":

            endpoint_category = """
Authentication Endpoint

Focus on:

- SQL Injection
- Authentication Bypass
- Empty Password
- Default Credentials
- Credential Stuffing
- Username Enumeration
"""

            example_payload = """
{
    "endpoint": "/login",
    "method": "POST",
    "payload": {
        "username": "' OR '1'='1",
        "password": "password"
    },
    "reason": "SQL Injection authentication bypass"
}
"""

        elif endpoint_path == "/transfer":

            endpoint_category = """
Financial Transaction Endpoint

Focus on:

- Negative Amount
- Integer Overflow
- Business Logic Abuse
- BOLA
- Unauthorized Transfer
- Self Transfer
- Large Numbers
- Boundary Values
"""

            example_payload = """
{
    "endpoint": "/transfer",
    "method": "POST",
    "payload": {
        "sender": "alice",
        "receiver": "bob",
        "amount": -1000
    },
    "reason": "Negative amount business logic attack"
}
"""

        else:

            endpoint_category = """
Public Endpoint

Focus on:

- Information Disclosure
- Header Enumeration
- Unexpected Parameters
- Cache Poisoning
"""

            example_payload = f"""
{{
    "endpoint":"{endpoint_path}",
    "method":"GET",
    "payload":{{}},
    "reason":"Information disclosure test"
}}
"""

        # -----------------------------------------------------
        # Gemini Prompt
        # -----------------------------------------------------

        prompt = f"""
You are novaRAG's Autonomous AI Penetration Tester.

Your job is to intelligently attack APIs based on endpoint type.

==================================================
TARGET ENDPOINT
==================================================

{json.dumps(endpoint_info, indent=2)}

==================================================
ENDPOINT CATEGORY
==================================================

{endpoint_category}

==================================================
ATTACK STRATEGY
==================================================

{strategy_context}

==================================================
PREVIOUS ATTEMPT
==================================================

{previous_context}

==================================================
IMPORTANT RULES
==================================================

Generate ONLY ONE attack.

Allowed HTTP Method:

{endpoint_method}

Never generate:

- OPTIONS
- TRACE
- CONNECT
- PATCH

Use ONLY:

{endpoint_method}

If the endpoint is GET,
generate a GET attack.

If the endpoint is POST,
generate a POST attack.

Generate a NEW attack if the previous attempt failed.

Do NOT repeat previous payloads.

Focus on business logic instead of simple syntax attacks.

Return ONLY valid JSON.

Example:

{example_payload}
"""

        try:

            response = client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=prompt
            )

            attack = json.loads(response.text)

            # Ensure endpoint and method stay correct
            attack["endpoint"] = endpoint_path
            attack["method"] = endpoint_method

            return attack

        except Exception as e:

            print(f"Gemini unavailable: {e}")
            print("Using fallback payload...")

            if endpoint_path == "/transfer":

                return {
                    "endpoint": "/transfer",
                    "method": "POST",
                    "payload": {
                        "sender": "alice",
                        "receiver": "bob",
                        "amount": -1000
                    },
                    "reason": "Fallback negative transfer attack"
                }

            elif endpoint_path == "/login":

                return {
                    "endpoint": "/login",
                    "method": "POST",
                    "payload": {
                        "username": "' OR '1'='1",
                        "password": "password"
                    },
                    "reason": "Fallback SQL Injection attack"
                }

            else:

                return {
                    "endpoint": endpoint_path,
                    "method": "GET",
                    "payload": {},
                    "reason": "Fallback information disclosure test"
                }