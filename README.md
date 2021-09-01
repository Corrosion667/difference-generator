# Difference generator

[![Actions Status](https://github.com/Corrosion667/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Corrosion667/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/50b02185e2d65163855c/maintainability)](https://codeclimate.com/github/Corrosion667/python-project-lvl2/maintainability)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![linter-and-test-check](https://github.com/Corrosion667/python-project-lvl2/actions/workflows/linter-and-test-check.yml/badge.svg)](https://github.com/Corrosion667/python-project-lvl2/actions/workflows/linter-and-test-check.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/50b02185e2d65163855c/test_coverage)](https://codeclimate.com/github/Corrosion667/python-project-lvl2/test_coverage)

---

## Basic information

**Difference generator** *(further - gendiff)* is a programm that determines the difference between two data structures.
Then made difference is being presented in one of three formats to choose from.
Gendiff currently works with **JSON** and **YML/YAML** files.


## Quickstart

**Gendiff** at the moment are stored only at *github* so the quickest and the easiest way to install them is to use *pip* with URL of repository.
```bash
pip install git+HTTPS
```

## Running

Basic **Gendiff** syntax looks like this:
```bash
gendiff --format path/to/file1 path/to/file2
```
*format* is an optional argument. Its deafult value is *'stylish'*. But all three formatters will be described below.

You can also recall about main features and syntax of a program using *help command*:
```bash
gendiff -h
```

## Formatters

As was said above, there are three formatters which gendiff currently supports:

|   **Formatter**   |                                    **Description**                                    |
|-------------------|---------------------------------------------------------------------------------------|
|     *stylish*     | default one; json-like format with '-' for deleted elements and '+' for added         |       
|      *plain*      | thesis-like format with satements about adding, updating and removal of elements      |      
|      *json*       | classic json; list of lists with following structure: [key, value_file1, value_file2] |

The work of different formatters will be clearly demonstrated below using asciinema service.

## Asciinema demonstrations:

Installing the whole package. Then launching **Gendiff** for two flat JSON files using stylish (default) formatter.
[![asciicast](https://asciinema.org/a/pGDPAA50ZBFo46MyBhIZvIejW.svg)](https://asciinema.org/a/pGDPAA50ZBFo46MyBhIZvIejW)

Launching **Gendiff** for two flat YAML files using stylish (default) formatter.
[![asciicast](https://asciinema.org/a/6iRsV5E8hMk4tMzYUScoHhsoe.svg)](https://asciinema.org/a/6iRsV5E8hMk4tMzYUScoHhsoe)
