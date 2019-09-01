# ML-for-FF

This is a machine learning project to get an optimized set of force-field (FF) parameters for lipid molecules for a molecular dynamics (MD) simulation. The FF parameters are based on thousands of MD simulation run where the lennard-jones (LJ) parameters and partial charges were changed for the lipid atoms and some experimental quantities were calculated for these MD simulation. The aim of this project is to train a neural-network with the experimental quantities as the input vector and the LJ parameters and the partial charges as the output vector. From this trained network, a set of LJ parameters and partial charges will be obtained, when the experimental quantities (to be precise, their values in in vitro experiments) is an input vector. The author of this project is Swapnil Wagle, Max Planck Institute of Colloids and Interfaces, Potsdam, Germany.

For this project, the github commits will be made time-to-time and details for every commit will be briefly explained. All the history of the commits' details will be removed once the project is complete and only the full description of the code will be available. 

Commits on 16.08.2019 and 22.08.2019: File parser code is written which reads a .itp file (gromacs format) as well as a "Fitness File" that has the values of the order parameters values for the lipid tails, both in experiments and in MD simulations.

Commit on 26.08.2019: The reader program is almost completed. It reads the itp and txt (containg the output values of order parameters, obtained from MD simulaitons) and generated the input and output vectors, to be read by the subsequent program (the neural network).

Commit on 01.09.2019: The readrer program is completed. It parses the txt and itp files and yields the input and output venctors as numpy arrays!
