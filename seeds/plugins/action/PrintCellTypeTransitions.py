# -*- coding: utf-8 -*-
"""
Print the number of transitions between each cell type
"""

__author__ = "Brian Connelly <bdc@msu.edu>"
__credits__ = "Brian Connelly"


import csv

from seeds.Action import *
from seeds.Plugin import *


class PrintCellTypeTransitions(Action, Plugin):
    """ Write the number of transitions between cells types

    Configuration is done in the [PrintCellTypeTransitions] section

    Configuration Options:

    epoch_start
        The epoch at which to start executing (default: 0)
    epoch_end
        The epoch at which to stop executing (default: end of experiment)
    frequency
        The frequency (epochs) at which to execute (default: 1)
    priority
        The priority of this action.  Actions with higher priority get run
        first.  (default: 0)
    filename
        The name of the file to write to (default: cell_type_transitions.csv)
    header
        Whether or not to write a header to the output file.  The header will
        be an uncommented, comma-separated list of property names corresponding
        to the data in each row. (default: True)


    Configuration Example:

    [PrintCellTypeTransitions]
    epoch_start = 3
    epoch_end = 100
    frequency = 2
    priority = 0
    filename = cell_type_transitions.csv
    header = True

    """

    __name__ = "PrintCellTypeTransitions"
    __version__ = (1,0)
    __author__ = "Brian Connelly <bdc@msu.edu>"
    __credits__ = "Brian Connelly"
    __description__ = "Print the number of transitions between each cell type"
    __type__ = 4
    __requirements__ = []


    def __init__(self, experiment, label=None):
        """Initialize the PrintCellTypeTransitions Action"""

        super(PrintCellTypeTransitions, self).__init__(experiment,
                                                 name="PrintCellTypeTransitions",
                                                 label=label)

        self.epoch_start = self.experiment.config.getint(self.config_section, 'epoch_start', 0)
        self.epoch_end = self.experiment.config.getint(self.config_section, 'epoch_end', default=self.experiment.config.getint('Experiment', 'epochs', default=-1))
        self.frequency = self.experiment.config.getint(self.config_section, 'frequency', 1)
        self.priority = self.experiment.config.getint(self.config_section, 'priority', 0)
        self.filename = self.experiment.config.get(self.config_section, 'filename', 'cell_type_transitions.csv')
        self.header = self.experiment.config.getboolean(self.config_section, 'header', default=True)

        self.types = self.experiment.population._cell_class.types
        self.max_types = self.experiment.population._cell_class.max_types

        data_file = self.datafile_path(self.filename)
        self.transitions = ['%s->%s' % (ftype, ttype) for ftype in self.types for ttype in self.types]
        fieldnames = ['epoch'] + self.transitions
        self.writer = csv.DictWriter(open(data_file, 'w'), fieldnames)

        if self.header:
            self.writer.writeheader()

    def update(self):
        """Execute the action"""
        if self.skip_update():
	        return

        row = {'epoch' : self.experiment.epoch}

        if self.experiment.epoch == 0:
            for transition in self.transitions:
                row[transition] = 0
        else:
            trans_counts = [self.experiment.data['population']['transitions'][f][t]
                    for f in range(self.max_types)
                    for t in range(self.max_types)]
            for transition, count in zip (self.transitions, trans_counts):
                row[transition] = count

        self.writer.writerow(row)
