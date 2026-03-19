def ranking_score(row):
    return (
        0.5 * row['rating'] +
        0.3 * row['popularity'] +
        0.2 * int(row['price_bucket'])
    )
