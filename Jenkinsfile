pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'i200405/house-price-prediction-app:latest' // Docker Hub username and image name
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the Git repository
                git branch: 'master', url: 'https://github.com/HamzaSalarian/House-prodiction.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the specified tag
                    bat 'docker build -t %DOCKER_IMAGE% .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub and push the image
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                        bat 'docker push %DOCKER_IMAGE%'
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    bat 'docker run -d -p 5000:5000 %DOCKER_IMAGE%'
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker environment after build
            bat 'docker system prune -f'
        }
    }
}
