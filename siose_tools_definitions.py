# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SIOSETools
                                 A QGIS plugin
 Este plugin permite consultar la cartografía SIOSE del IGN.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-10-18
        git sha              : $Format:%H$
        copyright            : (C) 2023 by IGN-UCLM
        email                : david.hernandez@uclm.es
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
CONST_GDAL_TOOL_OGR2OGR = 'ogr2ogr'
CONST_GDAL_TOOL_OGR2OGR_EXT = 'ogr2ogr.exe'
CONST_GDAL_TOOL_OGRINFO = 'ogrinfo'
CONST_GDAL_TOOL_OGRINFO_EXT = 'ogrinfo.exe'
CONST_GDAL_TOOLS_WINDOWS_BIN_BASE = 'bin'
CONST_GDAL_TOOLS_PATH = ''#'C:\\Program Files\\QGIS 3.34.15\\bin'

CONST_TEMPLATES_PATH = 'templates'
CONST_SIOSE_TEMPLATE = 'SIOSE.gpkg'
CONST_SIOSE_HR_TEMPLATE = 'SIOSEAR.gpkg'
CONST_GPKG_DRIVER_TAG = 'GPKG'
CONST_TEMPORAL_PATH = 'temp'
CONST_SETTINGS_FILE_NAME = 'siose_tools.ini'
CONST_CLIP_TYPE_SIOSEHR_ADMINISTRATIVE_UNIT = "Clip SIOSE HR administrative unit"
CONST_CLIP_TYPE_SIOSE_MAP_CANVAS = "Clip SIOSE MapCanvas"
CONST_CLIP_TYPE_SIOSE_SELECTED_FEATURES = "Clip SIOSE Selected Features"
select_clip = False
# predefined coverages querys for siose
coverages_ids_by_query = {}
CONST_COVERAGES_CATEGORY_SOIL = u'Zonas de suelo sellado'
coverages_ids_by_query[CONST_COVERAGES_CATEGORY_SOIL] = [101, 104, 111, 140, 141, 142, 143]
CONST_COVERAGES_CATEGORY_FCC = u'Fracción de cabida cubierta arbórea'
coverages_ids_by_query[CONST_COVERAGES_CATEGORY_FCC] = [302, 310, 312, 313, 316]
CONST_COVERAGES_CATEGORY_CROPS = u'Cultivos leñosos'
coverages_ids_by_query[CONST_COVERAGES_CATEGORY_CROPS] = [222, 223, 224, 231, 232, 251, 252, 253, 254, 255, 256, 257,
                                                          258, 259, 260, 241]
CONST_COVERAGES_CATEGORY_WATER = u'Zonas de agua'
coverages_ids_by_query[CONST_COVERAGES_CATEGORY_WATER] = [500, 511, 513, 514, 515, 522, 523]
# predefined coverages querys for siose hr
coverages_hr_ids_by_query = {}
CONST_COVERAGES_HR_CATEGORY_SOIL = u'Zonas de suelo sellado'
coverages_hr_ids_by_query[CONST_COVERAGES_HR_CATEGORY_SOIL] = [101, 104, 111, 140, 141, 142, 143]
# CONST_COVERAGES_HR_CATEGORY_FCC = u'Fracción de cabida cubierta arbórea'
# coverages_hr_ids_by_query[CONST_COVERAGES_HR_CATEGORY_FCC] = [302, 310, 312, 313, 316]
CONST_COVERAGES_HR_CATEGORY_CROPS = u'Cultivos leñosos'
coverages_hr_ids_by_query[CONST_COVERAGES_HR_CATEGORY_CROPS] = [222, 223, 224, 231, 232, 251, 252, 253, 254, 255, 256,
                                                                257, 258, 259, 260, 241]
CONST_COVERAGES_HR_CATEGORY_WATER = u'Zonas de agua'
coverages_hr_ids_by_query[CONST_COVERAGES_HR_CATEGORY_WATER] = [500, 511, 513, 514, 515, 522, 523]
# predefinided uses querys for siose hr
uses_ids_by_query = {}
CONST_USES_CATEGORY_INFRASTRUCTURES = u'Infraestructuras'
uses_ids_by_query[CONST_USES_CATEGORY_INFRASTRUCTURES] = [4100, 4111, 4112, 4113, 4121, 4122, 4130, 4140, 4150]
CONST_USES_CATEGORY_PRIMARY_SECTOR = u'Sector primario'
uses_ids_by_query[CONST_USES_CATEGORY_PRIMARY_SECTOR] = [1110, 1120, 1200, 1300, 1310, 1320, 1330, 1410, 1420,
                                                         1500, 1600]
