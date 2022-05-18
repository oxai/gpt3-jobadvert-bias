# gpt3-jobadvert-bias

## Supplementary code for

Looking for a Handsome Carpenter! Debiasing GPT-3 Job Advertisements

<!--Please cite as:

```
coming soon
```
-->

## Repo structure

`1-gather-bias-measures.ipynb`: Code to download and aggregate all biased word lists used in the study. Outputs a `.json` file with keys corresponding to word lists and values corresponding to dictionaries with biased words as keys and their weighting as values (1 for unweighted).

`2-word-counter.py`: Exemplary implementation of a word counter class to apply the bias measures to a specified file holding job ad texts.

`3-prompt-templates.ipynb`: GPT-3 prompt templates to reproduce our job ad generation experiments using the OpenAI Python package.

### Setup the OpenAI API via Anaconda

Go to https://beta.openai.com/account/api-keys and copy the secret key and paste it into the command below and run it.

```
conda activate <YOUR-ENV>
conda env config vars set OPENAI_API_KEY="<YOUR-KEY>"
```
Then reactivate your environment and check whether the secret API key was correctly saved into an environment variable
```
conda deactivate
conda activate <YOUR-ENV>
conda env config vars list                                                                    
```
The output should include the line `OPENAI_API_KEY=<YOUR-KEY>`.

## Contact

Due to privacy concerns, we decided against making our data set publicly available as it contains prompt completions from models fine-tuned on real-world job advertisements. For further information, queries, and resources, please send an email to: [conrad.borchers@oii.ox.ac.uk](mailto:conrad.borchers@oii.ox.ac.uk)

