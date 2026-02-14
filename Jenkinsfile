pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/satyajitsonkar96-afk/Cloud-Native-CI-CD-Pipeline-on-AWS.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m py_compile app/main.py || exit 1
                '''
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t cloud-native-app .
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker rm -f cloud-native-app || true
                docker run -d -p 80:5000 --restart always --name cloud-native-app cloud-native-app
                '''
            }
        }
    }
}
