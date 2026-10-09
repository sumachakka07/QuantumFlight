# metrics.py

FUEL_PER_KM = 4.8
CO2_PER_KG_FUEL = 3.16


def calculate_fuel(distance, congestion):
    congestion_penalty = 1 + (congestion * 0.015)

    fuel = (
        distance
        * FUEL_PER_KM
        * congestion_penalty
    )

    return fuel


def calculate_co2(fuel):
    return fuel * CO2_PER_KG_FUEL


def calculate_delay(congestion):
    return congestion * 3


def calculate_metrics(distance, congestion):

    fuel = calculate_fuel(
        distance,
        congestion
    )

    co2 = calculate_co2(fuel)

    delay = calculate_delay(
        congestion
    )

    return {
        "distance": distance,
        "fuel": fuel,
        "co2": co2,
        "delay": delay,
        "congestion": congestion
    } 