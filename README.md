# Docker Bench Report Converter

This project provides a tool for converting the output of the `docker-bench` security script into a structured JSON format and generates an HTML report for easy viewing. 

## Features

- **Convert `docker-bench` Output to JSON:** Processes the raw text output from `docker-bench` and converts it into a well-structured JSON format.
- **Generate HTML Report:** Creates a user-friendly HTML report from the JSON data, making it easy to review and share the results.

## Prerequisites

- **Python:** Ensure you have Python 3.x installed on your machine.
- **Docker:** Docker should be installed if you plan to run `docker-bench` yourself.

## Usage

1. **Run Docker Bench:**

    First, run the `docker-bench` script to generate the `.txt` output file:

    ```bash
    docker run -it --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /var/lib:/var/lib \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /usr/lib/systemd:/usr/lib/systemd \
    -v /etc:/etc --label docker_bench_security \
    docker/docker-bench-security
    ```

2. **Convert to JSON and Generate Report:**

    Use the provided Python script `docker_bench_make_json.py` to convert the output to JSON format.

    This will produce a `docker_bench_results.json` file in the json_output directory.

    Then use the provided Python script `docker_bench_make_report.py` to generate the report.

    This will produce a `docker_bench_report.html` file in the same directory.


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your proposed changes. Ensure your code adheres to the existing style and passes all tests.

---

Thank you for using Docker Bench Report Maker!
