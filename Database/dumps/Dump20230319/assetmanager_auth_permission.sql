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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:02:02
