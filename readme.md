# Aviation Emissions and Flight-Path Optimisation

## Use Case 05 – Aviation Emissions and Flight-Path Optimisation

###  Problem Statement

Aviation is a difficult sector to decarbonize because aircraft consume large amounts of fuel and produce significant CO₂ emissions.

The aim of this project is to optimize flight paths by considering:

- Flight distance
- Fuel consumption
- CO₂ emissions
- Airspace congestion
- Flight risk
- Delay
- Conflicts

The project uses a graph-based airspace model and a hybrid optimization approach to identify a better flight path.

---

## 2. Proposed Solution

The airspace is represented as a graph.

- Nodes represent airports or waypoints.
- Edges represent possible flight paths.
- Each edge contains distance, risk and congestion information.

Different possible routes are generated between the origin and destination.

The routes are then evaluated using fuel, CO₂, risk, delay and conflict values.

A QUBO-style cost function is used to represent the optimization problem.

Simulated annealing is then used to find the route with the lowest optimization cost.

---

## 3. Project Modules

### Module 1 – Airspace Module

**File:** `airspace.py`

This module:

- Creates the airspace graph.
- Stores flight-path distances.
- Stores risk values.
- Stores congestion values.
- Calculates route distance.
- Calculates route risk.
- Calculates route congestion.

---

### Module 2 – Route Generation Module

**File:** `main.py`

This module:

- Takes the origin and destination.
- Generates possible flight paths.
- Avoids repeated nodes.
- Creates route candidates for optimization.

---

### Module 3 – Emission and Fuel Module

**File:** `metrics.py`

This module calculates:

- Fuel consumption
- CO₂ emissions
- Flight delay
- Congestion penalty

The fuel calculation considers both distance and congestion.

---

### Module 4 – QUBO Module

**File:** `qubo.py`

This module creates the optimization cost.

The objective considers:

```text
Fuel
+
Risk
+
Delay
+
Conflicts   