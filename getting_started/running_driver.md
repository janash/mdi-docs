# Driver Use Tutorial: Running an AIMD Simulation

:::{admonition} Prerequisites

Completion of this tutoral requires installing Docker.
Docker is a platform that allows you to run software in a container, which is a standalone environment with everything needed to run the software, including the software itself and all its dependencies.
If you don't have Docker installed already, we recommend downloading and installing [Docker Desktop](https://www.docker.com/products/docker-desktop) for your operating system.

You will also need to have `mdimechanic`. 
We recommend using an environment manager like `conda` or `pipenv` to install `mdimechanic` in a clean environment.

To install `mdimechanic`, you can use the following command:

```bash
pip install mdimechanic
```

We also recommend using `git`, though it is not absolutely necessary.

:::

In this tutorial we will use an MDI driver to perform a simple *Ab Initio* Molecular Dynamics (AIMD) simulation, using Quantum ESPRESSO (QE) to calculate forces and LAMMPS to update the atomic coordinates each time step.
In an AIMD simulation, the forces on the atoms are calculated using quantum mechanics, and the atomic coordinates are updated using classical mechanics.
Thus, we will use a QM code (in this case, Quantum ESPRESSO) to calculate the forces, and an MM code (in this case, LAMMPS) to perform the time integration.

LAMMPS is a code that simulates chemical systems using molecular mechanics (MM) force fields, which are computationally very efficient to evaluate and can be used for lengthy dynamics simulations of large systems.
Quantum ESPRESSO is a code that runs quantum mechanics (QM) calculations, which are much more computationally expensive, but can be applied much more straigtforwardly to chemically reactive systems and other specific use cases.

MM codes like LAMMPS often offer time integration features that are not widely available in QM codes, so it can be desirable to be able to mix the time integration functionality of an MM code with the force evaluation functionality of a QM code.

Although we will be using QE and LAMMPS as the MDI engines in this tutorial, you could do similar calculations using other MDI engines. This means you could switch out LAMMPS for another MM code, or QE for another QM code, and the MDI driver would still work as long as you had files to set up the input of the new codes.

A list of codes that support MDI can be found \ref mdi_ecosystem "here".

## Obtaining the MDI Driver and Engines

Often in computational chemistry, one of the hardest steps to performing a calculation is setting up the software.
Fortunately, we have compiled Docker images that contain the MDI-enabled codes we will use in this tutorial and can use for other calculations. 
This means you do not have to compile the codes, you just have to install Docker and "pull" (download) the images.

To get started with this tutorial, first download the necessary files using `git` (note: You can also download the files as a zip file from the GitHub repository if you don't have `git` installed using [this link](https://github.com/janash/MDI_AIMD_user_tutorial/archive/refs/heads/main.zip)):


:::{tab-set-code}
```bash
git clone git@github.com:janash/MDI_AIMD_user_tutorial.git
cd MDI_AIMD_user_tutorial
```
:::

## Setting Up the AIMD Simulation

When using an already-made MDI driver, you will be using a software package that someone else has prepared that performs some kind of molecular science calculation.
In this case, the MDI Driver performs ab-initio molecular dynamics (AIMD) calculations.
As far as the MDI driver is concerned, the only thing you need to know is how to run it and what files it needs to run.
You will need to specify what program you would like to use for the QM portion, and what program you would like to use for the MM portion along with input files for your choice of program.
The MDI driver will then take care of the rest.

To summarize, to use the AIMD Driver, you will need to provide:

* Input files for your MDI-enabled QM program of choice.
* Input files for your MDI-enabled MM program of choice.

This means you have freedom over your input parameters for each program, and freedom over the input system that you simulate.

For the purposes of this tutorial, we will use prepared input files to simulate a small water system using Quantum ESPRESSO and LAMMPS. 
You can find input files for this simulation in `simulation_files/starting` in the repository you just cloned.

When viewing the contents of this directory, you will see inputs for lammps (`lammps.in`, `lammps.data`) and input files for Quantum ESPRESSO (`qe.in`, `pseudo` - directory containing pseudopotential parameters).
If you wanted to simulate a different system using AIMD, you would use the same driver, but change these input files.

To build our AIMD simulation program, we will execute the following command:

:::{tab-set-code}
```bash
mdimechanic build
```
:::

## Running the AIMD Simulation
After you have the input files, you can run the AIMD simulation using the MDI driver.
When we use this AIMD Driver, LAMMPS and Quantum ESPRESSO will both be running, but the Driver will be sending information between the two programs. 
This Driver works in the following way:

1. Both programs are initialized with their respective input files.
2. Forces are calculated in our water system using Quantum ESPRESSO.
3. The AIMD Driver retrieves the forces from Quantum ESPRESSO and replaces the forces in the LAMMPS program for that time-step with these forces.
4. LAMMPS is used to update the atomic coordinates using the forces from Quantum ESPRESSO.
5. The AIMD Driver retrieves the new atomic coordinates from LAMMPS and sends them to Quantum ESPRESSO to calculate the forces for the next time step.

Our output will be the atomic coordinates and forces at each time step written by LAMMPS, which we can use to analyze the dynamics of our water system.

To start our simulation, we'll first copy our starting files to a new directory to ensure that we don't overwrite them. 
Note that you must use this exact file name for the configuration of our tutorial.

:::{tab-set-code}
```bash
mkdir simulation_files/working
cp -r simulation_files/starting/* simulation_files/working
```
:::

From the top level of your cloned repository, run the following command to start the AIMD simulation:

:::{tab-set-code}
```bash 
mdimechanic run --name multiple
```
:::

This will start an AIMD simulation. 
You may have to wait a minute or two for this to run. 
During this time, you will not see any message to the screen, but you should see files changing in your `simulation_files/working` directory.

## Examining the Output

Your `simulation_files/working` directory should now contain a number of files, including `dump.lammpstrj`, `log.lammps` and `qe.out`. 
If you are familiar with any of these programs, the output files will look the same as they usually do.

## Analyzing the Results

Watch trajectory in VMD.

Analyzie using MDAnalysis?