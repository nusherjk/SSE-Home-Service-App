-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: db_homeservice
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `accounts_address`
--

DROP TABLE IF EXISTS `accounts_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `line1` varchar(200) NOT NULL,
  `line2` varchar(200) DEFAULT NULL,
  `suburb` varchar(20) NOT NULL,
  `postcode` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_address`
--

LOCK TABLES `accounts_address` WRITE;
/*!40000 ALTER TABLE `accounts_address` DISABLE KEYS */;
INSERT INTO `accounts_address` VALUES (1,'15','boronia Street','klemzig','5087','SA'),(2,'15','boronia Street','klemzig','5087','SA');
/*!40000 ALTER TABLE `accounts_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customer`
--

DROP TABLE IF EXISTS `accounts_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `dob` date NOT NULL,
  `country` varchar(2) NOT NULL,
  `C19Vaccinated` tinyint(1) NOT NULL,
  `profession` varchar(200) NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  `address_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `accounts_customer_address_id_5ca9a572_fk_accounts_address_id` (`address_id`),
  CONSTRAINT `accounts_customer_address_id_5ca9a572_fk_accounts_address_id` FOREIGN KEY (`address_id`) REFERENCES `accounts_address` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer`
--

LOCK TABLES `accounts_customer` WRITE;
/*!40000 ALTER TABLE `accounts_customer` DISABLE KEYS */;
INSERT INTO `accounts_customer` VALUES (1,'!1XKXnN8Tpt8mnm6ReQh7FZN4DqELufwjxfvgrapg','2024-11-09 09:29:45.407252',0,'nusherjk',0,1,'2024-11-08 11:52:01.083851','Nusher','Jamil','nusherjk@gmail.com','2024-11-08','AU',1,'Student',1,1),(2,'pbkdf2_sha256$870000$dhArWafzJGoll6AzApVLJQ$71X6h+1aGJYUO3nupZia3mSVnKrlOD6sF777PY2ItBw=','2024-11-11 23:36:46.488771',1,'admin',1,1,'2024-11-08 11:55:29.589241','AdminData','AdminData','','2024-11-06','AU',1,'newProff',1,2),(3,'pbkdf2_sha256$870000$zOFfo1IRzghuH67qNsdE6R$bttr2dPxxh8OLZw0jkcBlX+mU39rKsBkIXz0+mvrU+w=','2024-11-11 23:36:07.957535',0,'Johnd',0,1,'2024-11-08 11:58:58.000000','John','Doe','johnD@gmail.com','2024-11-08','AU',0,'',0,NULL);
/*!40000 ALTER TABLE `accounts_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customer_groups`
--

DROP TABLE IF EXISTS `accounts_customer_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customer_groups_customer_id_group_id_5d65b72b_uniq` (`customer_id`,`group_id`),
  KEY `accounts_customer_groups_group_id_7c230d03_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customer_gr_customer_id_c2d5e358_fk_accounts_` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `accounts_customer_groups_group_id_7c230d03_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer_groups`
--

LOCK TABLES `accounts_customer_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customer_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customer_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customer_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customer_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customer_user_p_customer_id_permission_i_927fe894_uniq` (`customer_id`,`permission_id`),
  KEY `accounts_customer_us_permission_id_9c8a5ef6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customer_us_customer_id_701aa82b_fk_accounts_` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `accounts_customer_us_permission_id_9c8a5ef6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer_user_permissions`
--

LOCK TABLES `accounts_customer_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customer_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customer_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add association',6,'add_association'),(22,'Can change association',6,'change_association'),(23,'Can delete association',6,'delete_association'),(24,'Can view association',6,'view_association'),(25,'Can add code',7,'add_code'),(26,'Can change code',7,'change_code'),(27,'Can delete code',7,'delete_code'),(28,'Can view code',7,'view_code'),(29,'Can add nonce',8,'add_nonce'),(30,'Can change nonce',8,'change_nonce'),(31,'Can delete nonce',8,'delete_nonce'),(32,'Can view nonce',8,'view_nonce'),(33,'Can add user social auth',9,'add_usersocialauth'),(34,'Can change user social auth',9,'change_usersocialauth'),(35,'Can delete user social auth',9,'delete_usersocialauth'),(36,'Can view user social auth',9,'view_usersocialauth'),(37,'Can add partial',10,'add_partial'),(38,'Can change partial',10,'change_partial'),(39,'Can delete partial',10,'delete_partial'),(40,'Can view partial',10,'view_partial'),(41,'Can add service',11,'add_service'),(42,'Can change service',11,'change_service'),(43,'Can delete service',11,'delete_service'),(44,'Can view service',11,'view_service'),(45,'Can add service category',12,'add_servicecategory'),(46,'Can change service category',12,'change_servicecategory'),(47,'Can delete service category',12,'delete_servicecategory'),(48,'Can view service category',12,'view_servicecategory'),(49,'Can add booking',13,'add_booking'),(50,'Can change booking',13,'change_booking'),(51,'Can delete booking',13,'delete_booking'),(52,'Can view booking',13,'view_booking'),(53,'Can add payment',14,'add_payment'),(54,'Can change payment',14,'change_payment'),(55,'Can delete payment',14,'delete_payment'),(56,'Can view payment',14,'view_payment'),(57,'Can add provider profile',15,'add_providerprofile'),(58,'Can change provider profile',15,'change_providerprofile'),(59,'Can delete provider profile',15,'delete_providerprofile'),(60,'Can view provider profile',15,'view_providerprofile'),(61,'Can add review',16,'add_review'),(62,'Can change review',16,'change_review'),(63,'Can delete review',16,'delete_review'),(64,'Can view review',16,'view_review'),(65,'Can add Addresses',17,'add_address'),(66,'Can change Addresses',17,'change_address'),(67,'Can delete Addresses',17,'delete_address'),(68,'Can view Addresses',17,'view_address'),(69,'Can add user',18,'add_customer'),(70,'Can change user',18,'change_customer'),(71,'Can delete user',18,'delete_customer'),(72,'Can view user',18,'view_customer');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_booking`
--

DROP TABLE IF EXISTS `core_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `notes` longtext NOT NULL,
  `end_date` date DEFAULT NULL,
  `end_time` time(6) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `address_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  `provider_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_booking_provider_id_ff22360b_fk_core_providerprofile_id` (`provider_id`),
  KEY `core_booking_service_id_c8fb648d_fk_core_service_id` (`service_id`),
  KEY `core_booking_address_id_64f535d3_fk_accounts_address_id` (`address_id`),
  KEY `core_booking_customer_id_b4948c3d_fk_accounts_customer_id` (`customer_id`),
  CONSTRAINT `core_booking_address_id_64f535d3_fk_accounts_address_id` FOREIGN KEY (`address_id`) REFERENCES `accounts_address` (`id`),
  CONSTRAINT `core_booking_customer_id_b4948c3d_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `core_booking_provider_id_ff22360b_fk_core_providerprofile_id` FOREIGN KEY (`provider_id`) REFERENCES `core_providerprofile` (`id`),
  CONSTRAINT `core_booking_service_id_c8fb648d_fk_core_service_id` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_booking`
--

LOCK TABLES `core_booking` WRITE;
/*!40000 ALTER TABLE `core_booking` DISABLE KEYS */;
INSERT INTO `core_booking` VALUES (1,'2024-11-12','13:00:00.000000','','2024-11-12','15:00:00.000000','Cancelled',1,1,1,1),(2,'2024-11-11','15:00:00.000000','','2024-11-11','17:00:00.000000','Completed',2,2,1,1);
/*!40000 ALTER TABLE `core_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_payment`
--

DROP TABLE IF EXISTS `core_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `payment_date` datetime(6) NOT NULL,
  `payment_method` varchar(20) NOT NULL,
  `booking_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_payment_booking_id_cf0dceaa_fk_core_booking_id` (`booking_id`),
  CONSTRAINT `core_payment_booking_id_cf0dceaa_fk_core_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `core_booking` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_payment`
--

LOCK TABLES `core_payment` WRITE;
/*!40000 ALTER TABLE `core_payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_providerprofile`
--

DROP TABLE IF EXISTS `core_providerprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_providerprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `years_of_experience` int NOT NULL,
  `hourly_rate` decimal(6,2) NOT NULL,
  `rating` decimal(3,2) NOT NULL,
  `bio` longtext NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `core_providerprofile_user_id_0886da03_fk_accounts_customer_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_providerprofile`
--

LOCK TABLES `core_providerprofile` WRITE;
/*!40000 ALTER TABLE `core_providerprofile` DISABLE KEYS */;
INSERT INTO `core_providerprofile` VALUES (1,4,30.00,0.00,'With over 4 of experience, John Doe is a dedicated and highly skilled window cleaning expert who takes pride in making every window he works on shine. Whether it&#x27;s for a residential home, an office building, or a commercial space, John’s meticulous attention to detail ensures that every job is done to perfection.',3);
/*!40000 ALTER TABLE `core_providerprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_providerprofile_services`
--

DROP TABLE IF EXISTS `core_providerprofile_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_providerprofile_services` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `providerprofile_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_providerprofile_ser_providerprofile_id_servi_938c143f_uniq` (`providerprofile_id`,`service_id`),
  KEY `core_providerprofile_service_id_3526ca7f_fk_core_serv` (`service_id`),
  CONSTRAINT `core_providerprofile_providerprofile_id_e7cfb9e1_fk_core_prov` FOREIGN KEY (`providerprofile_id`) REFERENCES `core_providerprofile` (`id`),
  CONSTRAINT `core_providerprofile_service_id_3526ca7f_fk_core_serv` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_providerprofile_services`
--

LOCK TABLES `core_providerprofile_services` WRITE;
/*!40000 ALTER TABLE `core_providerprofile_services` DISABLE KEYS */;
INSERT INTO `core_providerprofile_services` VALUES (1,1,1);
/*!40000 ALTER TABLE `core_providerprofile_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_review`
--

DROP TABLE IF EXISTS `core_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` smallint unsigned NOT NULL,
  `comment` varchar(2000) NOT NULL,
  `booking_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  `provider_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `booking_id` (`booking_id`),
  KEY `core_review_customer_id_8def5fed_fk_accounts_customer_id` (`customer_id`),
  KEY `core_review_provider_id_d59dce18_fk_core_providerprofile_id` (`provider_id`),
  CONSTRAINT `core_review_booking_id_bd813940_fk_core_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `core_booking` (`id`),
  CONSTRAINT `core_review_customer_id_8def5fed_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `core_review_provider_id_d59dce18_fk_core_providerprofile_id` FOREIGN KEY (`provider_id`) REFERENCES `core_providerprofile` (`id`),
  CONSTRAINT `core_review_chk_1` CHECK ((`rating` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_review`
--

LOCK TABLES `core_review` WRITE;
/*!40000 ALTER TABLE `core_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_service`
--

DROP TABLE IF EXISTS `core_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_service` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `duration` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_service_category_id_7472ad4a_fk_core_servicecategory_id` (`category_id`),
  CONSTRAINT `core_service_category_id_7472ad4a_fk_core_servicecategory_id` FOREIGN KEY (`category_id`) REFERENCES `core_servicecategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_service`
--

LOCK TABLES `core_service` WRITE;
/*!40000 ALTER TABLE `core_service` DISABLE KEYS */;
INSERT INTO `core_service` VALUES (1,'House Cleaning','Complete house cleaning services.',100.00,7200000000,1),(2,'Window Cleaning','Window cleaning for homes and offices.',50.00,7200000000,1),(3,'Drainage Repair','Fix drainage problems and blocked pipes.',150.00,7200000000,2),(4,'Electrical Wiring','Electrical wiring and maintenance.',200.00,7200000000,3),(5,'Lawn Mowing','Mowing lawns and garden maintenance.',75.00,7200000000,4),(6,'Tree Trimming','Trimming and pruning trees in the garden.',120.00,7200000000,4);
/*!40000 ALTER TABLE `core_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_servicecategory`
--

DROP TABLE IF EXISTS `core_servicecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_servicecategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_servicecategory`
--

LOCK TABLES `core_servicecategory` WRITE;
/*!40000 ALTER TABLE `core_servicecategory` DISABLE KEYS */;
INSERT INTO `core_servicecategory` VALUES (1,'Cleaning'),(2,'Plumbing'),(3,'Electrical'),(4,'Gardening');
/*!40000 ALTER TABLE `core_servicecategory` ENABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customer_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customer_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-11-08 11:58:59.552235','3','Johnd',1,'[{\"added\": {}}]',18,2),(2,'2024-11-08 11:59:28.352212','3','Johnd',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email\"]}}]',18,2),(3,'2024-11-08 12:00:40.613935','1','John Doe',1,'[{\"added\": {}}]',15,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (17,'accounts','address'),(18,'accounts','customer'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(13,'core','booking'),(14,'core','payment'),(15,'core','providerprofile'),(16,'core','review'),(11,'core','service'),(12,'core','servicecategory'),(5,'sessions','session'),(6,'social_django','association'),(7,'social_django','code'),(8,'social_django','nonce'),(10,'social_django','partial'),(9,'social_django','usersocialauth');
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
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-11-08 11:51:04.065477'),(2,'contenttypes','0002_remove_content_type_name','2024-11-08 11:51:04.143179'),(3,'auth','0001_initial','2024-11-08 11:51:04.504354'),(4,'auth','0002_alter_permission_name_max_length','2024-11-08 11:51:04.630450'),(5,'auth','0003_alter_user_email_max_length','2024-11-08 11:51:04.637018'),(6,'auth','0004_alter_user_username_opts','2024-11-08 11:51:04.644023'),(7,'auth','0005_alter_user_last_login_null','2024-11-08 11:51:04.650374'),(8,'auth','0006_require_contenttypes_0002','2024-11-08 11:51:04.654340'),(9,'auth','0007_alter_validators_add_error_messages','2024-11-08 11:51:04.661375'),(10,'auth','0008_alter_user_username_max_length','2024-11-08 11:51:04.667913'),(11,'auth','0009_alter_user_last_name_max_length','2024-11-08 11:51:04.674476'),(12,'auth','0010_alter_group_name_max_length','2024-11-08 11:51:04.697515'),(13,'auth','0011_update_proxy_permissions','2024-11-08 11:51:04.707821'),(14,'auth','0012_alter_user_first_name_max_length','2024-11-08 11:51:04.717111'),(15,'accounts','0001_initial','2024-11-08 11:51:05.280286'),(16,'admin','0001_initial','2024-11-08 11:51:05.461478'),(17,'admin','0002_logentry_remove_auto_add','2024-11-08 11:51:05.472546'),(18,'admin','0003_logentry_add_action_flag_choices','2024-11-08 11:51:05.484869'),(19,'core','0001_initial','2024-11-08 11:51:06.683900'),(20,'sessions','0001_initial','2024-11-08 11:51:06.736536'),(21,'default','0001_initial','2024-11-08 11:51:06.997068'),(22,'social_auth','0001_initial','2024-11-08 11:51:07.000036'),(23,'default','0002_add_related_name','2024-11-08 11:51:07.014812'),(24,'social_auth','0002_add_related_name','2024-11-08 11:51:07.018802'),(25,'default','0003_alter_email_max_length','2024-11-08 11:51:07.033390'),(26,'social_auth','0003_alter_email_max_length','2024-11-08 11:51:07.036219'),(27,'default','0004_auto_20160423_0400','2024-11-08 11:51:07.050639'),(28,'social_auth','0004_auto_20160423_0400','2024-11-08 11:51:07.053605'),(29,'social_auth','0005_auto_20160727_2333','2024-11-08 11:51:07.074211'),(30,'social_django','0006_partial','2024-11-08 11:51:07.119774'),(31,'social_django','0007_code_timestamp','2024-11-08 11:51:07.172047'),(32,'social_django','0008_partial_timestamp','2024-11-08 11:51:07.221734'),(33,'social_django','0009_auto_20191118_0520','2024-11-08 11:51:07.303535'),(34,'social_django','0010_uid_db_index','2024-11-08 11:51:07.336005'),(35,'social_django','0011_alter_id_fields','2024-11-08 11:51:07.771964'),(36,'social_django','0012_usersocialauth_extra_data_new','2024-11-08 11:51:07.945170'),(37,'social_django','0013_migrate_extra_data','2024-11-08 11:51:07.964174'),(38,'social_django','0014_remove_usersocialauth_extra_data','2024-11-08 11:51:08.016354'),(39,'social_django','0015_rename_extra_data_new_usersocialauth_extra_data','2024-11-08 11:51:08.069318'),(40,'social_django','0016_alter_usersocialauth_extra_data','2024-11-08 11:51:08.083889'),(41,'social_django','0004_auto_20160423_0400','2024-11-08 11:51:08.089526'),(42,'social_django','0001_initial','2024-11-08 11:51:08.093160'),(43,'social_django','0003_alter_email_max_length','2024-11-08 11:51:08.096323'),(44,'social_django','0002_add_related_name','2024-11-08 11:51:08.099330'),(45,'social_django','0005_auto_20160727_2333','2024-11-08 11:51:08.101328');
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
INSERT INTO `django_session` VALUES ('bsdaa20jl8f83q0dj3tu8sf99drgyqgm','.eJxVjDsOwyAQRO9CHSF7WWBJmd5nQAusg5PIlvypotw9tuQiqUaa92beKvK21rgtMsehqKsCdfntEuenjAcoDx7vk87TuM5D0oeiT7robiryup3u30Hlpe5rEQtCTfJ5TyRGNoFCSwbQ9WKlYSByvYPWmACWkQr0HtExC3lp1ecLzuQ3KA:1tAdxe:jxJXL8IEiO-MRVyeJqJblXsGEAbtYdRAZ9fc3i7FKVE','2024-11-25 23:36:46.498362');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_association` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int NOT NULL,
  `lifetime` int NOT NULL,
  `assoc_type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_code`
--

DROP TABLE IF EXISTS `social_auth_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_code` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  KEY `social_auth_code_code_a2393167` (`code`),
  KEY `social_auth_code_timestamp_176b341f` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_code`
--

LOCK TABLES `social_auth_code` WRITE;
/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_nonce` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int NOT NULL,
  `salt` varchar(65) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_partial`
--

DROP TABLE IF EXISTS `social_auth_partial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_partial` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(32) NOT NULL,
  `next_step` smallint unsigned NOT NULL,
  `backend` varchar(32) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `data` json NOT NULL DEFAULT (_utf8mb3'{}'),
  PRIMARY KEY (`id`),
  KEY `social_auth_partial_token_3017fea3` (`token`),
  KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`),
  CONSTRAINT `social_auth_partial_chk_1` CHECK ((`next_step` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_partial`
--

LOCK TABLES `social_auth_partial` WRITE;
/*!40000 ALTER TABLE `social_auth_partial` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_partial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_usersocialauth` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `user_id` bigint NOT NULL,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `extra_data` json NOT NULL DEFAULT (_utf8mb3'{}'),
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  KEY `social_auth_usersoci_user_id_17d28448_fk_accounts_` (`user_id`),
  KEY `social_auth_usersocialauth_uid_796e51dc` (`uid`),
  CONSTRAINT `social_auth_usersoci_user_id_17d28448_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
INSERT INTO `social_auth_usersocialauth` VALUES (1,'google-oauth2','nusherjk@gmail.com',1,'2024-11-08 11:52:01.094043','2024-11-09 09:29:45.390409','{\"expires\": 3599, \"auth_time\": 1731144585, \"token_type\": \"Bearer\", \"access_token\": \"ya29.a0AeDClZChC2rwK8vwIWAg8Eblxy3vLeCzDzHVYE2HH_LaHrAT-XuJsmIVwexEsT0bAhDK35IVG9EBQZNkvyMZQqaUFXXrTvnrdxKo4EPDY-9Zq63cX1wPcP18-0wFSu0-rLMaG9FNFzvOgVJD9tZ9XJfK8GOY-qT8e1cTlhkzaCgYKAdISARESFQHGX2Mih1nmRDgFEkSi0L0qfPSrqw0175\"}');
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-12 17:46:46
