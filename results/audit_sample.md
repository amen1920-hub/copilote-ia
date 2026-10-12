# Audit manuel : 20 exemples tires au hasard

Pour chaque exemple, note ton verdict. Question a te poser : *un chef de projet trouverait-il ce decoupage et ces durees credibles ?*

## 1. gestion hôtelière (contraintes) - total 28 jours

**Demande :** Je souhaite développer une application web de gestion hôtelière pour faciliter les réservations de nos 15 chambres. Le projet doit être réalisé en moins de 6 semaines par notre petite équipe de 2 développeurs, en utilisant exclusivement le framework Next.js pour le frontend et le backend.

- [Base de données] 3 j - **Schéma de la base de données** : Modélisation des tables clients, chambres et réservations sous PostgreSQL.
- [Backend] 5 j - **API de gestion des réservations** : Développement des endpoints pour créer, lire et annuler une réservation via Next.js API routes.
- [Frontend] 6 j - **Interface de calendrier des disponibilités** : Création du dashboard interactif permettant de visualiser le taux d'occupation par date.
- [Sécurité] 4 j - **Système d'authentification des employés** : Mise en place de la connexion sécurisée via JWT pour l'accès au portail de gestion.
- [Frontend] 3 j - **Formulaire de saisie client** : Développement du module frontend pour l'enregistrement des nouveaux clients et de leurs coordonnées.
- [Tests] 3 j - **Tests unitaires des calculs de prix** : Vérification de la logique métier pour le calcul des tarifs selon la saisonnalité.
- [DevOps] 2 j - **Déploiement sur environnement cloud** : Configuration du pipeline CI/CD et déploiement de l'application sur Vercel.
- [Documentation] 2 j - **Guide utilisateur du back-office** : Rédaction de la documentation pour la gestion des réservations par le personnel.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 2. plateforme e-learning (detaillee) - total 37 jours

**Demande :** Nous voulons développer une plateforme d'apprentissage en ligne dédiée aux professionnels de l'artisanat, permettant aux experts de publier des tutoriels vidéo haute définition. Je veux que les apprenants puissent suivre leur progression, passer des quiz interactifs à la fin de chaque chapitre et obtenir un certificat numérique généré automatiquement. La plateforme doit intégrer un système de paiement sécurisé par abonnement mensuel pour accéder à l'intégralité du catalogue de formations.

- [Design] 5 j - **Design de l'interface utilisateur** : Création des maquettes haute fidélité pour le tableau de bord apprenant et le lecteur vidéo.
- [Base de données] 3 j - **Schéma de la base de données** : Conception du modèle relationnel pour les utilisateurs, les cours, les chapitres et les résultats des quiz.
- [Backend] 4 j - **API de gestion des utilisateurs et authentification** : Mise en place des endpoints pour l'inscription, la connexion et la gestion des profils avec JWT.
- [Frontend] 6 j - **Intégration du lecteur vidéo et suivi de progression** : Développement du composant frontend de lecture vidéo et synchronisation de l'état d'avancement avec le serveur.
- [Backend] 4 j - **Module de quiz interactifs** : Implémentation de la logique de validation des réponses aux quiz et calcul des scores.
- [Backend] 5 j - **Système de paiement et abonnements** : Intégration de Stripe pour gérer les abonnements récurrents et l'accès aux contenus restreints.
- [Backend] 3 j - **Service de génération de certificats PDF** : Développement d'un micro-service pour générer et télécharger des certificats personnalisés en PDF.
- [Tests] 4 j - **Tests d'acceptation utilisateur** : Rédaction et exécution des tests unitaires et fonctionnels sur le tunnel d'achat et le suivi de cours.
- [DevOps] 3 j - **Déploiement et infrastructure cloud** : Configuration du pipeline CI/CD et déploiement sur environnement cloud sécurisé.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 3. plateforme e-commerce de vêtements (contraintes) - total 32 jours

