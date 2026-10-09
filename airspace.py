# airspace.py

AIRSPACE = {
    "A": {
        "B": {"distance": 180, "risk": 1, "congestion": 1},
        "C": {"distance": 220, "risk": 0, "congestion": 0},
    },

    "B": {
        "A": {"distance": 180, "risk": 1, "congestion": 1},
        "D": {"distance": 170, "risk": 3, "congestion": 3},
        "E": {"distance": 150, "risk": 1, "congestion": 1},
    },

    "C": {
        "A": {"distance": 220, "risk": 0, "congestion": 0},
        "D": {"distance": 120, "risk": 0, "congestion": 0},
        "E": {"distance": 130, "risk": 1, "congestion": 1},
    },

    "D": {
        "B": {"distance": 170, "risk": 3, "congestion": 3},
        "C": {"distance": 120, "risk": 0, "congestion": 0},
        "E": {"distance": 100, "risk": 2, "congestion": 2},
        "F": {"distance": 180, "risk": 3, "congestion": 3},
    },

    "E": {
        "B": {"distance": 150, "risk": 1, "congestion": 1},
        "C": {"distance": 130, "risk": 1, "congestion": 1},
        "D": {"distance": 100, "risk": 2, "congestion": 2},
        "F": {"distance": 120, "risk": 0, "congestion": 0},
    },

    "F": {
        "D": {"distance": 180, "risk": 3, "congestion": 3},
        "E": {"distance": 120, "risk": 0, "congestion": 0},
    }
}


def get_neighbors(node):
    return AIRSPACE.get(node, {})


def route_distance(route):
    total = 0

    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]

        if end not in AIRSPACE[start]:
            return float("inf")

        total += AIRSPACE[start][end]["distance"]

    return total


def route_risk(route):
    total = 0

    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]

        total += AIRSPACE[start][end]["risk"]

    return total


def route_congestion(route):
    total = 0

    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]

        total += AIRSPACE[start][end]["congestion"]

    return total  