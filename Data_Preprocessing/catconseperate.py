def catconsep(df):
    cat = list(df.columns[df.dtypes=="object"])
    con = list(df.columns[df.dtypes!="object"])
    return cat,con

def replacer(df):
    cat, con = catconsep(df)
    for i in df.columns:
        if i in cat:
            md = df[i].mode()[0]
            df[i] = df[i].fillna(md)
        else:
            mn = df[i].mean()
            df[i] = df[i].fillna(mn)
    print('Missing Values replaced with mode and median')

        