**Demande :** Nous voulons lancer une boutique en ligne de prêt-à-porter fonctionnelle sous 6 semaines avec une équipe restreinte de 3 développeurs. La solution doit impérativement être développée en utilisant uniquement l'écosystème Next.js et Shopify Storefront API pour respecter notre budget serré.

- [Base de données] 3 j - **Configuration du schéma produit** : Mise en place de la structure des données et synchronisation avec l'API Shopify pour les variantes de vêtements.
- [Frontend] 5 j - **Intégration du catalogue et filtres** : Développement des pages de listing produits avec filtres dynamiques par taille, couleur et catégorie.
- [Backend] 4 j - **API de gestion du panier** : Implémentation de la logique de session pour le panier d'achat persistant via l'API Storefront.
- [Design] 5 j - **Maquettes UI responsive** : Conception des interfaces mobile-first pour les pages produits, le panier et le tunnel de commande.
- [Sécurité] 6 j - **Tunnel de checkout sécurisé** : Mise en œuvre du flux de paiement sécurisé en conformité avec les normes PCI-DSS via Shopify.
- [DevOps] 3 j - **Déploiement et CI/CD** : Configuration du pipeline de déploiement continu sur Vercel avec gestion des environnements de staging et production.
- [Tests] 4 j - **Tests d'acceptation utilisateur** : Rédaction et exécution de scripts de test pour valider le parcours client complet, de la sélection à l'achat.
- [Documentation] 2 j - **Guide d'administration boutique** : Rédaction de la documentation technique pour la gestion des stocks et des commandes par l'équipe marketing.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 4. gestion de copropriété (contraintes) - total 35 jours

**Demande :** Je souhaite développer une plateforme web de gestion de copropriété permettant aux résidents de payer leurs charges et de signaler des incidents en ligne. Nous avons un budget très limité et imposons l'utilisation de React et Node.js pour une équipe restreinte de 2 développeurs, avec une livraison complète prévue sous 8 semaines.

- [Base de données] 3 j - **Conception du schéma relationnel** : Modélisation des tables pour les résidents, les appartements, les charges et les tickets d'incidents.
- [Backend] 5 j - **API REST de gestion des charges** : Développement des endpoints pour calculer et consulter le solde des charges par copropriétaire.
- [Sécurité] 4 j - **Système d'authentification JWT** : Implémentation de la connexion sécurisée pour les résidents et les administrateurs avec gestion des rôles.
- [Frontend] 5 j - **Interface de saisie des incidents** : Développement du formulaire React permettant de signaler un problème avec upload de photo.
- [Frontend] 6 j - **Dashboard de suivi des requêtes** : Création de la vue administrateur pour consulter et mettre à jour le statut des tickets d'incidents.
- [Backend] 5 j - **Intégration du module de paiement** : Connexion à l'API Stripe pour permettre le règlement des charges en ligne.
- [Tests] 4 j - **Tests unitaires des services critiques** : Rédaction des tests pour le moteur de calcul des charges et l'authentification.
- [DevOps] 3 j - **Déploiement sur serveur cloud** : Configuration du pipeline CI/CD et déploiement de l'application sur un serveur VPS.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 5. suivi de notes de frais (courte) - total 27 jours

**Demande :** Nous voulons une application intuitive permettant à nos employés de soumettre leurs notes de frais et aux managers de les valider rapidement.

- [Base de données] 2 j - **Modèle de données des notes** : Conception du schéma relationnel pour stocker les justificatifs, les montants et les états de validation des notes.
- [Backend] 5 j - **API de gestion des frais** : Développement des points de terminaison REST pour la création, la lecture et la modification des notes de frais.
- [Frontend] 5 j - **Interface de saisie** : Développement du formulaire web réactif permettant le téléchargement des justificatifs et la saisie des montants.
- [Design] 3 j - **Maquettes UI/UX** : Conception des écrans de soumission et du tableau de bord de validation des managers.
- [Sécurité] 4 j - **Système d'authentification** : Mise en place de l'authentification sécurisée avec rôles distincts pour les employés et les validateurs.
- [DevOps] 3 j - **Pipeline de déploiement** : Configuration de l'infrastructure de déploiement continu et des environnements de staging et production.
- [Tests] 3 j - **Tests d'intégration API** : Rédaction et exécution des tests automatisés couvrant le cycle de vie complet d'une note de frais.
- [Documentation] 2 j - **Guide d'utilisation** : Rédaction de la documentation technique et du manuel utilisateur pour la prise en main de l'application.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 6. application de recherche d'appartement (detaillee) - total 42 jours

