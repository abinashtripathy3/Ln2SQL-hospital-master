-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 23, 2017 at 01:17 AM
-- Server version: 5.6.35
-- PHP Version: 5.6.30

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `heyzot-analytics`
--

-- --------------------------------------------------------

--
--

-- import mysql.connector    
-- cnx = mysql.connector.connect(user='root', password='!1Abinash',
--                               host='127.0.0.1',
--                               database='hospital')
-- cursor = connection.cursor()
-- cursor.execute("""
-- SELECT count(*) FROM patient;""")
-- result = cursor.fetchall()
-- print (result)
-- 
-- cursor.close()
-- connection.close()

-- Table structure for table `patient`


CREATE TABLE `patient` (
  `patientId` varchar(30) ,
  `type` varchar(10) ,
  `externalId` varchar(45)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=7 ;


-- Dumping data for table `patient`


INSERT INTO `patient` (`patientId`, `type`, `externalId`) VALUES
('entity_0P71OE6NG3800', 'ELATION', 'elation_77214371938305'),
('entity_0P7MLVPEO3800', 'HINT', 'hint_pat-Q7BPlagHqKjI'),
('entity_0P7469OIO2000', 'ELATION', 'elation_77244609003521'),
('entity_0P7NS0F885G00', 'ELATION', 'elation_77222664536065'),
('entity_0PAD61OK83800', 'HINT', 'hint_pat-UXFz0zjU3J1S');

-- --------------------------------------------------------
-- Table structure for table `doctor`


CREATE TABLE `doctor` (
  `doctorId` varchar(10) ,
  `doctorName` varchar(45) ,
  `attenedInd` varchar(5) ,
  `patientId` varchar(30)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=7 ;


-- Dumping data for table `doctor`


INSERT INTO `doctor` (`doctorId`, `doctorName`, `attenedInd`, `patientId`) VALUES
('1','Alan','Yes','entity_0P71OE6NG3800'),
('2','Paul','No','entity_0P7469OIO2000'),
('3','John','Yes','entity_0P7MLVPEO3800'),
('4','Mark','Yes','entity_0P7469OIO2000'),
('5','Tom','No','entity_0P7NS9QVG3800');


-- Indexes for table `city`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`externalId`),
  ADD KEY `externalId` (`externalId`);

--
-- Indexes for table `emp`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`doctorId`),
  ADD KEY `doctorId` (`doctorId`);


-- Constraints for table `emp`

ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`patientId`) REFERENCES `patient` (`externalId`);


