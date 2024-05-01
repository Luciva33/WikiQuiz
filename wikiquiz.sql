-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2024-05-01 09:07:49
-- サーバのバージョン： 10.4.32-MariaDB
-- PHP のバージョン: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `wikiquiz`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `ranking`
--

CREATE TABLE `ranking` (
  `id` int(11) NOT NULL,
  `player_name` varchar(16) DEFAULT NULL,
  `category` int(11) DEFAULT NULL,
  `clear_time` varchar(16) DEFAULT NULL,
  `updated` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `ranking`
--

INSERT INTO `ranking` (`id`, `player_name`, `category`, `clear_time`, `updated`) VALUES
(1, 'test', 0, '0分58秒', '2024-04-27 20:27:28'),
(2, 'test', 1, '1分10秒', '2024-04-30 17:02:01'),
(3, 'test', 2, '0分43秒', '2024-04-30 18:26:39');

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `ranking`
--
ALTER TABLE `ranking`
  ADD PRIMARY KEY (`id`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `ranking`
--
ALTER TABLE `ranking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
