"""
SwiftCart Intelligence - Synthetic Data Generator
Generates 6 months of daily city-level operations data for a fictional
quick-commerce company, with THREE deliberately embedded business problems
so the analytics pipeline has real root causes to discover:

  1. PUNE   - Delivery time degradation caused by a rider shortage (Mar 10-31)
  2. BHOPAL - Revenue drop caused by recurring stockouts (Feb 15 - Mar 5)
  3. BANGALORE - Customer churn spike caused by a competitor launch (Mar 1 onward)
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

CITIES = ["Bangalore", "Mumbai", "Delhi", "Pune", "Hyderabad", "Bhopal"]
START_DATE = datetime(2026, 1, 1)
N_DAYS = 180  # 6 months

city_base = {
    "Bangalore": {"orders": 2400, "aov": 340, "riders": 220, "stockout": 0.03},
    "Mumbai":    {"orders": 2600, "aov": 360, "riders": 240, "stockout": 0.03},
    "Delhi":     {"orders": 2300, "aov": 320, "riders": 210, "stockout": 0.04},
    "Pune":      {"orders": 1400, "aov": 300, "riders": 130, "stockout": 0.03},
    "Hyderabad": {"orders": 1600, "aov": 310, "riders": 150, "stockout": 0.03},
    "Bhopal":    {"orders": 700,  "aov": 260, "riders": 70,  "stockout": 0.03},
}

rows = []
for day_offset in range(N_DAYS):
    date = START_DATE + timedelta(days=day_offset)
    dow_factor = 1.15 if date.weekday() >= 5 else 1.0  # weekend bump

    for city in CITIES:
        base = city_base[city]

        orders = base["orders"] * dow_factor * np.random.normal(1.0, 0.05)
        aov = base["aov"] * np.random.normal(1.0, 0.04)
        riders = base["riders"] * np.random.normal(1.0, 0.03)
        stockout_rate = base["stockout"] * np.random.normal(1.0, 0.15)
        delivery_time = np.random.normal(24, 2.5)  # minutes
        churn_rate = np.random.normal(0.045, 0.005)
        marketing_spend = orders * np.random.normal(6, 0.5)
        competitor_launch = 0

        # ---- PROBLEM 1: Pune rider shortage -> delivery time spikes ----
        if city == "Pune" and datetime(2026, 3, 10) <= date <= datetime(2026, 3, 31):
            riders *= 0.55  # sudden rider attrition
            delivery_time += np.random.normal(18, 3)  # delivery time balloons
            orders *= 0.92  # some order cancellations from bad experience

        # ---- PROBLEM 2: Bhopal stockouts -> revenue drop ----
        if city == "Bhopal" and datetime(2026, 2, 15) <= date <= datetime(2026, 3, 5):
            stockout_rate *= 4.5
            orders *= 0.70  # customers can't complete orders
            aov *= 0.92     # smaller basket due to substitutions

        # ---- PROBLEM 3: Bangalore competitor launch -> churn spike ----
        if city == "Bangalore" and date >= datetime(2026, 3, 1):
            competitor_launch = 1
            churn_rate += 0.025 + 0.0006 * min((date - datetime(2026, 3, 1)).days, 30)
            orders *= 0.96  # slow order bleed as churn compounds

        revenue = orders * aov

        rows.append({
            "date": date.strftime("%Y-%m-%d"),
            "city": city,
            "orders": round(orders),
            "aov": round(aov, 2),
            "revenue": round(revenue, 2),
            "active_riders": round(riders),
            "avg_delivery_time_min": round(delivery_time, 1),
            "stockout_rate": round(stockout_rate, 4),
            "customer_churn_rate": round(churn_rate, 4),
            "marketing_spend": round(marketing_spend, 2),
            "competitor_launch_flag": competitor_launch,
        })

df = pd.DataFrame(rows)
df.to_csv("/home/claude/swiftcart/data/swiftcart_daily_ops.csv", index=False)
print(f"Generated {len(df)} rows across {df['city'].nunique()} cities")
print(df.head())
