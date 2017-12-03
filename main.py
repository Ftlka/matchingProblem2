f = open('in.txt', 'r').read()
graph = f.split('\n')
n = int(graph[0].split(' ')[0])
k = int(graph[0].split(' ')[1])
graph.pop(0)  # чтобы избавиться от первых двух строк
number_of_edges = graph.pop(0)  # чтобы избавиться от первых двух строк(2)
s = []
while len(graph) != 0:
    s.append(graph.pop(0).split(' '))


def make_graph(inputted_array):
    i = 0
    diction = {}
    while i < n:
        diff = int(inputted_array[i + 1]) - int(inputted_array[i])
        small_array = []
        current = int(inputted_array[i])
        while current < int(inputted_array[i]) + diff:
            small_array.append(inputted_array[current - 1])
            current += 1
        diction[i + 1] = small_array
        i += 1
    return diction


def kun(v):
    if used[v - 1]:
        return False
    used[v - 1] = True
    for idx, element in enumerate(g.get(v)):
        to = int(g[v][idx]) - 1
        if mt[to] == -1 or kun(mt[to]):
            mt[to] = v
            return True
    return False


def create_output(vertex_array):
    out = ''
    for v in vertex_array:
        out += str(v) + ' '
    return out.strip()


g = make_graph(*s)
mt = [-1] * k
used = [False] * n
vertices = list(range(1, n + 1))
full = True
bad_vertex = 0
for vertex in vertices:
    a = kun(vertex)
    if not a:
        bad_vertex = vertex
        full = False

if full:
    open('out.txt', 'w+').write('Y\n' + create_output(mt))
if not full:
    open('out.txt', 'w+').write('N\n' + str(bad_vertex))
