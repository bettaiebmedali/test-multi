pipeline {
    agent any

    environment {
        DOCKER_CREDS = credentials('docker_hub')
        ENV_FILE = readFile('.env').split("\n")
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${env.BRANCH_NAME}", url: 'https://github.com/bettaiebmedali/test-multi'
            }
        }

        stage('Charger .env') {
            steps {
                script {
                    for (line in ENV_FILE) {
                        if (line.trim() && !line.startsWith('#')) {
                            def parts = line.tokenize('=')
                            env[parts[0]] = parts[1]
                        }
                    }
                    echo "Application : ${APP_NAME}"
                    echo "Version : ${APP_VERSION}"
                }
            }
        }

   

      

        stage('Deploy') {
            when { branch 'main' }
            steps {
                echo "Déploiement de ${APP_NAME}:${APP_VERSION} sur PROD..."
            }
        }
    }

    post {
    success {
        echo "✅ Build réussi pour ${env.APP_NAME}:${env.APP_VERSION}"
    }
    failure {
        echo "❌ Échec du build ${env.APP_NAME}"
    }
}
}