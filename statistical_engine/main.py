import json
from src.stat_engine import StatEngine
from src.monte_carlo import run_simulation

# Load salary data
with open("data/sample_salaries.json") as f:
    data = json.load(f)

salaries = data["salaries"]

engine = StatEngine(salaries)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance:", engine.get_variance())
print("Standard Deviation:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

# Run simulation
run_simulation()