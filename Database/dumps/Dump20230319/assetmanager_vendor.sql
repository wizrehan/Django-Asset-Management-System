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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:02:03
