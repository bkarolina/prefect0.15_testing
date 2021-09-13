from typing import List
from prefect.run_configs import LocalRun
from prefect import Flow, Parameter, task
from prefect.engine.results import LocalResult
from prefect.tasks.prefect import create_flow_run, get_task_run_result
from recipes import recipe
import os

working_dir = os.getcwd()
with Flow("child") as child_flow:
    leng = Parameter("leng", default=1)
    file = Parameter("file", default='sample.csv')
    data = recipe.partial_data(file, leng)

@task(log_stdout=True)
def add_column(data):
    print(f"Got: {data!r}")
    new_data = ['value'] * leng
    print(f"Created: {new_data!r}")
    return new_data

with Flow("parent") as parent_flow:
    child_run_id = create_flow_run(flow_name=child_flow.name, parameters=dict(file='test.csv', leng=5))
    child_data = get_task_run_result(child_run_id, "get_some_data_1")
    add_column(child_data)
parent_flow.run_config = LocalRun(working_dir=working_dir)
