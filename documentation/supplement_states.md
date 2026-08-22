# Supplementary Table S7 — States a FIM-assisted ISAC system must track

Section 3.3 states that a FIM-assisted ISAC system tracks several states with different rates and different consequences for failure, and that the reviewed set fixes no relative rates among them. This table records each state with its governing driver, the control variable it binds, and the evidence available for it.

No column of this table contains an update deadline, and none is derivable from it; assigning one requires a performance tolerance the reviewed sources do not supply.

| State | What drives its variation | Which control variable it binds | Evidence in the reviewed set | Status of that evidence |
|---|---|---|---|---|
| **Instantaneous complex fading** | Doppler — ≈19.4 kHz at 28 GHz, 208 m/s | electronic phase state, and shape *if* shape is optimised per realisation | Doppler figure derived by us; 51-symbol >0.5-correlation window at 2.6 GHz | derived / simulated; no measurement, and no interval at 28 GHz |
| **Channel statistics and spatial correlation** | scattering environment, deliberately treated as slower than fading | shape, under statistical-CSI formulations | statistical-CSI FIM optimisation is published [12, 13]; the instantaneous-versus-statistical distinction is argued in [11, p. 20] | modelling choice, adopted by the literature; rate not measured |
| **Angles of arrival and departure; path geometry** | the user's traverse across the cell, not the fading | shape, beam direction | high-mobility models update angles explicitly and separately from fading correlation [19] | modelled; the *separation* is established, the *ratio* is not |
| **Target kinematics (sensing subproblem)** | target motion, independent of the communication user | sensing waveform and shape | communication and sensing may impose different movement and update requirements [11, pp. 24–25] | argued in a review; unquantified for FIM |
| **Blockage** | environmental, typically event-like rather than periodic | triggers reconfiguration rather than setting a rate | not quantified for any reviewed flexible aperture | absent |
| **Surface geometry** | deformation of the aperture itself — aeroelastic, mechanical, or commanded | the compensation layer; the actuator, if commanded | ≈4 ms strain-sensor read and 16.76 ms compensation loop on a flexible aperture [6]; 60 Hz stated deformation-rate limit | measured, on **externally imposed** deformation |
| **Calibration state** | how long the geometry-to-response mapping remains valid after a shape change | when the aperture may be trusted again | closed-loop refocusing demonstrated on a deformed active array [20] | capability demonstrated, duration not reported |

Read down the last two columns and the asymmetry is the one Section 5 develops: the fast-timescale demand is established by simulation and analysis, while the hardware capability is established by measurement on platforms that cannot do the thing being demanded. That is the reverse of how the comparison is usually presented.
