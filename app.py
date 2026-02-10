import gradio as gr
import subprocess
import os
import shutil

def process_video(video_file, template, enable_emojis, vertical_format):
    """Traite une vidéo avec pycaps"""

    if video_file is None:
        return None, "❌ Merci d'uploader une vidéo"

    # Crée un dossier de travail temporaire
    os.makedirs("temp", exist_ok=True)

    # Nom du fichier d'entrée
    input_path = "temp/input_video.mp4"

    # Copie la vidéo uploadée
    shutil.copy(video_file, input_path)

    # Construit la commande pycaps
    cmd = [
        "pycaps", "render",
        "--input", input_path,
        "--template", template,
        "--output", "temp/"
    ]

    # Ajoute les emojis si demandé
    if enable_emojis:
        cmd.extend(["--enable-emojis"])

    # Ajoute le format vertical si demandé
    if vertical_format:
        cmd.extend(["--aspect-ratio", "9:16"])

    try:
        # Lance pycaps
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            timeout=600  # Timeout 10 minutes
        )

        # Cherche le fichier de sortie
        output_path = "temp/input_video_subtitled.mp4"

        if os.path.exists(output_path):
            return output_path, "✅ Vidéo traitée avec succès !"
        else:
            return None, "❌ Erreur : fichier de sortie introuvable"

    except subprocess.TimeoutExpired:
        return None, "⏱️ Timeout : la vidéo est trop longue (max 10 min)"
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else str(e)
        return None, f"❌ Erreur pycaps : {error_msg}"
    except Exception as e:
        return None, f"❌ Erreur inattendue : {str(e)}"

# Interface Gradio
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 🎬 pycaps - Sous-titres automatiques avec emojis

    Upload ta vidéo, choisis un style, et télécharge-la avec des sous-titres animés mot par mot + emojis contextuels !

    ⚡ Propulsé par Whisper (reconnaissance vocale) + pycaps (animations)
    """)

    with gr.Row():
        with gr.Column():
            video_input = gr.Video(
                label="📹 Upload ta vidéo",
                sources=["upload"]
            )

            template_input = gr.Dropdown(
                choices=[
                    "tiktok_style",
                    "minimalist",
                    "youtube_classic",
                    "neon",
                    "elegant"
                ],
                value="tiktok_style",
                label="🎨 Style de sous-titres",
                info="TikTok style recommandé pour les réseaux sociaux"
            )

            with gr.Row():
                emojis_input = gr.Checkbox(
                    label="😀 Emojis automatiques",
                    value=True,
                    info="Ajoute des emojis pertinents selon le contexte"
                )

                vertical_input = gr.Checkbox(
                    label="📱 Format vertical 9:16",
                    value=False,
                    info="Pour TikTok/Reels/Shorts"
                )

            process_btn = gr.Button("🚀 Générer les sous-titres", variant="primary", size="lg")

        with gr.Column():
            video_output = gr.Video(label="✅ Vidéo sous-titrée")
            status_output = gr.Textbox(label="Status", lines=2)

    # Exemples
    gr.Markdown("### 📝 Exemples de styles")
    gr.Markdown("""
    - **TikTok Style** : Gros texte, animations pop, parfait pour réseaux sociaux
    - **Minimalist** : Sobre, blanc sur fond noir, style Netflix
    - **YouTube Classic** : Texte classique avec bordure noire
    - **Neon** : Style cyberpunk avec effet néon
    - **Elegant** : Serif raffiné pour contenu premium
    """)

    # Connecte le bouton
    process_btn.click(
        fn=process_video,
        inputs=[video_input, template_input, emojis_input, vertical_input],
        outputs=[video_output, status_output]
    )

# Lance l'app
if __name__ == "__main__":
    demo.launch()
