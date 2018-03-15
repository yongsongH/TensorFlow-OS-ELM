import argparse
import os
import tqdm
import time
import numpy as np
from nn import NN

parser = argparse.ArgumentParser()
parser.add_argument('--n_input_nodes', type=int, default=784)
parser.add_argument('--n_hidden_nodes', type=int, default=32)
parser.add_argument('--n_output_nodes', type=int, default=784)
parser.add_argument('--loss', default='mean_absolute_error')
parser.add_argument('--hidden_activation', default='relu')
parser.add_argument('--output_activation', default='sigmoid')
parser.add_argument('--batch_size', type=int, default=1)
parser.add_argument('--n', type=int, default=10000)

def main(args):

    model = NN(
        n_input_nodes=args.n_input_nodes,
        n_hidden_nodes=args.n_hidden_nodes,
        n_output_nodes=args.n_output_nodes,
        loss=args.loss,
        hidden_activation=args.hidden_activation,
        output_activation=args.output_activation,
    )

    pbar = tqdm.tqdm(total=args.n)
    times = []
    for i in range(args.n):
        x = np.random.normal(size=(args.batch_size, args.n_input_nodes))
        t = np.random.normal(size=(args.batch_size, args.n_output_nodes))
        stime = time.time()
        model.test_on_batch(x, t)
        etime = time.time()
        times.append(etime - stime)
        pbar.update(1)
    times = np.array(times)
    mean = np.mean(times)
    print('mean prediction time: %f [msec/batch]' % (1000*mean))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
