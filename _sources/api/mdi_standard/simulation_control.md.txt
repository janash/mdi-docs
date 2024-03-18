# Simulation Control and Node Management 

Commands that influence the flow of the simulation, such as starting or stopping processes, initializing different types of simulations. Each of these commands is used with the `MDI_Send_Command` function.

## Simulation Initialization

### `@INIT_MC`: Initialize Monte Carlo Simulation

The engine performs any initialization operations that are necessary before a Monte Carlo simulation can be performed, proceeding to the `@INIT_MC` node.

#### Example
::::{tab-set}

:::{tab-item} Python

```python
import mdi

# connect to the engine
mdi_engine = mdi.MDI_Accept_Communicator()

# initialize a Monte Carlo simulation
mdi.MDI_Send_Command("@INIT_MC", mdi_engine) 
```

:::

:::{tab-item} C++

```cpp
#include "mdi.h"

// connect to the engine
MDI_Comm mdi_engine = MDI_Accept_Communicator();

// initialize a Monte Carlo simulation
MDI_Send_Command("@INIT_MC", mdi_engine);
```

:::

::::

### `@INIT_MD`: Initialize Molecular Dynamics Simulation

The engine performs any initialization operations that are necessary before a molecular dynamics simulation can be performed, proceeding to the `@INIT_MD` node.

```{admonition} Warning
:class: caution

This command may change the engine's atomic coordinates under certain circumstances, such as if the SHAKE algorithm is used.
```

#### Example
::::{tab-set}

:::{tab-item} Python

```python
import mdi

# connect to the engine
mdi_engine = mdi.MDI_Accept_Communicator()

# initialize a Monte Dynamics simulation
mdi.MDI_Send_Command("@INIT_MD", mdi_engine) 
```

:::

:::{tab-item} C++

```cpp
#include "mdi.h"

// connect to the engine
MDI_Comm mdi_engine = MDI_Accept_Communicator();

// initialize a Molecular Dynamics simulation
MDI_Send_Command("@INIT_MD", mdi_engine);
```

:::

::::


### `@INIT_OPTG`: Initialize Geometry Optimization

The engine performs any initialization operations that are necessary before a geometry optimization can be performed, proceeding to the `@INIT_OPTG ` node.

```{admonition} Warning
:class: caution

This command may change the engine's atomic coordinates under certain circumstances, such as if the SHAKE algorithm is used.
```

## Simulation Flow Control - Node Management

MDI enabled engines have a number of nodes defined where they can pause and listen for new commands.

(next_node)=
### `@` : Go to Next Node
The engine proceeds to the next node (see {ref}`standard_nodes_sec`).
This command is typically not supported at the `@DEFAULT` node.

(send_node)=
###  `<@`: Send Node Name
The engine sends the driver a string that corresponds to the name of its current node (see {ref}`standard_nodes_sec`).

- **Data Type:** `MDI_CHAR` 
- **Quantity:** `MDI_NAME_LENGTH`

(coords_node)=
### `@COORDS`: Go to next Coords Node

The engine proceeds to the next `@COORDS` node (see {ref}`standard_nodes_sec`).
This command is not valid at the `@DEFAULT` node.

(default_node)=
###  `@DEFAULT`: Go to Default Node  

If not already at the `@DEFAULT` node, the engine exists whatever simulation (i.e. MD, OPTG, etc.) it is performing (possibly after completing an unfinished time step or geometry optimization step) and returns to the `@DEFAULT` node.


(forces_node)=
### `@FORCES`: Go to next Forces Node    
The engine proceeds to the next `@FORCES` node (see {ref}`standard_nodes_sec`).
This command is not valid at the `@DEFAULT node.

(pre-forces_node)=
### `@PRE-FORCES`: Go to next Pre-Forces Node

The engine proceeds to the next `@PRE-FORCES` node (see {ref}`standard_nodes_sec`).
This command is not valid at the `@DEFAULT` node.
