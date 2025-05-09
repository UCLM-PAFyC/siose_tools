# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SIOSETools
                                 A QGIS plugin
 Este plugin permite consultar la cartografía SIOSE del IGN.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-10-28
        copyright            : (C) 2023 by IGN-UCLM
        email                : david.hernandez@uclm.es
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SIOSETools class from file SIOSETools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .siose_tools import SIOSETools
    return SIOSETools(iface)
