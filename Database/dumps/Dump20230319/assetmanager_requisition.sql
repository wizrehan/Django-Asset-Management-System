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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:02:04