**Demande :** Je veux une application mobile pour les étudiants qui permet de filtrer les appartements en temps réel selon leur budget et leur proximité avec les universités. Nous voulons intégrer un système de messagerie instantanée entre les locataires et les propriétaires pour faciliter la prise de rendez-vous. L'interface doit être intuitive et proposer une carte interactive affichant les logements disponibles autour d'une zone géographique précise.

- [Design] 5 j - **Design de l'interface utilisateur** : Création des maquettes haute fidélité pour la recherche sur carte et le profil utilisateur.
- [Base de données] 3 j - **Modélisation du schéma de données** : Conception des tables PostgreSQL pour les utilisateurs, les annonces et les messages.
- [Backend] 6 j - **API de recherche et filtrage** : Développement des endpoints REST pour filtrer les annonces par prix, localisation et critères.
- [Frontend] 7 j - **Intégration de la carte interactive** : Implémentation de Mapbox ou Google Maps pour visualiser les appartements sur le frontend.
- [Backend] 8 j - **Service de messagerie instantanée** : Mise en place de WebSockets pour permettre l'échange de messages en temps réel.
- [Sécurité] 4 j - **Implémentation de l'authentification** : Configuration du système JWT sécurisé pour l'inscription et la connexion des utilisateurs.
- [DevOps] 4 j - **Pipeline de déploiement continu** : Configuration du workflow CI/CD pour automatiser le déploiement sur les serveurs cloud.
- [Tests] 5 j - **Tests unitaires et d'intégration** : Rédaction des tests pour valider les flux critiques de recherche et de messagerie.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 7. CRM pour une petite entreprise (contraintes) - total 32 jours

**Demande :** Nous voulons un CRM sur mesure pour gérer notre base de clients et nos opportunités de vente, conçu par une équipe de 2 développeurs maximum. Le projet doit être livré en 6 semaines avec un budget très limité, en utilisant exclusivement le framework Next.js pour le frontend et le backend.

- [Base de données] 3 j - **Schéma de base de données PostgreSQL** : Conception et implémentation des tables clients, prospects, interactions et opportunités commerciales.
- [Sécurité] 4 j - **Système d'authentification et rôles** : Mise en place de l'authentification des utilisateurs avec gestion des accès par niveau de privilège.
- [Backend] 5 j - **API de gestion des clients** : Développement des endpoints CRUD pour la gestion centralisée du répertoire des clients.
- [Frontend] 6 j - **Interface de tableau de bord** : Création de la vue principale affichant les statistiques clés et le pipeline de ventes.
- [Frontend] 4 j - **Formulaires dynamiques de saisie** : Développement des interfaces pour la création et la modification des opportunités de vente avec validation.
- [DevOps] 3 j - **Pipeline de déploiement continu** : Configuration du déploiement automatisé vers une plateforme cloud avec gestion des environnements.
- [Tests] 5 j - **Tests unitaires et intégration** : Rédaction des tests critiques pour le flux de création de leads et l'authentification.
- [Documentation] 2 j - **Guide utilisateur technique** : Rédaction de la documentation pour la configuration de l'instance et l'ajout de nouveaux utilisateurs.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 8. application de covoiturage (courte) - total 40 jours

**Demande :** Je veux une application mobile intuitive permettant aux conducteurs et aux passagers de planifier facilement des trajets quotidiens partagés entre collègues.

