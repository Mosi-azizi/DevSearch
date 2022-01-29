from django.db.models import Model
from django.shortcuts import render

# Create your views here.
from DjangoSSHTunnelDatabaseConnector import Connector

with Connector(ssh_host='192.168.119.183', ssh_port='22', ssh_username='informix', ssh_password='ODc4MTJjMjZiNjFh',
               database_username='informix', database_password='ODc4MTJjMjZiNjFh', database_name='bsicore_old',
               localhost='', verbose=False) as sshTunnelDatabaseConnector:
    # The response of the object is an array of model objects that are read from the database
    query = Model.objects.filter(some_column="filter_word")
    model_objects = sshTunnelDatabaseConnector.read(Model, query)
    print(model_objects)