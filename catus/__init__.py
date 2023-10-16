import matplotlib.pyplot as plt


default_rcParams = {
    'text.usetex': True,
    'font.family': 'serif',
    'font.size': 12,
    'figure.figsize': (5, 5),
    'figure.titlesize': 'large',
    'axes.titlesize': 'large',
    'axes.labelsize': 'large',
    'xtick.top': True,
    'xtick.major.size': 2,
    'xtick.minor.size': 1,
    'xtick.minor.visible': True,
    'xtick.direction': 'out',
    'xtick.labelsize': 'medium',
    'ytick.right': True,
    'ytick.major.size': 2,
    'ytick.minor.size': 1,
    'ytick.minor.visible': True,
    'ytick.direction': 'out',
    'ytick.labelsize': 'medium',
    'legend.frameon': True,
    'legend.framealpha': 1,
    'legend.fontsize': 'medium',
    'lines.linewidth': 2,
    'patch.linewidth': 2,
    'hatch.linewidth': 2,
    }

plt.rcParams.update(default_rcParams)


cmap = plt.get_cmap('tab10')


def savefig(fig, file):

    if file[-4:] != '.pdf':
        file += '.pdf'

    return fig.savefig(file, bbox_inches='tight')


class _Corner:

    def __init__(self, kde=False, bounds=None, reflect=None, smooth1d=None, smooth2d=None):

        pass

    def plot(self):

        pass

    def plot1d(self):

        pass

    def plot2d(self):

        pass



def _corner(*args, **kwargs):

    return Corner(*args, **kwargs).plot()

