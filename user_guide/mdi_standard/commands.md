(command_list)=
#  Command List

The following is a list of commands that are officially part of the MDI standard.





## recv_cdensity <CDENSITY

The engine sends the Cartesian coordinates of a set of grid points.
This command is intended to be used in conjuction with the recv_ndensity and recv_density commands; these three commands enable a driver to acquire the electronic density distribution of an engine in a grid representation.
See the recv_density command for more details.

\par
- **Data Type:** `MDI_DOUBLE` 
- **Quantity:** `3 * NDENSITY`



## send_cell >CELL

The driver sends a set of cell vectors to the engine, which resizes its simulation cell to the dimensions specified by the cell vectors.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 9 

- **Format:** The first 3 values correspond to the x, y, and z values, respectively, of the first cell vector.
The next 3 values correspond to the x, y, and z values, respectively, of the second cell vector.
The next 3 values correspond to the x, y, and z values, respectively, of the third cell vector. 




## recv_cell <CELL

The engine sends a set of cell vectors to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 9 

- **Format:** The first 3 values correspond to the x, y, and z values, respectively, of the first cell vector.
The next 3 values correspond to the x, y, and z values, respectively, of the second cell vector.
The next 3 values correspond to the x, y, and z values, respectively, of the third cell vector. 



## send_cell_displ >CELL_DISPL

The driver sends a displacement vector to the engine, which adjusts the origin of its simulation cell to the value of the displacement vector.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 3 

- **Format:** The 3 values correspond to the x, y, and z values, respectively, of the simulation cell displacement vector. 



## recv_cell_displ <CELL_DISPL

The engine sends the displacement vector of the origin of its simulation cell to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 3 

- **Format:** The 3 values correspond to the x, y, and z values, respectively, of the simulation cell displacement vector. 



## send_charges >CHARGES

The driver sends a set of atomic charges to the engine, which replaces its atomic charges with those sent by the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** `NATOMS 

- **Format:** Sequentially ascending order of atomic index 




## recv_charges <CHARGES

The engine sends a set of atomic charges to the driver, in the same format as specified for the `>CHARGES command.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** `NATOMS 

- **Format:** Sequentially ascending order of atomic index



## send_clattice >CLATTICE

This command, along with the `>NLATTICE and `>LATTICE commands, allows the driver to assign a lattice of point charges to an engine, which incorporates the effects of these charges in all further calculations.
After sending this command, the driver sends the coordinates of each of the point charges to the engine.
Prior to sending this command, the driver must have set the number of point charges using the `>NLATTICE command.

This command is primarily intended for use with gas-phase quantum mechanics codes.
For an alternative command that is more appropriate for plane wave quantum mechanics codes, see the `>POTENTIAL command.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NLATTICE </c> 

- **Format:** Sequentially ascending order of lattice charge index, with the coordinates for each individual lattice charge being provided in xyz order






## send_coords >COORDS

The driver sends a set of atomic coordinates to the engine, which replaces its atomic coordinates with those sent by the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index, with the coordinates for each individual atom being provided in xyz order 




## recv_coords <COORDS

The engine sends a set of atomic coordinates to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index, with the coordinates for each individual atom being provided in xyz order



## send_cpotential >CPOTENTIAL

The driver sends the Cartesian coordinates of a set of grid points.
This command is intended to be used in conjuction with the send_npotential and send_potential commands; these three commands enable a driver to set an external potential that is incorporated into a subsequent scf_command command.
See the send_potential command for more details.

Before sending this command, the driver must have first sent the number of grid points used to represent the potential via the send_npotential command.
It is also necessary that the driver send the values of the grid points via the send_cpotential command prior to any subsequent scf_command command.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NPOTENTIAL </c>






## recv_density <DENSITY

The engine sends the value of its electronic density on a set of grid points.
This command is intended to be used in conjuction with the recv_ndensity and recv_cdensity commands; these three commands enable a driver to acquire the electronic density distribution of an engine in a grid representation.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** `NDENSITY



## recv_dimensions <DIMENSIONS

