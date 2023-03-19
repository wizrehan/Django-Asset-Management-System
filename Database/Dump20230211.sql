CREATE DATABASE  IF NOT EXISTS `assetmanager` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `assetmanager`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: assetmanager
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `assign_asset`
--

DROP TABLE IF EXISTS `assign_asset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assign_asset` (
  `assign_id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `employee_id` int NOT NULL,
  `assign_date` varchar(100) NOT NULL,
  `quantity` int DEFAULT NULL,
  `status` varchar(500) NOT NULL,
  `comments` varchar(5000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `assigned_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assign_asset`
--

LOCK TABLES `assign_asset` WRITE;
/*!40000 ALTER TABLE `assign_asset` DISABLE KEYS */;
INSERT INTO `assign_asset` VALUES (54,16,65478,'2023-01-13',NULL,'Used','Re Updated','wiz','NO','wiz'),(60,14,65578,'2022-12-23',NULL,'Repaired','Broken Screen repaired ','Borhan','NO',NULL),(61,14,78321,'2022-12-22',NULL,'Re-Used','Lastly Used by MD Shahjahan Kabir','Borhan','NO',NULL),(62,21,65578,'2022-12-24',NULL,'Brand New','na/a','Borhan','NO',NULL),(66,18,65578,'2023-01-03',NULL,'Repaired','HII','wiz',NULL,'wiz'),(68,20,65478,'2023-01-02',NULL,'Brand New','N/A','wiz',NULL,NULL),(70,19,65478,'2022-12-09',NULL,'Used','Nothing','wiz',NULL,'wiz'),(71,19,65578,'2023-01-15',NULL,'Re-Used','N/A','wiz',NULL,NULL),(72,15,33657,'2023-01-07',NULL,'Brand New','N/A','wiz',NULL,NULL),(73,15,65578,'2023-01-11',NULL,'Repaired','CMOS battery replaced','wiz',NULL,NULL),(77,23,54897,'2023-01-13',NULL,'Brand New','n/a','wiz',NULL,NULL),(82,21,75486,'2023-01-19',NULL,'Repaired','CMOS battery replaced','wiz',NULL,NULL),(83,24,65478,'2023-01-25',NULL,'Brand New','N/A','wiz',NULL,NULL),(84,19,54897,'2023-02-01',NULL,'Brand New','N/A','wiz',NULL,NULL);
/*!40000 ALTER TABLE `assign_asset` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'admin'),(3,'Department'),(2,'user');
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
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add assign details',7,'add_assigndetails'),(26,'Can change assign details',7,'change_assigndetails'),(27,'Can delete assign details',7,'delete_assigndetails'),(28,'Can view assign details',7,'view_assigndetails'),(29,'Can add assign details',8,'add_assigndetails'),(30,'Can change assign details',8,'change_assigndetails'),(31,'Can delete assign details',8,'delete_assigndetails'),(32,'Can view assign details',8,'view_assigndetails'),(33,'Can add view dep',9,'add_viewdep'),(34,'Can change view dep',9,'change_viewdep'),(35,'Can delete view dep',9,'delete_viewdep'),(36,'Can view view dep',9,'view_viewdep'),(37,'Can add view des',10,'add_viewdes'),(38,'Can change view des',10,'change_viewdes'),(39,'Can delete view des',10,'delete_viewdes'),(40,'Can view view des',10,'view_viewdes'),(41,'Can add view emp',11,'add_viewemp'),(42,'Can change view emp',11,'change_viewemp'),(43,'Can delete view emp',11,'delete_viewemp'),(44,'Can view view emp',11,'view_viewemp'),(45,'Can add view office',12,'add_viewoffice'),(46,'Can change view office',12,'change_viewoffice'),(47,'Can delete view office',12,'delete_viewoffice'),(48,'Can view view office',12,'view_viewoffice'),(49,'Can add view prod',13,'add_viewprod'),(50,'Can change view prod',13,'change_viewprod'),(51,'Can delete view prod',13,'delete_viewprod'),(52,'Can view view prod',13,'view_viewprod'),(53,'Can add view uni',14,'add_viewuni'),(54,'Can change view uni',14,'change_viewuni'),(55,'Can delete view uni',14,'delete_viewuni'),(56,'Can view view uni',14,'view_viewuni'),(57,'Can add show department',15,'add_showdepartment'),(58,'Can change show department',15,'change_showdepartment'),(59,'Can delete show department',15,'delete_showdepartment'),(60,'Can view show department',15,'view_showdepartment'),(61,'Can add view manufacture',16,'add_viewmanufacture'),(62,'Can change view manufacture',16,'change_viewmanufacture'),(63,'Can delete view manufacture',16,'delete_viewmanufacture'),(64,'Can view view manufacture',16,'view_viewmanufacture'),(65,'Can add view category',17,'add_viewcategory'),(66,'Can change view category',17,'change_viewcategory'),(67,'Can delete view category',17,'delete_viewcategory'),(68,'Can view view category',17,'view_viewcategory'),(69,'Can add view stoock',18,'add_viewstoock'),(70,'Can change view stoock',18,'change_viewstoock'),(71,'Can delete view stoock',18,'delete_viewstoock'),(72,'Can view view stoock',18,'view_viewstoock'),(73,'Can add view vendoor',19,'add_viewvendoor'),(74,'Can change view vendoor',19,'change_viewvendoor'),(75,'Can delete view vendoor',19,'delete_viewvendoor'),(76,'Can view view vendoor',19,'view_viewvendoor');
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
  `employee_id` int DEFAULT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$5IvAhcpiirst$W8osjtCdHWvex/8i+vuzW5yuxMUGBWwX0/nGw3fuH9I=','2023-02-10 12:01:07.961617',1,'wiz',72750,'Abu','Raihan','18303059@iubat.edu',1,1,'2022-11-20 03:09:21.000000'),(5,'pbkdf2_sha256$180000$9zr0M9XMjoc2$v/u9IF3RcHMYgHu3GCt1y0A7F99SjkR0B5rV+EF1cu4=','2023-01-24 08:22:06.462007',0,'Raihan',5727,'Abu','Raihan','raihanfolio@gmail.com',1,1,'2022-12-14 09:00:49.000000'),(23,'pbkdf2_sha256$180000$naX5nwbkf7CL$lNEfEcR7TAFsooa5L+n8tjRvbaCyp5Ma5MjySbG8+UY=','2023-01-19 12:10:34.000000',0,'Ziaul_Marketing',75486,'Ziaul','Haque','ziaul@gmail.com',0,1,'2023-01-19 12:09:27.000000'),(24,'pbkdf2_sha256$180000$1eYwZlOSKPtc$Rs/cHm+SVtj7QkekX1rVCUvUneMe6KnZoLUG8aMNEks=','2023-02-01 11:18:03.520673',0,'Tanjim_Compliance',54897,'Tanjim','Hossain','tanjim@gmail.com',0,1,'2023-01-19 12:50:04.000000'),(25,'pbkdf2_sha256$180000$Iupnbwt3ImjX$kFX2xphw+MW7/JegORtZ5l5kOvPi+Wozn+DBtAjsq7c=','2023-01-24 09:00:02.507109',0,'test1',5689,'test','profile','test@gmail.com',0,1,'2023-01-24 08:48:55.000000');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,1,1),(4,5,2),(9,23,3),(10,24,3),(11,25,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(45) NOT NULL,
  `added_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (19,'Information And Technology','wiz','NO',NULL),(20,'Compliance','wiz','NO',NULL),(21,'Audit','wiz','NO',NULL),(22,'Marketing','wiz','NO',NULL),(23,'Human Resource','wiz','NO',NULL),(25,'Admin','wiz','YES','wiz'),(26,'Ghghsd','wiz','YES','wiz'),(27,'Nothing','wiz','YES','wiz');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `designation`
--

DROP TABLE IF EXISTS `designation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `designation` (
  `designation_id` int NOT NULL AUTO_INCREMENT,
  `designation_name` varchar(45) NOT NULL,
  `added_by` varchar(45) DEFAULT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`designation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designation`
--

LOCK TABLES `designation` WRITE;
/*!40000 ALTER TABLE `designation` DISABLE KEYS */;
INSERT INTO `designation` VALUES (9,'General Manager','wiz','NO',NULL),(10,'Assistant General Manager','wiz','NO',NULL),(11,'Manager','wiz','NO',NULL),(12,'Deputy Manger','wiz','NO',NULL),(13,'Sr. Executive','wiz','NO',NULL),(14,'Executive','wiz','NO',NULL),(15,'Intern','wiz','NO',NULL),(16,'Graphic Designer','wiz','YES','wiz'),(17,'Nothing250KL','wiz','YES','wiz');
/*!40000 ALTER TABLE `designation` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-12-07 05:38:59.565120','1','wiz',2,'[]',4,1),(2,'2022-12-14 05:56:37.916841','1','wiz',2,'[]',4,1),(3,'2022-12-14 07:59:40.885355','2','tawhid',3,'',4,1),(4,'2022-12-20 15:01:15.486559','1','Admin',1,'[{\"added\": {}}]',3,1),(5,'2022-12-21 05:15:57.994825','2','user',1,'[{\"added\": {}}]',3,1),(6,'2022-12-21 05:16:08.277357','1','admin',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',3,1),(7,'2022-12-21 05:16:22.236298','1','wiz',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(8,'2022-12-21 05:16:33.767621','3','Imran',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(9,'2022-12-21 05:16:40.578881','4','Lokman',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(10,'2022-12-21 05:16:47.120000','5','Raihan',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(11,'2022-12-22 07:51:20.956846','3','Imran',3,'',4,1),(12,'2023-01-11 03:27:26.645298','3','Department',1,'[{\"added\": {}}]',3,1),(13,'2023-01-11 03:27:33.733316','3','Department',2,'[]',3,1),(14,'2023-01-11 03:28:50.151958','5','Raihan',2,'[]',4,1),(15,'2023-01-11 03:31:05.457411','9','BGI-HR',2,'[{\"changed\": {\"fields\": [\"Groups\", \"User permissions\"]}}]',4,1),(16,'2023-01-11 18:06:59.156965','6','Borhan',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(17,'2023-01-11 18:07:09.873990','8','amir',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(18,'2023-01-11 18:52:53.274017','1','wiz',2,'[]',4,1),(19,'2023-01-11 18:55:07.718411','5','Raihan',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(20,'2023-01-12 04:36:07.218704','9','BGI-HR',2,'[]',4,1),(21,'2023-01-14 12:25:49.670422','10','BGI-Complience',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(22,'2023-01-16 06:22:24.460291','10','BGI-Complience',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(23,'2023-01-19 12:12:00.207557','23','Ziaul_Marketing',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(24,'2023-01-19 12:50:21.505644','24','Tanjim_Compliance',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(25,'2023-01-19 13:41:58.347197','8','amir',3,'',4,1),(26,'2023-01-19 13:41:58.353498','10','BGI-Complience',3,'',4,1),(27,'2023-01-19 13:41:58.358803','9','BGI-HR',3,'',4,1),(28,'2023-01-19 13:41:58.361489','6','Borhan',3,'',4,1),(29,'2023-01-19 13:41:58.365585','4','Lokman',3,'',4,1),(30,'2023-01-24 08:50:08.014360','25','test1',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'dashboard','assigndetails'),(15,'employee','showdepartment'),(6,'sessions','session'),(7,'view','assigndetails'),(9,'view_department','viewdep'),(10,'view_designation','viewdes'),(11,'view_employee','viewemp'),(16,'view_manufacturer','viewmanufacture'),(12,'view_office_location','viewoffice'),(13,'view_product','viewprod'),(17,'view_product_category','viewcategory'),(18,'view_stock','viewstoock'),(14,'view_unit','viewuni'),(19,'view_vendor','viewvendoor');
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-11-14 09:17:36.292685'),(2,'auth','0001_initial','2022-11-14 09:17:37.011931'),(3,'admin','0001_initial','2022-11-14 09:17:37.160281'),(4,'admin','0002_logentry_remove_auto_add','2022-11-14 09:17:37.169787'),(5,'admin','0003_logentry_add_action_flag_choices','2022-11-14 09:17:37.183354'),(6,'contenttypes','0002_remove_content_type_name','2022-11-14 09:17:37.366214'),(7,'auth','0002_alter_permission_name_max_length','2022-11-14 09:17:37.438671'),(8,'auth','0003_alter_user_email_max_length','2022-11-14 09:17:37.473323'),(9,'auth','0004_alter_user_username_opts','2022-11-14 09:17:37.489330'),(10,'auth','0005_alter_user_last_login_null','2022-11-14 09:17:37.567160'),(11,'auth','0006_require_contenttypes_0002','2022-11-14 09:17:37.572947'),(12,'auth','0007_alter_validators_add_error_messages','2022-11-14 09:17:37.584948'),(13,'auth','0008_alter_user_username_max_length','2022-11-14 09:17:37.658065'),(14,'auth','0009_alter_user_last_name_max_length','2022-11-14 09:17:37.726734'),(15,'auth','0010_alter_group_name_max_length','2022-11-14 09:17:37.769001'),(16,'auth','0011_update_proxy_permissions','2022-11-14 09:17:37.784418'),(17,'auth','0012_alter_user_first_name_max_length','2022-11-14 09:17:37.862384'),(18,'sessions','0001_initial','2022-11-14 09:17:37.906726'),(19,'view','0001_initial','2022-12-01 09:22:19.297429'),(20,'dashboard','0001_initial','2022-12-06 04:07:14.189257'),(21,'view_department','0001_initial','2022-12-06 09:07:17.233714'),(22,'view_designation','0001_initial','2022-12-06 09:07:17.267063'),(23,'view_employee','0001_initial','2022-12-06 09:07:17.301126'),(24,'view_office_location','0001_initial','2022-12-06 09:07:17.337747'),(25,'view_product','0001_initial','2022-12-06 09:07:17.379611'),(26,'view_unit','0001_initial','2022-12-06 09:07:17.416640'),(27,'dashboard','0002_remove_assigndetails_employee_id_and_more','2022-12-11 10:01:12.437392'),(28,'employee','0001_initial','2022-12-11 10:01:12.486284'),(29,'view_manufacturer','0001_initial','2022-12-11 10:01:12.520116'),(30,'view_product_category','0001_initial','2022-12-11 10:01:12.553440'),(31,'view_stock','0001_initial','2022-12-11 10:01:12.586430'),(32,'view_vendor','0001_initial','2022-12-11 10:01:12.663564');
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
INSERT INTO `django_session` VALUES ('8qj262znbrpp0u2ya9ud1f1p0709j0pl','.eJxVjDEOwjAMRe-SGUU2qRNgZO8ZKsd2aAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzN6i7OHSH3y2zPGzcgN55vE1epnGZh-w3xe-0-nZSe1539--g59p_a0gQY0yWTyoEZ1LRmNGKqZI1jYhhYOCGImIISYJRAYRjViAslNz7A-6BN-o:1p922x:QZMx7ILjv3qtPxGXxwaBtVV21Ioiz92jcJJXbMdSCqw','2023-01-07 10:46:31.760125'),('968nsopmtxv1jazbinh0k4xzcojv87ae','.eJxVjEEOwiAQRe_C2hBhHAou3XsGMsyAVA1NSrsy3l2bdKHb_977LxVpXWpce57jKOqsUB1-t0T8yG0Dcqd2mzRPbZnHpDdF77Tr6yT5edndv4NKvX5rjwMgiDOhUHGmWAY-hYQmBBfYJwZnEb1N4BiRxQ3eCwFJsUDHAur9AcxdN4w:1p7b1s:ORs5D1QrWd5ra1XZ8JgPn_gHQY4PxzOBha48FmF8oAc','2023-01-03 11:43:28.950549'),('foagkwkrnwkzl5a56x469ylov6rlz1ur','ZmI3NTZiYjA3YzI4MmRjNGFkNDJjZjBiNDBhOGY1ODFhZjY3NGYwZDp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODVlMjcwNDE4ZWNlMGNhYzhlZDhhZjY0YmNhZGU5YWE0MDNlMmQxMiJ9','2023-02-15 11:18:03.528691'),('l633h343t6vknmwr0e1irky7mbnoekek','.eJxVjDsOwjAQRO_iGlmxN_5R0ucMlj-7OIBsKU4qxN1JpBRQTDPvzbyZD9ta_NZx8XNmVybY5beLIT2xHiA_Qr03nlpdlznyQ-En7XxqGV-30_07KKGXfU0uWqOsAxLGkgxG2zRECVlBRMx7JGpNo4JMMNCIKREGkMJJIIuafb71fjis:1oweXx:26_hLhteXSnMOJ79F1IWnTmABOE0Upeu3WyAt7JI7Xg','2022-12-04 07:15:21.691835'),('lk9niwbhfpoc6td19d2m61o16n96s44z','ZmI3NTZiYjA3YzI4MmRjNGFkNDJjZjBiNDBhOGY1ODFhZjY3NGYwZDp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODVlMjcwNDE4ZWNlMGNhYzhlZDhhZjY0YmNhZGU5YWE0MDNlMmQxMiJ9','2023-02-14 19:16:24.943582'),('osvjzlyeeabj1trvy2fpy20xq8i9vql4','.eJxVjDEOwjAMRe-SGUU2qRNgZO8ZKsd2aAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzN6i7OHSH3y2zPGzcgN55vE1epnGZh-w3xe-0-nZSe1539--g59p_a0gQY0yWTyoEZ1LRmNGKqZI1jYhhYOCGImIISYJRAYRjViAslNz7A-6BN-o:1p8vRs:cgBSJmGUNyC4pkfEXsd-Z9fcJ8TnNAnwfbGCp5xHOzE','2023-01-07 03:43:48.492593'),('pyy3n8w7rf824npxuptfhmrvlaum1l1t','ZDQyOTFjNzJlNDAyYzE4NTU1ZmRmNDc3MTI0MjVlZmJhMjUwMjM3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0Y2Q4MDQ5YjhiMDljZGZjNzE4Mjg2OWIxZjNkYjljNzZjMThlZDY5In0=','2023-02-14 11:52:21.422755'),('rcqxaosheegfdvicvq3d3crwq6gbct8a','ZDQyOTFjNzJlNDAyYzE4NTU1ZmRmNDc3MTI0MjVlZmJhMjUwMjM3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0Y2Q4MDQ5YjhiMDljZGZjNzE4Mjg2OWIxZjNkYjljNzZjMThlZDY5In0=','2023-02-24 12:01:08.062999');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_id` int NOT NULL,
  `employee_name` varchar(45) NOT NULL,
  `department_id` int NOT NULL,
  `designation_id` int NOT NULL,
  `unit_id` int NOT NULL,
  `contact` varchar(45) NOT NULL,
  `employee_mail` varchar(45) NOT NULL,
  `office_location_id` int NOT NULL,
  `employee_status` varchar(45) NOT NULL,
  `create_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (5689,'TEST',21,14,15,'014587935','test@gmail.com',19,'Active','wiz','YES','wiz'),(5727,'Abu Raihan_IT',19,15,23,'01706652934','18303059@iubat.edu',19,'Active','wiz','NO','wiz'),(25364,'Shafin Khan',20,11,20,'0179834467','shafin@bengal.com',21,'Active','wiz','YES','wiz'),(25469,'Md Shohag',19,11,20,'01787823655','sohag@gmail.com',19,'Active','wiz','NO',NULL),(33657,'Md Zakir Hossain',19,13,23,'0179834467','zakir@bengal.com',19,'Active','wiz','NO',NULL),(54897,'Tanjim Hossain',20,14,15,'0189756423','tanjim@gmail.com',20,'Active','wiz','NO',NULL),(65478,'Tawhid rahman',23,14,23,'0165678967','tawhid__a@bengal.com',19,'Active','wiz','NO','wiz'),(65578,'MD Asad Miaa',23,13,23,'0147896322','asad_miaa@gmail.com',20,'Active','wiz','NO','wiz'),(72750,'IT_Admin',19,9,23,'015689745','it3@bengal.com',19,'Active','wiz','NO',NULL),(75486,'Ziaul Haque',22,14,15,'015469832','ziaul@gmail.com',21,'Active','wiz','NO',NULL),(78321,'Md Iresh Zaker',21,9,11,'0179834467','iresh@bengal.com',19,'Active','wiz','NO',NULL);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturer`
--

DROP TABLE IF EXISTS `manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturer` (
  `manufacturer_id` int NOT NULL AUTO_INCREMENT,
  `manufacturer_name` varchar(45) NOT NULL,
  `country` varchar(45) NOT NULL,
  `added_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`manufacturer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturer`
--

LOCK TABLES `manufacturer` WRITE;
/*!40000 ALTER TABLE `manufacturer` DISABLE KEYS */;
INSERT INTO `manufacturer` VALUES (11,'Dell','USA','wiz','NO',NULL),(12,'Lenevo','Japan','wiz','NO',NULL),(13,'Tosiba','Taiwan','wiz','NO',NULL),(14,'Samsung','Taiwan','wiz','NO',NULL),(15,'HP','China','wiz','NO',NULL),(16,'Huwai','Hungery','wiz','NO',NULL),(17,'A4Tech','USA','wiz','NO',NULL),(18,'MSI','USA','wiz','NO',NULL),(19,'DCL','Taiwan','wiz','YES','wiz'),(20,'Nothing','Malaysia','wiz','YES','wiz'),(21,'Nothing23-89','Uganda23','wiz','YES','wiz');
/*!40000 ALTER TABLE `manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `office_location`
--

DROP TABLE IF EXISTS `office_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `office_location` (
  `office_location_id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(45) NOT NULL,
  `added_by` varchar(45) DEFAULT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`office_location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `office_location`
--

LOCK TABLES `office_location` WRITE;
/*!40000 ALTER TABLE `office_location` DISABLE KEYS */;
INSERT INTO `office_location` VALUES (19,'Bengal House','wiz','NO',NULL),(20,'Learning and Development Building','wiz','NO',NULL),(21,'Romanian Building','wiz','NO',NULL),(22,'NX1 Building','wiz','NO','wiz'),(24,'Uttara','wiz','YES','wiz'),(25,'MIRPUR','wiz','YES','wiz');
/*!40000 ALTER TABLE `office_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(45) NOT NULL,
  `manufacture_id` int NOT NULL,
  `category_id` int NOT NULL,
  `vendor_id` int NOT NULL,
  `warranty_till` date NOT NULL,
  `serial_IMEI` varchar(45) NOT NULL,
  `specification` varchar(45) NOT NULL,
  `invoice_no` varchar(45) NOT NULL,
  `purchase_date` date NOT NULL,
  `added_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `serial_IMEI_UNIQUE` (`serial_IMEI`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (14,'Dell Aspirion',11,9,1,'2024-06-22','4588965665','Intel Core i3,  8th Gen, 8 GB RAM, 256GB SSD','325973','2022-12-14','wiz','NO',NULL),(15,'Lenevo Ideapad 330',12,9,2,'2026-06-11','MX45474267grMN','Intel Core i5,  8th Gen, 4 GB RAM, 256GB SSD','8e7383e8r8384','2022-12-08','wiz','NO',NULL),(16,'Headphone',14,8,5,'2023-12-22','n/a','Black','344521','2022-12-15','wiz','NO',NULL),(18,'Keyborad',11,8,4,'2024-06-06',' ','Black','344521','2022-12-01','wiz','NO',NULL),(19,'Mouse',17,8,1,'2023-07-12','null','Black','3259737','2022-12-09','wiz','NO',NULL),(20,'Monitor',15,7,2,'2026-07-09','4588965665bcb','LED','3259737','2022-12-17','wiz','NO',NULL),(21,'MSI 330 7th Gen Laptop',18,9,9,'2026-01-01','hsgfhsfg67724','256 BF of SSd','877875hh','2022-12-22','Borhan','NO',NULL),(22,'DCL 105',11,9,2,'2024-07-03','55454882369','Intel Core i3,  5th Gen, 4 GB RAM, 256GB SSD','21495aHga','2023-01-02','wiz','YES','wiz'),(23,'IP Camera',14,12,8,'2026-01-20','2666389R','HD Cameraa','5897R','2023-01-14','wiz','NO','wiz'),(24,'TEST',15,8,5,'2026-01-01','6767242','Intel Core i3,  5th Gen, 4 GB RAM, 256GB SSD','848648','2023-01-27','wiz','NO',NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_category`
--

DROP TABLE IF EXISTS `product_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(45) NOT NULL,
  `added_by` varchar(45) DEFAULT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_category`
--

LOCK TABLES `product_category` WRITE;
/*!40000 ALTER TABLE `product_category` DISABLE KEYS */;
INSERT INTO `product_category` VALUES (6,'Software','wiz','NO','wiz'),(7,'Monitor','wiz','NO',NULL),(8,'Wireless','wiz','NO',NULL),(9,'Laptop','wiz','NO',NULL),(10,'Desktop','wiz','NO',NULL),(11,'USB Dongle','wiz','NO',NULL),(12,'Hardware','wiz','NO',NULL),(13,'Adapter','wiz','NO',NULL),(14,'XYZ','wiz','YES','wiz'),(15,'Nothing23','wiz','YES','wiz');
/*!40000 ALTER TABLE `product_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_status`
--

DROP TABLE IF EXISTS `product_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_status` (
  `product_status_id` int NOT NULL AUTO_INCREMENT,
  `status` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `added_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`product_status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_status`
--

LOCK TABLES `product_status` WRITE;
/*!40000 ALTER TABLE `product_status` DISABLE KEYS */;
INSERT INTO `product_status` VALUES (7,'Brand New','wiz','NO',NULL),(8,'Repaired','Raihan','NO',NULL),(12,'Used','wiz','NO',NULL),(13,'Re-Used','wiz','NO',NULL),(14,'Damaged','wiz','NO',NULL),(15,'Returned','wiz','YES','wiz'),(16,'Returned','wiz','YES','wiz'),(17,'Nothing23+89','wiz','YES','wiz');
/*!40000 ALTER TABLE `product_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requisition`
--

DROP TABLE IF EXISTS `requisition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requisition` (
  `requisition_id` int NOT NULL AUTO_INCREMENT,
  `product_id` varchar(200) NOT NULL,
  `employee_id` int NOT NULL,
  `request_date` date NOT NULL,
  `message` varchar(2000) DEFAULT NULL,
  `feedback` varchar(3000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `request_by` varchar(100) NOT NULL,
  `is_accepted` varchar(45) NOT NULL,
  `accept_reject_by` varchar(45) DEFAULT NULL,
  `quantity` varchar(45) NOT NULL,
  PRIMARY KEY (`requisition_id`),
  UNIQUE KEY `requisition_id_UNIQUE` (`requisition_id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requisition`
--

LOCK TABLES `requisition` WRITE;
/*!40000 ALTER TABLE `requisition` DISABLE KEYS */;
INSERT INTO `requisition` VALUES (46,'19',33657,'2023-01-19','hyu','please come','wiz','Accepted','wiz','5'),(49,'21',54897,'2023-01-19','I need this for high priority task ','Sorry!\r\nYou are only allowed to take one laptop','Tanjim_Compliance','Rejected','wiz','2'),(50,'19',54897,'2023-01-19','Please provide','Please come with all the approval copy','Tanjim_Compliance','Accepted','wiz','1'),(95,'16',54897,'2023-01-24','Assign please','','Tanjim_Compliance','NO','','2'),(121,'24',72750,'2023-01-29','yt','Not possible','wiz','Rejected','wiz','3'),(122,'23',54897,'2023-01-29','sds','Come to department','Tanjim_Compliance','Accepted','wiz','1'),(123,'16',72750,'2023-02-01','gdjgf','dimu na','wiz','Rejected','wiz','3'),(126,'18',54897,'2023-02-01','Please provide the asset by 5th february','ok','Tanjim_Compliance','Accepted','wiz','2'),(127,'19',54897,'2023-02-01','Please provide the asset by 5th february','Please with approval of line manager','Tanjim_Compliance','Accepted','wiz','1');
/*!40000 ALTER TABLE `requisition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `return_asset`
--

DROP TABLE IF EXISTS `return_asset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `return_asset` (
  `return_asset_id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `employee_id` int NOT NULL,
  `return_date` date NOT NULL,
  `product_status` varchar(45) NOT NULL,
  `return_reason` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `comments` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `received_by` varchar(45) NOT NULL,
  `countr` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`return_asset_id`),
  UNIQUE KEY `idreturn_asset_UNIQUE` (`return_asset_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `return_asset`
--

LOCK TABLES `return_asset` WRITE;
/*!40000 ALTER TABLE `return_asset` DISABLE KEYS */;
INSERT INTO `return_asset` VALUES (10,21,65578,'2023-01-29','Damaged','Damaged','N/A','wiz','NO',NULL);
/*!40000 ALTER TABLE `return_asset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(45) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Admin'),(2,'General Manager'),(3,'Assistant General Manager');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `stock_id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `stock_in_date` date NOT NULL,
  `available_stock` int DEFAULT NULL,
  `added_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES (15,14,4,'2022-12-16',2,'wiz'),(16,15,5,'2022-05-18',3,'wiz'),(17,16,7,'2022-10-07',6,'wiz'),(18,18,6,'2023-02-01',5,'wiz'),(19,19,8,'2022-12-02',5,'wiz'),(20,20,6,'2022-09-09',5,'wiz'),(22,21,4,'2022-07-08',3,'wiz'),(25,23,5,'2022-11-10',4,'wiz'),(26,24,10,'2022-12-01',9,'wiz');
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit`
--

DROP TABLE IF EXISTS `unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unit` (
  `unit_id` int NOT NULL AUTO_INCREMENT,
  `unit_name` varchar(45) NOT NULL,
  `added_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`unit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit`
--

LOCK TABLES `unit` WRITE;
/*!40000 ALTER TABLE `unit` DISABLE KEYS */;
INSERT INTO `unit` VALUES (11,'PIPE','wiz','NO',NULL),(14,'Polymar','wiz','NO',''),(15,'Hanger','wiz','NO',NULL),(20,'Romania','wiz','NO',''),(23,'PUBL','wiz','NO','wiz'),(24,'XYZ','wiz','YES','wiz'),(27,'Polymar','wiz','YES','wiz');
/*!40000 ALTER TABLE `unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `full_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `contact` varchar(45) NOT NULL,
  `mail` varchar(45) NOT NULL,
  `role_id` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'raihan','Abu Raihan','Zxcvbn#21','01706652934','raihanfolio@gmail.com','1','active'),(13,'ruhul','Ruhul Amin','789adadg','0147896325','adgh@gjhajd','3','Active');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendor` (
  `vendor_id` int NOT NULL AUTO_INCREMENT,
  `vendor_name` varchar(45) NOT NULL,
  `vendor_contact` varchar(45) NOT NULL,
  `vendor_mail` varchar(45) NOT NULL,
  `vendor_location` varchar(45) NOT NULL,
  `contact_person` varchar(45) NOT NULL,
  `vendor_type` varchar(45) NOT NULL,
  `vendor_status` varchar(45) NOT NULL,
  `has_trade` varchar(45) NOT NULL,
  `trade_document` longblob NOT NULL,
  `added_by` varchar(45) NOT NULL,
  `is_deleted` varchar(45) DEFAULT NULL,
  `delete_edited_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor`
--

LOCK TABLES `vendor` WRITE;
/*!40000 ALTER TABLE `vendor` DISABLE KEYS */;
INSERT INTO `vendor` VALUES (1,'Rayans','0178459632','rayans@gmail.com','Gulshan- 2','Anik - 01425369875','Local','Active','on',_binary 'GATE PASS BD.pdf','wiz','NO',NULL),(2,'Start Tech','0145789326','startec@gmail.com','Mirpur','Fazlu - 01578963254','Local','Active','on',_binary 'anydesk00000.png','wiz','NO',NULL),(4,'Tech Solutions','0178459632','tech@gmail.com','Mirpur','Anik - 01425369875','Local','Active','on',_binary 'anydesk00000.png','Raihan','NO',NULL),(5,'Techy Gen','0145789326','techy@gmail.com','Mirpur','Fazlu - 01578963254','Local','Active','on',_binary 'anydesk00000.png','Raihan','NO',NULL),(8,'BIO-Tech','01865435277','bio@gmail.com','Gulshan-3','Abid - 01875463738','Local','Active','Yes',_binary 'GATE PASS BD.pdf','Raihan','NO',NULL),(9,'SHOP TECH','0153396323','shoptech@gmail.com','Uttara 10','Rasel - 0191276746','Local','Active','Yes',_binary 'Asset Management System.pdf','Borhan','NO','wiz'),(10,'Dong Tech','014578956','dongtecg@gmail.com','Gulshan 1','Aminur - 0145789632','Local','Active','Yes',_binary 'ICECTE final presentation.pptx','wiz','YES','wiz'),(11,'Nothing','0145789326','no@gmail.com','Zigatola','Amir - 019879645','International','Active','Yes',_binary '33_Final.pdf','wiz','YES','wiz');
/*!40000 ALTER TABLE `vendor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'assetmanager'
--

--
-- Dumping routines for database 'assetmanager'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-11  9:58:58
