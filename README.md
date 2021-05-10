# gridlab-d-helics-bug-reproduction
Reproduce a possible GridLAB-D bug that is (possibly) related to HELICS
integration.

## Prerequisites
- Git
- Docker

Version used to generate output in this README:
```shell
$ docker --version
Docker version 20.10.5, build 55c4c88
```

If your version of Docker does not come bundled with `docker-compose`,
you'll need to separately install `docker-compose`, and replace all
`docker compose` commands in this document with `docker-compose`.

# Reproducing The Bug

## Clone the repository
```shell
cd /path/to/where/you/keep/your/git/repos
git clone https://github.com/utilidata/gridlab-d-helics-bug-reproduction.git
cd gridlab-d-helics-bug-reproduction
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
Network "gridlab-d-helics-bug-reproduction_default"  Creating
Network "gridlab-d-helics-bug-reproduction_default"  Created
Container tap-controller  Creating
Container helics-broker  Creating
Container gridlab-d  Creating
Container tap-controller  Created
Container helics-broker  Created
Container gridlab-d  Created
Attaching to gridlab-d, helics-broker, tap-controller
tap-controller  | 2021-05-07 22:16:15,299 [INFO] [tap_controller]: Helics version = 2.7.0 (2021-04-29)
tap-controller  | 2021-05-07 22:16:15,413 [INFO] [tap_controller]: Combination federate created
tap-controller  | 2021-05-07 22:16:15,413 [INFO] [tap_controller]: Tap position publications registered.
tap-controller  | 2021-05-07 22:16:15,414 [INFO] [tap_controller]: Voltage message subscriptions registered.
tap-controller  | 2021-05-07 22:16:15,415 [INFO] [tap_controller]: Entering execution mode.
tap-controller  | 2021-05-07 22:16:15,429 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,430 [INFO] [tap_controller]: Received time from broker: 1.0
tap-controller  | 2021-05-07 22:16:15,430 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 0
tap-controller  | 2021-05-07 22:16:15,430 [INFO] [tap_controller]: Commanded taps to position 16
tap-controller  | /usr/local/lib/python3.7/site-packages/helics/capi.py:7079: UserWarning: This function will return a complex number in the next major release
tap-controller  |   warnings.warn("This function will return a complex number in the next major release")
tap-controller  | 2021-05-07 22:16:15,435 [INFO] [tap_controller]: Phase voltage_A voltage is 118.06.
tap-controller  | 2021-05-07 22:16:15,435 [INFO] [tap_controller]: Phase voltage_B voltage is 118.06.
tap-controller  | 2021-05-07 22:16:15,435 [INFO] [tap_controller]: Phase voltage_C voltage is 118.06.
tap-controller  | 2021-05-07 22:16:15,435 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,436 [INFO] [tap_controller]: Received time from broker: 60.0
tap-controller  | 2021-05-07 22:16:15,436 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 0
tap-controller  | 2021-05-07 22:16:15,436 [INFO] [tap_controller]: Commanded taps to position 15
tap-controller  | 2021-05-07 22:16:15,436 [INFO] [tap_controller]: Phase voltage_A voltage is 118.06.
tap-controller  | 2021-05-07 22:16:15,436 [INFO] [tap_controller]: Phase voltage_B voltage is 118.06.
tap-controller  | 2021-05-07 22:16:15,436 [INFO] [tap_controller]: Phase voltage_C voltage is 118.06.
tap-controller  | 2021-05-07 22:16:15,438 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,438 [INFO] [tap_controller]: Received time from broker: 61.0
tap-controller  | 2021-05-07 22:16:15,438 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 16
tap-controller  | 2021-05-07 22:16:15,439 [INFO] [tap_controller]: Commanded taps to position 14
tap-controller  | 2021-05-07 22:16:15,439 [INFO] [tap_controller]: Phase voltage_A voltage is 131.39.
tap-controller  | 2021-05-07 22:16:15,439 [INFO] [tap_controller]: Phase voltage_B voltage is 131.39.
tap-controller  | 2021-05-07 22:16:15,439 [INFO] [tap_controller]: Phase voltage_C voltage is 131.39.
tap-controller  | 2021-05-07 22:16:15,441 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,441 [INFO] [tap_controller]: Received time from broker: 120.0
tap-controller  | 2021-05-07 22:16:15,441 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 14
tap-controller  | 2021-05-07 22:16:15,441 [INFO] [tap_controller]: Commanded taps to position 13
tap-controller  | 2021-05-07 22:16:15,441 [INFO] [tap_controller]: Phase voltage_A voltage is 129.56.
tap-controller  | 2021-05-07 22:16:15,442 [INFO] [tap_controller]: Phase voltage_B voltage is 129.57.
tap-controller  | 2021-05-07 22:16:15,442 [INFO] [tap_controller]: Phase voltage_C voltage is 129.57.
tap-controller  | 2021-05-07 22:16:15,444 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,444 [INFO] [tap_controller]: Received time from broker: 180.0
tap-controller  | 2021-05-07 22:16:15,444 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 13
tap-controller  | 2021-05-07 22:16:15,444 [INFO] [tap_controller]: Commanded taps to position 12
tap-controller  | 2021-05-07 22:16:15,444 [INFO] [tap_controller]: Phase voltage_A voltage is 128.67.
tap-controller  | 2021-05-07 22:16:15,444 [INFO] [tap_controller]: Phase voltage_B voltage is 128.67.
tap-controller  | 2021-05-07 22:16:15,444 [INFO] [tap_controller]: Phase voltage_C voltage is 128.67.
tap-controller  | 2021-05-07 22:16:15,446 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,446 [INFO] [tap_controller]: Received time from broker: 240.0
tap-controller  | 2021-05-07 22:16:15,446 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 12
tap-controller  | 2021-05-07 22:16:15,446 [INFO] [tap_controller]: Commanded taps to position 11
tap-controller  | 2021-05-07 22:16:15,446 [INFO] [tap_controller]: Phase voltage_A voltage is 127.79.
tap-controller  | 2021-05-07 22:16:15,446 [INFO] [tap_controller]: Phase voltage_B voltage is 127.79.
tap-controller  | 2021-05-07 22:16:15,446 [INFO] [tap_controller]: Phase voltage_C voltage is 127.79.
tap-controller  | 2021-05-07 22:16:15,448 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,448 [INFO] [tap_controller]: Received time from broker: 300.0
tap-controller  | 2021-05-07 22:16:15,448 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 11
tap-controller  | 2021-05-07 22:16:15,448 [INFO] [tap_controller]: Commanded taps to position 10
tap-controller  | 2021-05-07 22:16:15,448 [INFO] [tap_controller]: Phase voltage_A voltage is 126.92.
tap-controller  | 2021-05-07 22:16:15,448 [INFO] [tap_controller]: Phase voltage_B voltage is 126.92.
tap-controller  | 2021-05-07 22:16:15,448 [INFO] [tap_controller]: Phase voltage_C voltage is 126.92.
tap-controller  | 2021-05-07 22:16:15,450 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,450 [INFO] [tap_controller]: Received time from broker: 360.0
tap-controller  | 2021-05-07 22:16:15,450 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 10
tap-controller  | 2021-05-07 22:16:15,450 [INFO] [tap_controller]: Commanded taps to position 9
tap-controller  | 2021-05-07 22:16:15,450 [INFO] [tap_controller]: Phase voltage_A voltage is 126.06.
tap-controller  | 2021-05-07 22:16:15,451 [INFO] [tap_controller]: Phase voltage_B voltage is 126.06.
tap-controller  | 2021-05-07 22:16:15,451 [INFO] [tap_controller]: Phase voltage_C voltage is 126.06.
tap-controller  | 2021-05-07 22:16:15,452 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,452 [INFO] [tap_controller]: Received time from broker: 420.0
tap-controller  | 2021-05-07 22:16:15,452 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 9
tap-controller  | 2021-05-07 22:16:15,452 [INFO] [tap_controller]: Commanded taps to position 8
tap-controller  | 2021-05-07 22:16:15,453 [INFO] [tap_controller]: Phase voltage_A voltage is 125.21.
tap-controller  | 2021-05-07 22:16:15,453 [INFO] [tap_controller]: Phase voltage_B voltage is 125.21.
tap-controller  | 2021-05-07 22:16:15,453 [INFO] [tap_controller]: Phase voltage_C voltage is 125.21.
tap-controller  | 2021-05-07 22:16:15,454 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,454 [INFO] [tap_controller]: Received time from broker: 480.0
tap-controller  | 2021-05-07 22:16:15,454 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 8
tap-controller  | 2021-05-07 22:16:15,455 [INFO] [tap_controller]: Commanded taps to position 7
tap-controller  | 2021-05-07 22:16:15,455 [INFO] [tap_controller]: Phase voltage_A voltage is 124.37.
tap-controller  | 2021-05-07 22:16:15,455 [INFO] [tap_controller]: Phase voltage_B voltage is 124.38.
tap-controller  | 2021-05-07 22:16:15,455 [INFO] [tap_controller]: Phase voltage_C voltage is 124.37.
tap-controller  | 2021-05-07 22:16:15,457 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,457 [INFO] [tap_controller]: Received time from broker: 540.0
tap-controller  | 2021-05-07 22:16:15,457 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 7
tap-controller  | 2021-05-07 22:16:15,457 [INFO] [tap_controller]: Commanded taps to position 6
tap-controller  | 2021-05-07 22:16:15,457 [INFO] [tap_controller]: Phase voltage_A voltage is 123.55.
tap-controller  | 2021-05-07 22:16:15,457 [INFO] [tap_controller]: Phase voltage_B voltage is 123.55.
tap-controller  | 2021-05-07 22:16:15,457 [INFO] [tap_controller]: Phase voltage_C voltage is 123.55.
tap-controller  | 2021-05-07 22:16:15,459 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,459 [INFO] [tap_controller]: Received time from broker: 600.0
tap-controller  | 2021-05-07 22:16:15,459 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 6
tap-controller  | 2021-05-07 22:16:15,459 [INFO] [tap_controller]: Commanded taps to position 5
tap-controller  | 2021-05-07 22:16:15,459 [INFO] [tap_controller]: Phase voltage_A voltage is 122.73.
tap-controller  | 2021-05-07 22:16:15,459 [INFO] [tap_controller]: Phase voltage_B voltage is 122.74.
tap-controller  | 2021-05-07 22:16:15,459 [INFO] [tap_controller]: Phase voltage_C voltage is 122.73.
tap-controller  | 2021-05-07 22:16:15,461 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,461 [INFO] [tap_controller]: Received time from broker: 660.0
tap-controller  | 2021-05-07 22:16:15,461 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 5
tap-controller  | 2021-05-07 22:16:15,461 [INFO] [tap_controller]: Commanded taps to position 4
tap-controller  | 2021-05-07 22:16:15,461 [INFO] [tap_controller]: Phase voltage_A voltage is 121.93.
tap-controller  | 2021-05-07 22:16:15,461 [INFO] [tap_controller]: Phase voltage_B voltage is 121.93.
tap-controller  | 2021-05-07 22:16:15,461 [INFO] [tap_controller]: Phase voltage_C voltage is 121.93.
tap-controller  | 2021-05-07 22:16:15,463 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,463 [INFO] [tap_controller]: Received time from broker: 720.0
tap-controller  | 2021-05-07 22:16:15,463 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 4
tap-controller  | 2021-05-07 22:16:15,463 [INFO] [tap_controller]: Commanded taps to position 3
tap-controller  | 2021-05-07 22:16:15,463 [INFO] [tap_controller]: Phase voltage_A voltage is 121.13.
tap-controller  | 2021-05-07 22:16:15,464 [INFO] [tap_controller]: Phase voltage_B voltage is 121.14.
tap-controller  | 2021-05-07 22:16:15,464 [INFO] [tap_controller]: Phase voltage_C voltage is 121.14.
tap-controller  | 2021-05-07 22:16:15,465 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,465 [INFO] [tap_controller]: Received time from broker: 780.0
tap-controller  | 2021-05-07 22:16:15,465 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 3
tap-controller  | 2021-05-07 22:16:15,466 [INFO] [tap_controller]: Commanded taps to position 2
tap-controller  | 2021-05-07 22:16:15,466 [INFO] [tap_controller]: Phase voltage_A voltage is 120.35.
tap-controller  | 2021-05-07 22:16:15,466 [INFO] [tap_controller]: Phase voltage_B voltage is 120.35.
tap-controller  | 2021-05-07 22:16:15,466 [INFO] [tap_controller]: Phase voltage_C voltage is 120.35.
tap-controller  | 2021-05-07 22:16:15,467 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,468 [INFO] [tap_controller]: Received time from broker: 840.0
tap-controller  | 2021-05-07 22:16:15,468 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 2
tap-controller  | 2021-05-07 22:16:15,468 [INFO] [tap_controller]: Commanded taps to position 1
tap-controller  | 2021-05-07 22:16:15,468 [INFO] [tap_controller]: Phase voltage_A voltage is 119.58.
tap-controller  | 2021-05-07 22:16:15,468 [INFO] [tap_controller]: Phase voltage_B voltage is 119.58.
tap-controller  | 2021-05-07 22:16:15,468 [INFO] [tap_controller]: Phase voltage_C voltage is 119.58.
tap-controller  | 2021-05-07 22:16:15,470 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,470 [INFO] [tap_controller]: Received time from broker: 900.0
tap-controller  | 2021-05-07 22:16:15,470 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 1
tap-controller  | 2021-05-07 22:16:15,470 [INFO] [tap_controller]: Commanded taps to position 0
tap-controller  | 2021-05-07 22:16:15,470 [INFO] [tap_controller]: Phase voltage_A voltage is 118.81.
tap-controller  | 2021-05-07 22:16:15,470 [INFO] [tap_controller]: Phase voltage_B voltage is 118.81.
tap-controller  | 2021-05-07 22:16:15,470 [INFO] [tap_controller]: Phase voltage_C voltage is 118.81.
tap-controller  | 2021-05-07 22:16:15,543 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,543 [INFO] [tap_controller]: Received time from broker: 960.0
tap-controller  | 2021-05-07 22:16:15,543 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 0
tap-controller  | 2021-05-07 22:16:15,543 [INFO] [tap_controller]: Commanded taps to position -1
tap-controller  | 2021-05-07 22:16:15,543 [INFO] [tap_controller]: Phase voltage_A voltage is 229875055515407064904343715613585620048757388616190073076416283167732951594637426972067942237369003210005679556790813211330233062912382862887940001890304.00.
tap-controller  | 2021-05-07 22:16:15,544 [INFO] [tap_controller]: Phase voltage_B voltage is 229875818661329754697189469188994696519355669917146388721657930181775383420684872207740893066893443946401399138267403137388265281878403287809920660930560.00.
tap-controller  | 2021-05-07 22:16:15,544 [INFO] [tap_controller]: Phase voltage_C voltage is 229873237025445726628833050516994416563744608855778611684337580010758168008609431560419147474992763464100273628988035362995672962388197040915267270475776.00.
tap-controller  | 2021-05-07 22:16:15,546 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,546 [INFO] [tap_controller]: Received time from broker: 1020.0
tap-controller  | 2021-05-07 22:16:15,546 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -1
tap-controller  | 2021-05-07 22:16:15,546 [INFO] [tap_controller]: Commanded taps to position -2
tap-controller  | 2021-05-07 22:16:15,546 [INFO] [tap_controller]: Phase voltage_A voltage is 229875055515267511869278959090600149877642891745594173935164318100158905476394744228750169836090374528268636952203146807181829956749144219375245987938304.00.
tap-controller  | 2021-05-07 22:16:15,546 [INFO] [tap_controller]: Phase voltage_B voltage is 229875818661335104230200284855709139542581725630519231522072588842699055188550841712901407675609124712534652438109930349547287400947994102477907264798720.00.
tap-controller  | 2021-05-07 22:16:15,547 [INFO] [tap_controller]: Phase voltage_C voltage is 229873237025472706882278903444771607463493411584093818851646293257155816924803016890793916805906631675902768532541650867797697562913089845327721446506496.00.
tap-controller  | 2021-05-07 22:16:15,548 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,549 [INFO] [tap_controller]: Received time from broker: 1080.0
tap-controller  | 2021-05-07 22:16:15,549 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -2
tap-controller  | 2021-05-07 22:16:15,549 [INFO] [tap_controller]: Commanded taps to position -3
tap-controller  | 2021-05-07 22:16:15,549 [INFO] [tap_controller]: Phase voltage_A voltage is 229875055503837001873194881805906259101996682068825267073498363345303936023373086089078067992160456464550951295636566976194428337130593406537504693157888.00.
tap-controller  | 2021-05-07 22:16:15,549 [INFO] [tap_controller]: Phase voltage_B voltage is 229875818659536916855712542138200361231047728620600872453993934958651612939621127004337471027666901272125612797129652843293730576999276434602340663689216.00.
tap-controller  | 2021-05-07 22:16:15,549 [INFO] [tap_controller]: Phase voltage_C voltage is 229873237022950518361875203886014209904217404809523935038752444602534223414430264109897376940130882634641951858960560056822225424189490094908298301014016.00.
tap-controller  | 2021-05-07 22:16:15,551 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,551 [INFO] [tap_controller]: Received time from broker: 1140.0
tap-controller  | 2021-05-07 22:16:15,551 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -3
tap-controller  | 2021-05-07 22:16:15,551 [INFO] [tap_controller]: Commanded taps to position -4
tap-controller  | 2021-05-07 22:16:15,551 [INFO] [tap_controller]: Phase voltage_A voltage is inf.
tap-controller  | 2021-05-07 22:16:15,551 [INFO] [tap_controller]: Phase voltage_B voltage is inf.
tap-controller  | 2021-05-07 22:16:15,551 [INFO] [tap_controller]: Phase voltage_C voltage is inf.
tap-controller  | 2021-05-07 22:16:15,553 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,553 [INFO] [tap_controller]: Received time from broker: 1200.0
tap-controller  | 2021-05-07 22:16:15,553 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -4
tap-controller  | 2021-05-07 22:16:15,553 [INFO] [tap_controller]: Commanded taps to position -5
tap-controller  | 2021-05-07 22:16:15,553 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,553 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,553 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,555 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,555 [INFO] [tap_controller]: Received time from broker: 1260.0
tap-controller  | 2021-05-07 22:16:15,555 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -5
tap-controller  | 2021-05-07 22:16:15,555 [INFO] [tap_controller]: Commanded taps to position -6
tap-controller  | 2021-05-07 22:16:15,555 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,556 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,556 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,557 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,557 [INFO] [tap_controller]: Received time from broker: 1320.0
tap-controller  | 2021-05-07 22:16:15,557 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -6
tap-controller  | 2021-05-07 22:16:15,558 [INFO] [tap_controller]: Commanded taps to position -7
tap-controller  | 2021-05-07 22:16:15,558 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,558 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,558 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,559 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,560 [INFO] [tap_controller]: Received time from broker: 1380.0
tap-controller  | 2021-05-07 22:16:15,560 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -7
tap-controller  | 2021-05-07 22:16:15,560 [INFO] [tap_controller]: Commanded taps to position -8
tap-controller  | 2021-05-07 22:16:15,560 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,560 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,560 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,562 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,562 [INFO] [tap_controller]: Received time from broker: 1440.0
tap-controller  | 2021-05-07 22:16:15,562 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -8
tap-controller  | 2021-05-07 22:16:15,562 [INFO] [tap_controller]: Commanded taps to position -9
tap-controller  | 2021-05-07 22:16:15,562 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,562 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,562 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,564 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,564 [INFO] [tap_controller]: Received time from broker: 1500.0
tap-controller  | 2021-05-07 22:16:15,564 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -9
tap-controller  | 2021-05-07 22:16:15,564 [INFO] [tap_controller]: Commanded taps to position -10
tap-controller  | 2021-05-07 22:16:15,564 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,565 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,565 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,566 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,566 [INFO] [tap_controller]: Received time from broker: 1560.0
tap-controller  | 2021-05-07 22:16:15,567 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -10
tap-controller  | 2021-05-07 22:16:15,567 [INFO] [tap_controller]: Commanded taps to position -11
tap-controller  | 2021-05-07 22:16:15,567 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,567 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,567 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,569 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,569 [INFO] [tap_controller]: Received time from broker: 1620.0
tap-controller  | 2021-05-07 22:16:15,569 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -11
tap-controller  | 2021-05-07 22:16:15,569 [INFO] [tap_controller]: Commanded taps to position -12
tap-controller  | 2021-05-07 22:16:15,569 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,569 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,569 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,571 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,571 [INFO] [tap_controller]: Received time from broker: 1680.0
tap-controller  | 2021-05-07 22:16:15,571 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -12
tap-controller  | 2021-05-07 22:16:15,571 [INFO] [tap_controller]: Commanded taps to position -13
tap-controller  | 2021-05-07 22:16:15,571 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,571 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,571 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,573 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,573 [INFO] [tap_controller]: Received time from broker: 1740.0
tap-controller  | 2021-05-07 22:16:15,573 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -13
tap-controller  | 2021-05-07 22:16:15,573 [INFO] [tap_controller]: Commanded taps to position -14
tap-controller  | 2021-05-07 22:16:15,574 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,574 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,574 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,575 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,576 [INFO] [tap_controller]: Received time from broker: 1800.0
tap-controller  | 2021-05-07 22:16:15,576 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -14
tap-controller  | 2021-05-07 22:16:15,576 [INFO] [tap_controller]: Commanded taps to position -15
tap-controller  | 2021-05-07 22:16:15,576 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,576 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,576 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,578 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:16:15,578 [INFO] [tap_controller]: Received time from broker: 1860.0
tap-controller  | 2021-05-07 22:16:15,579 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -15
tap-controller  | 2021-05-07 22:16:15,579 [INFO] [tap_controller]: Commanded taps to position -16
tap-controller  | 2021-05-07 22:16:15,579 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:16:15,579 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:16:15,579 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:16:15,580 [INFO] [tap_controller]: Federate finalized.
helics-broker   | [2021-05-07 22:16:15.580] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(3) size 17 at 1920 to 131073
helics-broker   | [2021-05-07 22:16:15.580] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(4) size 17 at 1920 to 131073
helics-broker   | [2021-05-07 22:16:15.580] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(5) size 17 at 1920 to 131073
helics-broker   | [2021-05-07 22:16:15.580] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(6) size 9 at 1920 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(3) size 17 at 1980 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(4) size 17 at 1980 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(5) size 17 at 1980 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(6) size 9 at 1980 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(3) size 17 at 2040 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(4) size 17 at 2040 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(5) size 17 at 2040 to 131073
helics-broker   | [2021-05-07 22:16:15.581] [console] [warning] commWarning||8-ereyB-dIYDq-EfqhS-r0RD3 (1)::unknown route and no broker, dropping message pub:From (131072) handle(6) size 9 at 2040 to 131073
gridlab-d       | WARNING  [INIT] : The external solver solver_KLU could not be found, defaulting to superLU
gridlab-d       | WARNING  [2017-12-31 23:59:00 UTC] : Regulator vreg has phase A at the maximum tap value
gridlab-d       | WARNING  [2018-01-01 00:30:00 UTC] : last warning message was repeated 2 times
gridlab-d       | WARNING  [2018-01-01 00:30:00 UTC] : Regulator vreg has phase A at the minimum tap value
gridlab-d       |
gridlab-d       | Core profiler results
gridlab-d       | ======================
gridlab-d       |
gridlab-d       | Total objects                 36 objects
gridlab-d       | Parallelism                    1 thread
gridlab-d       | Total time                   1.0 seconds
gridlab-d       |   Core time                  0.8 seconds (75.3%)
gridlab-d       |     Compiler                 0.0 seconds (1.2%)
gridlab-d       |     Instances                0.0 seconds (0.0%)
gridlab-d       |     Random variables         0.0 seconds (0.0%)
gridlab-d       |     Schedules                0.0 seconds (0.0%)
gridlab-d       |     Loadshapes               0.0 seconds (0.0%)
gridlab-d       |     Enduses                  0.0 seconds (0.0%)
gridlab-d       |     Transforms               0.0 seconds (0.0%)
gridlab-d       |   Model time                 0.2 seconds/thread (24.7%)
gridlab-d       | Simulation time                0 days
gridlab-d       | Simulation speed              21 object.hours/second
gridlab-d       | Passes completed              36 passes
gridlab-d       | Time steps completed          36 timesteps
gridlab-d       | Convergence efficiency      1.00 passes/timestep
gridlab-d       | Read lock contention        0.0%
gridlab-d       | Write lock contention       0.0%
gridlab-d       | Average timestep             58 seconds/timestep
gridlab-d       | Simulation rate            2100 x realtime
gridlab-d       |
gridlab-d       |
gridlab-d       | Model profiler results
gridlab-d       | ======================
gridlab-d       |
gridlab-d       | Class            Time (s) Time (%) msec/obj
gridlab-d       | ---------------- -------- -------- --------
gridlab-d       | helics_msg         0.144     58.3%    144.0
gridlab-d       | node               0.083     33.6%     27.7
gridlab-d       | recorder           0.013      5.3%      3.2
gridlab-d       | triplex_meter      0.002      0.8%      0.7
gridlab-d       | meter              0.001      0.4%      1.0
gridlab-d       | transformer        0.001      0.4%      0.2
gridlab-d       | triplex_node       0.001      0.4%      0.3
gridlab-d       | triplex_line       0.001      0.4%      0.3
gridlab-d       | triplex_load       0.001      0.4%      0.3
gridlab-d       | ================ ======== ======== ========
gridlab-d       | Total              0.247    100.0%      6.9
gridlab-d       |
gridlab-d       | WARNING  [2018-01-01 00:33:00 UTC] : last warning message was repeated 11 times
helics-broker exited with code 0
tap-controller exited with code 0
gridlab-d exited with code 0
```

