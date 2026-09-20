# System Architecture
## Dual-Side Laser Hazard Marker (BX) System

### 1. High-Level Architecture
- **Sensor / Input Layer:** Simulates real-time road hazard and pothole detection inputs.
- **Control Logic Layer:** Python-based core controller managing system state, safety checks, and power thresholds.
- **Actuator Layer:** Independent Left and Right Laser Unit controllers for high-visibility cross-beam projection.

### 2. Tech Stack
- **Language:** Python 3.x (for robust control logic, logging, and simulation)
- **Architecture Pattern:** Modular Class-Based System Design
- **Version Control:** Git & GitHub

### 3. Folder Structure
- `docs/`: Contains project documentation (PRD, Architecture, Rules, Design, Tasks, Memory)
- `bx_system.py`: Main execution script handling the hazard safety mechanism lifecycle
- 
