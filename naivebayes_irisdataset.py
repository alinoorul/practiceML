from csv import reader
import numpy as np
from random import seed
from random import randrange

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    class_values=dict()
    for i in dataset:
        for j in range(len(i)-1):
            i[j]=float(i[j].strip())
        if(i[-1] not in class_values):
            class_values[i[-1]]=len(class_values)
        i[-1]=class_values[i[-1]]
    return (dataset,class_values)
def separate_classes(dataset):
    separated=dict()
    for row in dataset:
        if(row[-1] not in separated):
            separated[row[-1]]=list()
        separated[row[-1]].append(row[0:4])
    return separated
def stats_dataset(dataset):
    statistics=[(np.mean(column),np.std(column), len(column)) for column in zip(*dataset)]
    return statistics
def stats_all(dataset):
    stats=dict()
    for label in dataset:
        stats[label]=stats_dataset(dataset[label])
    return stats
def gen_dist(mean,std):
    dist=norm(mean,std)
    return dist
def dist(stats):
    dists=dict()
    for label in stats:
        dists[label]=list()
        for stat in stats[label]:
            dists[label].append(gen_dist(stat[0],stat[1]))
    return dists
def class_len(dataset):
    class_lengths=dict()
    for label in dataset:
        class_lengths[label]=len(dataset[label])
    return class_lengths
def prob(class_lengths):
    total=0
    for label in class_lengths:
        total=total+class_lengths[label]
    probs=dict()
    for label in class_lengths:
        probs[label]=class_lengths[label]/total
    return probs

def predict_class(row,dists):
    prob=dict()
    for label in dists:
        prob[label]=class_prob[label]
        for i in range(len(row)):
            prob[label]=prob[label]*dists[label][i].pdf(row[i])
    best_p=-1
    best_val=None
    for class_value,p in prob.items():
        if best_val is None or best_p<p:
            best_val=class_value
            best_p=p
    return best_val

def split_data(dataset,n_folds):
    data_copy=list(dataset)
    data_folds=list()
    fold_size=int(len(dataset)/n_folds)
    for _ in range(n_folds):
        fold=list()
        while len(fold) < fold_size:
            i=randrange(len(data_copy))
            fold.append(data_copy.pop(i))
        data_folds.append(fold)
    return data_folds

def evaluate(dataset,n_folds,dists):
    data_fold=split_data(dataset,n_folds)
    accuracy=list()
    for fold in data_fold:
        correct=0
        for row in fold:
            predicted = predict_class(row[0:4],dists)
            actual = row[4]
            if(actual==predicted):
                correct=correct+1
        accuracy.append((correct/len(fold))*100)
    mean_accuracy=0
    for i in accuracy:
        mean_accuracy=mean_accuracy+i
    mean_accuracy=mean_accuracy/len(accuracy)
    return accuracy,mean_accuracy
    
seed(1)
n_folds=5
filename='iris.csv'
data,class_values=load_csv(filename)
dataset=separate_classes(data)
stats=stats_all(dataset)
dists=dist(stats)
class_prob=prob(class_len(dataset))
accuracy,mean=evaluate(data,n_folds,dists)

print("MEAN ACCURACY: {}".format(mean))
print("ACCURACY OF FOLDS({}): {}".format(n_folds,accuracy))