## Discussion
Look in the output from the co-simulation for
`Received time from broker: 960.0` and notice that voltage numbers begin
to get insanely large.

Next, take a look at the `.csv` files that are now in the `models`
directory. `tap_output.csv` shows that the regulator taps are in the
expected positions (as commanded by the `tap_controller`). The files
that start with `triplex_output_` shows normal voltages through
timestamp `2018-01-01 00:13:00`, after which something goes horribly
wrong.

## Further Digging

### Start Taps Low, Increment Upward
In the original co-simulation, the `tap_controller` commands taps to
position `16` and decrements them by one until they're at `-16`. To
illustrate this isn't an issue solving the power flow at lower voltages,
we'll reverse the taps.

1.  In `tap_controller/tap_controller.py`, replace `range(16, -17, -1)`
    with `range(-16, 17, 1)`.
    
2.  Execute `docker compose up` and observe the output:

```
Network "gridlab-d-helics-bug-reproduction_default"  Creating
Network "gridlab-d-helics-bug-reproduction_default"  Created
Container helics-broker  Creating
Container gridlab-d  Creating
Container tap-controller  Creating
Container tap-controller  Created
Container helics-broker  Created
Container gridlab-d  Created
Attaching to gridlab-d, helics-broker, tap-controller
tap-controller  | 2021-05-07 22:29:14,135 [INFO] [tap_controller]: Helics version = 2.7.0 (2021-04-29)
tap-controller  | 2021-05-07 22:29:14,249 [INFO] [tap_controller]: Combination federate created
tap-controller  | 2021-05-07 22:29:14,249 [INFO] [tap_controller]: Tap position publications registered.
tap-controller  | 2021-05-07 22:29:14,250 [INFO] [tap_controller]: Voltage message subscriptions registered.
tap-controller  | 2021-05-07 22:29:14,804 [INFO] [tap_controller]: Entering execution mode.
tap-controller  | 2021-05-07 22:29:14,822 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,822 [INFO] [tap_controller]: Received time from broker: 1.0
tap-controller  | 2021-05-07 22:29:14,822 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 0
tap-controller  | 2021-05-07 22:29:14,822 [INFO] [tap_controller]: Commanded taps to position -16
tap-controller  | 2021-05-07 22:29:14,828 [INFO] [tap_controller]: Phase voltage_A voltage is 118.06.
tap-controller  | 2021-05-07 22:29:14,828 [INFO] [tap_controller]: Phase voltage_B voltage is 118.06.
tap-controller  | /usr/local/lib/python3.7/site-packages/helics/capi.py:7079: UserWarning: This function will return a complex number in the next major release
tap-controller  |   warnings.warn("This function will return a complex number in the next major release")
tap-controller  | 2021-05-07 22:29:14,828 [INFO] [tap_controller]: Phase voltage_C voltage is 118.06.
tap-controller  | 2021-05-07 22:29:14,828 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,829 [INFO] [tap_controller]: Received time from broker: 60.0
tap-controller  | 2021-05-07 22:29:14,829 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 0
tap-controller  | 2021-05-07 22:29:14,829 [INFO] [tap_controller]: Commanded taps to position -15
tap-controller  | 2021-05-07 22:29:14,829 [INFO] [tap_controller]: Phase voltage_A voltage is 118.06.
tap-controller  | 2021-05-07 22:29:14,829 [INFO] [tap_controller]: Phase voltage_B voltage is 118.06.
tap-controller  | 2021-05-07 22:29:14,829 [INFO] [tap_controller]: Phase voltage_C voltage is 118.06.
tap-controller  | 2021-05-07 22:29:14,832 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,833 [INFO] [tap_controller]: Received time from broker: 61.0
tap-controller  | 2021-05-07 22:29:14,833 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -16
tap-controller  | 2021-05-07 22:29:14,833 [INFO] [tap_controller]: Commanded taps to position -14
tap-controller  | 2021-05-07 22:29:14,833 [INFO] [tap_controller]: Phase voltage_A voltage is 107.15.
tap-controller  | 2021-05-07 22:29:14,833 [INFO] [tap_controller]: Phase voltage_B voltage is 107.15.
tap-controller  | 2021-05-07 22:29:14,833 [INFO] [tap_controller]: Phase voltage_C voltage is 107.15.
tap-controller  | 2021-05-07 22:29:14,836 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,836 [INFO] [tap_controller]: Received time from broker: 120.0
tap-controller  | 2021-05-07 22:29:14,836 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -14
tap-controller  | 2021-05-07 22:29:14,837 [INFO] [tap_controller]: Commanded taps to position -13
tap-controller  | 2021-05-07 22:29:14,837 [INFO] [tap_controller]: Phase voltage_A voltage is 108.40.
tap-controller  | 2021-05-07 22:29:14,837 [INFO] [tap_controller]: Phase voltage_B voltage is 108.40.
tap-controller  | 2021-05-07 22:29:14,837 [INFO] [tap_controller]: Phase voltage_C voltage is 108.40.
tap-controller  | 2021-05-07 22:29:14,841 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,841 [INFO] [tap_controller]: Received time from broker: 180.0
tap-controller  | 2021-05-07 22:29:14,841 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -13
tap-controller  | 2021-05-07 22:29:14,841 [INFO] [tap_controller]: Commanded taps to position -12
tap-controller  | 2021-05-07 22:29:14,841 [INFO] [tap_controller]: Phase voltage_A voltage is 109.04.
tap-controller  | 2021-05-07 22:29:14,841 [INFO] [tap_controller]: Phase voltage_B voltage is 109.04.
tap-controller  | 2021-05-07 22:29:14,841 [INFO] [tap_controller]: Phase voltage_C voltage is 109.04.
tap-controller  | 2021-05-07 22:29:14,844 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,844 [INFO] [tap_controller]: Received time from broker: 240.0
tap-controller  | 2021-05-07 22:29:14,844 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -12
tap-controller  | 2021-05-07 22:29:14,844 [INFO] [tap_controller]: Commanded taps to position -11
tap-controller  | 2021-05-07 22:29:14,845 [INFO] [tap_controller]: Phase voltage_A voltage is 109.68.
tap-controller  | 2021-05-07 22:29:14,845 [INFO] [tap_controller]: Phase voltage_B voltage is 109.69.
tap-controller  | 2021-05-07 22:29:14,845 [INFO] [tap_controller]: Phase voltage_C voltage is 109.69.
tap-controller  | 2021-05-07 22:29:14,847 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,847 [INFO] [tap_controller]: Received time from broker: 300.0
tap-controller  | 2021-05-07 22:29:14,848 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -11
tap-controller  | 2021-05-07 22:29:14,848 [INFO] [tap_controller]: Commanded taps to position -10
tap-controller  | 2021-05-07 22:29:14,848 [INFO] [tap_controller]: Phase voltage_A voltage is 110.34.
tap-controller  | 2021-05-07 22:29:14,848 [INFO] [tap_controller]: Phase voltage_B voltage is 110.34.
tap-controller  | 2021-05-07 22:29:14,848 [INFO] [tap_controller]: Phase voltage_C voltage is 110.34.
tap-controller  | 2021-05-07 22:29:14,851 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,851 [INFO] [tap_controller]: Received time from broker: 360.0
tap-controller  | 2021-05-07 22:29:14,851 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -10
tap-controller  | 2021-05-07 22:29:14,851 [INFO] [tap_controller]: Commanded taps to position -9
tap-controller  | 2021-05-07 22:29:14,851 [INFO] [tap_controller]: Phase voltage_A voltage is 111.00.
tap-controller  | 2021-05-07 22:29:14,851 [INFO] [tap_controller]: Phase voltage_B voltage is 111.00.
tap-controller  | 2021-05-07 22:29:14,852 [INFO] [tap_controller]: Phase voltage_C voltage is 111.00.
tap-controller  | 2021-05-07 22:29:14,854 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,854 [INFO] [tap_controller]: Received time from broker: 420.0
tap-controller  | 2021-05-07 22:29:14,854 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -9
tap-controller  | 2021-05-07 22:29:14,855 [INFO] [tap_controller]: Commanded taps to position -8
tap-controller  | 2021-05-07 22:29:14,855 [INFO] [tap_controller]: Phase voltage_A voltage is 111.67.
tap-controller  | 2021-05-07 22:29:14,855 [INFO] [tap_controller]: Phase voltage_B voltage is 111.67.
tap-controller  | 2021-05-07 22:29:14,855 [INFO] [tap_controller]: Phase voltage_C voltage is 111.67.
tap-controller  | 2021-05-07 22:29:14,857 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,857 [INFO] [tap_controller]: Received time from broker: 480.0
tap-controller  | 2021-05-07 22:29:14,858 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -8
tap-controller  | 2021-05-07 22:29:14,858 [INFO] [tap_controller]: Commanded taps to position -7
tap-controller  | 2021-05-07 22:29:14,858 [INFO] [tap_controller]: Phase voltage_A voltage is 112.34.
tap-controller  | 2021-05-07 22:29:14,858 [INFO] [tap_controller]: Phase voltage_B voltage is 112.35.
tap-controller  | 2021-05-07 22:29:14,858 [INFO] [tap_controller]: Phase voltage_C voltage is 112.34.
tap-controller  | 2021-05-07 22:29:14,861 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,861 [INFO] [tap_controller]: Received time from broker: 540.0
tap-controller  | 2021-05-07 22:29:14,861 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -7
tap-controller  | 2021-05-07 22:29:14,862 [INFO] [tap_controller]: Commanded taps to position -6
tap-controller  | 2021-05-07 22:29:14,862 [INFO] [tap_controller]: Phase voltage_A voltage is 113.03.
tap-controller  | 2021-05-07 22:29:14,862 [INFO] [tap_controller]: Phase voltage_B voltage is 113.03.
tap-controller  | 2021-05-07 22:29:14,862 [INFO] [tap_controller]: Phase voltage_C voltage is 113.03.
tap-controller  | 2021-05-07 22:29:14,864 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,865 [INFO] [tap_controller]: Received time from broker: 600.0
tap-controller  | 2021-05-07 22:29:14,865 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -6
tap-controller  | 2021-05-07 22:29:14,865 [INFO] [tap_controller]: Commanded taps to position -5
tap-controller  | 2021-05-07 22:29:14,865 [INFO] [tap_controller]: Phase voltage_A voltage is 113.72.
tap-controller  | 2021-05-07 22:29:14,865 [INFO] [tap_controller]: Phase voltage_B voltage is 113.72.
tap-controller  | 2021-05-07 22:29:14,865 [INFO] [tap_controller]: Phase voltage_C voltage is 113.72.
tap-controller  | 2021-05-07 22:29:14,868 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,868 [INFO] [tap_controller]: Received time from broker: 660.0
tap-controller  | 2021-05-07 22:29:14,868 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -5
tap-controller  | 2021-05-07 22:29:14,869 [INFO] [tap_controller]: Commanded taps to position -4
tap-controller  | 2021-05-07 22:29:14,869 [INFO] [tap_controller]: Phase voltage_A voltage is 114.42.
tap-controller  | 2021-05-07 22:29:14,869 [INFO] [tap_controller]: Phase voltage_B voltage is 114.42.
tap-controller  | 2021-05-07 22:29:14,869 [INFO] [tap_controller]: Phase voltage_C voltage is 114.42.
tap-controller  | 2021-05-07 22:29:14,872 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,872 [INFO] [tap_controller]: Received time from broker: 720.0
tap-controller  | 2021-05-07 22:29:14,872 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -4
tap-controller  | 2021-05-07 22:29:14,872 [INFO] [tap_controller]: Commanded taps to position -3
tap-controller  | 2021-05-07 22:29:14,872 [INFO] [tap_controller]: Phase voltage_A voltage is 115.13.
tap-controller  | 2021-05-07 22:29:14,873 [INFO] [tap_controller]: Phase voltage_B voltage is 115.13.
tap-controller  | 2021-05-07 22:29:14,873 [INFO] [tap_controller]: Phase voltage_C voltage is 115.13.
tap-controller  | 2021-05-07 22:29:14,876 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,877 [INFO] [tap_controller]: Received time from broker: 780.0
tap-controller  | 2021-05-07 22:29:14,877 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -3
tap-controller  | 2021-05-07 22:29:14,877 [INFO] [tap_controller]: Commanded taps to position -2
tap-controller  | 2021-05-07 22:29:14,877 [INFO] [tap_controller]: Phase voltage_A voltage is 115.85.
tap-controller  | 2021-05-07 22:29:14,877 [INFO] [tap_controller]: Phase voltage_B voltage is 115.85.
tap-controller  | 2021-05-07 22:29:14,877 [INFO] [tap_controller]: Phase voltage_C voltage is 115.85.
tap-controller  | 2021-05-07 22:29:14,880 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,880 [INFO] [tap_controller]: Received time from broker: 840.0
tap-controller  | 2021-05-07 22:29:14,880 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -2
tap-controller  | 2021-05-07 22:29:14,880 [INFO] [tap_controller]: Commanded taps to position -1
tap-controller  | 2021-05-07 22:29:14,881 [INFO] [tap_controller]: Phase voltage_A voltage is 116.57.
tap-controller  | 2021-05-07 22:29:14,881 [INFO] [tap_controller]: Phase voltage_B voltage is 116.58.
tap-controller  | 2021-05-07 22:29:14,881 [INFO] [tap_controller]: Phase voltage_C voltage is 116.58.
tap-controller  | 2021-05-07 22:29:14,980 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,980 [INFO] [tap_controller]: Received time from broker: 900.0
tap-controller  | 2021-05-07 22:29:14,981 [INFO] [tap_controller]: GridLAB-D reports tap_A at position -1
tap-controller  | 2021-05-07 22:29:14,981 [INFO] [tap_controller]: Commanded taps to position 0
tap-controller  | 2021-05-07 22:29:14,981 [INFO] [tap_controller]: Phase voltage_A voltage is 412920696554284973970028957617016489346871487119093719924381423680619582610190584280673539902510187416942783851071223837396074685665715121141220391256064.00.
tap-controller  | 2021-05-07 22:29:14,981 [INFO] [tap_controller]: Phase voltage_B voltage is 412919892220086182177526020293047886132811682282981290658613461383636826559363136773981346705746982531274086791893551890007662242075745393706491222949888.00.
tap-controller  | 2021-05-07 22:29:14,981 [INFO] [tap_controller]: Phase voltage_C voltage is 412916616518544018058764427536443786156749972980509280793366206823638073186475903394916664945774541543969106259319600804446684565132911446530315748638720.00.
tap-controller  | 2021-05-07 22:29:14,984 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,984 [INFO] [tap_controller]: Received time from broker: 960.0
tap-controller  | 2021-05-07 22:29:14,984 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 0
tap-controller  | 2021-05-07 22:29:14,984 [INFO] [tap_controller]: Commanded taps to position 1
tap-controller  | 2021-05-07 22:29:14,984 [INFO] [tap_controller]: Phase voltage_A voltage is 412920696554276089093463168118386414412643864151665781012388381904650701673995800146015641726295448057538858805245809076331959687906655594170912205701120.00.
tap-controller  | 2021-05-07 22:29:14,985 [INFO] [tap_controller]: Phase voltage_B voltage is 412919892220017336013560740408375054181728530493487313748929158616966963807696746620611245654449525714950479106963636463961116709701880996240228842733568.00.
tap-controller  | 2021-05-07 22:29:14,985 [INFO] [tap_controller]: Phase voltage_C voltage is 412916616518262865210787298061469058918677966618548742656790581200832228273589645228045792814665197626496211091943648888889035107249373326066741541863424.00.
tap-controller  | 2021-05-07 22:29:14,987 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,987 [INFO] [tap_controller]: Received time from broker: 1020.0
tap-controller  | 2021-05-07 22:29:14,987 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 1
tap-controller  | 2021-05-07 22:29:14,988 [INFO] [tap_controller]: Commanded taps to position 2
tap-controller  | 2021-05-07 22:29:14,988 [INFO] [tap_controller]: Phase voltage_A voltage is 412920696564680977317177994796819089744045931494135226451946561389548148188679235244130994935761631062943772679829432614431364079296177869619360960610304.00.
tap-controller  | 2021-05-07 22:29:14,988 [INFO] [tap_controller]: Phase voltage_B voltage is 412919892229042649450303739019414366558216386605535898911117495432183248412805767679201540162342278448930235473461785819450790794597013788136688807051264.00.
tap-controller  | 2021-05-07 22:29:14,988 [INFO] [tap_controller]: Phase voltage_C voltage is 412916616519392640064993211952718430267297228450602943471319406399555847631509657157032038917949882557612062337817200208073123853711565637731008047480832.00.
tap-controller  | 2021-05-07 22:29:14,990 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,990 [INFO] [tap_controller]: Received time from broker: 1080.0
tap-controller  | 2021-05-07 22:29:14,990 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 2
tap-controller  | 2021-05-07 22:29:14,990 [INFO] [tap_controller]: Commanded taps to position 3
tap-controller  | 2021-05-07 22:29:14,991 [INFO] [tap_controller]: Phase voltage_A voltage is inf.
tap-controller  | 2021-05-07 22:29:14,991 [INFO] [tap_controller]: Phase voltage_B voltage is inf.
tap-controller  | 2021-05-07 22:29:14,991 [INFO] [tap_controller]: Phase voltage_C voltage is inf.
tap-controller  | 2021-05-07 22:29:14,993 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,993 [INFO] [tap_controller]: Received time from broker: 1140.0
tap-controller  | 2021-05-07 22:29:14,993 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 3
tap-controller  | 2021-05-07 22:29:14,994 [INFO] [tap_controller]: Commanded taps to position 4
tap-controller  | 2021-05-07 22:29:14,994 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:14,994 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:14,994 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:14,996 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,996 [INFO] [tap_controller]: Received time from broker: 1200.0
tap-controller  | 2021-05-07 22:29:14,996 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 4
tap-controller  | 2021-05-07 22:29:14,996 [INFO] [tap_controller]: Commanded taps to position 5
tap-controller  | 2021-05-07 22:29:14,997 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:14,997 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:14,997 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:14,999 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:14,999 [INFO] [tap_controller]: Received time from broker: 1260.0
tap-controller  | 2021-05-07 22:29:14,999 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 5
tap-controller  | 2021-05-07 22:29:14,999 [INFO] [tap_controller]: Commanded taps to position 6
tap-controller  | 2021-05-07 22:29:14,999 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:14,999 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,000 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
gridlab-d       | WARNING  [INIT] : The external solver solver_KLU could not be found, defaulting to superLU
gridlab-d       | WARNING  [2017-12-31 23:59:00 UTC] : Regulator vreg has phase A at the minimum tap value
tap-controller  | 2021-05-07 22:29:15,002 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,002 [INFO] [tap_controller]: Received time from broker: 1320.0
tap-controller  | 2021-05-07 22:29:15,002 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 6
tap-controller  | 2021-05-07 22:29:15,002 [INFO] [tap_controller]: Commanded taps to position 7
tap-controller  | 2021-05-07 22:29:15,002 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,002 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,003 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,004 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,005 [INFO] [tap_controller]: Received time from broker: 1380.0
tap-controller  | 2021-05-07 22:29:15,005 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 7
tap-controller  | 2021-05-07 22:29:15,005 [INFO] [tap_controller]: Commanded taps to position 8
tap-controller  | 2021-05-07 22:29:15,005 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,005 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,005 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,007 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,007 [INFO] [tap_controller]: Received time from broker: 1440.0
tap-controller  | 2021-05-07 22:29:15,008 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 8
tap-controller  | 2021-05-07 22:29:15,008 [INFO] [tap_controller]: Commanded taps to position 9
tap-controller  | 2021-05-07 22:29:15,008 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,008 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,008 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,010 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,010 [INFO] [tap_controller]: Received time from broker: 1500.0
tap-controller  | 2021-05-07 22:29:15,010 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 9
tap-controller  | 2021-05-07 22:29:15,010 [INFO] [tap_controller]: Commanded taps to position 10
tap-controller  | 2021-05-07 22:29:15,011 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,011 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,011 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,013 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,013 [INFO] [tap_controller]: Received time from broker: 1560.0
tap-controller  | 2021-05-07 22:29:15,013 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 10
tap-controller  | 2021-05-07 22:29:15,013 [INFO] [tap_controller]: Commanded taps to position 11
tap-controller  | 2021-05-07 22:29:15,013 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,013 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,013 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,015 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,015 [INFO] [tap_controller]: Received time from broker: 1620.0
tap-controller  | 2021-05-07 22:29:15,015 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 11
tap-controller  | 2021-05-07 22:29:15,015 [INFO] [tap_controller]: Commanded taps to position 12
tap-controller  | 2021-05-07 22:29:15,015 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,015 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,015 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,017 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,017 [INFO] [tap_controller]: Received time from broker: 1680.0
tap-controller  | 2021-05-07 22:29:15,017 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 12
tap-controller  | 2021-05-07 22:29:15,017 [INFO] [tap_controller]: Commanded taps to position 13
tap-controller  | 2021-05-07 22:29:15,018 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,018 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,018 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,022 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,023 [INFO] [tap_controller]: Received time from broker: 1740.0
tap-controller  | 2021-05-07 22:29:15,023 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 13
tap-controller  | 2021-05-07 22:29:15,023 [INFO] [tap_controller]: Commanded taps to position 14
tap-controller  | 2021-05-07 22:29:15,023 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,023 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,023 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,026 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,027 [INFO] [tap_controller]: Received time from broker: 1800.0
tap-controller  | 2021-05-07 22:29:15,027 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 14
tap-controller  | 2021-05-07 22:29:15,027 [INFO] [tap_controller]: Commanded taps to position 15
tap-controller  | 2021-05-07 22:29:15,027 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,027 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,027 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,030 [INFO] [tap_controller]: ********************************************************************************
tap-controller  | 2021-05-07 22:29:15,030 [INFO] [tap_controller]: Received time from broker: 1860.0
tap-controller  | 2021-05-07 22:29:15,030 [INFO] [tap_controller]: GridLAB-D reports tap_A at position 15
tap-controller  | 2021-05-07 22:29:15,030 [INFO] [tap_controller]: Commanded taps to position 16
tap-controller  | 2021-05-07 22:29:15,030 [INFO] [tap_controller]: Phase voltage_A voltage is nan.
tap-controller  | 2021-05-07 22:29:15,031 [INFO] [tap_controller]: Phase voltage_B voltage is nan.
tap-controller  | 2021-05-07 22:29:15,031 [INFO] [tap_controller]: Phase voltage_C voltage is nan.
tap-controller  | 2021-05-07 22:29:15,032 [INFO] [tap_controller]: Federate finalized.
helics-broker   | [2021-05-07 22:29:15.033] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(3) size 17 at 1920 to 131072
helics-broker   | [2021-05-07 22:29:15.033] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(4) size 17 at 1920 to 131072
helics-broker   | [2021-05-07 22:29:15.033] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(5) size 17 at 1920 to 131072
helics-broker   | [2021-05-07 22:29:15.033] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(6) size 9 at 1920 to 131072
helics-broker   | [2021-05-07 22:29:15.033] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(3) size 17 at 1980 to 131072
helics-broker   | [2021-05-07 22:29:15.034] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(4) size 17 at 1980 to 131072
helics-broker   | [2021-05-07 22:29:15.034] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(5) size 17 at 1980 to 131072
helics-broker   | [2021-05-07 22:29:15.034] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(6) size 9 at 1980 to 131072
helics-broker   | [2021-05-07 22:29:15.034] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(3) size 17 at 2040 to 131072
helics-broker   | [2021-05-07 22:29:15.034] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(4) size 17 at 2040 to 131072
helics-broker   | [2021-05-07 22:29:15.034] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(5) size 17 at 2040 to 131072
helics-broker   | [2021-05-07 22:29:15.034] [console] [warning] commWarning||8-iyFCl-yoKAc-OaIIL-yfe7X (1)::unknown route and no broker, dropping message pub:From (131073) handle(6) size 9 at 2040 to 131072
WARNING  [2018-01-01 00:30:00 UTC] : last warning message was repeated 2 times
gridlab-d       | WARNING  [2018-01-01 00:30:00 UTC] : Regulator vreg has phase A at the maximum tap value
gridlab-d       |
gridlab-d       | Core profiler results
gridlab-d       | ======================
gridlab-d       |
gridlab-d       | Total objects                 36 objects
gridlab-d       | Parallelism                    1 thread
gridlab-d       | Total time                   3.0 seconds
gridlab-d       |   Core time                  1.7 seconds (55.1%)
gridlab-d       |     Compiler                 0.0 seconds (0.6%)
gridlab-d       |     Instances                0.0 seconds (0.0%)
gridlab-d       |     Random variables         0.0 seconds (0.0%)
gridlab-d       |     Schedules                0.0 seconds (0.0%)
gridlab-d       |     Loadshapes               0.0 seconds (0.0%)
gridlab-d       |     Enduses                  0.0 seconds (0.0%)
gridlab-d       |     Transforms               0.0 seconds (0.0%)
gridlab-d       |   Model time                 1.3 seconds/thread (44.9%)
gridlab-d       | Simulation time                0 days
gridlab-d       | Simulation speed               7 object.hours/second
gridlab-d       | Passes completed              36 passes
gridlab-d       | Time steps completed          36 timesteps
gridlab-d       | Convergence efficiency      1.00 passes/timestep
gridlab-d       | Read lock contention        0.0%
gridlab-d       | Write lock contention       0.0%
gridlab-d       | Average timestep             58 seconds/timestep
gridlab-d       | Simulation rate             700 x realtime
gridlab-d       |
gridlab-d       |
gridlab-d       | Model profiler results
gridlab-d       | ======================
gridlab-d       |
gridlab-d       | Class            Time (s) Time (%) msec/obj
gridlab-d       | ---------------- -------- -------- --------
gridlab-d       | helics_msg         1.210     89.9%   1210.0
gridlab-d       | node               0.115      8.5%     38.3
gridlab-d       | recorder           0.016      1.2%      4.0
gridlab-d       | triplex_meter      0.002      0.1%      0.7
gridlab-d       | transformer        0.001      0.1%      0.2
gridlab-d       | triplex_node       0.001      0.1%      0.3
gridlab-d       | triplex_line       0.001      0.1%      0.3
gridlab-d       | ================ ======== ======== ========
gridlab-d       | Total              1.346    100.0%     37.4
gridlab-d       |
gridlab-d       | WARNING  [2018-01-01 00:33:00 UTC] : last warning message was repeated 11 times
helics-broker exited with code 0
tap-controller exited with code 0
gridlab-d exited with code 0
```

