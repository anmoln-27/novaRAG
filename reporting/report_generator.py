import json
import os
from datetime import datetime


class ReportGenerator:

    def generate(self, history):

        findings = []

        confirmed = 0
        potential = 0
        total_attacks = len(history)

        # -----------------------------
        # Process Findings
        # -----------------------------
        for item in history:

            analysis = item["analysis"]

            status = analysis.get("finding_status", "Unknown")

            if status == "No Vulnerability":
                continue

            if status == "Confirmed Vulnerability":
                confirmed += 1

            elif status == "Potential Vulnerability":
                potential += 1

            findings.append({
                "endpoint": item["attack"]["endpoint"],
                "method": item["attack"]["method"],
                "attack_reason": item["attack"].get("reason"),
                "finding_status": status,
                "confidence": analysis.get("confidence"),
                "severity": analysis.get("severity"),
                "owasp_category": analysis.get("owasp_category"),
                "business_impact": analysis.get("business_impact"),
                "recommendation": analysis.get("recommendation"),
                "next_attack": analysis.get("next_attack")
            })

        # -----------------------------
        # Executive Summary
        # -----------------------------
        report = {

            "executive_summary": {

                "application": "Target Banking API",

                "scan_status": "Completed",

                "scan_time": str(datetime.now()),

                "endpoints_tested": len(
                    list(
                        set(
                            item["attack"]["endpoint"]
                            for item in history
                        )
                    )
                ),

                "attacks_executed": total_attacks,

                "confirmed_findings": confirmed,

                "potential_findings": potential,

                "total_findings": len(findings),

                "overall_risk": self.calculate_risk(
                    confirmed,
                    potential
                )
            },

            "findings": findings
        }

        os.makedirs("reports", exist_ok=True)

        with open(
            "reports/security_report.json",
            "w"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )

        return report

    # -----------------------------
    # Overall Risk Calculation
    # -----------------------------
    def calculate_risk(
        self,
        confirmed,
        potential
    ):

        if confirmed >= 3:
            return "CRITICAL"

        elif confirmed >= 1:
            return "HIGH"

        elif potential >= 2:
            return "MEDIUM"

        elif potential >= 1:
            return "LOW"

        return "MINIMAL"