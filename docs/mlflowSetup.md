# MLFLOW setup

 install mlflow
 create MLproject file containing details of conda environments, below is the basic structure of file.
```
name: project name

conda_env: conda.yaml
# Can have a docker_env instead of a conda_env, e.g.
# docker_env:
#    image:  mlflow-docker-example

entry_points:
  main:  
    command: "python src/main.py"
```
