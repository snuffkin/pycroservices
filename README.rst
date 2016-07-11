pycroservices
=============
pycroservices is a microservices framework on AWS Lambda.

pycroservices runs AWS Lambda functions designed as a directed acyclic graph.
Here is a list of the package contents:

* provide mechanism that makes functions loosely coupled with each other

* run on AWS Lambda

* run on local machine

* provide template creation tool (future work)

* provide graph creation tool (future work)

* provide endopoint creation tool (future work)

* provide validation tool (future work)

* provide deployment tool (future work)

* provide event tracing mechanism

* provide infinite loop limiter

pycroservices is a free software distributed under the Apache license version 2.0.


Installation
============

To install pycroservices, type at your function directory::

    pip install pycroservices -t /path/to/your-function-dir

pycroservices requires Python 2.7 and boto3.


Deployment
==========

Zip the content of the your-function-dir directory, which consists of the following contents:

* your function codes

* configuration files (<function_name>.json)

* pycroservices.py

Upload the zip file to AWS Lambda.


Websites
========

* `pycroservices project at GitHub <https://github.com/snuffkingit/pycroservices>`_: source
  code, bug tracker
