# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator

# Will show up under airflow.operators.test_plugin.PluginOperator
class PluginOperator(BaseOperator):
    pass

# Defining the plugin class
class AirflowTestPlugin(AirflowPlugin):
    name = "test_plugin"
    operators = [PluginOperator]