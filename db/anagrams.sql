create table if not exists words (
    id integer primary key,
    word text not null
);

create table if not exists anagrams (
    id integer primary key,
    word_id integer not null,
    anagram text not null
);
