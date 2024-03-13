SELECT 
  c.pacient_id AS "pacient_id",
  c.fio_pacient AS "fio",
  CASE
    WHEN c."SexNew" = 1 THEN 'Муж.'
    WHEN c."SexNew" = 0 THEN 'Жен.'
  END AS "sex",
  TO_CHAR(c.date_of_birth, 'DD-MM-YYYY') AS "born_date",
  TO_CHAR(za."DateResultReady", 'DD-MM-YYYY') AS "analiz_data",
  MAX(zp.result) FILTER (WHERE spa.nameid = 'Тиреотропный гормон ТТГ') AS "ТТГ",
  MAX(zp.result) FILTER (WHERE spa.nameid = 'Общий Т3 (Total T3)') AS "Общий Т3",
  MAX(zp.result) FILTER (WHERE spa.nameid = 'Свободный Т3') AS "Свободный Т3",
  MAX(zp.result) FILTER (WHERE spa.nameid = 'Общий Т4 (Total T4)') AS "Общий Т4",
  MAX(zp.result) FILTER (WHERE spa.nameid = 'Свободный Т4') AS "Свободный Т4"
FROM zakazy z
JOIN clients c ON c.pacient_id = z.client_id
JOIN zakazy_analiz za ON z.codeid = za.codeid_zakazy
JOIN zakazy_podanaliz zp ON za.codeid = zp.codeid_analiz
JOIN sp_podanaliz zpp ON zp.codeid_podanaliz = zpp.codeid
JOIN sp_analiz spa ON spa.codeid = za.codeid_spanaliz
WHERE zp.result != ''
  AND c.date_of_birth >= '19920101'
  AND c.date_of_birth < '20061231'
  AND za.codeid_spanaliz IN (528, 530, 471, 531, 472)
  AND z.date_reg >= '20210501'
  AND z.date_reg <= '20220531'
GROUP BY pacient_id, fio, sex, born_date, analiz_data
ORDER BY c.fio_pacient;

DECLARE @from DATETIME, @to DATETIME;
SET @from = '{0}';
SET @to = '{1}';

SELECT
  sg.nameid AS 'Группа',
  sa.nameid AS 'Исследование',
  sl.login AS 'Логин',
  sl.nameid + ' ' + lastName AS 'ФИО Регистратора',
  sp.nameid AS 'Пункт',
  sr.nameid AS 'Регион',
  CASE
    WHEN z.IdPayer IS NOT NULL AND z.IdPayer NOT LIKE '%ГОБМП%' THEN 'КК'
    ELSE CASE
      WHEN za.DoctorId IS NOT NULL THEN 'ВП'
      WHEN z.IdPayer IS NOT NULL AND z.IdPayer LIKE '%ГОБМП%' THEN 'ГОБМП'
      ELSE 'Улица'
    END
  END AS 'Структура',
  COUNT(za.codeid) AS 'Кол-во',
  SUM(za.PriceInOrder - za.DiscountAmount) AS 'Сумма',
  CASE
    WHEN CHARINDEX('ППФ', sp.nameid) > 0 THEN 'Франшиза'
    ELSE 'Собственный'
  END AS 'Тип пункта',
  CASE
    WHEN sa.codeid IN (7365, 7420, 7421, 7631, 7634, 7650, 7637, 7581, 7405, 7372, 7365, 7631, 7421, 7650, 7420, 7373, 7409, 7410, 7415, 7626, 7406, 7581) THEN 'ПЦР Ковид'
    ELSE 'Другие'
  END AS 'Тип исследования',
  'Общее' AS 'Вид продажи'
FROM zakazy AS z
INNER JOIN zakazy_analiz za ON z.codeid = za.codeid_zakazy AND za.codeid_paket IS NULL
INNER JOIN sp_login sl ON z.codeid_login = sl.codeid
INNER JOIN sp_punkt sp ON z.codeid_punkt = sp.codeid
INNER JOIN sp_region sr ON sp.codeid_region = sr.codeid
INNER JOIN sp_analiz sa ON za.codeid_spanaliz = sa.codeid
INNER JOIN sp_gruppa_result sgr ON sa.IdSubGroup = sgr.codeid
INNER JOIN sp_gruppa sg ON sgr.fid_research_group = sg.codeid
WHERE z.date_reg >= @from AND z.date_reg <= @to
  AND za.typeid IN (0, 1)
  AND za.codeid_spanaliz != -1
  AND z.status != 2
  AND za.Status NOT IN (11, 13)
