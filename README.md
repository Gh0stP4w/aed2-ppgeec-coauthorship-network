# AED2 – PPgEEC Co-Authorship Network

Temporal analysis of PPgEEC co-authorship networks (2010–2025) using NetworkX – AED2 project

---

## 🧠 Project Overview

This repository contains all code, data, and visualizations for the temporal network analysis of academic co-authorship in the PPgEEC program (2010–2025), as part of the *Algorithms and Data Structures II* (AED2) course at *Federal University of Rio Grande do Norte (UFRN)*.

The main goal is to explore how the network of collaborations evolved over time, using graph theory and data science tools.

---

## 🛠️ Stack

- Python **3.12.3**
- NetworkX **3.2.1**
- Matplotlib **3.8.2**
- Seaborn **0.13.2**
- Pandas **2.2.1**
- NumPy **1.26.4**

---

## 📊 Main Features

- 📈 Yearly metrics: density, node/edge counts, average degree
- 🎯 Ridgeline plot of degree distributions (per year)
- 🕸️ Graph visualizations for 3-year and 4-year snapshots
- ✂️ Subgraph filtering based on degree thresholds
- 🧭 Ego-network exploration

---

## 📁 Repository Structure

```bash
aed2-ppgeec-coauthorship-network/
├── data/               # .gexf files (per year)
├── notebooks/          # Jupyter notebooks (exploration & plotting)
├── src/                # Python scripts and helper functions
├── output/             # Generated figures, tables and exports
└── README.md           # This file
```

---

## 🚀 Getting Started 

1. Clone this repo:
```bash
git clone https://github.com/Gh0stP4w/aed2-ppgeec-coauthorship-network.git
cd aed2-ppgeec-coauthorship-network
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv_ppgeec-coauthorship-network
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

---


## 🤖 AI Assistance Disclosure

This project received support from generative AI tools (ChatGPT) for structuring the project, writing documentation, and assisting with code development and analysis.

---

## 📚 References

- PPgEEC datasets provided by the course instructors
- [NetworkX Documentation](https://networkx.org/documentation/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- Example repositories recommended by the instructor:
  - https://github.com/Morsinaldo/embedded_artificial_intelligence/
  - https://github.com/thaisaraujom/algorithms_datastructure_ii/
