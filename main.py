# main.py

from airspace import (
    AIRSPACE,
    route_distance,
    route_risk,
    route_congestion
)

from metrics import calculate_metrics
from optimizer import solve_hybrid
from report import print_report


def find_all_routes(
    graph,
    start,
    destination,
    max_stops=5
):

    routes = []

    def dfs(
        current,
        path,
        visited
    ):

        if current == destination:

            routes.append(
                path.copy()
            )

            return

        if len(path) - 1 >= max_stops:
            return

        for neighbour in graph.get(
            current,
            {}
        ):

            if neighbour not in visited:

                visited.add(
                    neighbour
                )

                path.append(
                    neighbour
                )

                dfs(
                    neighbour,
                    path,
                    visited
                )

                path.pop()

                visited.remove(
                    neighbour
                )

    dfs(
        start,
        [start],
        {start}
    )

    return routes


def create_route_data(routes):

    route_data = []

    for route in routes:

        distance = route_distance(
            route
        )

        risk = route_risk(
            route
        )

        congestion = route_congestion(
            route
        )

        metrics = calculate_metrics(
            distance,
            congestion
        )

        conflicts = sum(
            1
            for i in range(
                len(route) - 1
            )
            if AIRSPACE[
                route[i]
            ][
                route[i + 1]
            ]["risk"] >= 3
        )

        route_data.append({

            "route": route,

            "distance": distance,

            "risk": risk,

            "congestion": congestion,

            "fuel": metrics["fuel"],

            "co2": metrics["co2"],

            "delay": metrics["delay"],

            "conflicts": conflicts

        })

    return route_data


def main():

    print()
    print(
        "AVIATION EMISSIONS & FLIGHT-PATH OPTIMISATION"
    )

    print(
        "Quantum Hybrid Optimisation Prototype"
    )

    print()

    origin = "A"
    destination = "F"

    print("Flight Information")

    print(
        f"Origin          : {origin}"
    )

    print(
        f"Destination     : {destination}"
    )

    print(
        "Airspace Model  : Graph-based"
    )

    print(
        "Optimisation    : QUBO + Simulated Annealing"
    )

    print(
        "Objective       : Fuel + Risk + Delay + Conflicts"
    )

    print()

    print(
        "Generating possible flight paths..."
    )

    routes = find_all_routes(
        AIRSPACE,
        origin,
        destination
    )

    route_candidates = create_route_data(
        routes
    )

    print(
        f"Possible routes found: {len(route_candidates)}"
    )

    print()

    print("Candidate Flight Paths")
    print()

    for index, route in enumerate(
        route_candidates,
        1
    ):

        route_name = " → ".join(
            route["route"]
        )

        print(
            f"{index:2}. "
            f"{route_name:<25}"
            f" Distance: {route['distance']:>4.0f} km"
            f"  Fuel: {route['fuel']:>7.1f} kg"
            f"  CO2: {route['co2']:>8.1f} kg"
            f"  Risk: {route['risk']}"
            f"  Conflicts: {route['conflicts']}"
        )

    print()

    print(
        "Running QUBO + hybrid optimisation..."
    )

    baseline = min(
        route_candidates,
        key=lambda route:
        route["distance"]
    )

    optimized = solve_hybrid(
        route_candidates
    )

    print_report(
        baseline,
        optimized
    )


if __name__ == "__main__":
    main() 