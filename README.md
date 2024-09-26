# LangChain 101

This tutorial is inspired from and follows the amazing and beginner friendly tutorial from [codewithbrandon](https://www.youtube.com/watch?v=yF9kGESAi3M&t=731s).

- [LangChain 101](#langchain-101)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction

This repository contains the code for the LangChain 101 tutorial. As explained on their [website](https://python.langchain.com/docs/introduction/), LangChain is a framework for developing applications powered by large language models (LLMs). It simplifies every stage of the LLM application lifecycle: development, productionization, and deployment.

## Installation

To follow this tutorial it's recommended to install poetry. Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.  

You can install poetry by following the instructions on their [official website](https://python-poetry.org/docs/). Then use poetry to install the dependencies for this project:

```bash
poetry install
```

## Usage

The tutorial is divided into 5 parts:

1. Chat Models
2. Prompt Templates
3. Chains
4. RAG
5. Agents and Tools

To run the code for each part, you can use the following command:

```bash
poetry shell # to activate the virtual environment
python part-name/file-name.py
```

For example, to run the first file for the first part, you can use:

```bash
poetry shell # to activate the virtual environment
python 1-chat-models/1_chat_models_basic.py
```

That's it! You are now ready to start the tutorial. Happy coding! 🚀
