#!/usr/bin/python3
import torch
from net import TextClassificationModel
from torchtext.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer

def test():
    def yield_tokens(data_iter):
        for text in data_iter:
            yield tokenizer(text)


    tokenizer = get_tokenizer("basic_english")
    word = "asd taxi bus"
    vocab = build_vocab_from_iterator(yield_tokens([word]), specials=["<unk>"])
    vocab.set_default_index(vocab["<unk>"])

    # num_class = len(set([x for x in ["BMV"]]))
    num_class = 3
    # vocab_size = len(vocab)
    vocab_size = 10
    print(vocab_size)
    emsize = 64
    net = TextClassificationModel(vocab_size, emsize, num_class)
    a = torch.load("models/value.pth", map_location=torch.device('cpu'))
    net.load_state_dict(a)

    text_pipeline = lambda x: vocab(tokenizer(x))
    processed_text = torch.tensor(text_pipeline(word), dtype=torch.int64)
    print(processed_text)
    text_list = []
    text = text_list.append(processed_text)
    # text = torch.cat(text)
    offsets = [0]
    offsets.append(processed_text.size(0))
    offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
    print(offsets[0])

    a = net(processed_text, offsets)
    print(a)
    result = a.argmax(1).item()
    print(result)

if __name__ == "__main__":
    test()
