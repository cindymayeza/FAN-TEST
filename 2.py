#!/usr/bin/env python
# coding: utf-8

# In[13]:


def count_words(sentence, special_characters):
    words = sentence.split()
    word_count = 0
    for word in words:
        if all(char not in special_characters for char in word):
            word_count += 1
    return word_count

a. Input : Saat meng*ecat tembok, Agung dib_antu oleh Raihan.
   Output: 5
# In[14]:


sentence = "Saat meng*ecat tembok, Agung dib_antu oleh Raihan."
special_characters = "!@#$%^&*()_"
word_count = count_words(sentence, special_characters)
print("Jumlah kata:", word_count)

b. Input: Berapa u(mur minimal[ untuk !mengurus ktp?
   Output: 3
# In[15]:


sentence = "Berapa u(mur minimal[ untuk !mengurus ktp?"
special_characters = "!@#$%^&*()_["
word_count = count_words(sentence, special_characters)
print("Jumlah kata:", word_count)

c. Input: Masing-masing anak mendap(atkan uang jajan ya=ng be&rbeda.
   Output: 4
# In[17]:


sentence = "Masing-masing anak mendap(atkan uang jajan ya=ng be&rbeda."
special_characters = "!@#$%^&*()_[="
word_count = count_words(sentence, special_characters)
print("Jumlah kata:", word_count)

Thankyou ^-^