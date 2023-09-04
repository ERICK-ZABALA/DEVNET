from graphviz import Digraph

my_graph = Digraph(comment="My Network")
my_graph.node("core")
my_graph.node("distribution")
my_graph.node("access1")
my_graph.node("access2")
my_graph.edge("core", "distribution")
my_graph.edge("distribution", "access1")
my_graph.edge("distribution", "access2")
print(my_graph.source)
my_graph.render("output/gv_03.gv")