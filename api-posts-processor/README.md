# API Posts Processor

Python script that consumes a REST API using the requests library, processes JSON data based on configurable criteria, and exports filtered results to a CSV file.

The project demonstrates clean code structure, error handling, and a gradual refactoring process similar to real-world development practices.

## Features

- Consumes a public REST API
- Handles HTTP and network errors
- Filters data based on configurable parameters
- Exports processed data to CSV
- Logs execution summary
- Clean and readable code structure

## Technologies

- Python
- requests
- CSV (standard library)

## How it works

1. Fetches post data from a REST API  
2. Filters posts by user ID  
3. Exports selected fields to a CSV file  
4. Displays an execution summary

## Configuration

The script can be easily configured by modifying the constants at the top of the file:

- API endpoint
- Timeout
- User ID filter
- Output file name

## Usage

```bash
python api_posts_processor.py
