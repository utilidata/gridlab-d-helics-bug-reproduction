# gridlab-d-helics-bug-reproduction
Reproduce GridLAB-D bug(s) related to HELICS integration.

## Prerequisites
- Git
- Docker

Version used to generate output in this README:
```shell
$ docker --version
Docker version 20.10.6, build 370c289
```

If your version of Docker does not come bundled with `docker-compose`,
you'll need to separately install `docker-compose`, and replace all
`docker compose` commands in this document with `docker-compose`.

# Reproducing The Bug

## Clone the repository, (optionally) check out relevant branch
```shell
cd /path/to/where/you/keep/your/git/repos
git clone https://github.com/utilidata/gridlab-d-helics-bug-reproduction.git
cd gridlab-d-helics-bug-reproduction
git checkout <relevant branch>
git pull
```

## Build the Docker containers
```shell
docker compose build
```

## Run the co-simulation
```shell
docker compose up
```

Output will look something like:

```
Container helics-broker  Created
Container grid-controller  Created
Container gridlab-d  Created
Attaching to grid-controller, gridlab-d, helics-broker
grid-controller  | 2021-06-17 16:47:39,918 [INFO] [grid_controller]: Message federate created
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/tap_A_output
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/tap_B_output
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/tap_C_output
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/inverter_Q_output
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/inverter_power
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/tap_A
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/tap_B
grid-controller  | 2021-06-17 16:47:39,919 [INFO] [grid_controller]: Registered endpoint grid_controller/tap_C
grid-controller  | 2021-06-17 16:47:39,920 [INFO] [grid_controller]: Registered endpoint grid_controller/voltage_A
grid-controller  | 2021-06-17 16:47:39,920 [INFO] [grid_controller]: Registered endpoint grid_controller/voltage_B
grid-controller  | 2021-06-17 16:47:39,920 [INFO] [grid_controller]: Registered endpoint grid_controller/voltage_C
helics-broker    | [2021-06-17 16:47:42.009] [console] [warning] 8-DsRO6-SFASH-E8PFh-Bd8T3 (0)::Unable to connect to filter target grid_controller/inverter_Q_output
helics-broker    | [2021-06-17 16:47:42.009] [console] [warning] 8-DsRO6-SFASH-E8PFh-Bd8T3 (0)::Unable to connect to filter target grid_controller/tap_C_output
helics-broker    | [2021-06-17 16:47:42.009] [console] [warning] 8-DsRO6-SFASH-E8PFh-Bd8T3 (0)::Unable to connect to filter target grid_controller/tap_A_output
helics-broker    | [2021-06-17 16:47:42.009] [console] [warning] 8-DsRO6-SFASH-E8PFh-Bd8T3 (0)::Unable to connect to filter target grid_controller/tap_B_output
gridlab-d        | WARNING  [INIT] : class_find_property(CLASS *oclass='diesel_dg', PROPERTYNAME name='phases': property is deprecated
gridlab-d        | [2021-06-17 16:47:42.010] [console] [warning] gld_federate (131073) (0)::Unable to connect to filter target grid_controller/inverter_Q_output
gridlab-d        | [2021-06-17 16:47:42.010] [console] [warning] gld_federate (131073) (0)::Unable to connect to filter target grid_controller/tap_C_output
gridlab-d        | [2021-06-17 16:47:42.010] [console] [warning] gld_federate (131073) (0)::Unable to connect to filter target grid_controller/tap_A_output
gridlab-d        | [2021-06-17 16:47:42.010] [console] [warning] gld_federate (131073) (0)::Unable to connect to filter target grid_controller/tap_B_output
grid-controller  | 2021-06-17 16:47:42,010 [INFO] [grid_controller]: Entering execution mode.
grid-controller  | 2021-06-17 16:47:42,020 [INFO] [grid_controller]: ********************************************************************************
grid-controller  | 2021-06-17 16:47:42,021 [INFO] [grid_controller]: Received time from broker: 60.0
grid-controller  | /usr/local/lib/python3.7/site-packages/helics/capi.py:5070: UserWarning: This function has been deprecated. Use `helicsEndpointCreateMessage` instead
grid-controller  |   warnings.warn("This function has been deprecated. Use `helicsEndpointCreateMessage` instead")
grid-controller  | 2021-06-17 16:47:42,022 [INFO] [grid_controller]: Sending 16 to tap_A_input.
grid-controller  | 2021-06-17 16:47:42,023 [INFO] [grid_controller]: Sending 16 to tap_B_input.
grid-controller  | 2021-06-17 16:47:42,023 [INFO] [grid_controller]: Sending 16 to tap_C_input.
grid-controller  | 2021-06-17 16:47:42,023 [INFO] [grid_controller]: Sending 16 to inverter_Q_input.
grid-controller  | 2021-06-17 16:47:42,023 [INFO] [grid_controller]: GridLAB-D reports inverter_power at 10000.000+1000.000j
grid-controller  | 2021-06-17 16:47:42,023 [INFO] [grid_controller]: GridLAB-D reports tap_A at 16
grid-controller  | 2021-06-17 16:47:42,024 [INFO] [grid_controller]: GridLAB-D reports tap_B at 16
grid-controller  | 2021-06-17 16:47:42,024 [INFO] [grid_controller]: GridLAB-D reports tap_C at 16
grid-controller  | 2021-06-17 16:47:42,024 [INFO] [grid_controller]: GridLAB-D reports voltage_A at 132.915+0.552j
grid-controller  | 2021-06-17 16:47:42,024 [INFO] [grid_controller]: GridLAB-D reports voltage_B at -66.049-113.573j
grid-controller  | 2021-06-17 16:47:42,024 [INFO] [grid_controller]: GridLAB-D reports voltage_C at -65.334+114.002j
grid-controller  | 2021-06-17 16:47:42,025 [INFO] [grid_controller]: ********************************************************************************
grid-controller  | 2021-06-17 16:47:42,025 [INFO] [grid_controller]: Received time from broker: 120.0
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : unit_find(char *unit='<▒U'): unitfile.txt(202): unable to find or derive unit '<▒U'
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : could not find unit '<▒U'
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : could not run unit_convert_ex due to null arguement
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : convert_to_double(const char *buffer='16<▒U', void *data=0x0x558ee63a8a20, PROPERTY *prop={name='Q_Out',...}): unit conversion failed
grid-controller  | 2021-06-17 16:47:42,025 [INFO] [grid_controller]: Sending 15 to tap_A_input.
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: Sending 15 to tap_B_input.
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: Sending 15 to tap_C_input.
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: Sending 15 to inverter_Q_input.
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: GridLAB-D reports inverter_power at 10000.000+1000.000j
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: GridLAB-D reports tap_A at 16
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: GridLAB-D reports tap_B at 16
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: GridLAB-D reports tap_C at 16
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: GridLAB-D reports voltage_A at 132.915+0.552j
grid-controller  | 2021-06-17 16:47:42,026 [INFO] [grid_controller]: GridLAB-D reports voltage_B at -66.049-113.573j
grid-controller  | 2021-06-17 16:47:42,027 [INFO] [grid_controller]: GridLAB-D reports voltage_C at -65.334+114.002j
grid-controller  | 2021-06-17 16:47:42,027 [INFO] [grid_controller]: ********************************************************************************

...
```

## Discussion
For the unit conversion bug, the relevant section is:
```
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : unit_find(char *unit='<▒U'): unitfile.txt(202): unable to find or derive unit '<▒U'
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : could not find unit '<▒U'
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : could not run unit_convert_ex due to null arguement
gridlab-d        | ERROR    [2018-01-01 00:00:00 UTC] : convert_to_double(const char *buffer='16<▒U', void *data=0x0x558ee63a8a20, PROPERTY *prop={name='Q_Out',...}): unit conversion failed
```

Note that in both `grid_controller/grid_controller.json` (endpoint named
`"inverter_Q_output"`) and `models/gld_federate.json` (endpoint named
`"inverter_Q_input"`), the units are defined as `VAr`, yet some bizarre
(to a non-C++ programmer ;) characters show up in the GridLAB-D error
logs.
