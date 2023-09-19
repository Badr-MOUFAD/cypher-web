from cypherweb.core.node import Node
from cypherweb.core.graph import Graph


def node_is_link_list(graph, node_id):
    # all childs are links
    childs = graph.get_neighbors(node_id)
    # get hrefs
    child_is_a_list = [
        n for n in childs if graph._graph.nodes[n["id"]]["element_type"] == "a"
    ]
    return len(child_is_a_list) == len(childs) and len(childs) > 0


def get_link_list_candidates(graph):
    return [node for node in graph._graph.nodes if node_is_link_list(graph, node)]


class LinkListClassifier(Node):
    def __init__(self) -> None:
        pass

    def process(self, graph: Graph) -> None:
        grid_candidates = get_link_list_candidates(graph)
        # annotate vertices
        attrs = {
            node: {"type": ["linklist"] + graph._graph.nodes[node]["type"]}
            for node in grid_candidates
        }

        graph.set_node_attributes(attrs)