- [Design] 5 j - **Maquettes d'interface utilisateur** : Création des wireframes et des parcours utilisateurs pour la réservation et le suivi de trajet.
- [Base de données] 3 j - **Schéma de la base de données** : Modélisation des tables pour les utilisateurs, les véhicules, les trajets et les réservations.
- [Backend] 8 j - **API de gestion des trajets** : Développement des endpoints pour la création, la recherche et l'annulation de trajets en covoiturage.
- [Frontend] 10 j - **Interface mobile de recherche** : Développement des écrans permettant de filtrer les trajets disponibles selon le lieu et l'horaire.
- [Sécurité] 4 j - **Configuration de l'authentification** : Mise en place de l'inscription et du login sécurisé avec gestion des rôles passager/conducteur.
- [DevOps] 3 j - **Déploiement du pipeline CI/CD** : Mise en place de l'automatisation pour les déploiements sur les serveurs de staging et de production.
- [Tests] 5 j - **Tests d'intégration** : Rédaction et exécution des tests pour valider le flux complet de réservation entre client et serveur.
- [Documentation] 2 j - **Documentation de l'API** : Rédaction de la documentation technique via Swagger pour l'intégration des services tiers.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 9. système de réservation pour un restaurant (detaillee) - total 30 jours

**Demande :** Nous voulons développer un système de réservation en ligne pour notre restaurant gastronomique afin de permettre à nos clients de réserver une table en temps réel. Je veux un calendrier interactif qui affiche les créneaux disponibles par service, ainsi qu'un espace client pour gérer ou annuler ses réservations. Nous visons principalement une clientèle moderne et connectée qui souhaite éviter les appels téléphoniques lors de nos heures de forte affluence.

- [Base de données] 3 j - **Schéma de base de données des tables et réservations** : Conception des tables SQL pour gérer les services, la capacité d'accueil et les créneaux horaires.
- [Backend] 5 j - **API de gestion des disponibilités** : Développement des points de terminaison pour vérifier les tables libres selon la date et le nombre de couverts.
- [Frontend] 4 j - **Interface du calendrier de réservation** : Intégration du composant visuel de sélection de date et d'heure pour l'utilisateur final.
- [Backend] 5 j - **Système d'authentification et espace client** : Mise en place de l'inscription/connexion et du tableau de bord pour visualiser l'historique des réservations.
- [Frontend] 5 j - **Interface d'administration pour la gestion des réservations** : Création d'un panneau de contrôle pour le personnel permettant de valider ou modifier les réservations manuelles.
- [Sécurité] 3 j - **Mise en place du protocole HTTPS et validation des entrées** : Sécurisation des flux de données et protection contre les injections SQL sur les formulaires de réservation.
- [Tests] 3 j - **Tests unitaires des flux de réservation** : Validation des cas limites : surbooking, annulations et conflits d'horaires.
- [DevOps] 2 j - **Déploiement sur serveur cloud** : Configuration de l'environnement de production, du serveur web et du certificat SSL.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 10. gestion de cabinet d'avocats (detaillee) - total 40 jours

**Demande :** Je souhaite faire développer une plateforme SaaS centralisée pour mon cabinet d'avocats afin de gérer efficacement les dossiers de mes clients. Nous voulons une interface intuitive permettant de suivre le cycle de vie des affaires juridiques, d'automatiser la génération de documents légaux à partir de modèles et d'intégrer un système sécurisé d'échange de fichiers confidentiels. Le système doit également inclure un module de facturation horaire basé sur le suivi du temps passé par dossier.

