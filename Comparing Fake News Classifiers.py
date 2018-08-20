
    "import pandas as pd\n",
    "import numpy as np\n",
    "import itertools\n",
    "from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier\n",
    "from sklearn.svm import LinearSVC\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn import metrics\n",
    "import matplotlib.pyplot as plt"
   ]
 
    "count_vectorizer = CountVectorizer(stop_words='english')\n",
    "count_train = count_vectorizer.fit_transform(X_train)\n",
    "count_test = count_vectorizer.transform(X_test)"
   ]
  },
   [
    "tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)\n",
    "tfidf_train = tfidf_vectorizer.fit_transform(X_train)\n",
    "tfidf_test = tfidf_vectorizer.transform(X_test)"
   ]
  },
  {
 
    "\n",
    "- multinomialNB with counts (`sgd_count_clf`)\n",
    "- multinomialNB with tf-idf (`mn_tfidf_clf`)\n",
    "- passive aggressive with tf-idf (`pa_tfidf_clf`)\n",
    "- linear svc with tf-idf (`svc_tfidf_clf`)\n",
    "- linear sgd with tf-idf (`sgd_tfidf_clf`)\n",
    "\n",
   
   ]
  },
  {
  
  },
   [
    "mn_count_clf.fit(count_train, y_train)\n",
    "pred = mn_count_clf.predict(count_test)\n",
    "score = metrics.accuracy_score(y_test, pred)\n",
    "print(\"accuracy:   %0.3f\" % score)"
   ]
  },
  {
   
  },
  {
   
    }
   ],
   "source": [
    "mn_tfidf_clf.fit(tfidf_train, y_train)\n",
    "pred = mn_tfidf_clf.predict(tfidf_test)\n",
    "score = metrics.accuracy_score(y_test, pred)\n",
    "print(\"accuracy:   %0.3f\" % score)"
   ]
  },
  {
  
   
  },
  
     
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "accuracy:   0.937\n"
     ]
    }
   ],
   "source": [
    "pa_tfidf_clf.fit(tfidf_train, y_train)\n",
    "pred = pa_tfidf_clf.predict(tfidf_test)\n",
    "score = metrics.accuracy_score(y_test, pred)\n",
    "print(\"accuracy:   %0.3f\" % score)"
   ]
  },
  {
   
  {
   
    }
   ],
   "source": [
    "svc_tfidf_clf.fit(tfidf_train, y_train)\n",
    "pred = svc_tfidf_clf.predict(tfidf_test)\n",
    "score = metrics.accuracy_score(y_test, pred)\n",
    "print(\"accuracy:   %0.3f\" % score)"
   ]
  },
  {
   
  },
  {
   
     
    },
    {
     "name": "stderr",
     "output_type": "stream",
     
      
     
    }
   ],
   "source": [
    "sgd_tfidf_clf.fit(tfidf_train, y_train)\n",
    "pred = sgd_tfidf_clf.predict(tfidf_test)\n",
    "score = metrics.accuracy_score(y_test, pred)\n",
    "print(\"accuracy:   %0.3f\" % score)"
   ]
  },
  
  
  
  
  
  {
   
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x228e10f97b8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(0).clf()\n",
    "\n",
    "for model, name in [ (mn_count_clf, 'multinomial nb count'),\n",
    "                     (mn_tfidf_clf, 'multinomial nb tfidf'),\n",
    "                     (pa_tfidf_clf, 'passive aggressive'),\n",
    "                     (svc_tfidf_clf, 'svc'),\n",
    "                     (sgd_tfidf_clf, 'sgd')]:\n",
    "    if 'count' in name:\n",
    "        pred = model.predict_proba(count_test)[:,1]\n",
    "    elif 'multinomial' in name:\n",
    "        pred = model.predict_proba(tfidf_test)[:,1]\n",
    "    else: \n",
    "        pred = model.decision_function(tfidf_test)\n",
    "    fpr, tpr, thresh = metrics.roc_curve(y_test.values, pred, pos_label='REAL')\n",
    "    plt.plot(fpr,tpr,label=\"{}\".format(name))\n",
    "\n",
    "plt.legend(loc=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Introspecting models\n",
    "\n",
    
   
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'FAKE': [(-5.0704500064211739, '2016'),\n",
       "  (-4.1811459729896665, 'hillary'),\n",
       "  (-4.1043916932753328, 'october'),\n",
       "  (-3.161751604776756, 'share'),\n",
       "  (-3.0540663668918477, 'november'),\n",
       "  (-2.8953093031761803, 'article'),\n",
       "  (-2.5738440216996303, 'print'),\n",
       "  (-2.4717551272899585, 'oct'),\n",
       "  (-2.4579988269172151, 'mosul'),\n",
       "  (-2.3902493881902882, 'email')],\n",
       " 'REAL': [(2.1814094723594208, 'cruz'),\n",
       "  (2.2633554669640392, 'rush'),\n",
       "  (2.2847774276674842, 'friday'),\n",
       "  (2.2879745036977206, 'candidates'),\n",
       "  (2.2976071939915341, 'monday'),\n",
       "  (2.3306680602495802, 'islamic'),\n",
       "  (2.4054655897577644, 'gop'),\n",
       "  (2.6450750492749582, 'says'),\n",
       "  (3.0188941376824454, 'tuesday'),\n",
       "  (4.8411759073070835, 'said')]}"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
  
  
    
    "    class_labels = classifier.classes_\n",
    "    feature_names = vectorizer.get_feature_names()\n",
    "    topn_class1 = sorted(zip(classifier.coef_[0], feature_names))[:n]\n",
    "    topn_class2 = sorted(zip(classifier.coef_[0], feature_names))[-n:]\n",
    "\n",
    "    return {class_labels[0]: topn_class1,\n",
    "            class_labels[1]: topn_class2\n",
    "    }\n",
    "\n",
    "\n",
    
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifiers = [(mn_count_clf, count_vectorizer),\n",
    "               (mn_tfidf_clf, tfidf_vectorizer),\n",
    "               (pa_tfidf_clf, tfidf_vectorizer),\n",
    "               (svc_tfidf_clf, tfidf_vectorizer),\n",
    "               (sgd_tfidf_clf, tfidf_vectorizer)]"
   ]
  },
  
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,\n",
       "      intercept_scaling=1, loss='squared_hinge', max_iter=1000,\n",
       "      multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,\n",
       "      verbose=0): {'FAKE': [(-2.5736808460603888, '2016'),\n",
       "   (-2.5339788375310164, 'hillary'),\n",
       "   (-2.2832621342882073, 'october'),\n",
       "   (-1.7249559807941066, 'article'),\n",
       "   (-1.7001461818146473, 'november'),\n",
       "   (-1.6804837498062837, 'share'),\n",
       "   (-1.4612989573975417, 'election'),\n",
       "   (-1.3994859149695913, 'print'),\n",
       "   (-1.3618728377602229, 'war'),\n",
       "   (-1.3083278305862753, 'advertisement')],\n",
       "  'REAL': [(1.3417946674266665, 'friday'),\n",
       "   (1.3487563583023812, 'monday'),\n",
       "   (1.3541847224218029, 'cruz'),\n",
       "   (1.378918892720107, 'gop'),\n",
       "   (1.391984769332395, 'candidates'),\n",
       "   (1.4222360151943452, 'conservative'),\n",
       "   (1.4570608201497384, 'islamic'),\n",
       "   (1.5834318817325421, 'says'),\n",
       "   (1.6805120677152638, 'tuesday'),\n",
       "   (3.4802142567828591, 'said')]},\n",
       " MultinomialNB(alpha=0.1, class_prior=None, fit_prior=True): {'FAKE': [(-16.067750538483136,\n",
       "    '0000'),\n",
       "   (-16.067750538483136, '000035'),\n",
       "   (-16.067750538483136, '0001'),\n",
       "   (-16.067750538483136, '0001pt'),\n",
       "   (-16.067750538483136, '000km'),\n",
       "   (-16.067750538483136, '0011'),\n",
       "   (-16.067750538483136, '006s'),\n",
       "   (-16.067750538483136, '007'),\n",
       "   (-16.067750538483136, '007s'),\n",
       "   (-16.067750538483136, '008s')],\n",
       "  'REAL': [(-5.6759590828633062, 'republican'),\n",
       "   (-5.5822987943478246, 'campaign'),\n",
       "   (-5.5205424220494219, 'new'),\n",
       "   (-5.463370874939617, 'state'),\n",
       "   (-5.4591625312696053, 'obama'),\n",
       "   (-5.4299498700212414, 'president'),\n",
       "   (-5.403667459399097, 'people'),\n",
       "   (-4.9293585357529537, 'clinton'),\n",
       "   (-4.5413068577119997, 'trump'),\n",
       "   (-4.424753408851144, 'said')]},\n",
       " MultinomialNB(alpha=0.1, class_prior=None, fit_prior=True): {'FAKE': [(-12.641778440826338,\n",
       "    '0000'),\n",
       "   (-12.641778440826338, '000035'),\n",
       "   (-12.641778440826338, '0001'),\n",
       "   (-12.641778440826338, '0001pt'),\n",
       "   (-12.641778440826338, '000km'),\n",
       "   (-12.641778440826338, '0011'),\n",
       "   (-12.641778440826338, '006s'),\n",
       "   (-12.641778440826338, '007'),\n",
       "   (-12.641778440826338, '007s'),\n",
       "   (-12.641778440826338, '008s')],\n",
       "  'REAL': [(-6.4523190824225267, 'cruz'),\n",
       "   (-6.4520765155758752, 'state'),\n",
       "   (-6.3976966482380719, 'republican'),\n",
       "   (-6.3763430603633546, 'campaign'),\n",
       "   (-6.3243977353920071, 'president'),\n",
       "   (-6.2546017970213645, 'sanders'),\n",
       "   (-6.1446218997380431, 'obama'),\n",
       "   (-5.7568172481528066, 'clinton'),\n",
       "   (-5.5960857857331119, 'said'),\n",
       "   (-5.3575239145044948, 'trump')]},\n",
       " PassiveAggressiveClassifier(C=1.0, average=False, class_weight=None,\n",
       "               fit_intercept=True, loss='hinge', max_iter=None, n_iter=50,\n",
       "               n_jobs=1, random_state=None, shuffle=True, tol=None,\n",
       "               verbose=0, warm_start=False): {'FAKE': [(-5.0704500064211739,\n",
       "    '2016'),\n",
       "   (-4.1811459729896665, 'hillary'),\n",
       "   (-4.1043916932753328, 'october'),\n",
       "   (-3.161751604776756, 'share'),\n",
       "   (-3.0540663668918477, 'november'),\n",
       "   (-2.8953093031761803, 'article'),\n",
       "   (-2.5738440216996303, 'print'),\n",
       "   (-2.4717551272899585, 'oct'),\n",
       "   (-2.4579988269172151, 'mosul'),\n",
       "   (-2.3902493881902882, 'email')],\n",
       "  'REAL': [(2.1814094723594208, 'cruz'),\n",
       "   (2.2633554669640392, 'rush'),\n",
       "   (2.2847774276674842, 'friday'),\n",
       "   (2.2879745036977206, 'candidates'),\n",
       "   (2.2976071939915341, 'monday'),\n",
       "   (2.3306680602495802, 'islamic'),\n",
       "   (2.4054655897577644, 'gop'),\n",
       "   (2.6450750492749582, 'says'),\n",
       "   (3.0188941376824454, 'tuesday'),\n",
       "   (4.8411759073070835, 'said')]},\n",
       " SGDClassifier(alpha=0.0001, average=False, class_weight=None, epsilon=0.1,\n",
       "        eta0=0.0, fit_intercept=True, l1_ratio=0.15,\n",
       "        learning_rate='optimal', loss='hinge', max_iter=None, n_iter=None,\n",
       "        n_jobs=1, penalty='l2', power_t=0.5, random_state=None,\n",
       "        shuffle=True, tol=None, verbose=0, warm_start=False): {'FAKE': [(-3.9926782292700946,\n",
       "    '2016'),\n",
       "   (-3.8552905108925266, 'hillary'),\n",
       "   (-3.5953189595316917, 'october'),\n",
       "   (-2.8546820303891476, 'article'),\n",
       "   (-2.6373462952563442, 'november'),\n",
       "   (-2.5278145100297338, 'share'),\n",
       "   (-2.3886732371914743, 'print'),\n",
       "   (-2.2004356045226778, 'war'),\n",
       "   (-2.0497810198244792, 'election'),\n",
       "   (-2.024057720243408, 'advertisement')],\n",
       "  'REAL': [(1.9532759272677389, 'conservatives'),\n",
       "   (1.9961771336381626, 'candidates'),\n",
       "   (2.0156322506803068, 'jobs'),\n",
       "   (2.0470309463663865, 'cruz'),\n",
       "   (2.17912687799517, 'conservative'),\n",
       "   (2.219227830610758, 'islamic'),\n",
       "   (2.3891950805392534, 'monday'),\n",
       "   (2.4638100910508833, 'says'),\n",
       "   (2.6680106730577231, 'tuesday'),\n",
       "   (4.9057317454884029, 'said')]}}"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   
  
   
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "comparable_results = {'REAL': {}, 'FAKE': {}}\n",
    "for clf, data in results.items():\n",
    "    clf_name = clf.__class__.__name__\n",
    "    for label, features in data.items():\n",
    "        for rank, score_tuple in enumerate(features):\n",
    "            if score_tuple[1] in comparable_results[label]:\n",
    "                comparable_results[label][score_tuple[1]].append((rank + 1, clf_name))\n",
    "            else:\n",
    "                comparable_results[label][score_tuple[1]] = [(rank + 1, clf_name)]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   
    
   
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'0000': [(1, 'MultinomialNB'), (1, 'MultinomialNB')],\n",
       " '000035': [(2, 'MultinomialNB'), (2, 'MultinomialNB')],\n",
       " '0001': [(3, 'MultinomialNB'), (3, 'MultinomialNB')],\n",
       " '0001pt': [(4, 'MultinomialNB'), (4, 'MultinomialNB')],\n",
       " '000km': [(5, 'MultinomialNB'), (5, 'MultinomialNB')],\n",
       " '0011': [(6, 'MultinomialNB'), (6, 'MultinomialNB')],\n",
       " '006s': [(7, 'MultinomialNB'), (7, 'MultinomialNB')],\n",
       " '007': [(8, 'MultinomialNB'), (8, 'MultinomialNB')],\n",
       " '007s': [(9, 'MultinomialNB'), (9, 'MultinomialNB')],\n",
       " '008s': [(10, 'MultinomialNB'), (10, 'MultinomialNB')],\n",
       " '2016': [(1, 'PassiveAggressiveClassifier'),\n",
       "  (1, 'LinearSVC'),\n",
       "  (1, 'SGDClassifier')],\n",
       " 'advertisement': [(10, 'LinearSVC'), (10, 'SGDClassifier')],\n",
       " 'article': [(6, 'PassiveAggressiveClassifier'),\n",
       "  (4, 'LinearSVC'),\n",
       "  (4, 'SGDClassifier')],\n",
       " 'election': [(7, 'LinearSVC'), (9, 'SGDClassifier')],\n",
       " 'email': [(10, 'PassiveAggressiveClassifier')],\n",
       " 'hillary': [(2, 'PassiveAggressiveClassifier'),\n",
       "  (2, 'LinearSVC'),\n",
       "  (2, 'SGDClassifier')],\n",
       " 'mosul': [(9, 'PassiveAggressiveClassifier')],\n",
       " 'november': [(5, 'PassiveAggressiveClassifier'),\n",
       "  (5, 'LinearSVC'),\n",
       "  (5, 'SGDClassifier')],\n",
       " 'oct': [(8, 'PassiveAggressiveClassifier')],\n",
       " 'october': [(3, 'PassiveAggressiveClassifier'),\n",
       "  (3, 'LinearSVC'),\n",
       "  (3, 'SGDClassifier')],\n",
       " 'print': [(7, 'PassiveAggressiveClassifier'),\n",
       "  (8, 'LinearSVC'),\n",
       "  (7, 'SGDClassifier')],\n",
       " 'share': [(4, 'PassiveAggressiveClassifier'),\n",
       "  (6, 'LinearSVC'),\n",
       "  (6, 'SGDClassifier')],\n",
       " 'war': [(9, 'LinearSVC'), (8, 'SGDClassifier')]}"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "comparable_results['FAKE']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
  
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "agg_results = {}\n",
    "for label, features in comparable_results.items():\n",
    "    for feature, ranks in features.items():\n",
    "        if feature in agg_results:\n",
    "            print(\"WARNING! DUPLICATE LABEL!!! {}\".format(feature))\n",
    "        agg_results[feature] = {\n",
    "            'label': label,\n",
    "            'agg_rank': np.mean([r[0] for r in ranks]),\n",
    "            'count': len(ranks)\n",
    "        }"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
 
   
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "comparison_df = pd.DataFrame(agg_results).T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>agg_rank</th>\n",
       "      <th>count</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0000</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>000035</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0001</th>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0001pt</th>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>000km</th>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       agg_rank count label\n",
       "0000          1     2  FAKE\n",
       "000035        2     2  FAKE\n",
       "0001          3     2  FAKE\n",
       "0001pt        4     2  FAKE\n",
       "000km         5     2  FAKE"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "comparison_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   
  
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>agg_rank</th>\n",
       "      <th>count</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>said</th>\n",
       "      <td>9.8</td>\n",
       "      <td>5</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cruz</th>\n",
       "      <td>2.25</td>\n",
       "      <td>4</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>tuesday</th>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>says</th>\n",
       "      <td>8</td>\n",
       "      <td>3</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>islamic</th>\n",
       "      <td>6.33333</td>\n",
       "      <td>3</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>monday</th>\n",
       "      <td>4.66667</td>\n",
       "      <td>3</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>candidates</th>\n",
       "      <td>3.66667</td>\n",
       "      <td>3</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>obama</th>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>trump</th>\n",
       "      <td>9.5</td>\n",
       "      <td>2</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>state</th>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           agg_rank count label\n",
       "said            9.8     5  REAL\n",
       "cruz           2.25     4  REAL\n",
       "tuesday           9     3  REAL\n",
       "says              8     3  REAL\n",
       "islamic     6.33333     3  REAL\n",
       "monday      4.66667     3  REAL\n",
       "candidates  3.66667     3  REAL\n",
       "obama             6     2  REAL\n",
       "trump           9.5     2  REAL\n",
       "state             3     2  REAL"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   
   
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>agg_rank</th>\n",
       "      <th>count</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2016</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>share</th>\n",
       "      <td>5.33333</td>\n",
       "      <td>3</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>print</th>\n",
       "      <td>7.33333</td>\n",
       "      <td>3</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>october</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>november</th>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hillary</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>article</th>\n",
       "      <td>4.66667</td>\n",
       "      <td>3</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0000</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>election</th>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>000035</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         agg_rank count label\n",
       "2016            1     3  FAKE\n",
       "share     5.33333     3  FAKE\n",
       "print     7.33333     3  FAKE\n",
       "october         3     3  FAKE\n",
       "november        5     3  FAKE\n",
       "hillary         2     3  FAKE\n",
       "article   4.66667     3  FAKE\n",
       "0000            1     2  FAKE\n",
       "election        8     2  FAKE\n",
       "000035          2     2  FAKE"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
 
   
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   
  },
  {
   "cell_type": "markdown",
   "metadata": {},
  
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20161 (-13.669855265684765, '00000031')\n"
     ]
    }
   ],
   "source": [
    "feature_names = count_vectorizer.get_feature_names()\n",
    "for idx, ftr_weight in enumerate(sorted(zip(mn_count_clf.coef_[0], feature_names))):\n",
    "    if ftr_weight[0] <= -16.067750538483136:\n",
    "        continue\n",
    "    print(idx, ftr_weight)\n",
    "    break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 
}
