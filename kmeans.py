import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
from argparse import ArgumentParser
from sklearn.decomposition import PCA

def verify_arguments():
    parser = ArgumentParser()
    parser.add_argument('-f', '--csv', help='csv file')
    parser.add_argument('-d', '--dummy', help='dummy column')
    parser.add_argument('-c', '--columns', help='columns to be analyzed by the kmeans algorithm')
    parser.add_argument('-k', '--kmeans', help='number of kmeans clusters')
    parser.add_argument('-o', '--output', help='output csv file')

    args = vars(parser.parse_args())

    if None in args.values():
        parser.print_help()
        exit()

    return args


def main():
    args = verify_arguments()

    CSV = args['csv'] # Ex: animals.csv
    DUMMY = args['dummy'] # Ex: Animal
    COLUMNS = [s.strip() for s in args['columns'].split(',')] # Ex: "Small, Medium, Big, Two Legs, Four Legs, Hair, Hooves, Mane, Feathers, Hunt, Run, Fly, Swim"
    KMEANS = int(args['kmeans'])
    OUTPUT = args['output']

    df = pd.read_csv(CSV, sep=',')
    #Make a copy of DF
    df_tr = df

    #Transsform the dummy column
    df_tr = pd.get_dummies(df_tr, columns=[DUMMY])

    #Standardize
    clmns = [DUMMY+'_'+a for a in df[DUMMY]]
    clmns = clmns+COLUMNS

    df_tr_std = stats.zscore(df_tr[clmns])

    #Cluster the data
    kmeans = KMeans(n_clusters=KMEANS, random_state=0).fit(df_tr_std)
    labels = kmeans.labels_

    #Glue back to originaal data
    df_tr['clusters'] = labels

    #Add the column into our list
    clmns.extend(['clusters'])

    #Lets analyze the clusters
    df_tr[clmns].groupby(['clusters']).mean().to_csv(
        OUTPUT, sep=',', encoding='utf-8')

if __name__ == '__main__':
    main()
