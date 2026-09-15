<h1 align="center">🛒 SwiftCart Intelligence</h1>
<h3 align="center">Diagnostic Business Analytics & Root-Cause Engine</h3>

<p align="center">
<img src="https://img.shields.io/badge/PYTHON-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/PANDAS-DATA_MANIPULATION-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
<img src="https://img.shields.io/badge/SCIKIT_LEARN-MACHINE_LEARNING-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
<img src="https://img.shields.io/badge/JUPYTER-NOTEBOOKS-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
<img src="https://img.shields.io/badge/POWER_BI-VISUAL_ANALYTICS-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI">
</p>

<p align="center">
  <strong>SwiftCart Intelligence</strong> is an automated diagnostic business analytics platform. By pairing <strong>rolling statistical control charts</strong> with an <strong>automated root-cause engine</strong>, SwiftCart transforms passive descriptive dashboards into active, self-diagnosing systems capable of continuous, real-time business anomaly detection and executive recommendation.
</p>

<hr>

### 📌 Project Overview
<hr>

Most analytics portfolios stop at descriptive analytics—showing *what* happened via revenue or operational dashboards. Traditional business intelligence relies on human analysts to manually hunt for the root causes of these deviations.

**SwiftCart Intelligence** solves this critical inefficiency by constructing an automated diagnostic pipeline:

- **Continuous Monitoring:** Ingests daily operational telemetry (orders, delivery times, rider counts, stockout rates) across 6 cities directly from the data warehouse.
- **Diagnostic Reasoning:** Statistically evaluates anomalous periods against baseline driver metrics to isolate exact root causes (e.g., distinguishing rider attrition from a competitor launch).
- **Forward Recommendation Generation:** Calculates estimated business impact and utilizes structured Natural Language Generation (NLG) to automatically generate and distribute executive action memos.

### 🔥 Key Features
<hr>

- **Automated Root-Cause Engine:** Continuous statistical comparison between anomalous events and candidate driver metrics.
- **Dynamic Control Charts:** Rolling 30-day baseline profiling (median ± 2.5σ) adapting dynamically to business growth and seasonality.
- **Template-Driven NLG:** Reproducible, auditable plain-English insight generation without relying on hallucination-prone LLMs.
- **Business Ground Truth Integration:** Synthetic data pre-embedded with 3 genuine business problems for the pipeline to detect.

**Step-by-Step Execution:**

1. **Telemetry Streaming:** The data generator creates daily metric logs (revenue, riders, stockouts) for 6 cities.
2. **Control Chart Evaluation:** The pipeline evaluates current daily metrics against a 30-day rolling baseline.
3. **Diagnostic Comparison:** Flags anomalies and performs percentage deviation checks on secondary drivers.
4. **Insight Translation:** Converts raw statistical deviations into actionable executive insights.
5. **Dashboard Visualization:** Renders interactive visualizations alongside the generated recommendation memo.

### 🛠️ System Architecture
<hr>

SwiftCart Intelligence operates a multi-layer analytical architecture connecting data ingestion, statistical anomaly detection, root-cause isolation, and dashboard presentation.

```mermaid
graph LR
    A[Data Generation] -->|Time-Series| B(Detection Engine)
    B -->|Flagged Anomalies| C{Root-Cause Analyzer}
    C -->|Driver Match| D(NLG Engine)
    D -->|Insights| E[BI Dashboard]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
```

### 📁 Folder Structure
<hr>

Below is the production-ready directory structure designed for modular execution and interactive dashboarding.

```text
SwiftCart-Dashboard/
├── generate_data.py                    # Synthetic operational data generator
├── SwiftCart_Intelligence.ipynb        # Core pipeline: EDA, Detection, Root-Cause, NLG
├── dashboard_data.json                 # Extracted metrics for web visualization
├── executive_memo.md                   # Auto-generated executive recommendation memo
├── powerbi_tableau_build_guide.md      # BI tool integration documentation
├── swiftcart_daily_ops.csv             # Raw operational telemetry dataset
├── swiftcart_flagged_daily.csv         # Processed anomaly dataset
├── city_summary.csv                    # Aggregate city-level performance data
├── SwiftCart_Intelligence.html         # Notebook export (Analysis Report)
└── SwiftCart_Intelligence_Dashboard.html # Interactive web dashboard presentation
```

### 🔄 Product Workflow
<hr>

```mermaid
graph TD
    A[Synthetic Data Engine]
    A -->|Streams 180-Day Telemetry| B[Anomaly Detection Engine]
    B -->|Control Chart Deviations| C[Root-Cause Analyzer]
    C -->|Isolates Driver Metrics| D[Insight Generation Layer NLG]
    D -->|Calculates Business Impact| E[Executive Memo & Dashboard]
    
    classDef default fill:#f4f4ff,stroke:#8b8bff,stroke-width:1px;
    classDef greyBox fill:#f0f0f0,stroke:#d0d0d0,stroke-width:1px;
    class A,B,C,D,E default;
```

### 📊 Business Scenarios & Ground Truth
<hr>

The dataset deliberately embeds **three real business problems** so the pipeline has genuine root causes to identify:

| City | Business Problem | Root Cause |
| :--- | :--- | :--- |
| **Pune** | Delivery times spike for 3 weeks | Sudden rider attrition (~45% drop in active riders) |
| **Bhopal** | Revenue drops for 3 weeks | Recurring stockouts (~4.5x normal rate) |
| **Bangalore** | Customer churn climbs steadily | A competitor launches in the market |
