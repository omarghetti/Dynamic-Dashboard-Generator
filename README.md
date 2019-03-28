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

Also, a `docker-compose*.yml` files are provided to speed-up development and lay the foundations for a more complex setup.

> N.B.: all the commands are intended to be executed from the project root directory (`dynamic-dashboards-generator/`)

### Docker Compose execution
Requirements to run with Docker Compose:

* Docker Engine 18.02.0+
* Docker Compose 1.20.0+

Run the following command to build the services:

```bash
$ docker-compose build
```

Then, run the following command to execute *all* the services:

```bash
$ docker-compose up
```

The `docker-compose.yml` contains the two main services. The `docker-compose.override.yml` contains the dependencies such as storage engines, message brokers and data visualization tools. It is strongly advised to specify the services to be run in order to reduce the workload.

For instance, the `docker-compose.override.yml` holds both Elasticsearch + Kibana and Grafana. However, most of the development scenarios requires to run only one of them.

Therefore, an example could be:

```bash
$ docker-compose up dynamic-dashboards-generator dynamic-dashboards-generator-redis-worker mongodb redis kafka kibana
```

## How to publish messages using the Kafka shell
The Dynamic Dashboards Generator works using an event-driven approach. Thus, it is subscribed to one or more Kafka topics and reacts to the messages received.

To publish a message using the Kafka shell run the following commands:

```bash
$ docker-compose exec kafka bash
$ $KAFKA_HOME/bin/kafka-console-producer.sh --topic=your_topic --broker-list='localhost:9092' # substitute your_topic with the topic in the .env file
$ your_message # publish whatever you want, i.e. a JSON payload
```

## License
This project is licensed under the AGPLv3. See the [LICENSE.md](LICENSE.md) file for details.
