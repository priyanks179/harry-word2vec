# HARRY-WORD2VEC

### Harry potter's 7 books are used to create corpus

### Then gensim framework is used to create word2vec out of corpus

### Model itself learns similarities between characters

model.most_similar(positive=['ron'], topn=7)

### o/p->

[('ginny', 0.8942017555236816),
 ('neville', 0.8824698328971863),
 ('hagrid', 0.8696408867835999),
 ('hermione', 0.8595108985900879),
 ('quickly', 0.7818440198898315),
 ('harry', 0.7702754735946655),
 ('luna', 0.7642109394073486)]

###Then using tsne visualiztion of vectors is done
![word2vec](https://raw.githubusercontent.com/priyanks179/harry-word2vec/master/harry%20visualization.png)
