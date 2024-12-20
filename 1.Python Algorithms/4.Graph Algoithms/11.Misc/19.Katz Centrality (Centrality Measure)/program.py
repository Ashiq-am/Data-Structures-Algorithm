import networkx as nx


def katz_centrality(G, alpha=0.1, beta=1.0,
                    max_iter=1000, tol=1.0e-6,
                    nstart=None, normalized=True,
                    weight='weight'):
    """Compute the Katz centrality for the nodes
        of the graph G.


    Katz centrality computes the centrality for a node
    based on the centrality of its neighbors. It is a
    generalization of the eigenvector centrality. The
    Katz centrality for node `i` is

    .. math::

        x_i = \alpha \sum_{j} A_{ij} x_j + \beta,

    where `A` is the adjacency matrix of the graph G
    with eigenvalues `\lambda`.

    The parameter `\beta` controls the initial centrality and

    .. math::

        \alpha < \frac{1}{\lambda_{max}}.


    Katz centrality computes the relative influence of
    a node within a network by measuring the number of
    the immediate neighbors (first degree nodes) and
    also all other nodes in the network that connect
    to the node under consideration through these
    immediate neighbors.

    Extra weight can be provided to immediate neighbors
    through the parameter :math:`\beta`. Connections
    made with distant neighbors are, however, penalized
    by an attenuation factor `\alpha` which should be
    strictly less than the inverse largest eigenvalue
    of the adjacency matrix in order for the Katz
    centrality to be computed correctly.


    Parameters
    ----------
    G : graph
    A NetworkX graph

    alpha : float
    Attenuation factor

    beta : scalar or dictionary, optional (default=1.0)
    Weight attributed to the immediate neighborhood.
    If not a scalar, the dictionary must have an value
    for every node.

    max_iter : integer, optional (default=1000)
    Maximum number of iterations in power method.

    tol : float, optional (default=1.0e-6)
    Error tolerance used to check convergence in
    power method iteration.

    nstart : dictionary, optional
    Starting value of Katz iteration for each node.

    normalized : bool, optional (default=True)
    If True normalize the resulting values.

    weight : None or string, optional
    If None, all edge weights are considered equal.
    Otherwise holds the name of the edge attribute
    used as weight.

    Returns
    -------
    nodes : dictionary
    Dictionary of nodes with Katz centrality as
    the value.

    Raises
    ------
    NetworkXError
    If the parameter `beta` is not a scalar but
    lacks a value for at least one node



    Notes
    -----

    This algorithm it uses the power method to find
    the eigenvector corresponding to the largest
    eigenvalue of the adjacency matrix of G.
    The constant alpha should be strictly less than
    the inverse of largest eigenvalue of the adjacency
    matrix for the algorithm to converge.
    The iteration will stop after max_iter iterations
    or an error tolerance ofnumber_of_nodes(G)*tol
    has been reached.

    When `\alpha = 1/\lambda_{max}` and `\beta=0`,
    Katz centrality is the same as eigenvector centrality.

    For directed graphs this finds "left" eigenvectors
    which corresponds to the in-edges in the graph.
    For out-edges Katz centrality first reverse the
    graph with G.reverse().


    """
    from math import sqrt

    if len(G) == 0:
        return {}

    nnodes = G.number_of_nodes()

    if nstart is None:

        # choose starting vector with entries of 0
        x = dict([(n, 0) for n in G])
    else:
        x = nstart

    try:
        b = dict.fromkeys(G, float(beta))
    except (TypeError, ValueError, AttributeError):
        b = beta
        if set(beta) != set(G):
            raise nx.NetworkXError('beta dictionary '
                                   'must have a value for every node')

    # make up to max_iter iterations
    for i in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast, 0)

        # do the multiplication y^T = Alpha * x^T A - Beta
        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
        for n in x:
            x[n] = alpha * x[n] + b[n]

        # check convergence
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < nnodes * tol:
            if normalized:

                # normalize vector
                try:
                    s = 1.0 / sqrt(sum(v ** 2 for v in x.values()))

                # this should never be zero?
                except ZeroDivisionError:
                    s = 1.0
            else:
                s = 1
            for n in x:
                x[n] *= s
            return x

    raise nx.NetworkXError('Power iteration failed to converge in ''%d iterations.' % max_iter)
