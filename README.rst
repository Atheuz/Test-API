README
======

|version|

Your documentation goes here...

Running locally
---------------

To run locally, use the following commands:

.. code:: bash

  docker-compose up -d redis
  python run.py

Then try to visit `http://localhost:8000/api/v1/basic/ping`.

Running in docker
-----------------

To run in docker, use the following command:

.. code:: bash

  docker-compose up -d

Building container images
-------------------------

To rebuild container images in docker-compose without caching, use the following command:

.. code:: bash

  docker-compose build --no-cache


.. |version| image:: https://img.shields.io/badge/calver-2019.03.1-blue.svg
   :alt: 2019.03.1
