import logging
import networkx as nx
import pandas as pd


def compute_metrics(graph: nx.Graph) -> dict:
    """
    Computes key network metrics for a given NetworkX graph.

    Args:
        graph (nx.Graph): A NetworkX graph object representing a co-authorship network.

    Returns:
        dict: A dictionary with the following metrics:
            - nodes (int): Total number of nodes.
            - edges (int): Total number of edges.
            - density (float): Graph density (0 ≤ density ≤ 1).
            - avg_degree (float): Average degree across all nodes.

    Notes:
        If the graph has no nodes, the average degree will be set to 0.
    """
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    density = nx.density(graph)
    avg_degree = 0

    if num_nodes > 0:
        avg_degree = sum(dict(graph.degree()).values()) / num_nodes

    return {
        "nodes": num_nodes,
        "edges": num_edges,
        "density": density,
        "avg_degree": avg_degree
    }


def compute_all_metrics(graphs_by_year: dict) -> pd.DataFrame:
    """
    Computes network metrics for each year in a dictionary of graphs.

    Args:
        graphs_by_year (dict): Dictionary mapping years (int) to NetworkX graphs (nx.Graph).
                               Example: {2010: <Graph>, 2011: <Graph>, ...}

    Returns:
        pd.DataFrame: A pandas DataFrame containing the computed metrics per year,
                      with the following columns:
                          - year (int)
                          - nodes (int)
                          - edges (int)
                          - density (float)
                          - avg_degree (float)

    Notes:
        The resulting DataFrame is sorted in ascending order by the 'year' column.
        Logs an info message during processing of each year.
    """
    rows = []
    for year, graph in graphs_by_year.items():
        logging.info(f"Computing metrics for year {year}")
        metrics = compute_metrics(graph)
        metrics["year"] = year
        rows.append(metrics)

    return pd.DataFrame(rows).sort_values("year")
