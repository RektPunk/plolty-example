import pandas as pd
import networkx as nx
import plotly.graph_objects as go


def vis_digraph(
    df: pd.DataFrame,
    from_: str,
    to_: str,
    edge_label_name: str,
) -> go.Figure:

    _df = df[[from_, to_, edge_label_name]]
    _nx_network_info = nx.from_pandas_edgelist(
        _df,
        source=from_,
        target=to_,
        edge_attr=edge_label_name,
    )
    _node_location = nx.layout.spring_layout(_nx_network_info)

    node_x = []
    node_y = []
    node_labels = []
    for node in _nx_network_info.nodes():
        _location_x, _location_y = _node_location[node]
        node_labels.append(node)
        node_x.append(_location_x)
        node_y.append(_location_y)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        text=node_labels,
        mode="markers+text",
        hoverinfo="text",
        textposition="top center",
        marker=dict(size=10),
    )

    fig = go.Figure(
        node_trace,
        layout=go.Layout(
            hovermode="closest",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        ),
    )
    for _, edges in _df.iterrows():
        _from_node = edges[from_]
        _to_node = edges[to_]
        _label = edges[edge_label_name]
        _location_from_x, _location_from_y = _node_location[_from_node]
        _location_to_x, _location_to_y = _node_location[_to_node]
        fig.add_annotation(
            dict(
                x=_location_to_x,
                y=_location_to_y,
                ax=_location_from_x,
                ay=_location_from_y,
                xref="x",
                yref="y",
                axref="x",
                ayref="y",
                showarrow=True,
                arrowhead=1,
                arrowsize=3,
                arrowwidth=1,
                arrowcolor="black",
            )
        )
        fig.add_annotation(
            dict(
                x=(_location_from_x + _location_to_x) / 2,
                y=(_location_from_y + _location_to_y) / 2,
                text=_label,
                showarrow=True,
                arrowhead=1,
            )
        )
    return fig
