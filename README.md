# CPSC 449 Project-1

Luc Dang

## Project Description:

- This project will mimic the behavior of FOAAS, but will filter and censor profanity using Purgomalum's API
  - The project will request data from the FOAAS API and filter it through Purgomalum's API, and either print to the command line or dynamically generate HTML on a local server
- Original FOAAS usage: https://foaas.com/

## Contents:

- README.md: README file for the project
- redact.py: command line utility for the project that will print the filtered result to the command prompt
- server.py: python server script that will host at port 8080 and will mimic the behavior of FOAAS and it's url queries but on the local server

## Instructions

- Extract the .tar file into a directory.
- Navigate into that directory and open a terminal or command prompt.
- For the command line utility, run `python3 redact.py /path/path` with the desired FOAAS path
- For the local server and dynamically generated HTML, run the python script with `python3 server.py`
- Open a browser and navigate to `localhost:8080`
- Complete the URL with desired FOAAS query
  - Example `localhost:8080/because/ProfAvery`
