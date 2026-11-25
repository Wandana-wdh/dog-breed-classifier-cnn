# Dog Breed Classifier using Pre-trained CNNs

Classifies pet images using three pre-trained convolutional neural networks (**ResNet**, **AlexNet** and **VGG**) to:

1. Identify which images are of dogs and which are not
2. Identify the breed of each dog image

The three architectures are compared on accuracy and runtime to find the best model for the task.

Project from the Udacity **Future AWS AI Programmer** program (*Introduction to Python for AI Programmers*).

## How It Works

| Step | File | What it does |
|---|---|---|
| 1 | `get_input_args.py` | Reads command-line arguments (`--dir`, `--arch`, `--dogfile`) |
| 2 | `get_pet_labels.py` | Creates the true labels from image filenames (e.g. `Golden_retriever_05182.jpg` → `golden retriever`) |
| 3 | `classify_images.py` | Classifies each image with the chosen CNN and compares it with the true label |
| 4 | `adjust_results4_isadog.py` | Uses `dognames.txt` to mark whether each label is a dog |
| 5 | `calculates_results_stats.py` | Calculates counts and accuracy percentages |
| 6 | `print_results.py` | Prints the summary and any misclassifications |
| — | `check_images.py` | Main program that runs all the steps and times the run |

## Usage

Requirements: Python 3, PyTorch, torchvision, Pillow

```bash
pip install -r requirements.txt
```

Run with a single model:

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

Run all three models and save the results to text files:

```bash
sh run_models_batch.sh
sh run_models_batch_uploaded.sh
```

## Results: Pet Images (40 images: 30 dogs, 10 not dogs)

| Model | % Not-a-Dog Correct | % Dogs Correct | % Breeds Correct | % Match Labels | Runtime |
|---|---|---|---|---|---|
| ResNet | 90.0 | 100.0 | 90.0 | 82.5 | 6 s |
| AlexNet | 100.0 | 100.0 | 80.0 | 75.0 | 2 s |
| **VGG** | **100.0** | **100.0** | **93.3** | **87.5** | 19 s |

**VGG is the best model overall.** It is the only architecture that scored 100% on both dog and not-dog images and also had the highest breed accuracy (93.3%). The trade-off is speed: VGG was about 10× slower than AlexNet.

Notable misclassifications:
- ResNet labelled a cat as a Norwegian elkhound (its only dog/not-dog error).
- All three models confused a Great Pyrenees with a kuvasz and a beagle with a walker hound, both pairs of very similar-looking breeds.

## Results: Uploaded Images

Four of my own images were tested: a golden retriever (`Dog_01.jpg`), the same image flipped horizontally (`Dog_02.jpg`), an elephant (`Tusker_01.jpg`) and a coffee mug (`Coffee_mug_01.jpg`).

| Image | ResNet | AlexNet | VGG |
|---|---|---|---|
| Dog_01.jpg | golden retriever ✅ | golden retriever ✅ | clumber spaniel ❌ |
| Dog_02.jpg (flipped) | golden retriever ✅ | standard poodle ❌ | golden retriever ✅ |
| Tusker_01.jpg | tusker ✅ | tusker ✅ | indian elephant (not a dog ✅) |
| Coffee_mug_01.jpg | coffee mug ✅ | cup (not a dog ✅) | espresso (not a dog ✅) |

All three models correctly separated dogs from not-dogs. **ResNet performed best on the uploaded images.** It was the only model that identified the golden retriever correctly in both the original and the flipped image, and it matched every label exactly.

## Project Structure

```
├── check_images.py
├── get_input_args.py
├── get_pet_labels.py
├── classify_images.py
├── adjust_results4_isadog.py
├── calculates_results_stats.py
├── print_results.py
├── classifier.py
├── test_classifier.py
├── print_functions_for_lab_checks.py
├── dognames.txt
├── imagenet1000_clsid_to_human.txt
├── run_models_batch.sh
├── run_models_batch_uploaded.sh
├── check_images.txt
├── pet_images/
├── uploaded_images/
└── results/  (*_pet-images.txt, *_uploaded-images.txt)
```

## What I Learned

- Using pre-trained ImageNet models from torchvision for inference (transfer learning without retraining)
- Designing and processing compound data structures (dictionaries of lists) in Python
- Comparing model architectures on accuracy and computational cost
- Command-line arguments, file I/O, batch processing with shell scripts and timing code

## Acknowledgements

Starter code (`classifier.py`, `test_classifier.py`, `print_functions_for_lab_checks.py`, `dognames.txt`, the batch scripts and the `pet_images` dataset) was provided by [Udacity](https://github.com/udacity/AIPND-revision). I implemented the functions in `check_images.py`, `get_input_args.py`, `get_pet_labels.py`, `classify_images.py`, `adjust_results4_isadog.py`, `calculates_results_stats.py` and `print_results.py`.

**Author:** Wandana
