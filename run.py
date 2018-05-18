# coding=utf-8
#  Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

print "--- Primero en Anchura ---"
print search.breadth_first_graph_search(ab).path()
print "\n"
print "--- Primero en Profundidad ---"
print search.depth_first_graph_search(ab).path()
print "\n"
print "--- Ramificacion y Acotacion ---"
print search.busqueda_ramificacion_acotacion(ab).path()
print "\n"
print "--- Ramificación y Acotación Subestimada ---"
print search.busqueda_ramificacion_acotacion_subestimada(ab).path()

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
