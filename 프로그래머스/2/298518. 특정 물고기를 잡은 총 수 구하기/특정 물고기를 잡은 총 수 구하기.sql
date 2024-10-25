-- 코드를 작성해주세요
select count(1) FISH_COUNT
from fish_info info
join fish_name_info name on info.fish_type = name.fish_type
where name.fish_name like "BASS" or name.fish_name like "SNAPPER"