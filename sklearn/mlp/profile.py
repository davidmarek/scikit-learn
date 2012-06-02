import pstats
import cProfile

from sklearn.mlp.classes import MLPClassifier
from sklearn import datasets, preprocessing

digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

data = preprocessing.scale(data)
classifier = MLPClassifier(n_hidden=10, lr=0.3, loss_function='cross-entropy', output_function='softmax', batch_size=100)
cProfile.runctx("""classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2],
    max_epochs=1000)""", globals(), locals(), "Profile.prof")
s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
