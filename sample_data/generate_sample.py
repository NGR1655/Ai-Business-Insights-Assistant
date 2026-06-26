"""
Run this once to generate sample_sales.csv for testing.
python sample_data/generate_sample.py
"""

import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

regions = ["North", "South", "East", "West"]
products = ["Analytics Suite", "CRM Pro", "Data Vault", "Report Engine", "API Gateway"]
months = pd.date_range("2023-01-01", periods=24, freq="ME")

rows = []
for month in months:
    for region in regions:
        for product in products:
            revenue = np.random.randint(20_000, 200_000)
            units = np.random.randint(10, 500)
            cost = revenue * np.random.uniform(0.3, 0.6)
            rows.append({
                "date": month.strftime("%Y-%m-%d"),
                "region": region,
                "product": product,
                "revenue": round(revenue, 2),
                "units_sold": units,
                "cost": round(cost, 2),
                "profit": round(revenue - cost, 2),
                "customer_satisfaction": round(np.random.uniform(3.0, 5.0), 1),
            })

df = pd.DataFrame(rows)
out = Path(__file__).parent / "sample_sales.csv"
df.to_csv(out, index=False)
print(f"Saved {len(df)} rows to {out}")
