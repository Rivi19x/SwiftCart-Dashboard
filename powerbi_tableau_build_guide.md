# Power BI / Tableau Build Guide

Use `swiftcart_flagged_daily.csv` (day-level, with anomaly flags) and
`city_summary.csv` (city-level rollups) as your two data sources.

## Recommended Dashboard Pages

### Page 1 — Executive Overview
- KPI cards: Total Revenue, Total Orders, Avg Delivery Time, Avg Churn Rate (from `city_summary.csv`)
- Bar chart: Revenue by City
- Table: `anomalous_days` by city, sorted descending — this is your "where's the fire" view

### Page 2 — City Deep Dive (with a City slicer)
- Line chart: `revenue` over `date`, with anomalous days highlighted (filter `anomaly == True`, overlay as points or a reference band)
- Line chart: `avg_delivery_time_min` over `date`
- Line chart: `stockout_rate` and `customer_churn_rate` over `date` (dual axis)
- Card: count of anomalous days in the selected city + date range of first/last anomaly

### Page 3 — Root Cause Comparison
- Small multiples or a grouped bar chart comparing each city's average `active_riders`,
  `stockout_rate`, and `customer_churn_rate` during anomalous vs. normal days
  (you'll need to pivot `swiftcart_flagged_daily.csv` on the `anomaly` boolean to get this)

## Tips
- In Power BI: create a calculated column `Period = IF(anomaly, "Anomalous", "Normal")` and use it as a legend/color field throughout — makes the "before vs during" story visually obvious.
- In Tableau: use `anomaly` as a color encoding on the city trend lines directly.
- Pull the ranked findings and recommendations straight from `executive_memo.md` into a text box on Page 1 — this is what makes the dashboard read like a real BA deliverable instead of a chart collection.
