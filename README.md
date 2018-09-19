# Recommender System 
Python implementation of Recommender System.
If you wanna have the full source code, email to hai.maituan@gmail.com

-------------------------------------
## Content Based Filter Model
### Description
This is the most simple filter to learn. It's very much based on the item features. As a master of fact, it's difficult for people to create the features and input the values for that features. Some people have confustion about Content Based Filter Model and Collaborative Filter with Item Based. Try an interesting Recommender System with Excel with [Simen Eide](https://simeneide.github.io/recommendations/2017/05/27/CFexcel.html)
### Code
![Content Based Filtering Code](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/ContentBasedCode.png)
### Output
![Recommend20](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/Recommend20.png)
## Collaborative Filter Model
### Description
Instead of using features of items to determine their similarity, we focus on the similarity of the user ratings for two items. That is, in place of the item-profile vector for an item, we use its column in the utility matrix. Further, instead of contriving a profile vector for users, we represent them by their rows in the utility matrix. Users are similar if their vectors are close according to some distance measure such as Jaccard or cosine distance. Recommendation for a user U is then made by looking at the users that are most similar to U in this sense, and recommending items that these users like. The process of identifying similar users and recommending what similar users like is called collaborative filtering.
### Pros and Cons
![Collaborative  Filtering Pros&Cons](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/ProsConsCF.png)
### Content Based vs. Collaborative Filter
Based on the choice of reference characteristics, a recommendation system could be based on content-based approach or collaborative filtering (CF) approach or both. As their names indicate, content-based approach is based on the “matching” of user profile and some specific characteristics of an item (e.g.the occurrence of specific words in a document) while collaborative filtering approach is a process of filtering information or pattern based on the collaboration of users, or the similarity between items.
* Content-based systems examine properties of the items recommended. For instance, if a Netflix user has watched many cowboy movies, then recom- mend a movie classified in the database as having the “cowboy” genre.
* Collaborative filtering systems recommend items based on similarity measures between users and/or items. The items recommended to a user are those preferred by similar users.
### Item based vs. User Based?
* In practice, it has been observed that item-item often works better than user-user
Why? Items are simpler, users have multiple tastes
![User Based and Item Based](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/CF_Filter.jpg)
![Users and Items Fitler, Which one better?](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/User_ItemsCF.png)
* Item-Item vs User-Item Matrix
![User-ItemMatrix](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/Item_UserBased_Cal.JPG)
* Predict from Matrix <br />
![PredictFromItemBased](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/ItemBasedFormula.JPG)
![PredictFromUserBased](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/UserBasedFormula.JPG)
* Matrix Factorization<br />
![ModelBased](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/MaxtrixFactorization.JPG)
## Collaborative Filter with Deep Learning
### Shallow implementation
Using Keras backed by tensorflow just some neural network layers and embedded layers. We use sparse matrix so we save a lot of memory space and computational cost.
![Shallow Architecture Code](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/ShallowCFCode.png)
![Shallow Architecture Neural Networks](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/ShallowCFNet.png)
### Keras AutoEncoder implementation
Using Keras backed by tensorflow for AutoEncoder to automatically discover latent factors and the features of users, items and ratings. We use sparse matrix so we save a lot of memory space and computational cost.
![Deep Architecture Code](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/DeepCFCode.png)
![Deep Architecture Neural Networks](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/DeepCFNet.png)
### Why do we need Embedded Layer?
* One Hot Endcoded Vectors for Recommender Systems are high dimensional and sparse. It is called One Hot because jsut one value is 1 and all others values are 0. It consumes a lot of memory space and increase computational cost. There are 1M items in Amazon but a user just rate for 1 item only. If they store in convientional vector it's really a bad solution.
* To save memory space we can make use of sparse matrices in numpy or Keras but Embedded Layer is more than that, it provides the latent factors to encode the characteristic of users of rating for items. So we can reduce a lot of redundant informations to represent characteristic of users.
* Embedded in Excel
![Excel](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/EmbeddedInExcel.png)
* Embedded in Text Example
![Text Example](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/EmbeddedText.png)
## Important Notes
### Books:
![Mining Massive Datasets](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/Book1.jpg)
![Introduction to Data Mining](https://github.com/HaiTMai/RecommenderSystem/blob/master/Images/book2.jpg)
### Courses:
1. Machine Learning, Deep Learning IO by Andrew Ng(Stanford)
2. Minining of Massive Datasets by Stanford
3. Introduction to Data Mining by U Kang, Seoul National University(SNU)
4. Introduction to Data Mining by CheongHee Park, Chungnam National University(CNU)
### Utility Matrices: 
Recommendation systems deal with users and items. A utility matrix offers known information about the degree to which a user likes an item. Normally, most entries are unknown, and the essential problem of recommending items to users is predicting the values of the unknown entries based on the values of the known entries.
### Two Classes of Recommendation Systems: 
These systems attempt to pre- dict a user’s response to an item by discovering similar items and the response of the user to those. One class of recommendation system is content-based; it measures similarity by looking for common features of the items. A second class of recommendation system uses collaborative fil- tering; these measure similarity of users by their item preferences and/or measure similarity of items by the users who like them.
### Item Profiles: 
These consist of features of items. Different kinds of items have different features on which content-based similarity can be based. Features of documents are typically important or unusual words. Prod- ucts have attributes such as screen size for a television. Media such as movies have a genre and details such as actor or performer. Tags can also be used as features if they can be acquired from interested users.
### User Profiles: 
A content-based collaborative filtering system can con- struct profiles for users by measuring the frequency with which features appear in the items the user likes. We can then estimate the degree to which a user will like an item by the closeness of the item’s profile to the user’s profile.
### Classification of Items: 
An alternative to constructing a user profile is to build a classifier for each user, e.g., a decision tree. The row of the utility matrix for that user becomes the training data, and the classifier must predict the response of the user to all items, whether or not the row had an entry for that item.
### Similarity of Rows and Columns of the Utility Matrix: 
Collaborative fil- tering algorithms must measure the similarity of rows and/or columns of the utility matrix. Jaccard distance is appropriate when the matrix consists only of 1’s and blanks (for “not rated”). Cosine distance works for more general values in the utility matrix. It is often useful to normal- ize the utility matrix by subtracting the average value (either by row, by column, or both) before measuring the cosine distance.
### Clustering Users and Items: 
Since the utility matrix tends to be mostly blanks, distance measures such as Jaccard or cosine often have too little data with which to compare two rows or two columns. A preliminary step or steps, in which similarity is used to cluster users and/or items into small groups with strong similarity, can help provide more common components with which to compare rows or columns.
### UV-Decomposition:
One way of predicting the blank values in a utility matrix is to find two long, thin matrices U and V , whose product is an approximation to the given utility matrix. Since the matrix product UV gives values for all user-item pairs, that value can be used to predict the value of a blank in the utility matrix. The intuitive reason this method makes sense is that often there are a relatively small number of issues (that number is the “thin” dimension of U and V ) that determine whether or not a user likes an item.
### Root-Mean-Square Error: 
A good measure of how close the product UV is to the given utility matrix is the RMSE (root-mean-square error). The RMSE is computed by averaging the square of the differences between UV and the utility matrix, in those elements where the utility matrix is nonblank. The square root of this average is the RMSE.
### Computing U and V: 
One way of finding a good choice for U and V in a UV-decomposition is to start with arbitrary matrices U and V . Repeat- edly adjust one of the elements of U or V to minimize the RMSE between the product UV and the given utility matrix. The process converges to a local optimum, although to have a good chance of obtaining a global optimum we must either repeat the process from many starting matrices, or search from the starting point in many different ways.
