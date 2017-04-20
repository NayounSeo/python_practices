import numpy as np
import seaborn as sns
import random

def main():
  # 0 ~ 100 사이의 수 100개짜리 np배열 하나!
  data = np.array([random.randrange(0, 100) for x in range(100)])
  for i in range(10):
    print(data[i], data[i + 1], data[i + 2], data[i + 3], data[i + 4], end=' ')
    print(data[i + 5], data[i + 6], data[i + 7], data[i + 8], data[i + 9])


  # sns.palplot(sns.color_palette("OrRd", 10))
  # sns.palplot(sns.color_palette("Spectral", 10))
  # sns.palplot(sns.color_palette("RdYlBu", 10))
  sns.set_palette(sns.color_palette("Spectral"))

  # sns.boxplot(data)
  # sns.kdeplot(np.array(data))
  sns.violinplot(data)
  
  # sns.violinplot(data=data, palette="Spectral")

  sns.plt.show()

if __name__ == "__main__":
  main()