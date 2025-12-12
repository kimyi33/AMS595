import torch.nn as nn
import torch_scatter


# activations = nn.ModuleDict([
#     ['lrelu', nn.LeakyReLU()],
#     ['relu', nn.ReLU()],
#     ])


class Identity(nn.Module):
    r"""A placeholder identity operator that is argument-insensitive.
    Args:
        args: any argument (unused)
        kwargs: any keyword argument (unused)
    """
    def __init__(self, *args, **kwargs):
        super(Identity, self).__init__()

    def forward(self, input):
        return input


def activation(act, negative_slope=0.2):
    activations = nn.ModuleDict([
        ['lrelu', nn.LeakyReLU(negative_slope)],
        ['relu', nn.ReLU()],
        ['elu', nn.ELU()],
        ['none', Identity()],
    ])
    return activations[act]

from torch_scatter import scatter_add, scatter_mean, scatter_max

def scatter_(name, src, index, dim_size=None, out=None):
    """
    Wrapper around torch_scatter (updated for the new API).

    name: 'add', 'mean', or 'max'
    src:  values to scatter  (E, ...)
    index: indices           (E,)
    dim_size: number of nodes (N)
    """
    assert name in ['add', 'mean', 'max']

    if name == 'add':
        # scatter_add(src, index, dim=0, out=None, dim_size=None)
        return scatter_add(src, index, dim=0, out=out, dim_size=dim_size)

    elif name == 'mean':
        return scatter_mean(src, index, dim=0, out=out, dim_size=dim_size)

    elif name == 'max':
        # scatter_max returns (values, indices)
        out_vals, _ = scatter_max(src, index, dim=0, out=out, dim_size=dim_size)
        # (Optional) replace -inf with 0 if you want the old behaviour
        out_vals[out_vals == float('-inf')] = 0
        return out_vals


def softmax(src, index, num_nodes=None):
    r"""Computes a sparsely evaluated softmax.
    Given a value tensor :attr:`botdet`, this function first groups those values
    along the first dimension based on the indices specified in :attr:`index`,
    and then proceeds to compute the softmax individually for each group.
    Args:
        botdet (Tensor): The source tensor.
        index (LongTensor): The indices of elements for applying the softmax.
        num_nodes (int, optional): The number of nodes, *i.e.*
            :obj:`max_val + 1` of :attr:`index`. (default: :obj:`None`)
    :rtype: :class:`Tensor`
    """

    if num_nodes is None:
        num_nodes = index.max().item() + 1

    out = src - torch_scatter.scatter_max(src, index, dim=0, dim_size=num_nodes,
                                          fill_value=-1e16)[0][index]
    # fill_value here above is crucial for correct operation!!
    out = out.exp()
    out = out / (
            torch_scatter.scatter_add(out, index, dim=0, dim_size=num_nodes)[index] + 1e-16)

    return out
