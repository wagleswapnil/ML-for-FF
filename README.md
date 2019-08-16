# ML-for-FF

This is a machine learning project to get an optimized set of force-field (FF) parameters for lipid molecules for a molecular dynamics (MD) simulation. The FF parameters are based on thousands of MD simulation run where the lennard-jones (LJ) parameters and partial charges were changed for the lipid atoms and some experimental quantities were calculated for these MD simulation. The aim of this project is to train a neural-network with the experimental quantities as the input vector and the LJ parameters and the partial charges as the output vector. From this trained network, a set of LJ parameters and partial charges will be obtained, when the experimental quantities (to be precise, their values in in vitro experiments) is an input vector. The author of this project is Swapnil Wagle, Max Planck Institute of Colloids and Interfaces, Potsdam, Germany.

For this project, the github commits will be made time-to-time and details for every commit will be briefly explained. All the history of the commits' details will be removed once the project is complete and only the full description of the code will be available. 

Commit on 16.08.2019: File parser code is written which reads a .itp file (gromacs format) as well as a "Fitness File" that has the values of the order parameters values for the lipid tails, both in experiments and in MD simulations.
