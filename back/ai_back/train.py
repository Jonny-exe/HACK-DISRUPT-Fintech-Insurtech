#!/usr/bin/python3

import torch
from torch.utils.data.dataset import random_split
from torchtext.data.functional import to_map_style_dataset
from net import TextClassificationModel

from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator

from get_data import get_data, create_data


def train(dataloader, model):
    model.train()
    total_acc, total_count = 0, 0
    log_interval = 500

    EPOCHS = 100  # epoch
    LR = 5  # learning rate
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=LR)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 1.0, gamma=0.1)

    for i in range(EPOCHS):
        for idx, (label, text, offsets) in enumerate(dataloader):
            optimizer.zero_grad()
            print(text)
            predited_label = model(text, offsets)
            loss = criterion(predited_label, label)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 0.1)
            optimizer.step()

    torch.save(model.state_dict(), "models/value.pth")


def get_dataloader():
    BATCH_SIZE = 64  # batch size for training

    tokenizer = get_tokenizer("basic_english")
    XY = create_data()

    def yield_tokens(data_iter):
        for text, _ in data_iter:
            yield tokenizer(text)

    def collate_batch(batch):
        label_list, text_list, offsets = [], [], [0]
        for (_text, _label) in batch:
            label_list.append(label_pipeline(_label))
            processed_text = torch.tensor(text_pipeline(_text), dtype=torch.int64)
            print(processed_text)
            text_list.append(processed_text)
            offsets.append(processed_text.size(0))
        label_list = torch.tensor(label_list, dtype=torch.int64)
        offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
        text_list = torch.cat(text_list)
        return label_list.to(), text_list.to(), offsets.to()

    vocab = build_vocab_from_iterator(yield_tokens(XY), specials=["<unk>"])
    vocab.set_default_index(vocab["<unk>"])
    num_class = len(set([Y for X, Y in XY]))
    vocab_size = len(vocab)
    emsize = 64
    model = TextClassificationModel(vocab_size, emsize, num_class)

    text_pipeline = lambda x: vocab(tokenizer(x))
    label_pipeline = lambda x: int(x)

    total_accu = None
    train_dataset = to_map_style_dataset(XY)
    num_train = int(len(train_dataset) * 0.95)
    split_train_, split_valid_ = random_split(
        train_dataset, [num_train, len(train_dataset) - num_train]
    )
    train_dataloader = torch.utils.data.DataLoader(
        split_train_,
        batch_size=BATCH_SIZE,
        shuffle=True,
        collate_fn=collate_batch
        # split_train_, batch_size=BATCH_SIZE, shuffle=True
    )
    return train_dataloader, model


from torch import nn

if __name__ == "__main__":
    dataloader, model = get_dataloader()
    train(dataloader, model)
