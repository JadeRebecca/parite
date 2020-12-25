import os
import logging as lg
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns # Pimp my Matplotlib

class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        #Création de 2 dataframes, un contenant les hommes et l'autre les femmes
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        #Stockage du nombre de député de chaque sexe dans une variable
        counts = [ len(female_mps), len(male_mps)]
        #transformation de la liste simple en objet ndarray
        counts = np.array(counts)
        #nombre total de membre
        nb_mps = counts.sum()
        #création d'une nouvelle liste contenant les proportions
        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        #assurer que le diagramme ne sera pas elliptique
        ax.axis("equal")
    
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f pourcents"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()


    def split_by_political_party(self):
        result = {}
        data = self.dataframe
        #dropna supprime les valeurs nulles
        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party = False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join("data",data_file))
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()