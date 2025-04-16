import os
import seaborn as sns
import matplotlib.pyplot as plt

# Apply a clean and professional Seaborn theme
sns.set_theme(style="whitegrid")

def plot_metric(df, metric, output_dir):
    """
    Plots the given metric over time and saves it as a PNG.

    Args:
        df (DataFrame): DataFrame with a 'year' column and the target metric
        metric (str): Metric to plot ('nodes', 'edges', 'density', 'avg_degree')
        output_dir (str): Path to save the plot
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="year", y=metric, marker="o", linewidth=2.5)

    plt.title(f"{metric.replace('_', ' ').title()} Over Time", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel(metric.replace('_', ' ').title(), fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_path = os.path.join(output_dir, f"{metric}_trend.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    