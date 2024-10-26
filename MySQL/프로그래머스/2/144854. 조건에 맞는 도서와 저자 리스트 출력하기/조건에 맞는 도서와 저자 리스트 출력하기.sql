select
    book_id,
    author_name,
    left(published_date, 10) published_date
from book b
join author a on b.author_id = a.author_id
where category like '경제'
order by 3