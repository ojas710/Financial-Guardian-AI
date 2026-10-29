from agents import DataAnalystAgent, RiskAgent, StrategyAgent

class FinancialGuardianAgent:
    def __init__(self):
        self.data_agent = DataAnalystAgent()
        self.risk_agent = RiskAgent()
        self.strategy_agent = StrategyAgent()

    def run(self, salary, expenses):
        analysis = self.data_agent.analyze(salary, expenses)
        risks = self.risk_agent.detect_risk(analysis)
        
        # Add specific category risks
        for cat, val in expenses.items():
            if val > salary * 0.30:
                risks.append(f"Excessive {cat} spending")
                
        strategy = self.strategy_agent.generate_strategy(risks)
        return analysis, risks, strategy

    def get_behavioral_nudge(self, analysis):
        if analysis['savings_rate'] < 10:
            return "💡 Nudge: Small changes add up. Cutting $50/week in 'Other' expenses adds $2,600 to your yearly net worth."
        return "🌟 You're on a roll! Your savings rate is in the top 10% of users this month."