The engine sends basic information about the dimensionality of its system to the driver.
For each of its three cell vectors (see the `<CELL command) the engine sends an integer that indicates whether that dimension is represented as periodic, non-periodic, or not represented at all (in the case of 1d or 2d systems).
The possible values for each cell vector are:

   - 0: Not represented
   - 1: Non-periodic
   - 2: Periodic

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 3 

- **Format:** Sequentially ascending order of cell vector (see the <CELL command)



## send_mult >ELEC_MULT

The driver sends the electronic multiplicity of the system to the engine.
This command is typically only appropriate for quantum mechanics engines.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1



## recv_mult <ELEC_MULT

The engine sends the electronic multiplicity of its system to the driver.
This command is typically only appropriate for quantum mechanics engines.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1



## recv_elements <ELEMENTS

The engine sends the atomic number of each atom in its system to the driver.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** `NATOMS 

- **Format:** Sequentially ascending order of atomic index



## send_elements >ELEMENTS

The driver sends a set of atomic numbers to the engine, which replaces the atomic number of each atom in its system with the values sent by the driver.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** `NATOMS 

- **Format:** Sequentially ascending order of atomic index



## recv_energy <ENERGY

If the engine is at the `@DEFAULT node, it calculates and sends its total energy to the driver.
If the engine has previously calculated the energy of the system, and no intervening commands from the driver could have changed the energy, the engine is permitted to send the previously calculated energy instead of recalculating it.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated total energy to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1










## send_forces >FORCES

The driver sends a set of atomic forces to the engine, which replaces its internal forces with the forces sent by the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index, with the forces for each individual atom being provided in xyz order 




## send_add_forces >+FORCES

The driver sends a set of atomic forces to the engine, which adds the forces sent by the driver to its internal forces.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index, with the forces for each individual atom being provided in xyz order 




## recv_forces <FORCES

If the engine is at the `@DEFAULT node, it calculates and sends its atomic forces to the driver.
These forces include all force contributions, including the force contributions associated with any constraint algorithm (e.g. SHAKE, RATTLE, etc.).
If the engine has previously calculated the atomic forces of the system, and no intervening commands from the driver could have changed the atomic forces, the engine is permitted to send the previously calculated atomic forces instead of recalculating them.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated atomic forces to the driver.
Depending on the engine's current node, these forces may not include all contributions to the atomic forces.
See the descriptions of the different nodes for more details.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index, with the forces for each individual atom being provided in xyz order





## recv_ke <KE

If the engine is at the `@DEFAULT node, it calculates and sends its total kinetic energy to the driver.
If the engine has previously calculated the energy of the system, and no intervening commands from the driver could have changed the energy, the engine is permitted to send the previously calculated energy instead of recalculating it.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated total kinetic energy to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1



## recv_ke_elec <KE_ELEC

If the engine is at the `@DEFAULT node, it calculates and sends the total kinetic energy of all electrons in its system to the driver.
If the engine has previously calculated the energy of the system, and no intervening commands from the driver could have changed the energy, the engine is permitted to send the previously calculated energy instead of recalculating it.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated electronic kinetic energy to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1



## recv_ke_nuc <KE_NUC

If the engine is at the `@DEFAULT node, it calculates and sends the total kinetic energy of all nuclei in its system to the driver.
If the engine has previously calculated the energy of the system, and no intervening commands from the driver could have changed the energy, the engine is permitted to send the previously calculated energy instead of recalculating it.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated nuclear kinetic energy to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1



## send_labels <LABELS

The engine sends a label for each atom in its system.
"Labels" are intended primarily for the purpose of providing a human-readable identifier for each of the atoms, and do not have a standardized physical meaning.
It is recommended that the labels correspond to the element of each atom (i.e., "H", "He", "Li", etc.), a name associated with atoms of a particular type (i.e., "Carboxyl_Hydrogen", "Methyl_Hydrogen"), or a similarly descriptive term.
The atom labels may correspond to a number identifier (i.e., "1", "2", "3", etc.) in cases where more descriptive labels are not practical, but note that such labels must be represented using the `MDI_CHAR data type, as indicated below.
It is required that atoms having different physical properties (i.e., different force field terms in a molecular mechanics simulation or different nuclear charges in a quantum chemistry simulation) have different labels.

\par
- **Data Type:** `MDI_CHAR 

- **Quantity:** `MDI_LABEL_LENGTH * `NATOMS 

- **Format:** An array of characters corresponding to the label of each atom in ascending order of atomic index, with each label consisting of `MDI_LABEL_LENGTH characters and being padded with spaces (" ") where necessary 




## send_lattice >LATTICE

This command, along with the `>NLATTICE and `>CLATTICE commands, allows the driver to assign a lattice of point charges to an engine, which incorporates the effects of these charges in all further calculations.
After sending this command, the driver sends the charges of each of the point charges to the engine.
Prior to sending this command, the driver must have set the number of point charges using the `>NLATTICE command.

This command is primarily intended for use with gas-phase quantum mechanics codes.
For an alternative command that is more appropriate for plane wave quantum mechanics codes, see the `>POTENTIAL command.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> NLATTICE </c> 

- **Format:** Sequentially ascending order of lattice charge index



## recv_lattice_forces <LATTICE_FORCES

If the engine is at the `@DEFAULT node, it calculates and sends the forces on any lattice charges (which must have previously assigned with the `>LATTICE command) to the driver.
Prior to sending this command, the driver must have set the number, coordinates, and magnitudes of the lattice charges using the `>NLATTICE, `>CLATTICE, and `>LATTICE commands.
These forces must include only electrostatic interactions between the lattice charges and the atomic nuclei, and between the lattice charges and any electrons.
They must not include electrostatic interactions between the lattice charges and other lattice charges.
If the engine has previously calculated these forces, and no intervening commands from the driver could have changed the forces, the engine is permitted to send the previously calculated forces instead of recalculating them.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated lattice forces to the driver.

This command is primarily intended for use with gas-phase quantum mechanics codes.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NLATTICE </c> 

- **Format:** Sequentially ascending order of lattice charge index, with the forces for each individual lattice charge being provided in xyz order



## recv_masses <MASSES

The engine sends the driver the mass of each of the atoms.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> <NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index




## send_Monkhorst_Pack >MONKHORST-PACK_NPOINTS

This command is typically expected for use with plane wave DFT engines.
The driver sends the engine the number of k-points to generate on a Monkhorst-Pack grid.
The engine then uses the k-points generated on this Monkhorst-Pack grid for all further simulations.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** <c> 3 </c> 

- **Format:** The number of k-points to generate along each vector of the Brillouin zone, in ascending order of vector.




## send_Monkhorst_Pack_shift >MONKHORST-PACK_SHIFT

This command is typically expected for use with plane wave DFT engines.
The driver sends the engine a set of values that indicate the extent to which a set of k-points on a Monkhorst-Pack grid should be displaced relative to the original (non-displaced) Monkhorst-Pack grid.
The engine then uses the shifted k-points for all further simulations.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 </c> 

- **Format:** The fraction of a grid step by which the k-points should be displaced, in ascending order of vector.  A value of 0.0 indicates no displacement along the corresponding vector, while a value of 0.5 indicates a displacement of half a grid step in along the corresponding vector.  Note that some engines can only support values of 0.0 or 0.5.




## send_name <NAME

The engine sends the driver a string that corresponds to the argument of `-name in the MDI initialization options.
This argument allows a driver to identify the purpose of connected engine codes within the simulation.
For example, a particular QM/MM driver might require a connection with a single MM code and a single QM code, with the expected name of the MM code being "MM" and the expected name of the QM code being "QM".
After initializing MDI and accepting communicators to the engines, the driver can use this command to identify which of the engines is the MM code and which is the QM code.

\par
- **Data Type:** `MDI_CHAR 

- **Quantity:** <c> MDI_NAME_LENGTH </c>



## recv_natoms <NATOMS

The engine sends the driver the number of atoms in the engine's system.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1



## recv_ndensity <NDENSITY

The engine sends the number of grid points it is using to represent its electronic density on a grid.
This command is intended to be used in conjuction with the recv_cdensity and recv_density commands; these three commands enable a driver to acquire the electronic density distribution of an engine in a grid representation.
See the recv_density command for more details.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1



## send_nlattice >NLATTICE

This command, along with the `>CLATTICE and `>LATTICE commands, allows the driver to assign a lattice of point charges to an engine, which incorporates the effects of these charges in all further calculations.
After sending this command, the driver sends the number of point charges to the engine.
This command must be sent before either the `>CLATTICE or `>LATTICE commands can be sent.

This command is primarily intended for use with gas-phase quantum mechanics codes.
For an alternative command that is more appropriate for plane wave quantum mechanics codes, see the `>POTENTIAL command.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1 




## send_npotential >NPOTENTIAL

The driver sends the number of grid points it is using to represent a potential on a grid.
This command is intended to be used in conjuction with the send_cpotential and send_potential commands; these three commands enable a driver to set an external potential that is incorporated into a subsequent scf_command command.
See the send_potential command for more details.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1



## send_potential >POTENTIAL

The driver sends an set of values to the engine that correspond to a potential on a grid.
If an scf_command command is later issued, this potential will be incorporated into the SCF calculation as an external potential.

Before sending this command, the driver must have first sent the number of grid points used to represent the potential via the send_npotential command.
It is also necessary that the driver send the Cartesian coordinates of the grid points via the send_cpotential command prior to any subsequent scf_command command.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** `NPOTENTIAL



## recv_pe <PE

If the engine is at the `@DEFAULT node, it calculates and sends its total potential energy to the driver.
If the engine has previously calculated the energy of the system, and no intervening commands from the driver could have changed the energy, the engine is permitted to send the previously calculated energy instead of recalculating it.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated total potential energy to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1



## recv_pe_elec <PE_ELEC

If the engine is at the `@DEFAULT node, it calculates and sends its electronic potential energy to the driver.
The electronic potential energy is defined as including all interactions between the electrons and any other particles or fields in the system.
It also includes the interactions between the electrons and themselves.
If the engine has previously calculated the energy of the system, and no intervening commands from the driver could have changed the energy, the engine is permitted to send the previously calculated energy instead of recalculating it.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated electronic potential energy to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1



## recv_pe_nuc <PE_NUC

If the engine is at the `@DEFAULT node, it calculates and sends its nuclear potential energy to the driver.
The nuclear potential energy is defined as including all interactions between the nuclei and any other particles or fields in the system, excluding any electrons.
It also includes the interactions between the nuclei and themselves.
If the engine has previously calculated the energy of the system, and no intervening commands from the driver could have changed the energy, the engine is permitted to send the previously calculated energy instead of recalculating it.

If the engine is not at the `@DEFAULT node, it sends its most recently calculated electronic potential energy to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1







## send_spin_polarization <SPIN_POLARIZATION

The engine sends a value that indicates the manner in which it is currently simulating spin polarization.
This command is typically intended for use with plane wave DFT engines.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1 

- **Format:** A value of 0 indicates that simulations will be performed in a non-spin-polarized manner.  A value of 1 indicates that simulations will be performed in a spin-polarized manner, within the local spin density approximation (LSDA).  A value of 2 indicates that simulations will be performed in a spin-polarized, noncollinear manner.



## recv_spin_polarization >SPIN_POLARIZATION

The driver sends a value that indicates the manner in which spin polarization should be simulated by the engine.
This command is typically intended for use with plane wave DFT engines.

\par
- **Data Type:** `MDI_INT 

- **Quantity:** 1 

- **Format:** A value of 0 indicates that simulations should be performed in a non-spin-polarized manner.  A value of 1 indicates that simulations should be performed in a spin-polarized manner, within the local spin density approximation (LSDA).  A value of 2 indicates that simulations should be performed in a spin-polarized, noncollinear manner.



## send_stress <STRESS

The engine sends its virial stress tensor to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 9 

- **Format:** The tensor components are sent in row-major order (xx, xy, xz, yx, yy, yz, zx, zy, zz). 




## recv_stress >STRESS

The driver sends a virial stress tensor to the engine, which replaces its internal stress tensor with the stress tensor sent by the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 9 

- **Format:** The tensor components are sent in row-major order (xx, xy, xz, yx, yy, yz, zx, zy, zz). 




## send_totcharge >TOTCHARGE

The driver sends a value for the total charge of the system, including electron and nuclear charges, to the engine, which adjusts the number of electrons present in its system to the value required to reproduce the value sent by the driver.
This command is typically only appropriate for quantum mechanics engines.
Engines that support this command are not required to support non-integer charges; they are permitted to produce an error message if the value received deviates by more than 10^-12 from an integer, and to otherwise round the value received to the nearest integer.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1



## recv_totcharge <TOTCHARGE

The engine sends the total charge of its system, including electron and nuclear charges, to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** 1



## send_velocities >VELOCITES

The driver sends a set of atomic velocities to the driver, which replaces its atomic velocities with those provided by the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index, with the velocities for each individual atom being provided in xyz order



## recv_velocities <VELOCITES

The engine sends the velocities of the atoms in its system to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 3 * NATOMS </c> 

- **Format:** Sequentially ascending order of atomic index, with the velocities for each individual atom being provided in xyz order



## recv_version <VERSION

The engine sends the version number of the MDI Library to which it is linked to the driver.

\par
- **Data Type:** `MDI_DOUBLE 

- **Quantity:** <c> 1 </c> 





**/


// >CELL: Define whether the atomic coordinates are scaled.
// >CELL: Describe in detail the format of the cell coordinates
// <FORCES: Need to clarify when forces are recalculated.
// <PRE-FORCES: Need to clarify when forces are recalculated.
// >STRESS: Add commands for stresses
// >STRESS: Describe in detail the format of the stress tensor
// >STRESS: Clarify when stresses are recalculated
