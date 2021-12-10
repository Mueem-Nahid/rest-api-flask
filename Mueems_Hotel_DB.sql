-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 10, 2021 at 01:55 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Mueems_Hotel_DB`
--

-- --------------------------------------------------------

--
-- Table structure for table `Hotel_details`
--

CREATE TABLE `Hotel_details` (
  `Name` varchar(250) NOT NULL,
  `Sleeps` varchar(30) DEFAULT NULL,
  `Bedroom` varchar(30) DEFAULT NULL,
  `Bathroom` varchar(30) DEFAULT NULL,
  `Image1` varchar(500) DEFAULT NULL,
  `Image2` varchar(500) DEFAULT NULL,
  `Image3` varchar(500) DEFAULT NULL,
  `Price` varchar(10) DEFAULT NULL,
  `Location` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Hotel_details`
--

INSERT INTO `Hotel_details` (`Name`, `Sleeps`, `Bedroom`, `Bathroom`, `Image1`, `Image2`, `Image3`, `Price`, `Location`) VALUES
('Cabin on Hwy 129 overlooking Cheoah River - 8 miles to Tail of the Dragon', 'Sleeps 6', '3 Bedrooms', '2 Bathrooms', '[\'https://media.vrbo.com/lodging/28000000/27140000/27138800/27138715/6c5a7857.c6.jpg\']', '[\'https://media.vrbo.com/lodging/28000000/27140000/27138800/27138715/c0cd857c.c6.jpg\']', '[\'https://media.vrbo.com/lodging/28000000/27140000/27138800/27138715/7d97a7a5.c6.jpg\']', '$140', 'North Carolina'),
('Couples Retreat with Incredible Mountain Views!', 'Sleeps 4', '1 Bedroom', '1 Bathroom', '[\'https://media.vrbo.com/lodging/34000000/33560000/33553100/33553019/74932eec.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33560000/33553100/33553019/95ee6167.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33560000/33553100/33553019/8467438b.c6.jpg\']', '$60', 'North Carolina'),
('Log cabin , riverfront,Hot Tub, mins to Chimney Rck /Lake Lure , Fishing', 'Sleeps 2', '1 Bedroom', '1 Bathroom', '[\'https://media.vrbo.com/lodging/34000000/33560000/33558900/33558825/83284fad.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33560000/33558900/33558825/253962a5.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33560000/33558900/33558825/521f0524.c6.jpg\']', '$165', 'North Carolina'),
('Secluded Beaufort Waterfront Pet Friendly!', 'Sleeps 6', '3 Bedrooms', '2 Bathrooms', '[\'https://media.vrbo.com/lodging/34000000/33650000/33643400/33643392/3de8abef.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33650000/33643400/33643392/c3e38645.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33650000/33643400/33643392/dbf4effb.c6.jpg\']', '$225', 'North Carolina'),
('Stunning Private Log Cabin! ~ Hot Tub, Views, Internet, Fireplace, Air Condition', 'Sleeps 6', '3 Bedrooms', '3 Bathrooms', '[\'https://media.vrbo.com/lodging/34000000/33510000/33503400/33503378/42059d35.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33510000/33503400/33503378/18ea7f32.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33510000/33503400/33503378/0a37e9ba.c6.jpg\']', '$152', 'North Carolina'),
('Your Mayberry Get-a-Way Cabin', 'Sleeps 3', '1 Bedroom', '1 Bathroom', '[\'https://media.vrbo.com/lodging/34000000/33500000/33494300/33494208/81907435.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33500000/33494300/33494208/351ef0a3.c6.jpg\']', '[\'https://media.vrbo.com/lodging/34000000/33500000/33494300/33494208/237a4593.c6.jpg\']', '$101', 'North Carolina');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Hotel_details`
--
ALTER TABLE `Hotel_details`
  ADD PRIMARY KEY (`Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
