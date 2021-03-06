# -*- coding: utf-8 -*-
"""This file defines several Exceptions which may be thrown by SEEDS."""

__author__ = "Brian Connelly <bdc@msu.edu>"
__credits__ = "Brian Connelly"

import warnings

def warn(message):
    warnings.warn(message, RuntimeWarning, stacklevel=2)


class SEEDSError(Exception):
    """Base class for all Exceptions related to SEEDS"""
    pass

class ResourceNotDefinedError(SEEDSError):
    """Error to be raised when a Resource is requested that has not been
    defined.

    Attributes:

    *resource*
        The name of the requested Resource (string)

    """

    def __init__(self, resource):
        self.resource = resource

    def __str__(self):
        return "Resource '{resname}' not defined".format(resname=self.resource)


class PluginNotFoundError(SEEDSError):
    """Error to be raised when a Plugin (of any type) is not found

    Attributes:

    *plugin*
        The name of the plugin requested (string)
    """

    def __init__(self, plugin):
        self.plugin = plugin

    def __str__(self):
        return "Plugin '{plugname}' not found".format(plugname=self.plugin)


class PluginVersionNotFoundError(SEEDSError):
    """Error to be raised when a Plugin (of any type) that matches a specified
    version is not found 

    Attributes:

    *plugin*
        The name of the plugin requested (string)
    *version*
        The version of the plugin requested (tuple)

    """

    def __init__(self, plugin, version):
        self.plugin = plugin
        self.version = version

    def __str__(self):
        return "Plugin '{plugname}' version {version} not found".format(plugname=self.plugin, version=self.version)


class SEEDSVersionError(SEEDSError):
    """Error to be raised when the required version of SEEDS is not met

    Attributes:

    *operator*
        The operator for the version comparison
    *version*
        The version of the plugin requested (tuple)

    """

    def __init__(self, operator, version):
        self.operator = operator
        self.version = version

    def __str__(self):
        return "SEEDS version {operator}{major}.{minor}.{patch} is required".format(operator=self.operator, major=self.version[0], minor=self.version[1], patch=self.version[2])


class ActionPluginNotFoundError(PluginNotFoundError):
    """Error to be raised when a Action Plugin is not found

    Attributes:

    *action*
        The name of the Action requested (string)
    """

    def __init__(self, action):
        self.action = action

    def __str__(self):
        return "Action '{action_name}' not found".format(action_name=self.action)


class CellPluginNotFoundError(PluginNotFoundError):
    """Error to be raised when a Cell Plugin is not found

    Attributes:

    *cell*
        The name of the cell requested (string)
    """

    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return "Cell plugin '{cellname}' not found".format(cellname=self.cell)

class CellTypeError(SEEDSError):
    """Error to be raised when an invalid Cell type is used

    Attributes:

    *celltype*
        The attempted cell type ID
    """

    def __init__(self, celltype):
        self.celltype = celltype

    def __str__(self):
        return "Cell type '{celltype}' not found".format(celltype=self.celltype)


class ResourceCellPluginNotFoundError(PluginNotFoundError):
    """Error to be raised when a ResourceCell Plugin is not found

    Attributes:

    *resource*
        The name of the ResourceCell requested (string)
    """

    def __init__(self, resource):
        self.resource = resource

    def __str__(self):
        return "ResourceCell '{rescell}' not found".format(rescell=self.resource)


class TopologyPluginNotFoundError(PluginNotFoundError):
    """Error to be raised when a Topology Plugin is not found

    Attributes:

    *topology*
        The name of the Topology requested (string)
    """

    def __init__(self, topology):
        self.topology = topology

    def __str__(self):
        return "Topology type '{toptype}' not found".format(toptype=self.topology)


class InvalidParameterValue(SEEDSError):
    """Error to be raised when a given parameter value is invalid

    Attributes:

    *section*
        The name of the section in which the parameter is defined
    *parameter*
        The name of the parameter
    """

    def __init__(self, section, parameter):
        self.section = section
        self.parameter = parameter

    def __str__(self):
        return "Invalid value for parameter '{section}.{param}'".format(section=self.section, param=self.parameter)

class NonExistentNodeError(SEEDSError):
    """Error to be raised when a node does not exist

    Attributes:

    *id*
        The ID of the node
    """

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "Node {node} does not exist in Topology".format(node=self.id)

class NonExistentEdgeError(SEEDSError):
    """Error to be raised when an edge does not exist

    Attributes:

    *src*
        The ID of the first node connected with the edge
    *dest*
        The ID of the second node connected with the edge
    """

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __str__(self):
        return "Edge {source}-{dest} does not exist in Topology".format(source=self.src, dest=self.dest)

class ConfigurationError(SEEDSError):
    """Error to be raised when an invalid configuration is given, either
    through one bad parameter value or through parameter value conflicts.

    Attributes:

    *message*
        The message to be displayed (string)

    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class VersionStringFormatError(SEEDSError):
    """Error to be raised when an invalid string specifying a version number is
    given. The correct format is <operator><major>.<minor>, where major and
    minor are integers and operator is one of <, <=, =, >=, or >.

    Attributes:

    *message*
        The message to be displayed (string)

    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class VersionOperatorError(SEEDSError):
    """Error to be raised when an invalid version comparison operator is used.  Valued operators are '<', '<=', '=', '>', and '>='.

    Attributes:

    *message*
        The message to be displayed (string)

    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class IntRangelistFormatError(SEEDSError):
    """Error to be raised when an invalid string specifying a range list of
    integers is given.  The correct format is <r>,<r>,... where <r> is either
    <integer> or <integer>-<integer>.


    Attributes:

    *message*
        The message to be displayed (string)

    """

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s
