=================================================
Installation with Miniconda (Windows, linux, OSX)
=================================================

0. Install Miniconda
--------------------

Follow official website instruction to install miniconda :

http://conda.pydata.org/miniconda.html

1. Install conda-build if not already installed
------------------------------------------------

.. code:: shell

    conda install conda-build

2. Create dss virtual environment and activate it
-------------------------------------------------

.. code:: shell

    conda create --name dss 
    source activate dss

3. Build and install dss package
---------------------------------

(Optional) Install several package managing tools :

.. code:: shell

    conda install -c openalea3 conda-forge dss 