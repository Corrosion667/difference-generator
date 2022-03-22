# Difference generator

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

**Gendiff** at the moment is stored only at *github* so the quickest and the easiest way to install it is to use *pip* with URL of repository.
```bash
pip install git+https://github.com/Corrosion667/difference-generator.git
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
|      *json*       | classic json; list of lists with following structure: [key, status, value(s)]         |

The work of different formatters will be clearly demonstrated below using asciinema service.

## Asciinema demonstrations:

Installing the whole package. Then launching *help* menu of **Gendiff**.
[![asciicast](https://asciinema.org/a/Ffoe9VgxrYA8CjudTMHcykBsg.svg)](https://asciinema.org/a/Ffoe9VgxrYA8CjudTMHcykBsg)

**Gendiff** usage for *flat* files.
[![asciicast](https://asciinema.org/a/Rq0Yc2OGVQSQvIX6hAK2f46dS.svg)](https://asciinema.org/a/Rq0Yc2OGVQSQvIX6hAK2f46dS)

**Gendiff** usage for *nested* files.
[![asciicast](https://asciinema.org/a/0GEMpuFgtyJWFscP8RuXlPLuH.svg)](https://asciinema.org/a/0GEMpuFgtyJWFscP8RuXlPLuH)