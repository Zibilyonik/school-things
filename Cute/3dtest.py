import numpy as np
from ase.io import read
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import io

# Load molecule
atoms = read(r"C:\Users\Win PRO\Documents\GitHub\compsci_2025-2027\Cute\molecule.xyz")
positions = atoms.get_positions()
elements = atoms.get_chemical_symbols()

colors = {
    "H": "white",
    "C": "black",
    "N": "blue",
    "O": "red",
    "S": "yellow"
}

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H2("ChemVis3D — Interactive Chemistry Viewer"),

    dcc.Slider(
        id="size-slider",
        min=5,
        max=30,
        step=1,
        value=15,
        marks={5:"Small",15:"Medium",30:"Large"}
    ),

    dcc.Graph(id="molecule-graph", style={"height": "80vh"})
])

@app.callback(
    Output("molecule-graph", "figure"),
    Input("size-slider", "value")
)
def update_graph(size):
    fig = go.Figure()

    for element in set(elements):
        idx = [i for i,e in enumerate(elements) if e == element]
        fig.add_trace(go.Scatter3d(
            x=positions[idx,0],
            y=positions[idx,1],
            z=positions[idx,2],
            mode="markers",
            marker=dict(
                size=size,
                color=colors.get(element, "gray")
            ),
            name=element
        ))

    fig.update_layout(
        scene=dict(
            xaxis_title="X (Å)",
            yaxis_title="Y (Å)",
            zaxis_title="Z (Å)"
        ),
        margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)

