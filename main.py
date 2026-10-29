from agent import FinancialGuardianAgent

salary = int(input("Enter salary: "))

rent = int(input("Rent: "))
food = int(input("Food: "))
transport = int(input("Transport: "))
subscriptions = int(input("Subscriptions: "))

expenses = {
    "rent": rent,
    "food": food,
    "transport": transport,
    "subscriptions": subscriptions
}

agent = FinancialGuardianAgent()

analysis, risks, strategy = agent.run(salary, expenses)

print("\nFinancial Analysis:", analysis)
print("\nDetected Risks:", risks)
print("\nStrategy:\n", strategy)
