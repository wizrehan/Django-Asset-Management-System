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
INSERT INTO `employee` VALUES (5689,'TEST',21,14,15,'014587935','test@gmail.com',19,'Active','wiz','YES','wiz'),(5727,'Abu Raihan_IT',19,15,23,'01706652934','18303059@iubat.edu',19,'Active','wiz','NO','wiz'),(25364,'Shafin Khan',20,11,20,'0179834467','shafin@bengal.com',21,'Active','wiz','YES','wiz'),(25469,'Md Shohag',19,11,20,'01787823655','sohag@gmail.com',19,'Active','wiz','NO',NULL),(33657,'Md Zakir Hossain',19,13,23,'0179834467','zakir@bengal.com',19,'Active','wiz','NO',NULL),(54897,'Tanjim Hossain',20,14,15,'0189756423','tanjim@gmail.com',20,'Active','wiz','NO',NULL),(65478,'Tohid Rahman',19,14,23,'01656789675','it15@bengal.com.bd',19,'Active','wiz','NO','Tawhid_Rahman'),(65578,'MD Asad Miaa',23,13,23,'0147896322','asad_miaa@gmail.com',20,'Active','wiz','NO','wiz'),(72750,'IT_Admin',19,9,23,'015689745','it3@bengal.com',19,'Active','wiz','NO',NULL),(75486,'Ziaul Haque',22,14,15,'015469832','ziaul@gmail.com',21,'Active','wiz','NO',NULL),(78321,'Md Iresh Zaker',21,9,11,'0179834467','iresh@bengal.com',19,'Active','wiz','NO',NULL);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
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
