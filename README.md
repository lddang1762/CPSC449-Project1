# CPSC 449 Project-1

Luc Dang

## Project Description:

- This project will mimic the behavior of FOAAS, but will filter and censor profanity using Purgomalum's API
  - The project will request data from the FOAAS API and filter it through Purgomalum's API, and finally dynamically generate HTML on a local server
- Original FOAAS usage: https://foaas.com/

## Contents:

- README.md: README file for the project
- redact.py: Python script that fulfills the project description

## Instructions

- Extract the .tar file into a directory.
- Navigate into that directory and open a terminal or command prompt.
- Run the python script with `python3 redact.py`
- Open a browser and navigate to `localhost:8080`
- Complete the URL with desired FOAAS query
  - Example `localhost:8080/because/ProfAvery`
