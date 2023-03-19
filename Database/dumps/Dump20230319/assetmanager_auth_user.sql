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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$5IvAhcpiirst$W8osjtCdHWvex/8i+vuzW5yuxMUGBWwX0/nGw3fuH9I=','2023-02-13 08:01:54.598575',1,'wiz',72750,'Abu','Raihan','18303059@iubat.edu',1,1,'2022-11-20 03:09:21.000000'),(5,'pbkdf2_sha256$180000$9zr0M9XMjoc2$v/u9IF3RcHMYgHu3GCt1y0A7F99SjkR0B5rV+EF1cu4=','2023-01-24 08:22:06.462007',0,'Raihan',5727,'Abu','Raihan','raihanfolio@gmail.com',1,1,'2022-12-14 09:00:49.000000'),(23,'pbkdf2_sha256$180000$naX5nwbkf7CL$lNEfEcR7TAFsooa5L+n8tjRvbaCyp5Ma5MjySbG8+UY=','2023-01-19 12:10:34.000000',0,'Ziaul_Marketing',75486,'Ziaul','Haque','ziaul@gmail.com',0,1,'2023-01-19 12:09:27.000000'),(24,'pbkdf2_sha256$180000$1eYwZlOSKPtc$Rs/cHm+SVtj7QkekX1rVCUvUneMe6KnZoLUG8aMNEks=','2023-02-01 11:18:03.520673',0,'Tanjim_Compliance',54897,'Tanjim','Hossain','tanjim@gmail.com',0,1,'2023-01-19 12:50:04.000000'),(25,'pbkdf2_sha256$180000$Iupnbwt3ImjX$kFX2xphw+MW7/JegORtZ5l5kOvPi+Wozn+DBtAjsq7c=','2023-01-24 09:00:02.507109',0,'test1',5689,'test','profile','test@gmail.com',0,1,'2023-01-24 08:48:55.000000'),(26,'pbkdf2_sha256$180000$RU5600YcjFUA$tPDHm46qFXksn4xV+gsAfUJ90aCyrf7mtqtH9yRZ+dc=','2023-02-13 08:57:19.329354',1,'Tawhid_Rahman',65478,'Tawhid','Rahman','it15@bengal.com.bd',1,1,'2023-02-12 03:47:43.000000'),(27,'pbkdf2_sha256$180000$jo4lnwJngkaN$/s+YPBi14YoH2UfEiyQ2h555ObmieqXTEG5QoOCotDc=','2023-02-12 04:30:59.620817',1,'IT_ADMIN',72750,'Mirza Borhan','Uddin','ithod@bengal.com.bd',1,1,'2023-02-12 04:25:59.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 15:01:59