- [Base de données] 3 j - **Modélisation du schéma relationnel** : Conception des tables pour les dossiers, clients, factures et logs d'activité avec contraintes d'intégrité.
- [Backend] 5 j - **API REST de gestion des dossiers** : Développement des endpoints pour la création, la lecture et la mise à jour des affaires juridiques.
- [Frontend] 7 j - **Interface de saisie et consultation des dossiers** : Développement du tableau de bord utilisateur en React pour la gestion des dossiers et la saisie des temps.
- [Backend] 4 j - **Service de génération de documents** : Implémentation d'un moteur de fusion de modèles (templates) pour générer des PDFs de documents légaux.
- [Sécurité] 5 j - **Système de chiffrement de fichiers** : Mise en place du chiffrement au repos et en transit pour les documents déposés par les clients.
- [Backend] 4 j - **Module de facturation automatique** : Logique métier pour convertir les logs de temps en factures PDF selon le taux horaire de l'avocat.
- [Design] 3 j - **Design du système de droits d'accès** : Création des maquettes pour la gestion des rôles (associés, collaborateurs, clients) et accès aux dossiers.
- [DevOps] 3 j - **Pipeline CI/CD et déploiement** : Configuration des pipelines de déploiement automatique sur environnement cloud sécurisé.
- [Tests] 4 j - **Tests d'intégration des flux métier** : Validation fonctionnelle des scénarios critiques : création de dossier -> saisie temps -> génération facture.
- [Documentation] 2 j - **Documentation technique API** : Rédaction de la documentation Swagger/OpenAPI pour les endpoints développés.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 11. gestion du transport scolaire (courte) - total 47 jours

**Demande :** Nous voulons une application intuitive pour gérer les trajets quotidiens des bus scolaires et suivre la localisation des élèves en temps réel.

- [Design] 5 j - **Conception de l'interface utilisateur** : Création des maquettes pour le tableau de bord des parents et le suivi des conducteurs.
- [Base de données] 3 j - **Schéma de la base de données** : Modélisation des relations entre les bus, les itinéraires, les arrêts et les profils des élèves.
- [Backend] 8 j - **API de gestion des trajets** : Développement des services REST pour créer et modifier les itinéraires des bus scolaires.
- [Frontend] 10 j - **Interface mobile de suivi** : Développement de la vue cartographique pour visualiser la position du bus en temps réel.
- [Backend] 7 j - **Service de géolocalisation** : Mise en place de l'intégration avec les données GPS transmises par les véhicules.
- [Sécurité] 5 j - **Système d'authentification sécurisé** : Gestion des rôles et accès sécurisés pour les parents, chauffeurs et administrateurs du système.
- [DevOps] 4 j - **Déploiement et infrastructure** : Configuration du serveur cloud et des pipelines CI/CD pour la mise en production.
- [Tests] 5 j - **Tests d'intégration** : Validation du flux complet entre le signal GPS du bus et l'affichage sur le téléphone parent.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 12. gestion de parking intelligent (contraintes) - total 25 jours

**Demande :** Nous voulons développer un MVP de gestion de parking intelligent capable de détecter en temps réel les places libres via des capteurs IoT, le tout avec une équipe réduite de 2 développeurs et un délai très serré de 6 semaines. Le système doit impérativement utiliser une architecture basée sur les WebSockets pour permettre une mise à jour instantanée de l'affichage des places disponibles.

- [Backend] 4 j - **API de réception des données capteurs** : Développement des endpoints REST/MQTT pour recevoir les flux de données en provenance des capteurs IoT du parking.
- [Backend] 3 j - **Service de diffusion WebSocket** : Mise en place d'un serveur WebSocket pour pousser les changements d'état des places aux clients connectés en temps réel.
- [Base de données] 3 j - **Schéma de données et indexation** : Conception et implémentation de la base de données relationnelle pour stocker l'état des places et l'historique des accès.
- [Frontend] 5 j - **Dashboard de supervision temps réel** : Création de l'interface utilisateur affichant la carte dynamique du parking avec mise à jour immédiate via WebSocket.
- [Design] 2 j - **Maquette UX/UI du dashboard** : Conception des wireframes et de la charte graphique pour une visualisation claire de l'occupation du parking.
- [DevOps] 3 j - **Conteneurisation et déploiement** : Configuration des Dockerfiles et du pipeline CI/CD pour un déploiement automatisé sur un serveur cloud.
- [Tests] 3 j - **Tests de charge des WebSockets** : Simulation de flux massifs de données pour garantir que le système supporte la mise à jour simultanée de 100+ places.
- [Sécurité] 2 j - **Sécurisation des flux IoT** : Mise en place de l'authentification par jetons JWT pour sécuriser la communication entre les capteurs et l'API.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 13. chatbot de support client (courte) - total 32 jours

