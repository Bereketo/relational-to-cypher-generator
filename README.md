# Relational to Graph Database Conversion

This repository contains tools and scripts for converting relational data into Cypher queries for Neo4j and visualizing both relational and graph data formats. Only trimmed versions of the dataset are included due to size constraints.

## Project Structure

- `dataset/raw/`: (Not included in the repository) Raw CSV files containing relational data.
- `dataset/trimmed_csv_files/`: Trimmed CSV files (5,000 lines) for processing.
- `scripts/`: Python scripts for data processing and Cypher query generation.
- `cypher_queries/`: Generated Cypher queries.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure Python 3 and pip are installed on your system.
- **Neo4j Database**: Running Neo4j instance for executing Cypher queries.

### Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/relational-to-cypher.git
    cd relational-to-cypher
    ```

2. **Install Dependencies**:

    Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Data Preparation

1. **Obtain Full Dataset**:

    The full dataset is not included in this repository due to size constraints. You can download the full dataset from Kaggle’s Olist dataset [here](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

2. **Trim Data**:

    Use the `trim_csv.py` script to reduce the size of your CSV files to the first 5,000 lines. Place your raw CSV files in the `data/` directory before running the script:

    ```bash
    python scripts/trim_csv.py
    ```

3. **Generate Cypher Queries**:

    Use the `generate_cypher_queries.py` script to convert the trimmed CSV files into Cypher queries:

    ```bash
    python scripts/generate_cypher_queries.py
    ```

### Visualization

#### Relational Format

Upload the trimmed CSV files to your preferred data visualization tool. The following image shows how the data is structured in relational form.

![Relational Data Visualization](images/ecommerce.png
)

#### Graph Format

1. **Upload Cypher Queries to Neo4j**:
    - Start your Neo4j database.
    - Use the Neo4j Browser or a Cypher shell to execute the queries found in the `cypher_queries/` directory.

    Example command to execute a Cypher file in Neo4j:

    ```bash
    neo4j-shell -file cypher_queries/create_customers.cypher
    ```

2. **Visualize Graph Data**:

    Explore the graph data using Neo4j Browser or other graph visualization tools. The following image show the structure of the nodes.

    ![Graph Data Visualization](images/neo4j.png
)

## Dataset

The dataset used for this project is from Kaggle’s Olist dataset. You can find it [here](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). 

**Note:** Only trimmed CSV files are included in this repository. Please download the full dataset from Kaggle and place the files in the `dataset/raw` directory before running the provided scripts.

## Scripts

### `trim_csv.py`

Trims CSV files to contain only the first 5,000 lines.

### `generate_cypher_queries.py`

Generates Cypher queries from the trimmed CSV files. The output queries are saved in the `cypher_queries/` directory.

## Requirements

To install the required Python packages, use the `requirements.txt` file. This file lists all dependencies for the project.

