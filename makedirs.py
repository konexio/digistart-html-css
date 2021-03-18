import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Creation des dossiers d\'une session digistart')
parser.add_argument('session', help="Session dans laquel créer les dossiers")

args = parser.parse_args()

apprenants = [
    "Alkher_KHALIL",
    "Amina_SY",
    "Axel_Melezan",
    "Axel_Siepak",
    "Kadidia_Niakate",
    "Nissaf_Abed",
    "Sandro_Tsang",
    "Tenzin_norzom",
    "Yves_Nelien"
]


apprenants.append("Konexio")

if not os.path.isdir(args.session):
    print("La session indiquée n'existe pas")
elif os.path.isdir("tmp"):
    print("Le dossier tmp doit être inexistant pour pouvoir utiliser ce script!")
else:
    shutil.move(args.session, "tmp")

    for n in apprenants:
        # os.mkdir(os.path.join(args.session, n))
        shutil.copytree("tmp", os.path.join(args.session, n))
    shutil.rmtree("tmp")