pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = 'dockerhub' // The ID of the Jenkins credentials
    }
    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t registration:v1 .'
            }
        }
        stage('Login & Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", 
                                                  usernameVariable: 'DOCKER_USER', 
                                                  passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    bat 'docker tag registration:v1 %DOCKER_USER%/registration:v1'
                    bat 'docker push %DOCKER_USER%/registration:v1'
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
                bat 'python C:/DevOps/week-2/test_registration.py'
            }
        }
    }
}
