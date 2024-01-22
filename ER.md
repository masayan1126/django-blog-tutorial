- 記事とタグ
  - 多対多
- 記事と著者
  - 多対一
  - 個人ブログのため、1記事に対して著者は1人
- 記事とコメント
  - 一対多
- 記事とSEOメタ情報
  - 一対一

```mermaid
erDiagram
    Article o{--|| Author : ""
    Article ||--o{ Comment : ""
    Article |{--|{ Tag : ""
    Article ||--|| ArticleMeta : ""

    Article {
        bigint id PK "ID"
        varchar title "Title"
        text content "Content"
        timestamp created_at "Created At"
        timestamp updated_at "Updated At"
    }

    ArticleMeta {
        bigint article_id FK "Article ID:Article.id"
        varchar meta_title "MetaTitle"
        varchar meta_description "MetaDescription"
    }

    Author {
        bigint id PK "ID"
        varchar name "Name"
        bigint article_id FK "Article ID:Article.id"
    }

    Comment {
        bigint id PK "ID"
        text content "Content"
        bigint article_id FK "Article ID:Article.id"
        timestamp created_at "Created At"
        timestamp updated_at "Updated At"
    }

    Tag {
        bigint id PK "ID"
        varchar name "Name"
    }

    Article_Tag {
        bigint article_id FK "Article ID:Article.id"
        bigint tag_id FK "Tag ID:Tag.id"
    }