**Demande :** Nous voulons mettre en place un chatbot intelligent capable de répondre automatiquement aux questions fréquentes de nos clients sur notre site web.

- [Backend] 8 j - **Architecture du moteur de dialogue** : Configuration de l'infrastructure logicielle pour le traitement du langage naturel et la gestion des flux de conversation.
- [Base de données] 4 j - **Base de connaissances FAQ** : Création et structuration des données sources contenant les questions et réponses types pour le chatbot.
- [Frontend] 6 j - **Interface de chat utilisateur** : Développement du widget flottant intégré au site web pour permettre aux clients d'interagir avec le bot.
- [Design] 3 j - **Interface de design conversationnel** : Création de la charte graphique et des éléments visuels du chatbot pour assurer une cohérence avec notre marque.
- [DevOps] 5 j - **Déploiement en environnement cloud** : Mise en place des pipelines CI/CD et déploiement sur les serveurs de production avec haute disponibilité.
- [Tests] 4 j - **Validation des scénarios critiques** : Exécution de campagnes de tests unitaires et fonctionnels pour vérifier la pertinence des réponses automatiques.
- [Documentation] 2 j - **Guide d'administration du système** : Rédaction d'un manuel utilisateur pour permettre aux équipes support de mettre à jour les réponses du bot.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 14. plateforme de crowdfunding (contraintes) - total 25 jours

**Demande :** Nous voulons lancer une plateforme de crowdfunding minimaliste permettant de créer des campagnes et d'accepter des dons en ligne. Le projet doit être réalisé par une équipe de 2 développeurs maximum avec un budget très limité, nous imposant l'utilisation du framework Next.js et de Stripe pour les paiements.

- [Base de données] 2 j - **Schéma de la base de données** : Conception des tables pour les utilisateurs, les campagnes de financement et les transactions.
- [Backend] 4 j - **API de gestion des campagnes** : Développement des endpoints pour créer, lire et lister les projets de crowdfunding.
- [Frontend] 4 j - **Interface de création de campagne** : Développement du formulaire React pour soumettre une nouvelle campagne avec validation.
- [Backend] 5 j - **Intégration du paiement Stripe** : Mise en place du tunnel de paiement sécurisé pour valider les dons des contributeurs.
- [Design] 5 j - **Interface utilisateur publique** : Conception et intégration des pages de présentation des projets et du suivi de progression.
- [DevOps] 2 j - **Déploiement en production** : Configuration du pipeline CI/CD et déploiement sur une plateforme cloud type Vercel.
- [Tests] 3 j - **Tests fonctionnels** : Réalisation de tests unitaires sur les transactions financières et les flux de dons.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 15. gestion de chantier BTP (courte) - total 36 jours

**Demande :** Nous voulons une plateforme numérique intuitive pour suivre en temps réel l'avancement, les ressources et les dépenses de nos divers chantiers BTP.