Note that the same voltage "explosion" happens, but this time at time
`900`.

### Run model, but without HELICS
This model can be run without HELICS, using player files to control
taps instead. This works with no problems. To do this, do the following:

1.  In `models/model.glm` remove the lines that say `module connection;`
    and remove the `object helics_msg {...}` block.
    
2.  At the end of `model.glm`, at the following objects:
```
object player {
    name tap_player_A;
    parent vreg;
    property tap_A;
    file ./tap_player.player;
    loop 100;
}
object player {
    name tap_player_B;
    parent vreg;
    property tap_B;
    file ./tap_player.player;
    loop 100;
}
object player {
    name tap_player_C;
    parent vreg;
    property tap_C;
    file ./tap_player.player;
    loop 100;
}
```

3. Create a file `models/tap_player.player` with the following contents:
```
2017-12-31 23:59:00, 16,
+60s, 16,
+60s, 15,
+60s, 14,
+60s, 13,
+60s, 12,
+60s, 11,
+60s, 10,
+60s, 9,
+60s, 8,
+60s, 7,
+60s, 6,
+60s, 5,
+60s, 4,
+60s, 3,
+60s, 2,
+60s, 1,
+60s, 0,
+60s, -1,
+60s, -2,
+60s, -3,
+60s, -4,
+60s, -5,
+60s, -6,
+60s, -7,
+60s, -8,
+60s, -9,
+60s, -10,
+60s, -11,
+60s, -12,
+60s, -13,
+60s, -14,
+60s, -15,
+60s, -16,
+60s, -16
```

4.  Run the model by changing directories to the top level of the repo,
    and execute `docker compose up`. Note you'll need to use `Ctrl + C`
    to kill the program, as the `helics_broker` will wait forever for
    the GridLAB-D federate to join the co-simulation, and it never will
    since we removed the HELICS connection.
    
5.  Take a look at the `.csv` files in the `models` directory, and
    notice that all is well (no voltage explosions.)
