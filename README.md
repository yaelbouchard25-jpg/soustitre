# 🎬 pycaps - Sous-titres automatiques avec emojis

Application web pour générer automatiquement des sous-titres animés mot-par-mot avec insertion contextuelle d'emojis.

## 🚀 Fonctionnalités

- ✅ Reconnaissance vocale multilingue (Whisper)
- ✅ Sous-titres animés mot par mot
- ✅ Emojis contextuels automatiques
- ✅ 5 styles préconçus (TikTok, YouTube, Neon, etc.)
- ✅ Format vertical 9:16 pour réseaux sociaux
- ✅ 100% gratuit et open-source

## 🛠️ Technologies

- [pycaps](https://github.com/francozanardi/pycaps) - Moteur de sous-titrage
- Gradio - Interface web
- Whisper - Reconnaissance vocale
- FFmpeg - Traitement vidéo

## 📝 Utilisation

1. Upload ta vidéo
2. Choisis un style
3. Active les emojis (recommandé)
4. Clique "Générer"
5. Télécharge ta vidéo sous-titrée !

## 🔗 Déployé sur Hugging Face Spaces

👉 [Utilise l'app ici](https://huggingface.co/spaces/TON_USERNAME/pycaps-subtitles-app)

## 📄 Licence

MIT - Libre d'utilisation
```

**Remplace `TON_USERNAME` par ton username Hugging Face** (tu le mettras à jour après le déploiement)

Clique **"Commit changes"**

---

## 🚀 ÉTAPE 3 : Créer le Space sur Hugging Face (3 min)

1. Va sur **huggingface.co/spaces**
2. Clique le bouton **"Create new Space"**

3. Remplis le formulaire :
   - **Space name** : `pycaps-subtitles-app`
   - **License** : Apache 2.0 (ou MIT)
   - **Select the Space SDK** : **Gradio**
   - **Visibility** : Public
   - **Space hardware** : **CPU basic** (gratuit) - tu pourras upgrader au GPU gratuit après

4. **NE clique PAS ENCORE "Create Space"**

5. Descends et trouve la section **"Link to a repository"**
   - Coche **"Import from existing repository"**
   - Entre l'URL de ton repo GitHub : `https://github.com/TON_USERNAME/pycaps-subtitles-app`

6. Maintenant clique **"Create Space"**

---

## ⚙️ ÉTAPE 4 : Activer le GPU gratuit (1 min)

1. Sur la page de ton Space, clique l'onglet **"Settings"** en haut

2. Dans la section **"Space hardware"**, clique sur le dropdown

3. Sélectionne **"T4 small"** (GPU gratuit)

4. Clique **"Request upgrade"** → Confirme

5. Le Space va redémarrer avec GPU (⚡ beaucoup plus rapide)

---

## ⏳ ÉTAPE 5 : Attendre le build (10-15 min)

Sur la page de ton Space, tu vas voir :
```
Building...
Installing requirements...
