# <center>Reinforcement Learning with Human Feedback: InstructGPT<center/>

This project implements a reinforcement learning-based dialog agent using the Proximal Policy Optimization (PPO) algorithm. The agent generates responses to given input sequences using a pre-trained GPT-2 language model and is trained using PPO to maximize its expected reward. 

## Requirements

- Python 3.7 or higher
- PyTorch 1.8 or higher
- Transformers 4.5 or higher
- Pandas 1.2 or higher
- NumPy 1.19 or higher
- tqdm 4.60 or higher

## Dataset

The project uses the IMDB movie review dataset, which can be downloaded from [here](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews). The dataset should be preprocessed to remove any reviews longer than 1000 characters and to keep the first 10,000 reviews.

## Usage

1. Clone the repository and navigate to the project directory.
2. Install the dependencies listed in `requirements.txt`.
3. Preprocess the IMDB dataset as described above.
4. Load the preprocessed dataset using the `IMDBDataset` class in `dataset.py`.
5. Load the pre-trained GPT-2 language model and tokenizer using `AutoModelForCausalLM` and `AutoTokenizer` from the `transformers` library.
6. Define the agent model using the `Agent` class in `agent.py`, passing in the pre-trained GPT-2 model as an argument.
7. Define the reference model by making a deep copy of the GPT-2 model using the `copy` module.
8. Define the PPO configuration using the `RLHFConfig` class in `ppo.py`.
9. Define the PPO trainer using the `RLHFTrainer` class in `ppo.py`, passing in the agent model, reference model, and PPO configuration as arguments.
10. Train the agent by iterating over the preprocessed dataset using a PyTorch dataloader, generating responses using the `generate` function in the agent model, computing rewards using a separate reward model, and calculating the PPO loss using the `compute_loss` function in the PPO trainer. The agent's parameters are updated using backpropagation and an optimizer.

## Files

- `agent.py`: Defines the `Agent` class, which adds functionality for generating responses and computing rewards to a pre-trained language model.
- `dataset.py`: Defines the `IMDBDataset` class, which preprocesses the IMDB dataset and creates a PyTorch dataset.
- `ppo.py`: Defines the `RLHFConfig` class, which sets the hyperparameters for PPO training, the `RLHFTrainer` class, which implements the PPO algorithm, and the `compute_advantage_and_return` and `compute_loss` functions used in the PPO training.
- `train.py`: Defines the training loop for the reinforcement learning-based dialog agent.

## Acknowledgements

This project was inspired by the paper "Reinforcement Learning for Dialogue Generation Using PPO" by Zhou et al. (2020).