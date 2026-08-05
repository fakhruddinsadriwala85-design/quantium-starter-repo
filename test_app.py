from data.app import app  # kyunki app.py data folder ke andar hai

def test_header_present():
    header = app.layout.children[0]
    assert "Soul Foods Sales Visualiser" in header.children

def test_visualisation_present():
    graph = app.layout.children[2]
    assert graph.id == "sales-chart"

def test_region_picker_present():
    radio = app.layout.children[1]
    assert radio.id == "region-filter"
    assert set([opt["value"] for opt in radio.options]) == {"north", "east", "south", "west", "all"}
