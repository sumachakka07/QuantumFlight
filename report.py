# report.py


def create_report(baseline, optimized):

    distance_saved = (
        baseline["distance"]
        - optimized["distance"]
    )

    fuel_saved = (
        baseline["fuel"]
        - optimized["fuel"]
    )

    co2_saved = (
        baseline["co2"]
        - optimized["co2"]
    )

    delay_change = (
        baseline["delay"]
        - optimized["delay"]
    )

    if baseline["fuel"] > 0:

        fuel_percentage = (
            fuel_saved
            / baseline["fuel"]
        ) * 100

    else:
        fuel_percentage = 0

    if baseline["co2"] > 0:

        co2_percentage = (
            co2_saved
            / baseline["co2"]
        ) * 100

    else:
        co2_percentage = 0

    report = f"""
AVIATION EMISSIONS & FLIGHT-PATH OPTIMISATION
Quantum Hybrid Optimisation Prototype

BASELINE ROUTE

Route       : {" → ".join(baseline["route"])}
Distance    : {baseline["distance"]:.2f} km
Fuel        : {baseline["fuel"]:.2f} kg
CO2         : {baseline["co2"]:.2f} kg
Delay       : {baseline["delay"]:.2f} minutes
Risk        : {baseline["risk"]}
Conflicts   : {baseline["conflicts"]}


OPTIMIZED ROUTE

Route       : {" → ".join(optimized["route"])}
Distance    : {optimized["distance"]:.2f} km
Fuel        : {optimized["fuel"]:.2f} kg
CO2         : {optimized["co2"]:.2f} kg
Delay       : {optimized["delay"]:.2f} minutes
Risk        : {optimized["risk"]}
Conflicts   : {optimized["conflicts"]}


ENVIRONMENTAL IMPACT

Distance saved : {distance_saved:+.2f} km
Fuel saved     : {fuel_saved:+.2f} kg
CO2 reduced    : {co2_saved:+.2f} kg
Delay change   : {delay_change:+.2f} minutes
Fuel reduction : {fuel_percentage:.2f}%
CO2 reduction  : {co2_percentage:.2f}%


OPTIMISATION METHOD

Airspace Graph
      ↓
Route Generation
      ↓
QUBO Cost Function
      ↓
Simulated Annealing
      ↓
Optimized Flight Path
      ↓
Fuel & CO2 Analysis
"""

    return report


def print_report(baseline, optimized):

    report = create_report(
        baseline,
        optimized
    )

    print(report)

    with open(
        "optimization_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print(
        "Report saved: optimization_report.txt"
    ) 