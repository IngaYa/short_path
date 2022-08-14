import short_path_func


class Node:
    def __init__(self, name):
        self.name = name
        self.out_edges = []

    def __str__(self):
        return f"City {self.name}"


class Edge:
    def __init__(self, tail, head, transport,cost, time):
        self.tail = tail
        self.tail.out_edges.append(self)
        self.head = head
        self.transport = transport
        self.cost = cost
        self.time = time

    def __str__(self):
        return f"{self.tail.name} - {self.head.name} by {self.transport} : {self.time} minutes, {self.cost} euros"


def main():
    paris = Node("Paris")
    lille = Node("Lille")
    lyon = Node("Lyon")
    strasbourg = Node("Strasbourg")

    paris_lille1 = Edge(paris, lille, "train", 60, 60)
    paris_lille2 = Edge(paris, lille, "bus", 10, 100)
    lyon_paris = Edge(lyon, paris, "train", 100, 120)
    lyon_strasbourg = Edge(lyon, strasbourg, "train", 50, 160)
    strasbourg_lille = Edge(strasbourg, lille, "bus", 20, 180)

    print("The quickest path Paris - Strasbourg")
    short_path_func(paris, strasbourg, lambda edge: edge.time)


if __name__ == '__main__':
    main()
