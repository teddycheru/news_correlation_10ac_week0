-- Schema for the merged_data_traffic table
-- To answer top and bottom 10 Websites with the highest numbers of visitor traffic

CREATE TABLE merged_data_traffic (
    article_id SERIAL PRIMARY KEY,
    source_id TEXT,
    source_name TEXT,
    author TEXT,
    title TEXT,
    description TEXT,
    url TEXT,
    url_to_image TEXT,
    published_at TIMESTAMP,
    content TEXT,
    category TEXT,
    full_content TEXT,
    GlobalRank INTEGER,
    TldRank INTEGER,
    Domain TEXT,
    TLD TEXT,
    RefSubNets INTEGER,
    RefIPs INTEGER,
    IDN_Domain TEXT,
    IDN_TLD TEXT,
    PrevGlobalRank INTEGER,
    PrevTldRank INTEGER,
    PrevRefSubNets INTEGER,
    PrevRefIPs INTEGER
);