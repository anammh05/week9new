pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t registration:v1 .'
            }
        }

        stage('Login & Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker tag registration:v1 anammh05/registration:v1'
                    bat 'docker push anammh05/registration:v1'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f C:\\Devops\\Week-2\\deployment.yaml'
                bat 'kubectl apply -f C:\\Devops\\Week-2\\service.yaml'
            }
        }

        stage('Automated UI Test') {
            steps {
                bat 'python D:\\Devops\\Week-2\\test_registration.py'
            }
        }
    }
}
