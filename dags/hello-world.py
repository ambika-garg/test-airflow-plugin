from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

from airflowPlugin import PluginOperator

with DAG(
    dag_id="hello-world",
    start_date=datetime(2023, 8, 15),
    schedule="@once",
    tags=["tutorial"]
) as dag:
    # Tasks are represented as operators
    task1 = BashOperator(task_id="task1", bash_command="echo task2")

    task2 = BashOperator(task_id="task2", bash_command="echo task2")

    task3 = BashOperator(task_id="task3", bash_command="ls /opt/airflow/git/test-airflow-plugin.git")

    task4 = BashOperator(task_id="task4", bash_command="ls")

    task5 = PluginOperator(task_id="plugin", name="foo_bar")

    # Set dependencies between tasks
    task1 >> task2 >> task3 >> task4 >> task5