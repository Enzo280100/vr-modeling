# VirtualLeap
Master Project @BSE
```
vr-modeling/
│
├── 📄 README.md
├── 📄 LICENSE
├── 📄 .gitignore
│
├── 📁 data/
│   ├── 📁 raw/              # Unmodified original data
│   ├── 📁 processed/        # Cleaned and ready-to-use data
│   └── 📄 data_description.md  # How data was collected, features, format, etc.
│
├── 📁 notebooks/
│   ├── 📄 01_data_exploration.ipynb
│   ├── 📄 02_preprocessing.ipynb
│   ├── 📄 03_modeling.ipynb
│   ├── 📄 04_evaluation.ipynb
│   └── 📄 05_final_model_export.ipynb
│
├── 📁 src/
│   ├── 📄 __init__.py
│   ├── 📁 data_preprocessing/
│   │   └── 📄 preprocessing.py
│   ├── 📁 modeling/
│   │   └── 📄 model_trainer.py
│   ├── 📁 evaluation/
│   │   └── 📄 metrics.py
│   └── 📁 utils/
│       └── 📄 helpers.py
│
├── 📁 models/
│   ├── 📄 best_model.pkl         # Saved model files
│   └── 📄 model_card.md          # Description of model, inputs, outputs, performance
│
├── 📁 results/
│   ├── 📁 plots/
│   └── 📁 reports/
│       └── 📄 evaluation_report.md
│
├── 📁 vr_assets/                # Optional: 3D assets, VR scenes or metadata if needed
│   └── 📁 models/               # Blender/Unity/FBX or GLTF models
│
├── 📁 deployment/
│   ├── 📄 inference_pipeline.py   # Final script for running the model
│   └── 📄 README.md               # Instructions for deploying the model (API, VR integration)
│
└── 📄 requirements.txt
```
