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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:02:02
