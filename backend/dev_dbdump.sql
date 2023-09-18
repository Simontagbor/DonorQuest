-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: dev_db
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add donation',1,'add_donation'),(2,'Can change donation',1,'change_donation'),(3,'Can delete donation',1,'delete_donation'),(4,'Can view donation',1,'view_donation'),(5,'Can add donation target',2,'add_donationtarget'),(6,'Can change donation target',2,'change_donationtarget'),(7,'Can delete donation target',2,'delete_donationtarget'),(8,'Can view donation target',2,'view_donationtarget'),(9,'Can add user profile',3,'add_userprofile'),(10,'Can change user profile',3,'change_userprofile'),(11,'Can delete user profile',3,'delete_userprofile'),(12,'Can view user profile',3,'view_userprofile'),(13,'Can add donation request',4,'add_donationrequest'),(14,'Can change donation request',4,'change_donationrequest'),(15,'Can delete donation request',4,'delete_donationrequest'),(16,'Can view donation request',4,'view_donationrequest'),(17,'Can add log entry',5,'add_logentry'),(18,'Can change log entry',5,'change_logentry'),(19,'Can delete log entry',5,'delete_logentry'),(20,'Can view log entry',5,'view_logentry'),(21,'Can add permission',6,'add_permission'),(22,'Can change permission',6,'change_permission'),(23,'Can delete permission',6,'delete_permission'),(24,'Can view permission',6,'view_permission'),(25,'Can add group',7,'add_group'),(26,'Can change group',7,'change_group'),(27,'Can delete group',7,'delete_group'),(28,'Can view group',7,'view_group'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add content type',9,'add_contenttype'),(34,'Can change content type',9,'change_contenttype'),(35,'Can delete content type',9,'delete_contenttype'),(36,'Can view content type',9,'view_contenttype'),(37,'Can add session',10,'add_session'),(38,'Can change session',10,'change_session'),(39,'Can delete session',10,'delete_session'),(40,'Can view session',10,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$yLd97bQhGXCb7ZhKFQzRF0$FZ9/RkvMHmIIVuRIvog2WQPVKaaJ18tBy0qVzvnY1So=','2023-09-04 12:08:19.936683',1,'simontagbor','','','simontagbor360@gmail.com',1,1,'2023-08-29 19:10:19.730408'),(2,'pbkdf2_sha256$600000$2lhaUDPG0GTaWRj1su0508$C0qWd96/5Av0aTUOECSFlAzLDNlyn8IkGEHSUvNub7Q=',NULL,0,'Simono','','','',0,1,'2023-08-29 19:12:40.262693'),(3,'pbkdf2_sha256$600000$SP8migNzM1x8nEDz2Yj28W$lA591UG9jGmdDGHIznXf42+HQAYp/WiEqnCPmCTYPMo=',NULL,0,'testuser1','','','',0,1,'2023-08-30 08:28:50.629784');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-08-29 19:12:40.935714','2','Simono',1,'[{\"added\": {}}]',8,1),(2,'2023-08-29 19:15:00.805847','0393d7bb-fc4c-4e90-be8b-471e1fc94212','Donation Request for travis',1,'[{\"added\": {}}]',4,1),(3,'2023-08-29 19:17:12.201122','47cb4032-626f-4556-9989-fe275a2b0fc7','Simon12',1,'[{\"added\": {}}]',3,1),(4,'2023-08-30 08:08:44.205306','caf51ceb-f46e-4440-b6eb-d87aef929ec0','Donation Request for Elvis',1,'[{\"added\": {}}]',4,1),(5,'2023-08-30 08:19:57.738178','afa0cd33-afe6-4de0-b790-ee43737b3c02','Donation by Tagbor scheduled on 2023-08-18 18:00:00+00:00',1,'[{\"added\": {}}]',1,1),(6,'2023-08-30 08:23:08.533178','9abe94e8-2bd1-43d1-8901-4504d29b6917','Donation by kwesi scheduled on 2023-08-31 12:00:00+00:00',1,'[{\"added\": {}}]',1,1),(7,'2023-08-30 08:23:33.125394','9abe94e8-2bd1-43d1-8901-4504d29b6917','Donation by kwesi scheduled on 2023-08-31 12:00:00+00:00',2,'[{\"changed\": {\"fields\": [\"Number of pints\"]}}]',1,1),(8,'2023-08-30 08:24:44.419884','afa0cd33-afe6-4de0-b790-ee43737b3c02','Donation by Tagbor scheduled on 2023-08-18 18:00:00+00:00',2,'[{\"changed\": {\"fields\": [\"Donation request\"]}}]',1,1),(9,'2023-08-30 08:26:24.759975','1','Target for Simon12',1,'[{\"added\": {}}]',2,1),(10,'2023-08-30 08:28:52.555621','3','testuser1',1,'[{\"added\": {}}]',8,1),(11,'2023-08-30 08:30:23.141170','1ee1e7a8-81e7-4a2b-a54a-a55726d2f39c','bestdonor',1,'[{\"added\": {}}]',3,1),(12,'2023-08-30 08:56:48.761106','1ee1e7a8-81e7-4a2b-a54a-a55726d2f39c','bestdonor',2,'[]',3,1),(13,'2023-08-30 08:56:52.440493','1ee1e7a8-81e7-4a2b-a54a-a55726d2f39c','bestdonor',2,'[]',3,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (5,'admin','logentry'),(7,'auth','group'),(6,'auth','permission'),(8,'auth','user'),(9,'contenttypes','contenttype'),(1,'donation','donation'),(4,'donation','donationrequest'),(2,'donation','donationtarget'),(3,'donation','userprofile'),(10,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-08-29 19:06:59.253712'),(2,'auth','0001_initial','2023-08-29 19:07:05.815929'),(3,'admin','0001_initial','2023-08-29 19:07:06.493895'),(4,'admin','0002_logentry_remove_auto_add','2023-08-29 19:07:06.528087'),(5,'admin','0003_logentry_add_action_flag_choices','2023-08-29 19:07:06.609163'),(6,'contenttypes','0002_remove_content_type_name','2023-08-29 19:07:07.079081'),(7,'auth','0002_alter_permission_name_max_length','2023-08-29 19:07:07.399447'),(8,'auth','0003_alter_user_email_max_length','2023-08-29 19:07:07.548366'),(9,'auth','0004_alter_user_username_opts','2023-08-29 19:07:07.618327'),(10,'auth','0005_alter_user_last_login_null','2023-08-29 19:07:07.942734'),(11,'auth','0006_require_contenttypes_0002','2023-08-29 19:07:07.964160'),(12,'auth','0007_alter_validators_add_error_messages','2023-08-29 19:07:08.018912'),(13,'auth','0008_alter_user_username_max_length','2023-08-29 19:07:08.395982'),(14,'auth','0009_alter_user_last_name_max_length','2023-08-29 19:07:08.711036'),(15,'auth','0010_alter_group_name_max_length','2023-08-29 19:07:08.842514'),(16,'auth','0011_update_proxy_permissions','2023-08-29 19:07:08.897464'),(17,'auth','0012_alter_user_first_name_max_length','2023-08-29 19:07:09.286005'),(18,'donation','0001_initial','2023-08-29 19:07:13.600630'),(19,'sessions','0001_initial','2023-08-29 19:07:13.812120'),(20,'donation','0002_remove_donationrequest_pending_donations_and_more','2023-08-30 08:55:08.851740');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('d5vspgwpbjzhpylbfy0ra3mz79jg5mre','.eJxVjEsOwiAUAO_C2hA-5VOX7nsG8h48pGogKe3KeHdD0oVuZybzZgGOvYSj0xbWxK5MsssvQ4hPqkOkB9R747HVfVuRj4SftvOlJXrdzvZvUKCXsTUC0U0WPcAUHXphtMjKKE3zDF4p7yxYrZzMXpOQ6DQlnYnIGgdo2OcLxnY3cQ:1qd8NQ:Ls9Osz80V67X1qqk2pTywKTg2px5-SfiOs3U5QW6e3Y','2023-09-18 12:08:20.041736');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donation_donation`
--

DROP TABLE IF EXISTS `donation_donation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donation_donation` (
  `id` char(32) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `blood_group` varchar(3) NOT NULL,
  `donation_option` varchar(20) NOT NULL,
  `donation_type` varchar(20) NOT NULL,
  `number_of_pints` int unsigned NOT NULL,
  `date` datetime(6) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `age` int unsigned NOT NULL,
  `donor_name` varchar(100) DEFAULT NULL,
  `donor_phone` varchar(20) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `scheduled_date` datetime(6) DEFAULT NULL,
  `verification_date` datetime(6) DEFAULT NULL,
  `verification_photo` varchar(100) DEFAULT NULL,
  `potential_lives_saved` int unsigned NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  `is_canceled` tinyint(1) NOT NULL,
  `is_rejected` tinyint(1) NOT NULL,
  `donation_request_id` char(32) DEFAULT NULL,
  `donor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `donation_donation_donation_request_id_a03d7695_fk_donation_` (`donation_request_id`),
  KEY `donation_donation_donor_id_7900ff09_fk_auth_user_id` (`donor_id`),
  CONSTRAINT `donation_donation_donation_request_id_a03d7695_fk_donation_` FOREIGN KEY (`donation_request_id`) REFERENCES `donation_donationrequest` (`id`),
  CONSTRAINT `donation_donation_donor_id_7900ff09_fk_auth_user_id` FOREIGN KEY (`donor_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `donation_donation_chk_1` CHECK ((`number_of_pints` >= 0)),
  CONSTRAINT `donation_donation_chk_2` CHECK ((`age` >= 0)),
  CONSTRAINT `donation_donation_chk_3` CHECK ((`potential_lives_saved` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donation_donation`
--

LOCK TABLES `donation_donation` WRITE;
/*!40000 ALTER TABLE `donation_donation` DISABLE KEYS */;
INSERT INTO `donation_donation` VALUES ('9abe94e82bd143d189014504d29b6917','2023-08-30 08:20:31.000000','2023-08-30 08:20:31.000000','O-','replacement','regular',2,'2023-08-30 08:23:08.397341','kwesi@gmail.com',18,'kwesi','0545990467','Pending','2023-08-31 12:00:00.000000',NULL,'donor_photos/Screenshot_2023-08-18_173941-removebg-preview_1.png',0,0,0,0,'caf51cebf46e4440b6ebd87aef929ec0',NULL),('afa0cd33afe64de0b790ee43737b3c02','2023-08-30 08:08:56.000000','2023-08-30 08:08:56.000000','A+','replacement','regular',2,'2023-08-30 08:19:57.646066',NULL,18,'Tagbor',NULL,'Pending','2023-08-18 18:00:00.000000',NULL,'',0,0,0,0,'0393d7bbfc4c4e90be8b471e1fc94212',NULL);
/*!40000 ALTER TABLE `donation_donation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donation_donationrequest`
--

DROP TABLE IF EXISTS `donation_donationrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donation_donationrequest` (
  `id` char(32) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `blood_group` varchar(3) NOT NULL,
  `status` varchar(20) NOT NULL,
  `donation_option` varchar(20) NOT NULL,
  `donation_type` varchar(20) NOT NULL,
  `number_of_pints` int unsigned NOT NULL,
  `date` datetime(6) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `age` int unsigned NOT NULL,
  `patient_name` varchar(100) DEFAULT NULL,
  `patient_story` longtext NOT NULL,
  `patient_avatar` varchar(100) NOT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `donors_needed` int unsigned NOT NULL,
  `pending_donations_id` char(32) DEFAULT NULL,
  `verified_donations_id` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `donation_donationreq_pending_donations_id_5a94d9ba_fk_donation_` (`pending_donations_id`),
  KEY `donation_donationreq_verified_donations_i_67b4dc3f_fk_donation_` (`verified_donations_id`),
  CONSTRAINT `donation_donationreq_pending_donations_id_5a94d9ba_fk_donation_` FOREIGN KEY (`pending_donations_id`) REFERENCES `donation_donation` (`id`),
  CONSTRAINT `donation_donationreq_verified_donations_i_67b4dc3f_fk_donation_` FOREIGN KEY (`verified_donations_id`) REFERENCES `donation_donation` (`id`),
  CONSTRAINT `donation_donationrequest_chk_1` CHECK ((`number_of_pints` >= 0)),
  CONSTRAINT `donation_donationrequest_chk_2` CHECK ((`age` >= 0)),
  CONSTRAINT `donation_donationrequest_chk_3` CHECK ((`donors_needed` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donation_donationrequest`
--

LOCK TABLES `donation_donationrequest` WRITE;
/*!40000 ALTER TABLE `donation_donationrequest` DISABLE KEYS */;
INSERT INTO `donation_donationrequest` VALUES ('0393d7bbfc4c4e90be8b471e1fc94212','2023-08-29 19:14:07.000000','2023-08-29 19:14:07.000000','A+','Pending','replacement','regular',1,'2023-08-29 19:15:00.665322','simontagbor360@gmail.com',18,'travis','jefwoifjojf;wlerfpwojefpewopefpojel','patient_avatars/Untitled_design_y5QCJkX.png','ridge',1,NULL,NULL),('0925fffc4c78493ca7de245067604906','2023-09-03 00:49:34.272088','2023-09-03 00:49:34.272103','A+','Pending','Voluntary','Regular',1,'2023-09-03 00:49:34.298150',NULL,18,'Deadass','If there is excess space on the right side of the list-item elements, it might be caused by the default behavior of the grid layout when dealing with items that don\'t perfectly fill the available space. To fix this without squishing the content of the li elements, you can make sure that the content inside each','','Dean',1,NULL,NULL),('1532b1fa7d07446eb7137ea6e018a9ec','2023-09-02 21:08:21.420891','2023-09-02 21:08:21.420906','A+','Pending','Voluntary','Regular',1,'2023-09-02 21:08:21.903980',NULL,18,'Sobolo','With these modifications, the input fields should have a solid and well-rounded appearance, the patient story textarea should auto-adjust its height, and all input fields should span the width of the form container.','patient_avatars/Brilliant-Room-Dividers-Partitions-Ideas-You-Should-Try-02.webp','alajo',1,NULL,NULL),('1e0b7625fb794f7a83fc7526fe956190','2023-09-03 17:26:15.822322','2023-09-03 17:26:15.822339','B-','Pending','Voluntary','Regular',1,'2023-09-03 17:26:15.894599',NULL,18,'van Helsing','Your CSS file appears to be well-structured and organized. If you have any specific questions or if there\'s anything else you\'d like to customize or implement, please let me know, and I\'d be happy to assist further.','','Tesla',1,NULL,NULL),('2b5d791707c145ffae8fa3379ca5ac29','2023-09-03 18:02:28.983791','2023-09-03 18:02:28.983805','O-','Pending','Voluntary','Regular',2,'2023-09-03 18:02:29.017147',NULL,18,'Curious Zelda','Your CSS file appears to be well-structured and organized. If you have any specific questions or if there\'s anything else you\'d like to customize or implement, please let me know, and I\'d be happy to assist further.','','Ridge Hospital',1,NULL,NULL),('3f9dbe5976734e078404e0d72be9ea2f','2023-09-04 12:17:20.630675','2023-09-04 12:17:20.630695','O+','Pending','Voluntary','Regular',2,'2023-09-04 12:17:21.331320',NULL,18,'Mavis','some random text','patient_avatars/heroimage.jpg','Hospital',1,NULL,NULL),('45bfb10db3c8462badda3119998458d0','2023-09-03 18:03:49.840616','2023-09-03 18:03:49.840632','B+','Pending','Voluntary','Regular',1,'2023-09-03 18:03:49.876816',NULL,18,'Molly Bob','Your CSS file appears to be well-structured and organized. If you have any specific questions or if there\'s anything else you\'d like to customize or implement, please let me know, and I\'d be happy to assist further.','','Nada',1,NULL,NULL),('5cc36153b2a6401b8b109cae01f52503','2023-09-03 00:48:31.620976','2023-09-03 00:48:31.620991','A+','Pending','Voluntary','Regular',1,'2023-09-03 00:48:31.689775',NULL,18,'Zerk','If there is excess space on the right side of the list-item elements, it might be caused by the default behavior of the grid layout when dealing with items that don\'t perfectly fill the available space. To fix this without squishing the content of the li elements, you can make sure that the content inside each','','Deats',1,NULL,NULL),('6f2ac3c3105b49da9c81ccf5c74c7d6d','2023-09-03 00:48:55.646181','2023-09-03 00:48:55.646198','A+','Pending','Voluntary','Regular',1,'2023-09-03 00:48:55.674865',NULL,18,'Holly','If there is excess space on the right side of the list-item elements, it might be caused by the default behavior of the grid layout when dealing with items that don\'t perfectly fill the available space. To fix this without squishing the content of the li elements, you can make sure that the content inside each','','Bean',1,NULL,NULL),('6f982a9fb97c4f639b75c388dbb28268','2023-09-03 18:06:03.026729','2023-09-03 18:06:03.026747','AB-','Pending','Voluntary','Regular',2,'2023-09-03 18:06:03.053885',NULL,18,'George','Your CSS file appears to be well-structured and organized. If you have any specific questions or if there\'s anything else you\'d like to customize or implement, please let me know, and I\'d be happy to assist further.','','Kenya',1,NULL,NULL),('7349b59e3dcf423c8e37a8a5c3e4c785','2023-09-03 01:09:12.339991','2023-09-03 01:09:12.340007','O+','Pending','Voluntary','Regular',1,'2023-09-03 01:09:12.371351',NULL,18,'kein','gfdcytuihojkpmkniuvutycghvbjk','','hbubjvb',1,NULL,NULL),('88b5cf9e2d9c49d7a982182d5ca22c57','2023-09-03 00:50:05.607594','2023-09-03 00:50:05.607609','A+','Pending','Voluntary','Regular',2,'2023-09-03 00:50:05.640679',NULL,18,'Smino','If there is excess space on the right side of the list-item elements, it might be caused by the default behavior of the grid layout when dealing with items that don\'t perfectly fill the available space. To fix this without squishing the content of the li elements, you can make sure that the content inside each','','Heat',1,NULL,NULL),('9001d7c964b5411d9c0b680a80e04e3f','2023-09-03 17:59:12.201588','2023-09-03 17:59:12.201616','AB+','Pending','Voluntary','Regular',1,'2023-09-03 17:59:12.261763',NULL,18,'Furious Joe','Your CSS file appears to be well-structured and organized. If you have any specific questions or if there\'s anything else you\'d like to customize or implement, please let me know, and I\'d be happy to assist further.','','Health Something',1,NULL,NULL),('95250b0cef844872a08f8083e872a70d','2023-09-03 00:57:57.412204','2023-09-03 00:57:57.412218','O-','Pending','Voluntary','Regular',1,'2023-09-03 00:57:57.436191',NULL,18,'Meridith','If there is excess space on the right side of the list-item elements, it might be caused by the default behavior of the grid layout when dealing with items that don\'t perfectly fill the available space. To fix this without squishing the content of the li elements, you can make sure that the content inside each','','Alexa-Hospital',1,NULL,NULL),('caf51cebf46e4440b6ebd87aef929ec0','2023-08-30 08:06:57.000000','2023-08-30 08:06:57.000000','A+','Pending','replacement','regular',2,'2023-08-30 08:08:43.070509','simontagbor360@gmail.com',18,'Elvis','Elvis is a fun loving gentleman','patient_avatars/ground-to-ceiling-partition-design-for-living-room-and-dining.jpg','Accra Regional Hospital',1,NULL,NULL),('d985b4562c45480792e24d175b2d9191','2023-09-03 00:51:03.393180','2023-09-03 00:51:03.393212','AB-','Pending','Voluntary','Regular',1,'2023-09-03 00:51:03.419670',NULL,18,'Mwangi','If there is excess space on the right side of the list-item elements, it might be caused by the default behavior of the grid layout when dealing with items that don\'t perfectly fill the available space. To fix this without squishing the content of the li elements, you can make sure that the content inside each','','Kenya-tech',1,NULL,NULL),('db76647b2aba4cf2a70edb1766a4d9f2','2023-09-03 17:27:47.106688','2023-09-03 17:27:47.106708','A+','Pending','Voluntary','Regular',3,'2023-09-03 17:27:47.571294',NULL,18,'Agitated Osborn','Your CSS file appears to be well-structured and organized. If you have any specific questions or if there\'s anything else you\'d like to customize or implement, please let me know, and I\'d be happy to assist further.','patient_avatars/mubarak-showole-Ve7xjKImd28-unsplash.jpg','Sus',1,NULL,NULL),('fbaa57dca7a94826bed69bd943ed1972','2023-09-02 18:00:38.393999','2023-09-02 18:00:38.394014','A+','Pending','Voluntary','Regular',1,'2023-09-02 18:00:40.595637',NULL,18,'holton','hello this is my story','patient_avatars/Screenshot_2023-08-18_173941-removebg-preview.png','aloha',1,NULL,NULL);
/*!40000 ALTER TABLE `donation_donationrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donation_donationtarget`
--

DROP TABLE IF EXISTS `donation_donationtarget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donation_donationtarget` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `target_amount` decimal(10,2) NOT NULL,
  `target_description` longtext,
  `created_at` datetime(6) NOT NULL,
  `user_profile_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `donation_donationtar_user_profile_id_a6075479_fk_donation_` (`user_profile_id`),
  CONSTRAINT `donation_donationtar_user_profile_id_a6075479_fk_donation_` FOREIGN KEY (`user_profile_id`) REFERENCES `donation_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donation_donationtarget`
--

LOCK TABLES `donation_donationtarget` WRITE;
/*!40000 ALTER TABLE `donation_donationtarget` DISABLE KEYS */;
INSERT INTO `donation_donationtarget` VALUES (1,4.00,'','2023-08-30 08:26:24.743715','47cb4032626f45569989fe275a2b0fc7');
/*!40000 ALTER TABLE `donation_donationtarget` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donation_userprofile`
--

DROP TABLE IF EXISTS `donation_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donation_userprofile` (
  `id` char(32) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_name` varchar(50) NOT NULL,
  `blood_type` varchar(5) NOT NULL,
  `profile_avatar` varchar(100) NOT NULL,
  `number_of_donations` int unsigned NOT NULL,
  `potential_lives_saved` int unsigned NOT NULL,
  `user_id` int DEFAULT NULL,
  `donation_history_id` char(32) DEFAULT NULL,
  `donation_targets_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `donation_userprofile_donation_history_id_0103c53c_fk_donation_` (`donation_history_id`),
  KEY `donation_userprofile_donation_targets_id_aaa8e6fd_fk_donation_` (`donation_targets_id`),
  CONSTRAINT `donation_userprofile_donation_history_id_0103c53c_fk_donation_` FOREIGN KEY (`donation_history_id`) REFERENCES `donation_donation` (`id`),
  CONSTRAINT `donation_userprofile_donation_targets_id_aaa8e6fd_fk_donation_` FOREIGN KEY (`donation_targets_id`) REFERENCES `donation_donationtarget` (`id`),
  CONSTRAINT `donation_userprofile_user_id_20144520_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `donation_userprofile_chk_1` CHECK ((`number_of_donations` >= 0)),
  CONSTRAINT `donation_userprofile_chk_2` CHECK ((`potential_lives_saved` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donation_userprofile`
--

LOCK TABLES `donation_userprofile` WRITE;
/*!40000 ALTER TABLE `donation_userprofile` DISABLE KEYS */;
INSERT INTO `donation_userprofile` VALUES ('1ee1e7a881e74a2ba54aa55726d2f39c','2023-08-30 08:28:59.000000','2023-08-30 08:28:59.000000','bestdonor','A+','profile_avatars/repository-open-graph-template.png',0,0,3,NULL,NULL),('47cb4032626f45569989fe275a2b0fc7','2023-08-29 19:11:07.000000','2023-08-29 19:11:07.000000','Simon12','O+','',0,0,2,NULL,NULL);
/*!40000 ALTER TABLE `donation_userprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-06 13:07:25
