# PoetGPT – Romanian Poetry Generation with Style Control

## 📌 Overview

PoetGPT is a project focused on generating Romanian poetry using a dual-architecture approach that combines a fine-tuned generative model with a stylistic classifier.

The system is designed to generate poems in the style of specific Romanian authors and to automatically evaluate how well the generated text matches the intended style.

---

## 🧠 Architecture

The project uses a dual-model pipeline:

- **RoGPT2** – a fine-tuned generative language model for poem generation  
- **XLM-RoBERTa** – a stylistic classifier used to evaluate and enforce author-specific styles  

This combination allows both generation and validation of stylistic fidelity.

---

## 🎯 Objectives

- Generate poems in the style of six Romanian authors  
- Automatically evaluate stylistic accuracy
- Understand the realtion between styl, creativity and machine learning

---

## ⚙️ Methodology

The system includes:

- Prompt design experiments for better text generation  
- A classification-based evaluation pipeline  
- An ablation study on different classifier variants  

Additionally, handcrafted style vectors are integrated to improve stylistic accuracy.

---

## 📊 Results

- The system was evaluated both qualitatively and quantitatively  
- Results show that stylistic accuracy improves significantly when using handcrafted style vectors  
- The evaluation pipeline enables automated validation of generated content  

---

## ⚠️ Limitations

- Current NLP models still struggle with fully capturing creative expression  
- Stylistic imitation does not fully replicate human poetic depth  

---

## 🚀 Future Work

- Incorporating literary criticism into training data  
- Embedding cultural and contextual metadata  
- Improving creative coherence and expressiveness  

---

## 💡 Contribution

PoetGPT provides:

- A functional pipeline for style-controlled poetry generation  
- An evaluation framework based on style classification  
- Insights into the challenges of modeling creativity in NLP  

---

## 🛠️ Technologies Used

- Python  
- Transformers (Hugging Face)  
- RoGPT2  
- XLM-RoBERTa  

---

## 📎 Conclusion

This project explores the intersection of AI and creativity, contributing to the ongoing discussion about whether creativity can be modeled mathematically and how closely machines can emulate a poetic voice.
