from moviepy.editor import VideoFileClip

def convert_to_webm(input_file):
    try:
        # Charger le fichier vidéo
        clip = VideoFileClip(input_file)

        # Générer le nom de fichier de sortie avec l'extension .webm
        output_file = f"{input_file.rsplit('.', 1)[0]}.webm"

        # Convertir en WebM
        clip.write_videofile(output_file, codec="libvpx")

        print("Conversion terminée avec succès !")
        print(f"Fichier de sortie : {output_file}")

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

# Demander le nom du fichier d'entrée à l'utilisateur
input_file = input("Entrez le nom du fichier d'entrée : ")
convert_to_webm(input_file)