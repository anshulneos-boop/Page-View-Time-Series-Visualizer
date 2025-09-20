import medical_data_visualizer as mdv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Draw and show categorical plot
    cat_fig = mdv.draw_cat_plot()
    cat_fig.savefig("catplot.png")
    plt.show()

    # Draw and show heatmap
    heat_fig = mdv.draw_heat_map()
    heat_fig.savefig("heatmap.png")
    plt.show()
