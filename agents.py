class DataAnalystAgent:

    def analyze(self, salary, expenses):

        total_expense = sum(expenses.values())
        savings = salary - total_expense
        savings_rate = (savings / salary) * 100

        return {
            "total_expense": total_expense,
            "savings": savings,
            "savings_rate": savings_rate
        }


class RiskAgent:

    def detect_risk(self, analysis):

        risks = []

        if analysis["savings_rate"] < 20:
            risks.append("Low savings rate detected")

        return risks


class StrategyAgent:

    def generate_strategy(self, risks):

        if not risks:
            return "Your financial health is stable."

        strategy = "Suggested Actions:\n"

        for r in risks:
            if "Low savings" in r:
                strategy += "- Reduce unnecessary expenses\n"
                strategy += "- Increase savings to at least 20%\n"

        return strategy
