import pandas
import utils
import monkey_model

def read_monkeys_from_csv(csv_path):
    df = pandas.read_csv(csv_path)

    if list(df.columns.values) != ['species', 'size', 'weight', 'color']:
        return ValueError

    df['monkey'] = ''
    df['bmi'] = 0.0
    df['fur_color_int'] = 0

    for i in range(len(df)):

        if (df['size'][i]<=0) or (df['weight'][i]<=0) or (not(utils.check_hexacolor(str(df['color'][i])))):

           df = df.drop([i])

        else:

            monkey = monkey_model.Monkey(df['color'][i], df['size'][i], df['weight'][i], df['species'][i])
            df['monkey'][i] = monkey
            df['bmi'][i] = monkey.compute_bmi()
            df['fur_color_int'][i] = int('0x'+monkey.fur_color[1:], 16)

    df = df.dropna()
    return df

path = r'E:\编程文件\python\Uni Lorraine\NLPLab\lab9_10\monkeys.csv'
df = read_monkeys_from_csv(path)
print(df['monkey'][1].size)

def compute_knn(dataframe, k=5):
    pass
