import json
import os


class AttackHistory:

    def __init__(self):
        self.history = []

    def add(self, attack, result, analysis):

        self.history.append({
            "attack": attack,
            "result": result,
            "analysis": analysis
        })

        # Save history for dashboard
        os.makedirs("reports", exist_ok=True)

        with open("reports/history.json", "w") as file:
            json.dump(
                self.history,
                file,
                indent=4
            )

    def latest(self):

        if len(self.history) == 0:
            return None

        return self.history[-1]

    def all(self):
        return self.history