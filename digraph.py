import pandas as pd
from logic.digraph import vis_digraph

FROM_ADDRESS = ["A", "B", "C", "A", "D", "B", "E"]
TO_ADDRESS = ["B", "C", "A", "D", "B", "E", "A"]
EDGE_LABEL = ["transfer", "sold", "transfer", "sold", "transfer", "sold", "transfer"]


df = pd.DataFrame(
    {
        "from_address": FROM_ADDRESS,
        "to_address": TO_ADDRESS,
        "edge_label": EDGE_LABEL,
    }
)

if __name__ == "__main__":
    fig = vis_digraph(
        df,
        "from_address",
        "to_address",
        "edge_label",
    )

    fig.write_html("plot/digraph.html")
