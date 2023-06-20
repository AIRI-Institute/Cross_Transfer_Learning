import os
import pandas as pd
from typing import List
import re
from tqdm import tqdm, trange
from datetime import datetime


acl_bib_path = "https://aclanthology.org/anthology+abstracts.bib.gz"
zip_file_path = "data/anthology+abstracts.bib.gz"
acl_file_path = "data/anthology+abstracts.bib"
wals_language_data = "https://raw.githubusercontent.com/cldf-datasets/wals/master/raw/language.csv"
wals_file_path = "data/language.csv"


def extract_indices(file_data: List[str]) -> List[int]:
    articles_index = []
    for i, string in enumerate(file_data):
        if string.startswith('@'):
            articles_index.append(i)
    return articles_index


def filter_language(lang: str) -> str:
    clear_lang = lang.split('(')[0].lower().strip()
    popular_words = [
        'even'
    ]
    if len(clear_lang) < 4 or clear_lang in popular_words:
        return f'{clear_lang} language'
    return clear_lang


def check_phrase_in_text(phrase, text):
    len_s = len(phrase)
    return any(phrase == text[i:len_s+i] for i in range(len(text) - len_s+1))


def extract_url_dataframe(bib_path: str, list_langs: List[str]) -> pd.DataFrame:
    f = open(bib_path)
    file_array = list(f)
    articles_index = extract_indices(file_array)

    final_df = {'language': [], 'url': []}
    for i in trange(len(articles_index)-1):
        snippet_array = file_array[articles_index[i]: articles_index[i+1]]
        for string in snippet_array:
            cleaned_string = string.strip()

            if cleaned_string.startswith('title'):
                temp_title = re.findall('(?<=\").*?(?=\")|(?<=\{).*?(?=\})', cleaned_string)[0]
                cleared_title = re.sub('[^a-zA-Z ]+', '', temp_title).lower().strip().split()

            if cleaned_string.startswith('url'):
                temp_url = re.findall('(?<=\").*?(?=\")', cleaned_string)[0]
            
            if cleaned_string.startswith('abstract'):
                temp_abstract = re.findall('(?<=\").*?(?=\")|(?<=\{).*?(?=\})', cleaned_string)[0]
                cleared_abstract = re.sub('[^a-zA-Z ]+', '', temp_abstract).lower().strip().split()
                for language_name in list_langs:
                    # language_subwords = re.sub('[^a-zA-Z ]+', '', language_name).lower().strip().split()
                    # if all([lang_word in cleared_abstract for lang_word in language_subwords]) or \
                    #     all([lang_word in cleared_title for lang_word in language_subwords]):
                    #     final_df['language'].append(language_name)
                    #     final_df['url'].append(temp_url)
                    language_name_clear = filter_language(language_name).split()
                    abstract_match = check_phrase_in_text(language_name_clear, cleared_abstract)
                    title_match = check_phrase_in_text(language_name_clear, cleared_title)
                    if abstract_match or title_match:
                        final_df['language'].append(language_name)
                        final_df['url'].append(temp_url)
   
    return pd.DataFrame(final_df)


def get_time() -> str:
        return datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")


def get_distribution():
    os.makedirs("data/", exist_ok=True)
    # get acl bib file
    os.system(f"wget -q {acl_bib_path} -O {zip_file_path}")
    os.system(f"gunzip -f {zip_file_path}")
    
    # get language data
    os.system(f"wget -q {wals_language_data} -O {wals_file_path}")
    
    df = pd.read_csv(wals_file_path)
    languages = df.name.tolist()
    
    # build dataframe
    lang_url_data = extract_url_dataframe(acl_file_path, languages)
    time = get_time()
    lang_url_data.to_csv(f"data/lang_url_{time}.csv", index=None)


if __name__ == '__main__':
    get_distribution()
