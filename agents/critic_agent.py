import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def analyze_result(result):

    # -------------------------------
    # Executor failed
    # -------------------------------

    if not result.get("success", False):

        return {
            "finding_status": "Execution Failed",
            "confidence": 0,
            "severity": "None",
            "vulnerability_found": False,
            "owasp_category": None,
            "business_impact": "Attack could not be executed.",
            "recommendation": "Verify the generated payload or supported HTTP method.",
            "next_attack": None
        }

    prompt = f"""
You are an expert Application Security Engineer.

Analyze the API execution result.

==============================
API RESULT
==============================

{json.dumps(result, indent=2)}

==============================
YOUR TASK
==============================

Determine whether this execution indicates:

1. Confirmed Vulnerability
2. Potential Vulnerability
3. No Vulnerability

Only classify as Confirmed if the evidence is conclusive.

If the response is simply HTTP 500,
classify it as Potential Vulnerability unless exploitation is proven.

Choose ONLY ONE OWASP category from:

- A01:2021-Broken Access Control
- A02:2021-Cryptographic Failures
- A03:2021-Injection
- A04:2021-Insecure Design
- A05:2021-Security Misconfiguration
- A06:2021-Vulnerable Components
- A07:2021-Authentication Failures
- A08:2021-Integrity Failures
- A09:2021-Logging Failures
- A10:2021-SSRF

Return ONLY JSON.

Example:

{{
    "finding_status":"Potential Vulnerability",
    "confidence":84,
    "severity":"Medium",
    "vulnerability_found":false,
    "owasp_category":"A05:2021-Security Misconfiguration",
    "business_impact":"Unexpected server failure may indicate improper validation.",
    "recommendation":"Validate all user input and improve exception handling.",
    "next_attack":"Try boundary value testing."
}}
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        analysis = json.loads(response.text)

        return analysis

    except Exception as e:

        print(f"Critic Gemini unavailable: {e}")
        print("Using heuristic critic...")

        status = result.get("status_code", 0)

        if status >= 500:

            return {
                "finding_status": "Potential Vulnerability",
                "confidence": 70,
                "severity": "Medium",
                "vulnerability_found": False,
                "owasp_category": "A05:2021-Security Misconfiguration",
                "business_impact": "Unexpected server error occurred during attack execution.",
                "recommendation": "Review exception handling and input validation.",
                "next_attack": "Test additional malformed payloads."
            }

        elif status == 401:

            return {
                "finding_status": "No Vulnerability",
                "confidence": 95,
                "severity": "None",
                "vulnerability_found": False,
                "owasp_category": None,
                "business_impact": "Authentication controls behaved correctly.",
                "recommendation": "Continue testing with alternative authentication attacks.",
                "next_attack": "Attempt SQL Injection or JWT manipulation."
            }

        elif status == 403:

            return {
                "finding_status": "No Vulnerability",
                "confidence": 95,
                "severity": "None",
                "vulnerability_found": False,
                "owasp_category": None,
                "business_impact": "Access control prevented the request.",
                "recommendation": "Attempt privilege escalation scenarios.",
                "next_attack": "Try BOLA testing."
            }

        elif status == 200:

            return {
                "finding_status": "No Vulnerability",
                "confidence": 80,
                "severity": "Low",
                "vulnerability_found": False,
                "owasp_category": None,
                "business_impact": "Request completed successfully.",
                "recommendation": "Attempt more advanced attack strategies.",
                "next_attack": "Test business logic edge cases."
            }

        else:

            return {
                "finding_status": "Potential Vulnerability",
                "confidence": 50,
                "severity": "Low",
                "vulnerability_found": False,
                "owasp_category": "A04:2021-Insecure Design",
                "business_impact": "Unexpected API behavior observed.",
                "recommendation": "Investigate application behavior.",
                "next_attack": "Perform additional fuzz testing."
            }