```text
Experiment 6 — Create Docker Image Using GitHub Repository and Build Using Jenkins Pipeline

Aim:
Create a Docker image from a GitHub repository, push it to Docker Hub, and automate the process using Jenkins Pipeline.

--------------------------------------------------

Step 1 — Open Required Applications

1. Open Docker Desktop
2. Wait until it shows:
   Engine running

3. Open Git Bash
4. Open VS Code
5. Open Jenkins in browser:
   http://localhost:8080

--------------------------------------------------

Step 2 — Create GitHub Repository

1. Open GitHub
2. Click:
   New Repository

3. Repository name:
   dockerprog

4. Click:
   Create Repository

5. Copy repository URL

Example:
https://github.com/username/dockerprog.git

--------------------------------------------------

Step 3 — Clone Repository Using Git Bash

Open Git Bash and type:

git clone https://github.com/username/dockerprog.git

After cloning:

cd dockerprog

--------------------------------------------------

Step 4 — Open Repository in VS Code

1. Open VS Code
2. Click:
   File → Open Folder
3. Select:
   dockerprog

--------------------------------------------------

Step 5 — Create Python File

Create file:
sample.py

Paste:

print("Hello World")

Save the file.

--------------------------------------------------

Step 6 — Create Dockerfile

Create file:
Dockerfile

Paste:

FROM python

WORKDIR /app

COPY . /app

CMD ["python","sample.py"]

Save the file.

--------------------------------------------------

Step 7 — Commit and Push Files to GitHub

Open terminal in VS Code or Git Bash.

Type:

git add .

git commit -m "Added Docker project"

git push origin main

Now files will be uploaded to GitHub repository.

--------------------------------------------------

Step 8 — Build Docker Image

In Git Bash terminal type:

docker build -t test.2 .

Explanation:
- docker build → builds image
- -t → tag/image name
- test.2 → image name
- . → current directory

--------------------------------------------------

Step 9 — Run Docker Container

Command:

docker run --name cont2 test.2

Output:

Hello World

--------------------------------------------------

Step 10 — Check Docker Images

Command:

docker images

You will see:

test.2

Copy the IMAGE ID.

--------------------------------------------------

Step 11 — Tag Docker Image

Command:

docker tag IMAGE_ID username/test.2

Example:

docker tag cb3ded3a739a shamanth/test.2

--------------------------------------------------

Step 12 — Push Image to Docker Hub

First login:

docker login

Then push image:

docker push username/test.2:latest

Example:

docker push shamanth/test.2:latest

--------------------------------------------------

Step 13 — Open Jenkins

Open browser:

http://localhost:8080

--------------------------------------------------

Step 14 — Install Required Plugins

In Jenkins:

1. Click:
   Manage Jenkins

2. Click:
   Plugins

3. Update installed plugins

4. Make sure these plugins are installed:

- Docker
- Docker Pipeline
- Docker Compose Build Step
- CloudBees Docker Build and Publish

--------------------------------------------------

Step 15 — Create Jenkins Pipeline Project

1. Click:
   New Item

2. Enter name:
   Doc2

3. Select:
   Pipeline

4. Click:
   OK

--------------------------------------------------

Step 16 — Add Pipeline Script

Scroll to:
Pipeline

Select:
Pipeline Script

Paste:

pipeline {

    agent any

    environment {

        dockerImage = "username/test.2"
        registry = "username/test.2"
        registryCredential = "jenkin_docker_token"

    }

    stages {

        stage('Checkout') {

            steps {

                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/username/dockerprog.git']]
                )

            }

        }

        stage('Build Docker Image') {

            steps {

                script {

                    dockerImage = docker.build(registry)

                }

            }

        }

    }

}

--------------------------------------------------

Step 17 — Save Pipeline

Click:
Save

--------------------------------------------------

Step 18 — Build Pipeline

On left sidebar click:

Build Now

If build is successful, you will see:
#1 Success

--------------------------------------------------

Output:

Hello World

Docker Image:
test.2

Container Name:
cont2
```
