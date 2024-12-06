import pandas as pd
ROOT_DIR = '../../input/' # Local Machine

# ROOT_DIR = '../input/all-the-news/' # Kaggle


# print(os.listdir('../input/all-the-news/'))
# path = "all-the-news/"
df = pd.read_csv(ROOT_DIR + "articles1.csv")
df.shape
(50000, 10)
df.head()