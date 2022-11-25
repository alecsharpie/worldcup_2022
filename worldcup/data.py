import pandas as pd

def get_fixtures():
    fix_df = pd.read_json(
        'https://fixturedownload.com/feed/json/fifa-world-cup-2022')
    return fix_df


def get_results():
    res_df = pd.read_csv(
        'https://raw.githubusercontent.com/martj42/international_results/master/results.csv'
    )
    return res_df


if __name__ == '__main__':
    print(get_fixtures())
    print(get_results())
