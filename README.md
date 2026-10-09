# Aviation Emissions and Flight Path Optimization

## 1. Novelty

This project combines aviation route optimization with environmental sustainability. It evaluates flight paths using distance, fuel consumption, CO₂ emissions, risk, and congestion. A hybrid optimization approach uses a QUBO-inspired cost function and simulated annealing to identify promising routes, helping demonstrate how optimization can support greener and more efficient aviation.

## 2. Level of Qiskit Programming

The current implementation uses Python, graph-based route modeling, classical algorithms, and simulated annealing. It does not yet implement Qiskit circuits or execute quantum algorithms. Qiskit integration can be added to formulate a quantum optimization problem, construct parameterized circuits, and experiment with QAOA using a simulator.

## 3. Measurable Results and Classical Benchmarking

The system compares a classical Dijkstra shortest-distance baseline with the selected optimized route. Measurable metrics include distance (km), fuel consumption (kg), CO₂ emissions (kg), estimated delay (minutes), risk, and congestion. Actual numerical improvements must be calculated through experiments using identical airspace data and reported without assuming predefined savings.

## 4. Technical Quantum Advantage

The project provides a foundation for exploring quantum-assisted flight-path optimization. QUBO formulations can represent competing objectives, while QAOA and quantum annealing are potential approaches for future experiments. However, quantum advantage has not yet been demonstrated. It would require rigorous benchmarking against strong classical methods, including solution quality, execution time, and scalability




                           //Use Case 05 – Aviation Emissions and Flight-Path Optimisation//
                                                 Problem Statement
Aviation is a difficult sector to decarbonize because aircraft consume large amounts of fuel and produce significant CO₂ emissions.

The aim of this project is to optimize flight paths by considering:

Flight distance
Fuel consumption
CO₂ emissions
Airspace congestion
Flight risk
Delay
Conflicts
The project uses a graph-based airspace model and a hybrid optimization approach to identify a better flight path.

2. Proposed Solution
The airspace is represented as a graph.

Nodes represent airports or waypoints.
Edges represent possible flight paths.
Each edge contains distance, risk and congestion information.
Different possible routes are generated between the origin and destination.

The routes are then evaluated using fuel, CO₂, risk, delay and conflict values.

A QUBO-style cost function is used to represent the optimization problem.

Simulated annealing is then used to find the route with the lowest optimization cost.

3. Project Modules
Module 1 – Airspace Module
File: airspace.py

This module:

Creates the airspace graph.
Stores flight-path distances.
Stores risk values.
Stores congestion values.
Calculates route distance.
Calculates route risk.
Calculates route congestion.
Module 2 – Route Generation Module
File: main.py

This module:

Takes the origin and destination.
Generates possible flight paths.
Avoids repeated nodes.
Creates route candidates for optimization.
Module 3 – Emission and Fuel Module
File: metrics.py

This module calculates:

Fuel consumption
CO₂ emissions
Flight delay
Congestion penalty
The fuel calculation considers both distance and congestion.

Module 4 – QUBO Module
File: qubo.py

This module creates the optimization cost.

The objective considers:

Fuel
+
Risk
+
Delay
+
Conflicts   

