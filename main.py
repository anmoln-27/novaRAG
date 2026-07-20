from discovery.parser import DiscoveryEngine
from agents.attack_strategy_agent import AttackStrategyAgent
from agents.hacker_agent import HackerAgent
from agents.critic_agent import analyze_result
from agents.attack_history import AttackHistory
from executor.executor import execute_attack
from reports.report_generator import ReportGenerator

import json
import os
import time

print("\n========== NOVARAG START ==========\n")

# ------------------------------------
# Initialize Components
# ------------------------------------
discovery = DiscoveryEngine()
strategy_agent = AttackStrategyAgent()
hacker = HackerAgent()
history = AttackHistory()
report_generator = ReportGenerator()

# ------------------------------------
# Discover APIs
# ------------------------------------
routes = discovery.discover_routes()

print("\n========== DISCOVERED ROUTES ==========\n")

for route in routes:
    print(route)

# ------------------------------------
# Generate Attack Strategy
# ------------------------------------
strategy = strategy_agent.create_strategy(routes)

# Save strategy for dashboard
os.makedirs("reports", exist_ok=True)

with open("reports/strategy.json", "w") as file:
    json.dump(strategy, file, indent=4)

print("\n========== ATTACK STRATEGY ==========\n")
print(json.dumps(strategy, indent=4))

# ------------------------------------
# Scan Endpoints
# ------------------------------------

for endpoint_strategy in strategy["strategy"]:

    endpoint_path = endpoint_strategy["endpoint"]

    # Adaptive scan depth
    if endpoint_path == "/transfer":
        max_rounds = 3

    elif endpoint_path == "/login":
        max_rounds = 2

    else:
        max_rounds = 1

    print("\n" + "=" * 70)
    print(f"Scanning Endpoint: {endpoint_path}")
    print("=" * 70)

    target = None

    for route in routes:
        if route["path"] == endpoint_path:
            target = route
            break

    if target is None:
        print(f"Endpoint {endpoint_path} not found.")
        continue

    # ------------------------------------
    # Attack Loop
    # ------------------------------------

    for round_number in range(max_rounds):

        print(f"\n---------- Round {round_number + 1} ----------\n")

        previous = history.latest()

        attack = hacker.generate_attack(
            target,
            strategy,
            previous
        )

        print("Generated Attack:")
        print(json.dumps(attack, indent=4))

        result = execute_attack(attack)

        print("\nExecution Result:")
        print(json.dumps(result, indent=4))

        # ------------------------------------
        # Skip AI Critic if attack failed
        # ------------------------------------

        if not result.get("success", False):

            analysis = {
                "finding_status": "Execution Failed",
                "confidence": 0,
                "severity": "None",
                "vulnerability_found": False,
                "business_impact": "Attack execution failed.",
                "recommendation": "Verify payload or supported HTTP method.",
                "next_attack": None
            }

        else:

            analysis = analyze_result(result)

        print("\nCritic Analysis:")
        print(json.dumps(analysis, indent=4))

        history.add(
            attack,
            result,
            analysis
        )

        if analysis.get("vulnerability_found"):

            print("\n🔴 Confirmed Vulnerability")

        elif analysis.get("finding_status") == "Potential Vulnerability":

            print("\n🟡 Potential Vulnerability")

        elif analysis.get("finding_status") == "Execution Failed":

            print("\n⚪ Execution Failed")

        else:

            print("\n🟢 No Vulnerability")

        # Prevent Gemini rate limiting
        time.sleep(2)

# ------------------------------------
# Print Attack History
# ------------------------------------

print("\n========== ATTACK HISTORY ==========\n")

for i, attack_round in enumerate(history.all()):

    print(f"\nRound {i + 1}")
    print(json.dumps(attack_round, indent=4))

# ------------------------------------
# Generate Security Report
# ------------------------------------

report = report_generator.generate(history.all())

summary = report["executive_summary"]

print("\n=========================================")
print("         NOVARAG SCAN SUMMARY")
print("=========================================\n")

print(f"Application            : {summary['application']}")
print(f"Scan Status            : {summary['scan_status']}")
print(f"Endpoints Tested       : {summary['endpoints_tested']}")
print(f"Attacks Executed       : {summary['attacks_executed']}")

print()

print(f"Confirmed Findings     : {summary['confirmed_findings']}")
print(f"Potential Findings     : {summary['potential_findings']}")
print(f"Total Findings         : {summary['total_findings']}")

print()

print(f"Overall Risk           : {summary['overall_risk']}")

print()

print("Security Report")
print("------------------------------")
print("reports/security_report.json")

print("\n=========================================")
print("      NOVARAG SCAN COMPLETE")
print("=========================================\n")