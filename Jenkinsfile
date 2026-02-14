pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/satyajitsonkar96-afk/Cloud-Native-CI-CD-Pipeline-on-AWS.git'
            }
        }

        stage('Install Dependencies') {
    steps {
        sh '''
            python3 -m venv venv
            ./venv/bin/python -m pip install -r app/requirements.txt
        '''
    }
}


        stage('Run Tests') {
            steps {
                sh 'python3 -m py_compile app/main.py'
            }
        }

stage('Build Docker Image') {
    steps {
        sh 'docker build -t cloud-native-app .'
    }
}

stage('Deploy Application') {
    steps {
        sh '''
        docker rm -rf cloud-native-app || true
        docker run -d -p 5000:5000 --name cloud-native-app cloud-native-app
        '''
    }
}


    }
}
