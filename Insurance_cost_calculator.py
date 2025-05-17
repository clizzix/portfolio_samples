# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name="Maria", age=31, sex=0, bmi=23.1, num_of_children=1, smoker=0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name=
                                               "Rohan", age=25, sex=1, bmi=28.5, num_of_children=3, smoker=0)
# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name="Valentina", age=53, sex=0, bmi=31.4, num_of_children=0,
                                                   smoker=1)
# Estimate Akira's insurance cost
akira_insurance_cost = estimate_insurance_cost(name="Akira", age=19, sex=1, bmi=27.1, num_of_children=0, smoker=0)

# Create a list called names and fill it with the names of the individuals you are estimating insurance costs for:
names = ["Maria", "Rohan", "Valentina", "Akira"]

# Next, create a list called insurance_costs and fill it with the actual amounts
# that Maria, Rohan, and Valentina paid for insurance:
insurance_costs = [4150.0, 5320.0, 35210.0, 2930.0]

# Create a new variable called insurance_data that combines names and insurance_costs using the zip() function. Convert zip object to list.
insurance_data = list(zip(names, insurance_costs))

print(f"Here is the actual insurance cost data: {insurance_data}")
# create an empty list called estimated_insurance_data.
estimated_insurance_data = []

# Use .append() to add ([name, cost]) to estimated_insurance_data.
for name, cost in zip(names,
                      [maria_insurance_cost, rohan_insurance_cost, valentina_insurance_cost, akira_insurance_cost]):
    estimated_insurance_data.append([name, cost])

print(f"Here is the estimated insurance cost data: {estimated_insurance_data}")

insurance_cost_difference = []
for i in range(len(names)):
    difference = insurance_costs[i] - estimated_insurance_data[i][1]
    insurance_cost_difference.append([names[i], difference])