- [Base de données] 3 j - **Modélisation du schéma relationnel** : Conception des tables pour les chantiers, les équipes, les matériaux et les transactions financières.
- [Frontend] 8 j - **Interface utilisateur du tableau de bord** : Développement de l'interface principale affichant les indicateurs clés de performance et l'état des chantiers.
- [Backend] 6 j - **API de gestion des chantiers** : Création des points de terminaison REST pour la création, mise à jour et consultation des données de chantier.
- [Sécurité] 4 j - **Système d'authentification sécurisé** : Mise en place de la gestion des rôles et accès via JWT pour protéger les données sensibles des projets.
- [Design] 5 j - **Maquette graphique haute fidélité** : Design des interfaces pour la saisie des rapports de chantier et la visualisation des plannings.
- [DevOps] 3 j - **Pipeline CI/CD** : Configuration du déploiement automatisé sur les environnements de test et de production.
- [Tests] 5 j - **Tests unitaires et d'intégration** : Écriture des tests automatisés pour valider la logique métier des transactions et des rapports.
- [Documentation] 2 j - **Documentation technique de l'API** : Rédaction de la documentation interactive via Swagger pour les développeurs tiers.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 16. outil interne de gestion des congés (contraintes) - total 24 jours

**Demande :** Nous voulons développer un outil interne de gestion des congés pour simplifier les demandes de nos 50 employés. Le projet doit être réalisé par une équipe réduite de 2 développeurs en seulement 4 semaines, en utilisant exclusivement le framework Django.

- [Base de données] 3 j - **Schéma de la base de données** : Conception des tables pour les utilisateurs, les rôles, les types de congés et les historiques de requêtes.
- [Backend] 5 j - **API de gestion des demandes** : Développement des endpoints Django pour créer, annuler et valider des demandes de congés.
- [Frontend] 4 j - **Interface de soumission des congés** : Création du formulaire web permettant aux employés de sélectionner des dates et un type de congé.
- [Frontend] 4 j - **Dashboard de validation RH** : Vue administrateur pour visualiser, approuver ou refuser les demandes en attente.
- [Sécurité] 3 j - **Système d'authentification RBAC** : Implémentation de la gestion des accès pour distinguer les employés simples des managers.
- [Tests] 3 j - **Tests unitaires des calculs de solde** : Validation logique du décompte des jours restants par employé.
- [DevOps] 2 j - **Déploiement sur serveur interne** : Configuration du serveur web et mise en place du workflow de déploiement.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 17. application de méditation (contraintes) - total 34 jours

**Demande :** Je souhaite lancer une application mobile de méditation guidée MVP avec un catalogue audio simple et un minuteur, le tout développé en 6 semaines par une équipe de 2 développeurs. Le budget est limité, donc nous devons impérativement utiliser une technologie hybride comme Flutter pour couvrir iOS et Android simultanément.

- [Design] 4 j - **Design de l'interface utilisateur** : Création des maquettes haute fidélité pour le lecteur audio et la bibliothèque de méditations sur Figma.
- [Base de données] 3 j - **Schéma de la base de données** : Modélisation des tables pour les utilisateurs, les catégories de méditation et les pistes audio dans Firebase.
- [Backend] 5 j - **API de gestion des contenus audio** : Développement des endpoints pour récupérer les listes de méditations et leurs métadonnées depuis le stockage Cloud.
- [Frontend] 7 j - **Lecteur audio cross-platform** : Implémentation du lecteur de flux audio avec contrôle de lecture (play, pause, seek) via Flutter.
- [Frontend] 4 j - **Système de minuteur paramétrable** : Développement de la fonctionnalité de minuteur personnalisable avec sons d'ambiance et alarmes de fin.
- [Sécurité] 3 j - **Authentification Firebase** : Mise en place de l'inscription et connexion utilisateur pour la sauvegarde des favoris.
- [DevOps] 3 j - **Pipeline de déploiement continu** : Configuration de GitHub Actions pour automatiser les builds Android (APK) et iOS.
- [Tests] 5 j - **Tests unitaires et fonctionnels** : Rédaction des tests pour les services audio et le processus d'authentification utilisateur.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 18. CRM pour une petite entreprise (courte) - total 29 jours

**Demande :** Nous voulons un outil simple pour centraliser les contacts de nos clients, suivre nos interactions et gérer nos opportunités de vente quotidiennes.

