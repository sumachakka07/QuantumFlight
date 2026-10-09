# Aviation Emissions and Flight Path Optimization

## 1. Novelty

This project combines aviation route optimization with environmental sustainability. It evaluates flight paths using distance, fuel consumption, CO₂ emissions, risk, and congestion. A hybrid optimization approach uses a QUBO-inspired cost function and simulated annealing to identify promising routes, helping demonstrate how optimization can support greener and more efficient aviation.

## 2. Level of Qiskit Programming

The current implementation uses Python, graph-based route modeling, classical algorithms, and simulated annealing. It does not yet implement Qiskit circuits or execute quantum algorithms. Qiskit integration can be added to formulate a quantum optimization problem, construct parameterized circuits, and experiment with QAOA using a simulator.

## 3. Measurable Results and Classical Benchmarking

The system compares a classical Dijkstra shortest-distance baseline with the selected optimized route. Measurable metrics include distance (km), fuel consumption (kg), CO₂ emissions (kg), estimated delay (minutes), risk, and congestion. Actual numerical improvements must be calculated through experiments using identical airspace data and reported without assuming predefined savings.

## 4. Technical Quantum Advantage

The project provides a foundation for exploring quantum-assisted flight-path optimization. QUBO formulations can represent competing objectives, while QAOA and quantum annealing are potential approaches for future experiments. However, quantum advantage has not yet been demonstrated. It would require rigorous benchmarking against strong classical methods, including solution quality, execution time, and scalability


# Use Case 05 – Aviation Emissions and Flight-Path Optimisation

## 1. Problem Statement

Aviation is a difficult sector to decarbonize because aircraft consume large amounts of fuel and produce significant CO₂ emissions.

The aim of this project is to optimize flight paths by considering:

* Flight distance
* Fuel consumption
* CO₂ emissions
* Airspace congestion
* Flight risk
* Delay
* Airspace conflicts

The project uses a graph-based airspace model and a hybrid optimization approach to identify better flight paths.

## 2. Proposed Solution

The airspace is represented as a graph.

* **Nodes:** Represent airports or waypoints.
* **Edges:** Represent possible flight paths.
* **Edge information:** Includes distance, risk, and congestion values.

Different possible routes are generated between the origin and destination. These routes are evaluated using fuel consumption, CO₂ emissions, risk, delay, and conflict values.

A QUBO-style cost function is used to represent the optimization problem. Simulated annealing is then used to search for a route combination with a lower optimization cost.

## 3. Project Modules

### Module 1 – Airspace Module

**File:** `airspace.py`

This module:

* Creates the airspace graph.
* Stores flight-path distances.
* Stores risk values.
* Stores congestion values.
* Calculates route distance.
* Calculates route risk.
* Calculates route congestion.

### Module 2 – Route Generation Module

**File:** `main.py`

This module:

* Takes the origin and destination.
* Generates possible flight paths.
* Avoids repeated nodes.
* Creates route candidates for optimization.

### Module 3 – Emission and Fuel Module

**File:** `metrics.py`

This module calculates:

* Fuel consumption.
* CO₂ emissions.
* Flight delay.
* Congestion penalty.

The fuel calculation considers distance and congestion.

### Module 4 – QUBO Module

**File:** `qubo.py`

This module creates the optimization cost function.

The objective considers:

**Fuel + Risk + Delay + Conflicts**

The QUBO model allows the route-selection problem to be expressed as a binary optimization problem.

## 4. Optimization Algorithm

The project uses Simulated Annealing to search for a good solution to the QUBO problem.

The optimization process:

1. Generates candidate flight paths.
2. Calculates the cost of each candidate.
3. Builds the QUBO cost function.
4. Runs the optimization algorithm.
5. Selects routes based on the resulting solution.
6. Evaluates fuel consumption, emissions, delays, and conflicts.

## 5. Technologies Used

* Python
* NumPy
* NetworkX
* QUBO (Quadratic Unconstrained Binary Optimization)
* Simulated Annealing
* Optional: D-Wave Ocean SDK and Neal sampler

## 6. Expected Outcome

The project aims to identify improved flight-path combinations that balance fuel consumption, CO₂ emissions, airspace congestion, risk, and delay.

The results are compared with a baseline solution to evaluate the effectiveness of the optimization approach.


Conflicts   

