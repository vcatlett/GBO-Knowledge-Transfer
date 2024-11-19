.. _jenkins:

*******
Jenkins
*******

.. figure:: ./img/jenkins_logo.png
  :align: center
  :width: 200
  :alt: The Jenkins logo

Jenkins is our continuous integration tool. 

Creating a Jenkins API Key
==========================

If you're just starting with Jenkins at GBO, you need to set up an API key. To set up a Jenkins API key, do the following:

#. Generate a Jenkins API key here: http://ci.greenbankobservatory.org/user/{username}/configure 
#. Save the key to ``/home/users/{username}/.jenkins_api_token``
#. Make sure this can only be read by you: ``chmod 600 .jenkins_api_token``