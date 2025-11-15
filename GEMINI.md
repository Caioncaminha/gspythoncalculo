# Project Overview

This project is a data analysis and mathematical modeling assignment for a university course. It combines Python for statistical analysis of socioeconomic data and Calculus to model a learning curve. The project is implemented in a Jupyter Notebook (`gs_dados/analise_dados.ipynb`) and uses a helper file with functions (`gs_dados/funcoes.py`).

## Building and Running

This project requires a Python environment with Jupyter, pandas, numpy, and matplotlib installed.

**1. Install Dependencies:**

```bash
python3 -m pip install jupyter pandas numpy matplotlib
```

**2. Run the Jupyter Notebook:**

To run the analysis, execute the following command in your terminal:

```bash
jupyter notebook gs_dados/analise_dados.ipynb
```

This will open the Jupyter Notebook in your web browser. You can then run the cells in the notebook to see the analysis and results.

## Development Conventions

*   **Data Loading:** Data is loaded from Wikipedia using `pandas.read_html`. The data loading logic is in `gs_dados/funcoes.py`.
*   **Data Cleaning:** The data is cleaned and prepared in the `limpar_e_preparar_dados` function in `gs_dados/funcoes.py`.
*   **Statistical Analysis:** The statistical functions are defined in `gs_dados/funcoes.py` and are called in the Jupyter Notebook.
*   **Calculus Modeling:** The learning curve modeling is done directly in the Jupyter Notebook using `numpy` and `matplotlib`.
*   **Modularity:** The code is organized into a functions file (`funcoes.py`) and a notebook file (`analise_dados.ipynb`) for better organization and reusability.
