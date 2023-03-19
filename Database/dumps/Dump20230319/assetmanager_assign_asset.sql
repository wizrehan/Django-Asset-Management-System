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
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assign_asset`
--

LOCK TABLES `assign_asset` WRITE;
/*!40000 ALTER TABLE `assign_asset` DISABLE KEYS */;
INSERT INTO `assign_asset` VALUES (54,16,65478,'2023-01-13',NULL,'Used','Re Updated','wiz','NO','wiz'),(60,14,65578,'2022-12-23',NULL,'Repaired','Broken Screen repaired ','Borhan','NO',NULL),(61,14,78321,'2022-12-22',NULL,'Re-Used','Lastly Used by MD Shahjahan Kabir','Borhan','NO',NULL),(62,21,65578,'2022-12-24',NULL,'Brand New','na/a','Borhan','NO',NULL),(66,18,65578,'2023-01-03',NULL,'Repaired','HII','wiz',NULL,'wiz'),(68,20,65478,'2023-01-02',NULL,'Brand New','N/A','wiz',NULL,NULL),(70,19,65478,'2022-12-09',NULL,'Used','Nothing','wiz',NULL,'wiz'),(71,19,65578,'2023-01-15',NULL,'Re-Used','N/A','wiz',NULL,NULL),(72,15,33657,'2023-01-07',NULL,'Brand New','N/A','wiz',NULL,NULL),(73,15,65578,'2023-01-11',NULL,'Repaired','CMOS battery replaced','wiz',NULL,NULL),(77,23,54897,'2023-01-13',NULL,'Brand New','n/a','wiz',NULL,NULL),(82,21,75486,'2023-01-19',NULL,'Repaired','CMOS battery replaced','wiz',NULL,NULL),(83,24,65478,'2023-01-25',NULL,'Brand New','N/A','wiz',NULL,NULL),(84,19,54897,'2023-02-01',NULL,'Brand New','N/A','wiz',NULL,NULL),(85,14,25469,'2023-02-01',NULL,'Used','test','Tawhid_Rahman',NULL,NULL);
/*!40000 ALTER TABLE `assign_asset` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:02:00
