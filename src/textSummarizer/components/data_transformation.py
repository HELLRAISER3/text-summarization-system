import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer.name)
    
    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'])