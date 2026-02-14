pipeline {
    agent any

    environment {
        APP_NAME = "cloud-native-app"
        CONTAINER_NAME = "cloud-native-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/satyajitsonkar96-afk/Cloud-Native-CI-CD-Pipeline-on-AWS.git'
            }
        }

        stage('Verify Environment') {
            steps {
                sh '''
                python3 --version
                docker --version
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m py_compile app/main.py || exit 1
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $APP_NAME .
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker rm -f $CONTAINER_NAME || true

                docker run -d \
                    -p 127.0.0.1:5000:5000 \
                    --restart always \
                    --name $CONTAINER_NAME \
                    $APP_NAME
                '''
            }
        }

        stage('Post Deployment Check') {
            steps {
                sh '''
                docker ps
                curl -I http://127.0.0.1:5000 || true
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }
}
