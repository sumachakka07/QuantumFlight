# qubo.py

FUEL_WEIGHT = 1.0
RISK_WEIGHT = 80.0
DELAY_WEIGHT = 20.0
CONFLICT_WEIGHT = 200.0


def calculate_qubo_cost(route):

    fuel = route["fuel"]
    risk = route["risk"]
    delay = route["delay"]
    conflicts = route["conflicts"]

    cost = (
        FUEL_WEIGHT * fuel
        + RISK_WEIGHT * risk
        + DELAY_WEIGHT * delay
        + CONFLICT_WEIGHT * conflicts
    )

    return cost


def build_qubo(route_candidates):

    qubo = {}

    for index, route in enumerate(route_candidates):
        qubo[index] = calculate_qubo_cost(route)

    return qubo 