- [Base de données] 3 j - **Modélisation du schéma relationnel** : Définition des tables pour les contacts, les comptes et le suivi des opportunités commerciales.
- [Backend] 5 j - **API de gestion des contacts** : Développement des endpoints REST pour créer, lire, mettre à jour et supprimer les fiches clients.
- [Frontend] 6 j - **Interface de liste et détails** : Développement des vues front-end permettant de visualiser et d'éditer les informations des clients.
- [Frontend] 4 j - **Tableau de bord des ventes** : Création d'une interface graphique pour suivre l'état d'avancement des opportunités de vente.
- [Sécurité] 3 j - **Authentification sécurisée** : Mise en place du contrôle d'accès utilisateur et du chiffrement des mots de passe.
- [DevOps] 3 j - **Configuration du déploiement** : Mise en place du pipeline CI/CD et déploiement sur une instance cloud sécurisée.
- [Tests] 3 j - **Tests fonctionnels** : Rédaction et exécution de tests unitaires et fonctionnels sur le cycle de vie d'un prospect.
- [Documentation] 2 j - **Guide d'utilisation** : Rédaction de la documentation pour aider les utilisateurs à manipuler les données clients.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 19. plateforme de formation en entreprise (contraintes) - total 30 jours

**Demande :** Je veux une plateforme de formation interne permettant aux employés de suivre des modules vidéo avec un quiz final, le tout devant être opérationnel en seulement 6 semaines avec une équipe restreinte de 2 développeurs. Nous imposons l'utilisation de React et Node.js pour respecter notre budget serré.

- [Base de données] 3 j - **Schéma de la base de données** : Modélisation des tables pour les utilisateurs, les cours et les résultats des quiz.
- [Backend] 5 j - **API d'authentification et gestion des accès** : Développement des endpoints pour l'inscription et la connexion des employés (JWT).
- [Frontend] 4 j - **Interface de catalogue de cours** : Développement de la vue listant les modules de formation avec filtrage par catégorie.
- [Backend] 5 j - **API de lecture vidéo et progression** : Développement des endpoints pour servir les vidéos et enregistrer le temps de visionnage.
- [Frontend] 6 j - **Moteur de quiz interactif** : Création du composant React pour afficher les questions et calculer le score final.
- [DevOps] 3 j - **Pipeline de déploiement CI/CD** : Configuration de l'automatisation du déploiement sur un serveur cloud dédié.
- [Tests] 4 j - **Tests unitaires critiques** : Couverture des tests sur la logique de calcul des scores et l'authentification.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

## 20. gestion d'une exploitation agricole (courte) - total 30 jours

**Demande :** Nous voulons une application centralisée permettant de suivre en temps réel nos stocks de récoltes, la planification des semis et l'entretien machine.

- [Base de données] 4 j - **Modélisation du schéma de données** : Conception des tables pour les cultures, les machines, les stocks et le calendrier des tâches agricoles.
- [Backend] 6 j - **API de gestion des stocks** : Développement des endpoints pour la saisie, la mise à jour et le suivi des niveaux de récoltes.
- [Frontend] 5 j - **Interface de saisie des semis** : Développement d'un formulaire intuitif pour planifier les cycles de plantation par parcelle.
- [Backend] 4 j - **Module de maintenance machine** : Création d'un système d'alertes pour le suivi préventif de l'état technique des véhicules agricoles.
- [Design] 3 j - **Design des tableaux de bord** : Conception des maquettes pour une vue d'ensemble rapide de l'exploitation sur tablette et PC.
- [Tests] 3 j - **Tests d'intégration** : Validation des flux de données entre la saisie des cultures et la mise à jour automatique des stocks.
- [DevOps] 2 j - **Configuration du déploiement** : Mise en place de l'environnement de production sur serveur cloud avec gestion des sauvegardes automatiques.
- [Sécurité] 3 j - **Gestion des accès utilisateurs** : Implémentation d'une authentification sécurisée par rôles pour les ouvriers et l'exploitant.

Verdict : [ ] credible   [ ] discutable   [ ] absurde

---

