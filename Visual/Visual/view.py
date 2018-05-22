from django.shortcuts import render
from django.http import HttpResponse
import json
import pymongo as mongo
import operator
animalClasses = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck',
                 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
                 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
                 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
                 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa',
                 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
                 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush', ]


def hello(request):
    f = open("../outPut.txt", "r+")
    name = f.read()
    f.close()
    conn = mongo.MongoClient('127.0.0.1', 27017)
    db = conn.Basasuya
    my_set = db.get_collection(name)
    tt = my_set.find({}).limit(1)[0]
    if(tt.get('path', -1) == -1):
        return render(request, 'fail.html')
    List = []
    flag = True
    Map = {}
    Name = {}
    for i in my_set.find({}):
        if(flag):
            flag = False
            continue
        if(Name.get(i['predict'], 0) == 0):
            Name[i['predict']] = 1
        if(Map.get((i['pos'], i['predict']), 0) == 0):
            Map[(i['pos'], i['predict'])] = 1
        else:
            Map[(i['pos'], i['predict'])] += 1

    for i in Map:
        List.append((i[0], Map[i], animalClasses[i[1]]))
    newList = sorted(List, key=operator.itemgetter(2, 0))
    newList2 = []
    for i in newList:
        newList2.append(list(i))
    NameList = []
    for i in Name:
        NameList.append(animalClasses[i])
    print(NameList)
    return render(request, 'vis1.html', {'data': json.dumps(newList2),
                                         'name': json.dumps(NameList)})
