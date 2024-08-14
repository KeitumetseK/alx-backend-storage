# Redis Cache Project

This project involves implementing a `Cache` class to interact with a Redis server in Python. The class provides methods to store and retrieve data, track method calls, and store the history of method inputs and outputs. It also includes a `replay` function to display the history of function calls.

## Requirements

- Python 3.7
- Redis
- pycodestyle 2.5

## Setup

1. Install Redis on Ubuntu 18.04 LTS:
    ```bash
    sudo apt-get -y install redis-server
    ```
2. Install Python dependencies:
    ```bash
    pip3 install redis
    ```

3. Ensure Redis server is running:
    ```bash
    service redis-server start
    ```

## Usage

Run the main script:
```bash
python3 main.py

