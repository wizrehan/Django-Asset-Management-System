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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:02:01