CONST_USES_CATEGORY_THIRD_SECTOR = u'Sector terciario'
uses_ids_by_query[CONST_USES_CATEGORY_THIRD_SECTOR] = [3110, 3120, 3131, 3132, 3133, 3140, 3210, 3220, 3230, 3240,
                                                       3250, 3310, 3311, 3320, 3330, 3340, 3350, 3351, 3410, 3421,
                                                       3422, 3431, 3432, 3441, 3442, 3450, 3500, 4200, 4310, 4321,
                                                       4322, 4331, 4332, 4340]
CONST_USES_CATEGORY_SECONDARY_SECTOR = u'Sector secundario'
uses_ids_by_query[CONST_USES_CATEGORY_SECONDARY_SECTOR] = [2000, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190,
                                                           2210, 2220, 2230, 2310, 2320, 2330, 2340, 2350, 2400, 2410,
                                                           2420, 2430, 2441, 2442, 2443, 2444, 2500]
CONST_QUERIES_FILE_NAME = 'siose_tools_queries.json'
CONST_QUERIES_COVERAGES_TAG = 'coverages'
CONST_QUERIES_COVERAGES_HR_TAG = 'coverages_hr'
CONST_QUERY_GENERIC = 'Consulta genérica'
CONST_QUERIES_USES_TAG = 'uses'
CONST_SIOSE_CODIIGE_QML_FILE_NAME = "CODIIGE.qml"
CONST_SIOSE_HILUCS_QML_FILE_NAME = "HILUCS.qml"
CONST_SIOSE_HR_COVERAGES_QML_FILE_NAME = "SAR_COBERTURAS_simbologia.qml"
CONST_SIOSE_HR_USES_QML_FILE_NAME = "SAR_USOS_simbologia.qml"
CONST_SIOSE_HR_LAYER_NAMES_PREFIX = 'SAR_'
siose_hr_layers_with_prefix = ['TABLA_PLANA', 'T_COMBINADA', 'T_POLIGONOS', 'T_USOS', 'T_VALORES']
CONST_CLIP_SIOSE_FROM_MAP_CANVAS_TEXT = 'Recortar SIOSE a la zona visible'
CONST_CLIP_SIOSE_FROM_SELECTED_FEATURES_TEXT = 'Recortar SIOSE a la zona seleccionada'
CONST_CLIP_SIOSE_HR_FROM_ADMINISTRATIVE_UNIT_TEXT = 'Recortar SIOSE AR a un municipio'
clip_type = CONST_CLIP_SIOSE_HR_FROM_ADMINISTRATIVE_UNIT_TEXT
CONST_CLIP_SIOSE_SELECTION_AUXILIAR_BASE_NAME = 'selection'
CONST_CLIP_SIOSE_SELECTION_AUXILIAR_FIELD_ID_NAME = 'id'
CONST_VRT_FILE_TAG_OGRVRTDATASOURCE = "OGRVRTDataSource"
CONST_VRT_FILE_TAG_OGRVRTLAYER = "OGRVRTLayer"
CONST_VRT_FILE_OGRVRTLAYER_ATTRIBUTE_NAME = "name"
CONST_VRT_FILE_TAG_SRCDATASOURCE = "SrcDataSource"
CONST_VRT_FILE_TAG_SRCLAYER = "SrcLayer"
CONST_ROI_NAME = "roi"
CONST_SIOSE_T_POLIGONOS_INPUT_NAME = "siose_t_poligonos_input"
CONST_SIOSE_T_VALORES_INPUT_NAME = "siose_t_valores_input"
CONST_SIOSE_T_POLIGONOS_LAYER = "T_POLIGONOS"
CONST_SIOSE_T_VALORES_LAYER = "T_VALORES"
CONST_SIOSE_T_POLIGONOS_OUTPUT_NAME = "siose_t_poligonos_output"
CONST_SIOSE_ID_POLYGON = 'ID_POLYGON'
CONST_SIOSE_ID_COVERAGES = 'ID_COBERTURAS'
CONST_SIOSE_ID_COVERAGE = 'ID_COBERTURA'
CONST_SIOSE_ID_PARCELA = 'ID_PARCELA'
CONST_SIOSE_TABLA_PLANA_INPUT_NAME = "siose_tabla_plana_input"
CONST_SIOSE_TABLA_PLANA_LAYER = "TABLA_PLANA"
CONST_SIOSE_SIOSE_CODE = 'SIOSE_CODE'
CONST_SIOSE_HR_SIOSE_CODE = 'ROTULO'
CONST_SIOSE_HR_T_POLIGONOS_LAYER = "SAR_T_POLIGONOS"
CONST_SIOSE_HR_T_VALORES_LAYER = "SAR_T_VALORES"
CONST_SIOSE_HR_T_USOS_LAYER = "SAR_T_USOS"
CONST_SIOSE_HR_T_COMBINADA_LAYER = "SAR_T_COMBINADA"
CONST_SIOSE_HR_TABLA_PLANA_LAYER = "SAR_TABLA_PLANA"
CONST_SIOSE_HR_ADMINISTRATIVE_UNIT_FIELD_ID = "MUNICIPIO"
CONST_SIOSE_HR_ADMINISTRATIVE_UNIT_FIELD_NAME = "MUNICIPIO_NOMBRE"
CONST_NO_COMBO_SELECT = ' ... '
CONST_SIOSE_T_USOS_INPUT_NAME = "siose_t_usos_input"
CONST_SIOSE_T_COMBINADA_INPUT_NAME = "siose_t_combinada_input"
CONST_SIOSE_T_USOS_LAYER = "T_USOS"
CONST_SIOSE_T_COMBINADA_LAYER = "T_COMBINADA"
CONST_QUERY_COVERAGE_TITLE = 'Consultar coberturas'
CONST_QUERY_USES_TITLE = 'Consultar usos'
CONST_GROUP_BOX_COVERAGES_TITLE = "Seleccione coberturas y porcentaje mínimo"
CONST_GROUP_BOX_USES_TITLE = "Seleccione usos y porcentaje mínimo"
CONST_NO_COMBO_SELECT = ' ... '
CONST_SQL_GET_SIOSE_COVERAGES = ('SELECT \"TC_SIOSE_COBERTURAS\".\"ID_COBERTURAS\", \"TC_SIOSE_COBERTURAS\".'
                                 '\"DESCRIPCION_COBERTURAS\", \"TC_SIOSE_COBERTURAS\".'
                                 '\"CODE_ABREVIADO\" FROM \"TC_SIOSE_COBERTURAS\" ORDER BY \"TC_SIOSE_COBERTURAS\".\"ID_COBERTURAS\"')
