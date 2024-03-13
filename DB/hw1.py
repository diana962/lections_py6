# 1. Найдите 10 самых часто встречающихся слов.
# shakespeare_db=# SELECT plaintext FROM wordform order by occurences desc limit 10;

# Answer:
#  plaintext 
# -----------
#  the
#  and
#  i
#  to
#  of
#  a
#  you
#  my
#  in
#  that
# (10 rows)

# 2. Найдите все слова, которые начинаются с буквы 'а', регистр не должен иметь значения.
# SELECT plaintext FROM wordform where plaintext like '%a%'

# Answer: got it

# 3. Найдите все произведения, которые относятся к жанру 'р'.
# SELECT title FROM work where genretype ilike 'p'

# Answer: got it

# 4. Найдите среднее количество параграфов в произведения жанра t'.

# select * from work;
# SELECT AVG(totalparagraphs) AS avg_paragraphs FROM work WHERE genretype = 't';

# Answer: 1070.81

# 5. Выведите все произведения, в которых количество слов выше среднего.
# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);

# Answer: 28 произведений

# 6. Выведите имя героя, количество его реплик, и произведение, в котором этот герой встречается.
# SELECT c.charname, c.speechcount, w.title FROM character c 
# JOIN character_work cw ON c.charid = cw.charid
# JOIN work w ON cw.workid = w.workid LIMIT 100

# Answer: got it

# 7. Выведите среднее количество реплик героев в произведении 'Romeo and Juliet'.
# SELECT AVG(c.speechcount) AS avg_speechcount FROM character c
# JOIN character_work cw ON c.charid = cw.charid
# JOIN work w ON cw.workid = w.workid
# WHERE w.title = 'Romeo and Juliet';

# Answer: 25.54

# 8. Выведите общее количество слов в каждой из секций в таблице paragraph.
# SELECT section, SUM(wordcount) AS total_words FROM paragraph GROUP BY section;

# Answer: got it

# 9. Выведите всех героев, которые имеют от 15 до 30 реплик.
# SELECT * FROM character WHERE speechcount BETWEEN 15 AND 30;

# Answer: got it

# 10. Выведите все произведения, которые были написаны в 17 веке
# SELECT * FROM work WHERE year BETWEEN 1601 AND 1700;
# Answer: got it

# 11. Найдите все произведения, которые имею в полном названии слово 'the'
# SELECT * FROM work WHERE LOWER(longtitle) LIKE '%the%';

# Answer: got it

# 12. Выведите все уникальные секции в paragraph.
# select distinct section from paragraph

# Answer: got it

# 13. Для каждой главы введите: id, описание и название прозведения, к которой относится данная глава.
# SELECT ch.chapterid, ch.description, w.title FROM chapter ch
# JOIN work w ON ch.workid = w.workid;

# Answer: got it

# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя

# SELECT p.paragraphnum, c.charname, c.speechcount FROM paragraph p
# JOIN "character" c ON p.charid = c.charid;

# Answer: got it

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и год выхода этого произведения.

# SELECT p.paragraphnum, w.title, w.year FROM paragraph p
# JOIN work w ON p.workid = w.workid;

# Answer: got it



# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100

# SELECT longtitle FROM work where source like 'Moby' and totalparagraphs < 100;

# 2. Найти кол-во глав в каждом произведении
# SELECT w.title, SUM(c.chapter) FROM work w
# JOIN chapter c ON w.workid = c.workid
# GROUP BY title 

# # 3. Найти сколько произведений относятся к каждому жанру?
# SELECT genretype, STRING_AGG(title, ', ') as title FROM work GROUP BY genretype LIMIT 100


# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений
# SELECT title, totalparagraphs FROM work LIMIT 100

# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания
# SELECT c.charname, w.title, w.genretype, w.year FROM character c 
# JOIN character_work cw on c.charid = cw.charid
# RIGHT JOIN work w on w.workid = cw.workid WHERE c.speechcount > 200 ORDER BY c.speechcount DESC LIMIT 100


# 6. Вытащить героя, который чаще всех появляется в произведениях
# SELECT c.charname FROM character c 
# JOIN paragraph p on c.charid = p.charid
# WHERE p.charcount > 0 ORDER BY p.charcount DESC

# with CharacterAppearances as (select w.title, c.charname, sum(p.charcount) as totalappearance
#                               from paragraph p
#                                   join character c  on c.charid = p.charid
#                                   join work w on w.workid = p.workid
#                               group by w.title, c.charname order by c.charname)
# SELECT title, charname, max(totalappearance) as app
# FROM CharacterAppearances
# where totalappearance in (select  max(totalappearance) from CharacterAppearances group by title)
# group by title, charname;


# SELECT c.charname, w.title, p.charcount FROM character c
# JOIN paragraph p ON c.charid = p.charid
# JOIN work w ON w.workid = p.workid
# WHERE p.charcount > 0 ORDER BY p.charcount DESC
