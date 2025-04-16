import os
import logging
import networkx as nx
from typing import Dict


def load_graphs_per_year(data_dir: str) -> Dict[int, nx.Graph]:
    """
    Loads yearly co-authorship networks from GEXF files (2010-2025).
    
    Args:
        data_dir (str): Path to directory containing yearly network files
                        (format: 'YYYY_authors_network.gexf')
    
    Returns:
        Dict[int, nx.Graph]: Dictionary mapping years to their NetworkX graphs
    
    Raises:
        FileNotFoundError: If the data directory or any yearly file is missing
        nx.NetworkXError: If any GEXF file is malformed
    """
    graphs = {}
    
    for year in range(2010, 2026):
        filename = f"{year}_authors_network.gexf"
        filepath = os.path.join(data_dir, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Network file not found: {filepath}")
        
        try:
            graphs[year] = nx.read_gexf(filepath)
            logging.info(f"Successfully loaded: {filename}")
        except Exception as e:
            raise nx.NetworkXError(f"Error loading {filename}: {str(e)}")
    
    return graphs


def validate_graph(graph: nx.Graph, year: int) -> None:
    """
    Performs basic sanity checks on loaded graphs.

    Args:
        graph (nx.Graph): Loaded co-authorship network
        year (int): Year for diagnostic messages
    """
    if graph.number_of_nodes() == 0:
        logging.warning(f"Empty graph detected for year {year}")

    sample_node = next(iter(graph.nodes(data=True)), None)
    if sample_node:
        node_id, attrs = sample_node
        logging.debug(f"[{year}] Sample node ID: {node_id}")
        logging.debug(f"[{year}] Sample node attributes: {attrs}")

        # Check for expected attributes
        expected_attrs = ['complete_name', 'h_index', 'is_permanent']
        for attr in expected_attrs:
            if attr not in attrs:
                logging.warning(f"[{year}] Missing expected attribute '{attr}' in node {node_id}")
