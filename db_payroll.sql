-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2020 at 04:00 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_payroll`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(16) NOT NULL,
  `username` varchar(2000) DEFAULT NULL,
  `password` varchar(2000) DEFAULT NULL,
  `admin_name` varchar(3000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`, `admin_name`) VALUES
(1, 'admin', 'admin', 'admin'),
(2, 'compranicles', 'compranicles', 'Earl Janiel Compra'),
(3, 'kenypan', 'panderecho', 'Kenyleen Pan'),
(4, 'mjlabastida', 'admin', 'Mary Jane Labastida');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int(16) NOT NULL,
  `last_name` varchar(3000) DEFAULT NULL,
  `first_name` varchar(3000) DEFAULT NULL,
  `department` varchar(3000) DEFAULT NULL,
  `designation` varchar(3000) DEFAULT NULL,
  `salary` decimal(30,2) DEFAULT NULL,
  `username` varchar(1000) DEFAULT NULL,
  `pwd` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`id`, `last_name`, `first_name`, `department`, `designation`, `salary`, `username`, `pwd`) VALUES
(1011, 'Pan', 'Kenyleen', 'BSIT', 'Student', '90000.00', 'pan123', 'password'),
(1012, 'Labastida', 'Mary Jean', 'BSIT', 'Student', '10000.00', 'labastida123', 'password'),
(1013, 'Compra', 'Earl Janiel', 'BSIT', 'Student', '25000.00', 'compranicles', 'compranicles'),
(1014, 'Carballo', 'Joey Glenn', 'BSIT', 'Student', '20000.00', 'carballo123', 'password'),
(1015, 'Pasoquin', 'Jessua', 'BSIT', 'Student', '20000.00', 'pasoquin123', 'password'),
(1016, 'Balona', 'Ivan Daniel', 'BSIT', 'Student', '20000.00', 'balona123', 'password'),
(1017, 'Beldeniza', 'Timothy', 'BSIT', 'Student', '50000.00', 'beldeniza123', 'password'),
(1018, 'Faranal', 'Fernan', 'BSIT', 'Student', '20000.00', 'faranal123', 'password');

-- --------------------------------------------------------

--
-- Table structure for table `records`
--

CREATE TABLE `records` (
  `id` int(16) NOT NULL,
  `id_e` int(16) NOT NULL,
  `date_save` varchar(2000) DEFAULT NULL,
  `date_payroll` varchar(2000) DEFAULT NULL,
  `rate_per_day` decimal(16,2) DEFAULT NULL,
  `days_worked` int(5) DEFAULT NULL,
  `allowance` decimal(16,2) DEFAULT NULL,
  `gross_salary` decimal(16,2) DEFAULT NULL,
  `sss` decimal(16,2) DEFAULT NULL,
  `philhealth` decimal(16,2) DEFAULT NULL,
  `other_deduct` decimal(16,2) DEFAULT NULL,
  `total_deduct` decimal(16,2) DEFAULT NULL,
  `net_salary` decimal(16,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `records`
--

INSERT INTO `records` (`id`, `id_e`, `date_save`, `date_payroll`, `rate_per_day`, `days_worked`, `allowance`, `gross_salary`, `sss`, `philhealth`, `other_deduct`, `total_deduct`, `net_salary`) VALUES
(1, 1012, 'February 08, 2020', 'January 2020', '333.33', 23, '0.00', '7666.67', '400.00', '137.50', '0.00', '537.50', '7129.17'),
(5, 1013, 'February 09, 2020', 'March 2020', '833.33', 24, '23.00', '19190.67', '800.00', '343.75', '0.00', '1143.75', '18046.92');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `records`
--
ALTER TABLE `records`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_e` (`id_e`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1019;

--
-- AUTO_INCREMENT for table `records`
--
ALTER TABLE `records`
  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `records`
--
ALTER TABLE `records`
  ADD CONSTRAINT `records_ibfk_1` FOREIGN KEY (`id_e`) REFERENCES `employees` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
