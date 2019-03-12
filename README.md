# NGPaaS Dynamic Dashboards Generator

## Synopsis
This is a Proof of Concept (POC) for the NGPaaS Dynamic Dashboards Generator.
The main aim is to provide an application to manage monitoring dashboards dynamically.

## Architecture and implementation design
The application is designed to operate in a event-driven environment where each event received on the
message broker represents a job to be enqueued and then worked.

So that, the application is mainly composed by two services:
* `dynamic-dashboards-generator`: which is charge of consuming events and enqueuing jobs
* `dynamic-dashboards-generator-redis-worker`: which is in charge of working jobs from the queue

The dashboard generation process has to:
* create a technology-agnostic dashboard model representation
* create a specific dashboard representation for one or more data visualization tools (e.g.: Kibana/Grafana/...)
* push the created dashboard to the data visualization tools

The generated dashboards need to be persisted in dedicated storage and eventually updated.

## How to execute
In order to create a reproducible environment, Dockerfiles are available.

Also, a `docker-compose.*.yml` files are provided to speed-up development and lay the foundations for a more complex setup.

> N.B.: all the commands are intended to be executed from the project root directory (`dynamic-dashboards-generator/`)

### Docker Compose execution
Requirements to run with Docker Compose:

* Docker Engine 18.02.0+
* Docker Compose 1.20.0+

Run the following command to build the services:
```
$ docker-compose build
```

Then, run the following command to run the services:
```
$ docker-compose up
```

The `docker-compose.yml` contains the two main services. The `docker-compose.override.yml` contains the dependencies such as storage engines and message brokers.

## License
This project is licensed under the AGPLv3. See the [LICENSE.md](LICENSE.md) file for details.
