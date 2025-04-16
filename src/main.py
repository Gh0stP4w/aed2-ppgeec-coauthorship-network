import os
import logging
from datetime import datetime
from analysis.metrics import compute_all_metrics
from graphs.load_graphs import load_graphs_per_year, validate_graph
from analysis.plot_metrics import plot_metric

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DATA_DIR = "../data/yearly_networks"
OUTPUT_DIR = "../output"

def main():
    # Initial checks
    if not os.path.exists(DATA_DIR):
        logging.error(f"Data directory not found: {DATA_DIR}")
        exit(1)

    try:
        # Main processing
        logging.info("Loading co-authorship networks (2010–2025)...")
        graphs = load_graphs_per_year(DATA_DIR)
        
        logging.info("Validating graphs...")
        for year, graph in graphs.items():
            validate_graph(graph, year)

        logging.info("Computing network metrics...")
        df = compute_all_metrics(graphs)

        # Ensures output directory
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Results output
        output_path = os.path.join(OUTPUT_DIR, "yearly_metrics.csv")
        df.to_csv(output_path, index=False)
        
        # Final report
        logging.info(f"Successfully processed {len(graphs)} years")
        logging.info(f"Output saved to: {output_path}")
        logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}")

        # Plotting metrics
        metrics_to_plot = ["nodes", "edges", "density", "avg_degree"]
        for metric in metrics_to_plot:
            plot_metric(df, metric, OUTPUT_DIR)
            logging.info(f"Plot saved for metric: {metric}")

    except FileNotFoundError as e:
        logging.error(f"Missing data file: {str(e)}")
        exit(1)
    except Exception as e:
        logging.critical(f"Critical error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
