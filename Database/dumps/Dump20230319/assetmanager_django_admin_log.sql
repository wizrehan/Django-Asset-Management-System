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
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-12-07 05:38:59.565120','1','wiz',2,'[]',4,1),(2,'2022-12-14 05:56:37.916841','1','wiz',2,'[]',4,1),(3,'2022-12-14 07:59:40.885355','2','tawhid',3,'',4,1),(4,'2022-12-20 15:01:15.486559','1','Admin',1,'[{\"added\": {}}]',3,1),(5,'2022-12-21 05:15:57.994825','2','user',1,'[{\"added\": {}}]',3,1),(6,'2022-12-21 05:16:08.277357','1','admin',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',3,1),(7,'2022-12-21 05:16:22.236298','1','wiz',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(8,'2022-12-21 05:16:33.767621','3','Imran',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(9,'2022-12-21 05:16:40.578881','4','Lokman',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(10,'2022-12-21 05:16:47.120000','5','Raihan',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(11,'2022-12-22 07:51:20.956846','3','Imran',3,'',4,1),(12,'2023-01-11 03:27:26.645298','3','Department',1,'[{\"added\": {}}]',3,1),(13,'2023-01-11 03:27:33.733316','3','Department',2,'[]',3,1),(14,'2023-01-11 03:28:50.151958','5','Raihan',2,'[]',4,1),(15,'2023-01-11 03:31:05.457411','9','BGI-HR',2,'[{\"changed\": {\"fields\": [\"Groups\", \"User permissions\"]}}]',4,1),(16,'2023-01-11 18:06:59.156965','6','Borhan',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(17,'2023-01-11 18:07:09.873990','8','amir',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(18,'2023-01-11 18:52:53.274017','1','wiz',2,'[]',4,1),(19,'2023-01-11 18:55:07.718411','5','Raihan',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(20,'2023-01-12 04:36:07.218704','9','BGI-HR',2,'[]',4,1),(21,'2023-01-14 12:25:49.670422','10','BGI-Complience',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(22,'2023-01-16 06:22:24.460291','10','BGI-Complience',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(23,'2023-01-19 12:12:00.207557','23','Ziaul_Marketing',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(24,'2023-01-19 12:50:21.505644','24','Tanjim_Compliance',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(25,'2023-01-19 13:41:58.347197','8','amir',3,'',4,1),(26,'2023-01-19 13:41:58.353498','10','BGI-Complience',3,'',4,1),(27,'2023-01-19 13:41:58.358803','9','BGI-HR',3,'',4,1),(28,'2023-01-19 13:41:58.361489','6','Borhan',3,'',4,1),(29,'2023-01-19 13:41:58.365585','4','Lokman',3,'',4,1),(30,'2023-01-24 08:50:08.014360','25','test1',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(31,'2023-02-12 03:48:40.942311','26','Tawhid_Rahman',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]',4,1),(32,'2023-02-12 03:59:33.024634','26','Tawhid_Rahman',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(33,'2023-02-12 04:09:22.841083','26','Tawhid_Rahman',2,'[{\"changed\": {\"fields\": [\"Superuser status\"]}}]',4,1),(34,'2023-02-12 04:26:26.905035','27','IT_ADMIN',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\", \"Groups\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:02:05
