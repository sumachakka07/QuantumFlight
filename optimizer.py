# optimizer.py

import random
import math

from qubo import build_qubo


def simulated_annealing(costs, iterations=10000):

    if not costs:
        return None

    current = random.randrange(
        len(costs)
    )

    best = current

    temperature = 1000.0
    cooling_rate = 0.995

    for _ in range(iterations):

        candidate = random.randrange(
            len(costs)
        )

        current_cost = costs[current]
        candidate_cost = costs[candidate]

        difference = (
            candidate_cost
            - current_cost
        )

        if difference < 0:

            current = candidate

        else:

            probability = math.exp(
                -difference
                / max(
                    temperature,
                    0.000001
                )
            )

            if random.random() < probability:
                current = candidate

        if costs[current] < costs[best]:
            best = current

        temperature *= cooling_rate

        if temperature < 0.01:
            temperature = 0.01

    return best


def solve_hybrid(route_candidates):

    if not route_candidates:
        return None

    qubo = build_qubo(
        route_candidates
    )

    costs = [
        qubo[index]
        for index in range(
            len(route_candidates)
        )
    ]

    best_index = simulated_annealing(
        costs,
        iterations=10000
    )

    return route_candidates[
        best_index
    ] 