GROUP BY sg.nameid, sa.nameid, sl.login, sl.nameid, sl.LastName, sp.nameid, sr.nameid, z.IdPayer, za.DoctorId, sa.codeid
UNION ALL
SELECT
  'Пакеты' AS 'Группа',
    -- Продолжение для 'Пакеты'
  sa.nameid AS 'Исследование',
  sl.login AS 'Логин',
  sl.nameid + ' ' + lastName AS 'ФИО Регистратора',
  sp.nameid AS 'Пункт',
  sr.nameid AS 'Регион',
  CASE
    WHEN z.IdPayer IS NOT NULL AND z.IdPayer NOT LIKE '%ГОБМП%' THEN 'КК'
    ELSE CASE
      WHEN za.DoctorId IS NOT NULL THEN 'ВП'
      WHEN z.IdPayer IS NOT NULL AND z.IdPayer LIKE '%ГОБМП%' THEN 'ГОБМП'
      ELSE 'Улица'
    END
  END AS 'Структура',
  COUNT(za.codeid) AS 'Кол-во',
  SUM(za.PriceInOrder - za.DiscountAmount) AS 'Сумма',
  CASE
    WHEN CHARINDEX('ППФ', sp.nameid) > 0 THEN 'Франшиза'
    ELSE 'Собственный'
  END AS 'Тип пункта',
  'Другие' AS 'Тип Исследования',
  CASE
    WHEN sa.codeid IN (313, 314, 315, 316, 317) THEN 'Доп продажа'
    ELSE 'Общее'
  END AS 'Вид продажи'
FROM zakazy AS z
INNER JOIN zakazy_paket za ON z.codeid = za.codeid_zakazy
INNER JOIN sp_login sl ON z.codeid_login = sl.codeid
INNER JOIN sp_punkt sp ON z.codeid_punkt = sp.codeid
INNER JOIN sp_region sr ON sp.codeid_region = sr.codeid
INNER JOIN sp_paket sa ON za.codeid_paket = sa.codeid
WHERE z.date_reg >= @from AND z.date_reg <= @to
  AND z.status != 2
GROUP BY sa.nameid, sl.login, sl.nameid, sp.nameid, sr.nameid, sl.LastName, z.IdPayer, za.DoctorId, sa.codeid

UNION ALL

SELECT
  'Доп услуги' AS 'Группа',
  sa.nameid AS 'Исследование',
  sl.login AS 'Логин',
  sl.nameid + ' ' + lastName AS 'ФИО Регистратора',
  sp.nameid AS 'Пункт',
  sr.nameid AS 'Регион',
  CASE
    WHEN z.IdPayer IS NOT NULL AND z.IdPayer NOT LIKE '%ГОБМП%' THEN 'КК'
    ELSE CASE
      WHEN za.DoctorId IS NOT NULL THEN 'ВП'
      WHEN z.IdPayer IS NOT NULL AND z.IdPayer LIKE '%ГОБМП%' THEN 'ГОБМП'
      ELSE 'Улица'
    END
  END AS 'Структура',
  SUM(za.quantity) AS 'Кол-во',
  SUM(za.PriceInOrder - za.DiscountAmount) AS 'Сумма',
  CASE
    WHEN CHARINDEX('ППФ', sp.nameid) > 0 THEN 'Франшиза'
    ELSE 'Собственный'
  END AS 'Тип пункта',
  'Другие' AS 'Тип Исследования',
  'Общее' AS 'Вид продажи'
FROM zakazy AS z
INNER JOIN zakazy_zabor za ON z.codeid = za.codeid_zakazy
INNER JOIN sp_login sl ON z.codeid_login = sl.codeid
INNER JOIN sp_punkt sp ON z.codeid_punkt = sp.codeid
INNER JOIN sp_region sr ON sp.codeid_region = sr.codeid
INNER JOIN sp_zakazy_zabor sa ON za.codeid_spzakazy_zabor = sa.codeid
WHERE z.date_reg >= @from AND z.date_reg <= @to
  AND z.status != 2
GROUP BY sa.nameid, sl.login, sl.nameid, sp.nameid, sr.nameid, sl.LastName, z.IdPayer, za.DoctorId, sa.codeid

