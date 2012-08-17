# -*- coding: utf-8 -*-
"""
Print the coordinates of each cell and its type
"""

__author__ = "Brian Connelly <bdc@msu.edu>"
__credits__ = "Brian Connelly"

import csv

from seeds.Action import *
from seeds.Plugin import *


class PrintCellLocations(Action, Plugin):
    """ Write the x,y coordinates of each cell and its type

    Configuration parameters for this action are set in the
    [PrintCellLocations] section.

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
        Base name for files.  The epoch at which the file was created and the
        extension (see format) will also comprise the resulting file name.  For
        example, a filename of 'cell_locations' when run at epoch 1200 would
        produce the file cell_locations-001200.csv.  (default:
        'cell_locations')
    header
        Whether or not to write a header to the output file.  The header will
        be an uncommented, comma-separated list of property names corresponding
        to the data in each row. (default: True)

    Configuration Example:

    [PrintCellLocations]
    epoch_start = 3
    epoch_end = 100
    frequency = 2
    priority = 0
    filename = cell_locations
    header = True

    """

    __name__ = "PrintCellLocations"
    __version__ = (1,0)
    __author__ = "Brian Connelly <bdc@msu.edu>"
    __credits__ = "Brian Connelly"
    __description__ = "Print the coordinates of each cell and its type"
    __type__ = 4
    __requirements__ = []

    def __init__(self, experiment, label=None):
        """Initialize the PrintCellLocations Action"""
        super(PrintCellLocations, self).__init__(experiment, name="PrintCellLocations", label=label)

        self.epoch_start = self.experiment.config.getint(self.config_section, 'epoch_start', 0)
        self.epoch_end = self.experiment.config.getint(self.config_section, 'epoch_end',
            default=self.experiment.config.getint('Experiment', 'epochs', default=-1))
        self.frequency = self.experiment.config.getint(self.config_section, 'frequency', 1)
        self.priority = self.experiment.config.getint(self.config_section, 'priority', 0)
        self.filename = self.experiment.config.get(self.config_section, 'filename', 'cell_locations')
        self.header = self.experiment.config.getboolean(self.config_section, 'header', default=True)

    def update(self):
        """Execute the Action"""
        if self.skip_update():
	        return

        filename = "%s-%06d.csv" % (self.filename, self.experiment.epoch)
        data_file = self.datafile_path(filename)
        fieldnames = ['epoch','cell_id','node_id','x','y','type']
        with open(data_file, 'w') as handle:
            self.writer = csv.DictWriter(open(data_file, 'w'), fieldnames)
            if self.header:
                self.writer.writeheader()

            g = self.experiment.population.topology.graph
            for n in g.nodes():
                cell = g.node[n]['cell']
                (xpos, ypos) = cell.coords()

                row = { 'epoch' : self.experiment.epoch,
                        'cell_id' : cell.id,
                        'node_id' : cell.node,
                        'x' : xpos,
                        'y' : ypos,
                        'type' : cell.type}
                self.writer.writerow(row)

