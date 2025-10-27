pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = 'dockerhub' // Jenkins credential ID
    }
    stages {
        stage('Build Docker Image') {
    steps {
        bat 'docker build -t anammh05/registration:v1 .'
    }
}

stage('Login & Push to Docker Hub') {
    steps {
        withCredentials([string(credentialsId: 'docker-pass', variable: 'DOCKER_PASS')]) {
            bat '''
            echo %DOCKER_PASS% | docker login -u anammh05 --password-stdin
            docker push anammh05/registration:v1
            '''
        }
    }
}


        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f C:/DevOps/week-2/deployment.yaml'
                bat 'kubectl apply -f C:/DevOps/week-2/service.yaml'
            }
        }

        stage('Automated UI Test') {
            steps {
                bat 'python C:/Devops/Week-2/test_registration.py'  
            }
        }
    }
}
