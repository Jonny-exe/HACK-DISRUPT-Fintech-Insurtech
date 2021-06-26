#!/usr/bin/python3
import torch
import torch.nn as nn
import string

# Loss and optimizier
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from get_data import get_data
from net import RNN, Net
import numpy as np


class DatasetValue(Dataset):
    def __init__(self, x, y):
        self.X = []
        for i in x:
            a = DatasetValue.lineToTensor(i)
            self.X.append(a)
        self.X = np.array(self.X)
        self.Y = DatasetValue.transform_Y(y)
        self.Y = np.array(self.Y)

    def letterToIndex(letter):
        return all_letters.find(letter)

    def transform_Y(Y):
        result = []
        for i in Y:
            a = [0] * 3
            a[i] = 1
            result.append(a)
        return result

    def lineToTensor(line):
        tensor = torch.zeros(len(line), 1, n_letters)
        for li, letter in enumerate(line):
            tensor[li][0][DatasetValue.letterToIndex(letter)] = 1
        return tensor

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):
        return (self.X[idx], self.Y[idx])


# all_letters = string.ascii_letters + " .,;'"
# n_letters = len(all_letters)
# n_hidden = 128
# n_categories = 3
# model = RNN(n_letters, n_hidden, n_categories)


# criterion = torch.nn.NLLLoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# X, Y = get_data()
# trainsetXY = DatasetValue(X, Y)
# train_loader = DataLoader(trainsetXY, batch_size=1, shuffle=True, drop_last=True)
# model.train()


# EPOCHS = 10
# for epoch in range(EPOCHS):
    # running_loss = 0.0
    # print(f"{epoch + 1} / {EPOCHS}")
    # for i, (data, target) in enumerate(train_loader, 0):
        # data = torch.as_tensor(data)
        # data = data.squeeze()
        # data = data.unsqueeze(-1)
        # print(data)
        # hidden = torch.zeros(len(data), 57, 1)
        # # hidden = hidden.reshape([len(data), 57,1])

        # # print("hidden: ", hidden, hidden.shape)
        # # print("Target: ", target, target.shape)

        # print("shapes", data.shape, hidden.shape)
        # device = "cpu"
        # if device == "cuda":
            # data, target = data.to(device), target.to(device)
        # data, target = data.to(torch.float32), target.to(torch.float32)

        # optimizer.zero_grad()
        # print("shape. ", data.shape)
        # # data = data.reshape([256, 1, 57])
        # outputs = model(data, hidden)
        # outputs = outputs.reshape([256, 64, 1])

        # loss = criterion(outputs, target)
        # loss.backward()
        # optimizer.step()

        # running_loss += loss.time()

        # if i % 2000 == 1999:
            # print('[%d, %5d] loss: %.3f' %
            # (epoch + 1, i + 1, running_loss / 2000))






def train(dataset=[]):
    EPOCHS = 5
    BATCH_SIZE = 256

    model = Net()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters())

    if len(dataset) == 0:
        print("creating data")
        trainset = initial_population()
    else:
        trainset = dataset

    trainsetXY = DatasetValue(trainset)
    train_loader = DataLoader(trainsetXY, batch_size=256, shuffle=True, drop_last=True)
    model.train()

    for epoch in range(EPOCHS):
        running_loss = 0.0
        print(f"{epoch + 1} / {EPOCHS}")
        for i, (data, target) in enumerate(train_loader, 0):
            target = target.unsqueeze(-1)
            if device == "cuda":
                data, target = data.to(device), target.to(device)
            data, target = data.to(torch.float32), target.to(torch.float32)

            optimizer.zero_grad()
            data = data.reshape([256, 1, 8, 8])
            outputs = model(data)
            outputs = outputs.reshape([256, 64, 1])

            loss = criterion(outputs, target)
            loss.backward()
            optimizer.step()

            running_loss = 0.0
    torch.save(model.state_dict(), "models/value.pth")
    print("Finished training")




torch.save(model.state_dict(), "models/value.pth")
print("Finished training")
