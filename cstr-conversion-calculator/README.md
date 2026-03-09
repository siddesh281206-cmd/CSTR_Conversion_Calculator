# CSTR Conversion Calculator

## Aim
To calculate the conversion of reactant in a Continuous Stirred Tank Reactor (CSTR) for a first-order reaction.

## Objective
This program determines the fractional conversion of reactants based on reaction rate constant and residence time.

## Theory
A Continuous Stirred Tank Reactor (CSTR) is a type of reactor where reactants are continuously fed into the reactor while products are continuously removed.

For a first-order reaction, the conversion can be estimated using:

X = (k × τ) / (1 + k × τ)

Where:

- X = Conversion
- k = Reaction rate constant
- τ = Residence time

The equation shows that increasing residence time or reaction rate constant increases conversion.

## Requirements

Python 3.x

## How to Run

python cstr.py

## Example Input

k = 0.5  
τ = 3

## Example Output

Conversion of reactant = 0.6

## Applications

- Chemical reactor design
- Reaction engineering studies
- Process optimization