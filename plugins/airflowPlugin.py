# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator

# Will show up under airflow.operators.test_plugin.PluginOperator
class PluginOperator(BaseOperator):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = f"Hello {self.name}"
        print(message)
        return message

# Defining the plugin class
class AirflowTestPlugin(AirflowPlugin):
    name = "test_plugin"
    operators = [PluginOperator]