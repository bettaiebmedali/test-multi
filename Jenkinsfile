pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: "${env.BRANCH_NAME}",
                    url: 'https://github.com/bettaiebmedali/test-multi.git'
            }
        }

        stage('Charger .env') {
            steps {
                script {
                    def envFile = readFile('.env').split("\n")

                    for (line in envFile) {
                        line = line.trim()

                        if (line && !line.startsWith('#')) {
                            def parts = line.split('=', 2)

                            if (parts.size() == 2) {
                                env[parts[0].trim()] = parts[1].trim()
                            }
                        }
                    }

                    echo "Application : ${env.APP_NAME}"
                    echo "Version : ${env.APP_VERSION}"
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }

            steps {
                echo "Déploiement de ${env.APP_NAME}:${env.APP_VERSION} sur PROD..."
            }
        }
    }

    post {
        success {
            echo "Build réussi pour ${env.APP_NAME}:${env.APP_VERSION}"
        }

        failure {
            echo "Echec du build ${env.APP_NAME ?: 'application inconnue'}"
        }
    }
}