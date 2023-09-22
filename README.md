# what was done

Here's a summary of the features and tasks that have been completed:
1.Integrated Automation Migration Tracking into Flask
2.Dockerized the Application (Both Sides)
3.Dockerized Database, Configured Environment
4.Used TypeScript for Code Design
5.Improved UI (integrated tailwind for styling)
6. Added "Add Task Feature"
7. Added  "Removed Task Feature"
8. done "Mark Task as Completed Feature"

# How to run 
1. `git clone <repo url>`
2. got to the folder of the project
3. ui (frontend side) api | (flask backend side)
4. how to run frontend without docker you can find dock in ./ui/Readme.md
5. how to run backend without docker you can find dock in ./api/Readme.md
6. configure .env files (you can find .env examples in each of directory just rename to .env)
6. to be able to run with docker
`
docker compose up
`
7. go to localhsot:3000 for the frontend part
8. for backend side ping to localhsot:5000

## Summary of the docker file 

In each of directory you can find Docker Files which will dockerize the app and in the root folder you can find the `docker-compose.yaml file` which are creating and configuring environment

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Create a pull request to merge your changes into the main repository.

Feel free to open issues for any bugs, feature requests, or questions you may have.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for more details.
