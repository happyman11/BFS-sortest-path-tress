if __name__=='__main__':
     
    import functionbfs as funct
    v = 8;

    adj = [[] for i in range(v)];
  

    funct.add_edge(adj, 0, 1);
    funct.add_edge(adj, 0, 3);
    funct.add_edge(adj, 1, 2);
    funct.add_edge(adj, 3, 4);
    funct.add_edge(adj, 3, 7);
    funct.add_edge(adj, 4, 5);
    funct.add_edge(adj, 4, 6);
    funct.add_edge(adj, 4, 7);
    funct.add_edge(adj, 5, 6);
    funct.add_edge(adj, 6, 7);
    source = 0
    dest = 7;
    funct.printShortestDistance(adj, source, dest, v);



