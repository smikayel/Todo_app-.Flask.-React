# Todo List

Thanks for your interest in joining Desupervised!

This is a small programming exercise to determine how well you deal with
challenges and can use material at your disposal to solve full stack programing tasks.

We estimate that the task should take no more than 3-5 hours (you're welcome to
spend longer on it, but please try to submit a solution within 5 working days).

## Description

In this exercise we'd like you to build a simple todo list, composed of a frontend,
backend and a database. One should be able to build and run it using `docker compose`.

We are intereseted in your over all skill level as a full stack developer, so we do not
require the a fancy UI expereince. It should just showcase the basic functionality
and your ability to set up a complete stack.

### Backend
It should be REST API written in python, using a framework such as `FastAPI`, `Litestar`, `Flask`,
or similar (Note internally we most commonly use `FastAPI`).

It should have a few endpoints that the UI can use too
 - add a task
 - remove a task

Optionally:
 - Mark task as completed
 - Archive a task

The tasks should be stored in a postgress db accessed via an ORM layer
ex. [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/).

## UI
We expect a very basic UI that shows the backend functionality. Similar to

![](basic_ui.png)


It should be buildt using [TypeScript](https://www.typescriptlang.org/) and [React](https://react.dev/), bonus points
if you use a component library such as [AntD](https://ant.design/) or [MUI](https://mui.com/).

## Reviewal

We'll be looking for a number of considerations when we review your submission:

- Coding style
- Correctness
- Usage of git or other tools (e.g. for testing/linting)

Note that we're interested in a balance of these considerations, so please don't
worry too much about any one particular aspect. Just code in a way you're
familiar with and be creative :)

If you have extra time there are a number of bonuses you can look into (these
are not at all mandatory):

- Search functionality
- Users
- Authentification
- Mark task as completed
- Acrive task

## Submission

Please include a README with a summary of your thoughts (why you included or
excluded certain things), if there was anything unclear about the task, or ideas
for things you would improve if you had more time.

In the repo there should be a `docker-compose.yml` file similar to

```yml
version: "3.7"

services:
  api:
    image: backend
    build: ./api
    ports:
    ...

  ui:
    image: backend
    build: ./ui
    ports:
      - 80:80
    ...

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres

```

and the README should also contain clear instructions on how to build and start the app e.x.

```bash
docker compose build
```
then
```bash
docker compose ui
```
then navigate to localhost:80.


Submit your solution as a link to a git repository owned by you. You can send
the link to [johan@desupervised.io](mailto:johan@desupervised.io).

Good luck!
