import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class AttackStrategyAgent:

    def create_strategy(self, routes):

        prompt = f"""
You are the Planning Agent of novaRAG.

Your task is to prioritize API endpoints for penetration testing.

==============================
DISCOVERED ENDPOINTS
==============================

{json.dumps(routes, indent=2)}

==============================
RULES
==============================

Prioritize endpoints in this order:

1. Financial transactions
2. Authentication endpoints
3. User management
4. Administrative endpoints
5. Public informational endpoints

Financial endpoints should ALWAYS receive the highest priority.

Public endpoints should ALWAYS receive the lowest priority.

For every endpoint include:

- endpoint
- priority
- attack_goal
- reason

Return ONLY JSON.

Example:

{{
    "strategy":[
        {{
            "endpoint":"/transfer",
            "priority":1,
            "attack_goal":"Business Logic Abuse",
            "reason":"Financial transaction endpoint."
        }},
        {{
            "endpoint":"/login",
            "priority":2,
            "attack_goal":"Authentication Bypass",
            "reason":"Authentication endpoint."
        }},
        {{
            "endpoint":"/",
            "priority":3,
            "attack_goal":"Information Disclosure",
            "reason":"Public endpoint."
        }}
    ]
}}
"""

        try:

            response = client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=prompt
            )

            strategy = json.loads(response.text)

            return strategy

        except Exception as e:

            print(f"Strategy Agent unavailable: {e}")
            print("Using heuristic strategy...")

            strategy = []

            for route in routes:

                path = route["path"].lower()

                if "transfer" in path:

                    strategy.append({
                        "endpoint": route["path"],
                        "priority": 1,
                        "attack_goal": "Business Logic Abuse",
                        "reason": "Financial transaction endpoint."
                    })

                elif "login" in path:

                    strategy.append({
                        "endpoint": route["path"],
                        "priority": 2,
                        "attack_goal": "Authentication Bypass",
                        "reason": "Authentication endpoint."
                    })

                else:

                    strategy.append({
                        "endpoint": route["path"],
                        "priority": 3,
                        "attack_goal": "Information Disclosure",
                        "reason": "Public endpoint."
                    })

            strategy.sort(key=lambda x: x["priority"])

            return {
                "strategy": strategy
            }