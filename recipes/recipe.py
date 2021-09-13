from prefect import Flow, Parameter, task
from prefect.engine.results import LocalResult
from prefect.tasks.prefect import create_flow_run, get_task_run_result

@task(result=LocalResult())
def partial_data(file, leng):
    data = pd.read_csv(file)
    return data[:leng]

#with Flow("child") as child_flow:
#    length = Parameter("length", default=1)
#    file = Parameter("file", default='sample.csv')
#    data = partial_data(file, length)


