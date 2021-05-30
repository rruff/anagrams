create table if not exists words (
    id integer primary key,
    word text not null,
    sortedword text not null
);

create index if not exists idx_words_sorted on words (sortedword);