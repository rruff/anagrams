create table if not exists words (
    id integer primary key,
    word text not null
);

-- Match words to their anagrams by doing a many-to-many self-join --
create table if not exists word_anagrams_join (
    word_id integer not null,
    anagram_word_id integer not null
);
