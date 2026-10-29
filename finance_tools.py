import pandas as pd
import numpy as np

class FinanceEngine:
    @staticmethod
    def calculate_metrics(salary, expenses):
        total_exp = sum(expenses.values())
        savings = salary - total_exp
        efficiency = (savings / salary) * 100 if salary > 0 else 0
        
        # Financial Burn Rate (How many months you can survive on ₹1,00,000 savings)
        runway = 100000 / total_exp if total_exp > 0 else float('inf')
        
        return {
            "total_expense": total_exp,
            "savings": savings,
            "savings_rate": efficiency,
            "runway": runway
        }

    @staticmethod
    def calculate_indian_tax(annual_income):
        """Estimates tax based on the New Tax Regime (India)."""
        # Exemption up to 3L, then 5% per 3L bracket (simplified)
        tax = 0
        if annual_income <= 300000:
            return 0
        elif annual_income <= 600000:
            tax = (annual_income - 300000) * 0.05
        elif annual_income <= 900000:
            tax = 15000 + (annual_income - 600000) * 0.10
        elif annual_income <= 1200000:
            tax = 45000 + (annual_income - 900000) * 0.15
        else:
            tax = 90000 + (annual_income - 1200000) * 0.20
        return tax

    @staticmethod
    def get_spending_personality(expenses, salary):
        discretionary = expenses.get("Lifestyle", 0) + expenses.get("Other", 0)
        ratio = discretionary / salary if salary > 0 else 0
        if ratio > 0.35: return "🛍️ The Big Spender (High Discretionary)"
        if ratio < 0.10: return "🏦 The Frugal Architect (High Savings)"
        return "⚖️ The Balanced Planner"