CONST_SQL_GET_SIOSE_HR_COVERAGES = ('SELECT \"LISTADO_COBERTURAS\".\"ID_COBERTURA\", \"LISTADO_COBERTURAS\".'
                                 '\"DESCRIPCION\", \"LISTADO_COBERTURAS\".'
                                 '\"ETIQUETA\" FROM \"LISTADO_COBERTURAS\" ORDER BY \"LISTADO_COBERTURAS\".\"ID_COBERTURA\"')
CONST_SQL_GET_SIOSE_HR_USES = ('SELECT \"LISTADO_USOS\".\"ID_USO\", \"LISTADO_USOS\".\"DESCRIPCION\", '
                               '\"LISTADO_USOS\".\"ETIQUETA\" FROM \"LISTADO_USOS\" ORDER BY \"LISTADO_USOS\".\"ID_USO\"')
CONST_PERCENTAGE_DEFAULT_VALUE = 10
CONST_QUERY_COVERAGES_VALID_NAME = "POLIGONOS"
CONST_QUERY_USES_VALID_NAME = "USOS"
CONST_HA_SUFFIX = '_HA'
CONST_M2_SUFFIX = '_M2'
CONST_POR_SUFFIX = '_POR'
CONST_SUPERF_HA = "SUPERF_HA"
CONST_SUPERF_M2 = "SUPERF_M2"
CONST_SUPERF_POR = "SUPERF_POR"
