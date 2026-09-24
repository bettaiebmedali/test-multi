pipeline {

    agent any

    environment {
        // Configuration de l'application
        APP_NAME = ''
        APP_VERSION = ''

        // Docker Hub
        DOCKER_USER = 'vincentsono'
    }

    stages {

        stage('Charger .env') {
            steps {
                script {

                    // Lecture du fichier .env
                    def config = [:]

                    readFile('.env').split('\n').each { line ->

                        line = line.trim()

                        // Ignore les lignes vides et les commentaires
                        if (line && !line.startsWith('#')) {

                            def parts = line.split('=', 2)

                            if (parts.size() == 2) {
                                config[parts[0].trim()] = parts[1].trim()
                            }
                        }
                    }

                    // Récupération des valeurs
                    APP_NAME = config['APP_NAME']
                    APP_VERSION = config['APP_VERSION']

                    echo "================================"
                    echo "Application : ${APP_NAME}"
                    echo "Version     : ${APP_VERSION}"
                    echo "================================"
                }
            }
        }


        stage('Build Docker') {
            steps {

                echo "🐳 Construction de l'image Docker..."

                sh """
                    docker build \
                        -t ${DOCKER_USER}/${APP_NAME}:${APP_VERSION} \
                        -t ${DOCKER_USER}/${APP_NAME}:latest \
                        .
                """

                echo "✅ Image Docker construite"
            }
        }


        stage('Login Docker Hub') {
            steps {

                withCredentials([
                    string(
                        credentialsId: 'DOCKER_PASSWORD_VINCENT',
                        variable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                            -u "$DOCKER_USER" \
                            --password-stdin
                    '''
                }

                echo "✅ Connexion à Docker Hub réussie"
            }
        }


        stage('Push Docker') {
            steps {

                echo "📦 Push de l'image vers Docker Hub..."

                sh """
                    docker push ${DOCKER_USER}/${APP_NAME}:${APP_VERSION}
                    docker push ${DOCKER_USER}/${APP_NAME}:latest
                """

                echo "✅ Images poussées sur Docker Hub"
            }
        }


        stage('Deploy') {
            when {
                branch 'main'
            }

            steps {

                echo "🚀 Déploiement sur PROD..."

                echo "Application : ${APP_NAME}"
                echo "Version     : ${APP_VERSION}"

                // Déploiement simulé
                sh '''
                    echo "Déploiement en cours..."
                    sleep 3
                    echo "✅ Déploiement terminé"
                '''
            }
        }
    }


    post {

        success {
            echo """
            ========================================
            ✅ PIPELINE RÉUSSIE
            ========================================
            Application : ${APP_NAME}
            Version     : ${APP_VERSION}
            ========================================
            """
        }

        failure {
            echo """
            ========================================
            ❌ PIPELINE EN ÉCHEC
            ========================================
            Application : ${APP_NAME}
            Version     : ${APP_VERSION}
            ========================================
            """
        }

        always {
            echo "🏁 Fin du pipeline"
        }
    }
}