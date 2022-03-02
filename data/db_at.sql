
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `num_at_not_recept_monthly_by_midia` (
`created_at` varchar(7)
,`nm_midia` varchar(50)
,`qtd_ligacoes` bigint(21)
);

CREATE TABLE `num_at_recept_daily_by_status_by_media` (
`created_at` varchar(10)
,`nm_status` varchar(50)
,`nm_midia` varchar(50)
,`qtd_ligacoes` bigint(21)
);

CREATE TABLE `tb_call` (
  `id` bigint(20) NOT NULL COMMENT "id da ligacao",
  `midia_id` int(11) NOT NULL COMMENT "id da midia",
  `user_id` int(11) NOT NULL COMMENT "id do usuario",
  `customer_id` int(11) NOT NULL COMMENT "id do cliente",
  `tipo_id` int(11) NOT NULL COMMENT "id do tipo de ligacao",
  `project_id` int(11) NOT NULL COMMENT "id do projeto",
  `status_id` int(11) NOT NULL COMMENT "id do status da ligacao",
  `nm_protocol` varchar(255) NOT NULL COMMENT "protocolo da ligacao",
  `qtd_minutos_call` int(11) DEFAULT NULL COMMENT "tempo de duracao da ligacao em minutos",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "data de criacao do registro",
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT "data de atualizacao do registro"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="Tabela de ligações ,receptivas e não receptivas.";


CREATE TABLE `tb_call_status` (
  `id` int(11) NOT NULL COMMENT "id status ligacao",
  `nm_status` varchar(50) NOT NULL COMMENT "nome do status",
  `st_status` int(1) NOT NULL DEFAULT "1" COMMENT "situacao do status - 1 = ativo, 0 = inativo",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "data de criacao",
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT "data de atualizacao"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="Tabela de status do atendimento" ROW_FORMAT=DYNAMIC;


INSERT INTO `tb_call_status` (`id`, `nm_status`, `st_status`, `created_at`, `updated_at`) VALUES
(1, "EM_ATENDIMENTO", 1, "2022-02-09 23:14:36", NULL),
(2, "FINALIZADO_SUCESSO", 1, "2022-02-09 23:14:36", NULL),
(3, "FINALIZADO_ERRO", 1, "2022-02-09 23:14:36", NULL),
(4, "ERRO", 1, "2022-02-09 23:14:36", NULL);


CREATE TABLE `tb_call_tipo` (
  `id` int(11) NOT NULL COMMENT "id do tipo da ligacao",
  `nm_tipo` varchar(50) NOT NULL COMMENT "nome do tipo da ligacao",
  `st_tipo` int(11) NOT NULL DEFAULT "1" COMMENT "status do tipo da ligacao. 1=ativo, 0=inativo",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "data de criacao",
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT "data de atualizacao"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="Tabela de tipos de atendimento";


INSERT INTO `tb_call_tipo` (`id`, `nm_tipo`, `st_tipo`, `created_at`, `updated_at`) VALUES
(1, "ENTRADA", 1, "2022-02-09 23:15:34", NULL),
(2, "SAIDA", 1, "2022-02-09 23:15:34", NULL),
(3, "DESCONHECIDO(A)", 1, "2022-02-10 02:51:02", NULL);


CREATE TABLE `tb_customer` (
  `id` int(11) NOT NULL COMMENT "id do cliente",
  `nm_customer` varchar(255) NOT NULL COMMENT "nome do cliente",
  `nm_sexo` varchar(1) DEFAULT NULL COMMENT "genero do cliente. M, F ou I",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "data de criacao",
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT "data de atualizacao"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="Tabela de clientes";


INSERT INTO `tb_customer` (`id`, `nm_customer`, `nm_sexo`, `created_at`, `updated_at`) VALUES
(1, "FULANO DA SILVA", "M", "2022-02-09 23:17:21", NULL),
(2, "FULANA DA SILVA", "F", "2022-02-09 23:17:21", NULL),
(3, "FULAN DA SILVA", "I", "2022-02-09 23:17:21", NULL);


CREATE TABLE `tb_midia` (
  `id` int(11) NOT NULL COMMENT "id da midia",
  `nm_midia` varchar(50) NOT NULL COMMENT "tipo da midia (nome)",
  `nm_campanha` varchar(50) NOT NULL COMMENT "nome da campanha",
  `nm_fonte` varchar(50) NOT NULL COMMENT "nome da fonte",
  `nm_pagina` varchar(50) NOT NULL COMMENT "nome da pagina",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "data de criacao",
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT "data de atualizacao"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="Tabela de mídias";


INSERT INTO `tb_midia` (`id`, `nm_midia`, `nm_campanha`, `nm_fonte`, `nm_pagina`, `created_at`, `updated_at`) VALUES
(1, "WEB", "Promoção - Planos a partir de $0,99 por mês.", "MKT", "www.emergeit.com.br", "2022-02-09 23:20:22", NULL),
(2, "PORTAL SAUDE", "Campanha do Agasalho", "IE", "www.emergeit.com.br", "2022-02-09 23:20:22", NULL);


CREATE TABLE `tb_project` (
  `id` int(11) NOT NULL COMMENT "id do projeto",
  `nm_project` varchar(50) NOT NULL COMMENT "nome do projeto",
  `st_project` int(11) NOT NULL DEFAULT "1" COMMENT "status do projeto. 1=ativo, 0=inativo",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "data de criacao",
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT "data de atualizacao"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="Tabela de tipos de atendimento" ROW_FORMAT=DYNAMIC;


INSERT INTO `tb_project` (`id`, `nm_project`, `st_project`, `created_at`, `updated_at`) VALUES
(1, "ATENDIMENTO_HOSP_A", 1, "2022-02-09 23:21:48", NULL),
(2, "ATENDIMENTO_HOSP_B", 1, "2022-02-09 23:21:48", NULL),
(3, "ATENDIMENTO_CLINICA_A", 1, "2022-02-09 23:21:48", NULL),
(4, "ATENDIMENTO_CLINICA_B", 1, "2022-02-09 23:21:48", NULL);


CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL COMMENT "id do usuario",
  `nm_user` varchar(255) NOT NULL COMMENT "nome abreviado do usuario",
  `nm_completo` varchar(255) NOT NULL COMMENT "nome completo do usuario",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "data de criacao",
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT "data de atualizacao"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="Tabela de clientes" ROW_FORMAT=DYNAMIC;


INSERT INTO `tb_user` (`id`, `nm_user`, `nm_completo`, `created_at`, `updated_at`) VALUES
(1, "bruno.farias", "Bruno Cardoso Farias", "2022-02-09 23:22:21", NULL),
(2, "teste.silva", "Teste da Silva", "2022-02-09 23:59:18", NULL);


DROP TABLE IF EXISTS `num_at_not_recept_monthly_by_midia`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `num_at_not_recept_monthly_by_midia`  AS SELECT date_format(`c`.`created_at`,"%Y-%m") AS `created_at`, `mid`.`nm_midia` AS `nm_midia`, count(0) AS `qtd_ligacoes` FROM ((`tb_call` `c` join `tb_midia` `mid` on((`c`.`midia_id` = `mid`.`id`))) join `tb_call_tipo` `ct` on((`c`.`tipo_id` = `ct`.`id`))) WHERE (`ct`.`nm_tipo` <> "ENTRADA") GROUP BY date_format(`c`.`created_at`,"%Y-%m"), `mid`.`nm_midia`;

DROP TABLE IF EXISTS `num_at_recept_daily_by_status_by_media`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `num_at_recept_daily_by_status_by_media`  AS SELECT date_format(`c`.`created_at`,"%Y-%m-%d") AS `created_at`, `cs`.`nm_status` AS `nm_status`, `mid`.`nm_midia` AS `nm_midia`, count(0) AS `qtd_ligacoes` FROM (((`tb_call` `c` join `tb_call_status` `cs` on((`c`.`status_id` = `cs`.`id`))) join `tb_midia` `mid` on((`c`.`midia_id` = `mid`.`id`))) join `tb_call_tipo` `ct` on((`c`.`tipo_id` = `ct`.`id`))) WHERE (`ct`.`nm_tipo` = "ENTRADA") GROUP BY date_format(`c`.`created_at`,"%Y-%m-%d"), `cs`.`nm_status`, `mid`.`nm_midia`;

ALTER TABLE `tb_call`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_midia_id` (`midia_id`),
  ADD KEY `fk_user_id` (`user_id`),
  ADD KEY `fk_customer_id` (`customer_id`),
  ADD KEY `fk_tipo_id` (`tipo_id`),
  ADD KEY `fk_project_id` (`project_id`),
  ADD KEY `fk_status_id` (`status_id`);


ALTER TABLE `tb_call_status`
  ADD PRIMARY KEY (`id`) USING BTREE;

ALTER TABLE `tb_call_tipo`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tb_customer`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tb_midia`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tb_project`
  ADD PRIMARY KEY (`id`) USING BTREE;

ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`id`) USING BTREE;

ALTER TABLE `tb_call`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT "id da ligacao";

ALTER TABLE `tb_call_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT "id status ligacao", AUTO_INCREMENT=5;

ALTER TABLE `tb_call_tipo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT "id do tipo da ligacao", AUTO_INCREMENT=4;

ALTER TABLE `tb_customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT "id do cliente", AUTO_INCREMENT=4;

ALTER TABLE `tb_midia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT "id da midia", AUTO_INCREMENT=3;

ALTER TABLE `tb_project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT "id do projeto", AUTO_INCREMENT=5;

ALTER TABLE `tb_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT "id do usuario", AUTO_INCREMENT=3;

ALTER TABLE `tb_call`
  ADD CONSTRAINT `fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `tb_customer` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_midia_id` FOREIGN KEY (`midia_id`) REFERENCES `tb_midia` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_project_id` FOREIGN KEY (`project_id`) REFERENCES `tb_project` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_status_id` FOREIGN KEY (`status_id`) REFERENCES `tb_call_status` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_tipo_id` FOREIGN KEY (`tipo_id`) REFERENCES `tb_call_tipo` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;