def apply_filters(df, year, region, category):
    return df[
        (df["Year"].isin(year)) &
        (df["Region"].isin(region)) &
        (df["Category"].isin(category))
    ]