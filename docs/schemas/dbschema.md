-- Schema for data table

Table data {
  article_id SERIAL [primary key]
  source_id TEXT
  source_name TEXT
  author TEXT
  title TEXT
  description TEXT
  url TEXT
  url_to_image TEXT
  published_at TIMESTAMP
  content TEXT
  category TEXT
  full_content TEXT
}

-- Schema for traffic table

CREATE TABLE traffic (
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

-- Schema for rating table

CREATE TABLE rating (
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
    article TEXT,
    title_sentiment TEXT
);

-- Schema for raw table

CREATE TABLE raw_data (
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
    category TEXT
);

-- Schema for domains_location table

CREATE TABLE domains_location (
    SourceCommonName TEXT,
    location TEXT,
    Country TEXT
);