from moviepy.editor import VideoFileClip

class VideoConverter:
    def __init__(self):
        self.codec_mapping = {
            "webm": "libvpx",
            "avi": "rawvideo",
            "mp4": "libx264",
            "gif": None,  # Pas de codec spécifique pour les GIFs
            "mov": "libx264",
            "flv": "flv",
            "mkv": "libx264",
            "wmv": "wmv2",
            "mpg": "mpeg1video",
            "3gp": "h263",
            "ogg": "libtheora",
            "m4v": "libx264"
            # Ajoutez d'autres formats et codecs si nécessaire
        }

    def convert_to_format(self, input_file, output_format):
        try:
            # Charger le fichier vidéo
            clip = VideoFileClip(input_file)

            # Extraire l'extension de fichier à partir du format de sortie
            output_extension = output_format.lower()

            # Vérifier si le format de sortie est pris en charge
            if output_extension not in self.codec_mapping:
                raise ValueError("Format de sortie non pris en charge.")

            # Générer le chemin de fichier de sortie avec l'extension appropriée
            output_file = f"{input_file.rsplit('.', maxsplit=1)[0]}.{output_extension}"

            # Convertir en format spécifié
            if output_extension == "gif":
                clip.write_gif(output_file)
            else:
                codec = self.codec_mapping[output_extension]
                clip.write_videofile(output_file, codec=codec)

            print("Conversion terminée avec succès !")
            print(f"Fichier de sortie : {output_file}")

        except FileNotFoundError:
            print("Le fichier d'entrée spécifié est introuvable.")
        except ValueError as e:
            print(str(e))
        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")

# Créer une instance de la classe VideoConverter
converter = VideoConverter()

# Afficher les formats disponibles à l'utilisateur
print("Formats de sortie disponibles :")
for output_format in converter.codec_mapping.keys():
    print(output_format)

# Demander le nom du fichier d'entrée à l'utilisateur
input_file = input("Entrez le nom du fichier d'entrée : ")

# Demander le format de sortie à l'utilisateur
output_format = input("Choisissez le format de sortie : ")

# Appeler la méthode de conversion de format
converter.convert_to_format(input_file, output_format)
