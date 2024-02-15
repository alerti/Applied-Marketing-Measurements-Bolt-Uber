import logging
import sys
import matplotlib.pyplot as plt
import seaborn as sns


class Visualize:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Visualize class created')

    def bar_chart(self, data, x, y, title, xlabel, ylabel,output_filepath = None):
        """ Create bar chart
        """
        self.logger.info('Creating bar chart')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x=x, y=y, data=data)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'),
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 9),
                        textcoords='offset points')
        plt.savefig(output_filepath)
        return None

    def scatter_plot(self, data, x, y, title, xlabel, ylabel, output_filepath = None):
        """ Create scatter plot
        """
        self.logger.info('Creating scatter plot')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.scatterplot(x=x, y=y, data=data)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.savefig(output_filepath)
        return None

    def histogram(self, data, x, title, xlabel, ylabel, output_filepath = None):
        """ Create histogram
        """
        self.logger.info('Creating histogram')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.histplot(data[x], kde=False)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.savefig(output_filepath)
        return None

    def line_plot(self, data, x, y, title, xlabel, ylabel):
        """ Create line plot
        """
        self.logger.info('Creating line plot')
        sns.set(style="whitegrid")
        sns.set_palette("husl")
        plt.figure(figsize=(10, 6))
        ax = sns.lineplot(x=x, y=y, data=data)
        ax.grid(False)
        ax.set_title(title)

    def box_plot(self, data, x, y, title, xlabel, ylabel, output_filepath = None):
        """ Create box plot
        """
        self.logger.info('Creating box plot')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.boxplot(x=x, y=y, data=data)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.savefig(output_filepath)
        return None

    def heatmap(self, data, title, output_filepath = None):
        """ Create heatmap
        """
        self.logger.info('Creating heatmap')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(data.corr(), annot=True)
        ax.set_title(title)
        plt.savefig(output_filepath)
        return None

    def correlation_matrix(self, data, title, output_filepath = None):
        """ Create correlation matrix
        """
        self.logger.info('Creating correlation matrix')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(data.corr(), annot=True)
        ax.set_title(title)
        plt.savefig(output_filepath)
        return None

    def pairplot(self, data, title, output_filepath = None):
        """ Create pairplot
        """
        self.logger.info('Creating pairplot')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.pairplot(data)
        ax.set_title(title)
        plt.savefig(output_filepath)
        return None

    def violin_plot(self, data, x, y, title, xlabel, ylabel, output_filepath = None):
        """ Create violin plot
        """
        self.logger.info('Creating violin plot')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.violinplot(x=x, y=y, data=data)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.savefig(output_filepath)
        return None

    def joint_plot(self, data, x, y, title, output_filepath = None):
        """ Create joint plot
        """
        self.logger.info('Creating joint plot')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.jointplot(x=x, y=y, data=data)
        ax.set_title(title)
        plt.savefig(output_filepath)
        return None

    def kde_plot(self, data, x, title, output_filepath = None):
        """ Create kde plot
        """
        self.logger.info('Creating kde plot')
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.kdeplot(data[x], shade=True)
        ax.set_title(title)
        plt.savefig(output_filepath)
        return None

    def test_environment(self):

        REQUIRED_PYTHON = "python3"
        system_major = sys.version_info.major
        if REQUIRED_PYTHON == "python":
            required_major = 2
        elif REQUIRED_PYTHON == "python3":
            required_major = 3
        else:
            raise ValueError("Unrecognized python interpreter: {}".format(
                REQUIRED_PYTHON))

        if system_major != required_major:
            raise TypeError(
                "This project requires Python {}. Found: Python {}".format(
                    required_major, sys.version))
        else:
            print(">>> Development environment passes all tests!")
        return None

#%%
