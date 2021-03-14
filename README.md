# Cloud DevOps Engineer Capstone Project

This is the final project of the Cloud DevOps Engineer Udacity Nanodegree.

## Introduction

In this project I will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

- Working in AWS
- Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines

## Application

I have used a Django demo backend application with RESTful API. The following three endpoints are available.

| Endpoint | HTTP Method | CRUD Method | Result |
| ------- | --- | --- | --- |
| /api/movies | GET | READ | all movies |
| /api/movies/:id | GET | READ | get a single movie |
| /api/movies | POST | CREATE | add a movie |

## Infra Setup

Deploy

```bash
./create.sh $STACK_NAME $TEMPLATE_BODY $PARAMETERS
```

Update:

```bash
./update.sh $STACK_NAME $TEMPLATE_BODY $PARAMETERS
```

Delete:

```bash
./delete.sh $STACK_NAME
```
