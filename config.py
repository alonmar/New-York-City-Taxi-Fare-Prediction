from distutils.command.config import config


config = {
	'version': 'v1',
	'config': {
		'visState': {
			'filters': [],
			'layers': [{
				'id': 'ohq60rq',
				'type': 'point',
				'config': {
					'dataId': 'data_1',
					'label': 'pickup',
					'color': [118, 255, 127],
					'highlightColor': [252, 242, 26, 255],
					'columns': {
						'lat': 'pickup_latitude',
						'lng': 'pickup_longitude',
						'altitude': None
					},
					'isVisible': True,
					'visConfig': {
						'radius': 7,
						'fixedRadius': False,
						'opacity': 0.8,
						'outline': False,
						'thickness': 2,
						'strokeColor': None,
						'colorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'strokeColorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'radiusRange': [0, 50],
						'filled': True
					},
					'hidden': False,
					'textLabel': [{
						'field': None,
						'color': [255, 255, 255],
						'size': 18,
						'offset': [0, 0],
						'anchor': 'start',
						'alignment': 'center'
					}]
				},
				'visualChannels': {
					'colorField': {
						'name': False,
						'type': 'integer'
					},
					'colorScale': 'quantile',
					'strokeColorField': None,
					'strokeColorScale': 'quantile',
					'sizeField': None,
					'sizeScale': 'linear'
				}
			}, {
				'id': 'fgocszd',
				'type': 'point',
				'config': {
					'dataId': 'data_1',
					'label': 'dropoff',
					'color': [255, 255, 255],
					'highlightColor': [252, 242, 26, 255],
					'columns': {
						'lat': 'dropoff_latitude',
						'lng': 'dropoff_longitude',
						'altitude': None
					},
					'isVisible': True,
					'visConfig': {
						'radius': 7,
						'fixedRadius': False,
						'opacity': 0.8,
						'outline': False,
						'thickness': 2,
						'strokeColor': None,
						'colorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'strokeColorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'radiusRange': [0, 50],
						'filled': True
					},
					'hidden': False,
					'textLabel': [{
						'field': None,
						'color': [255, 255, 255],
						'size': 18,
						'offset': [0, 0],
						'anchor': 'start',
						'alignment': 'center'
					}]
				},
				'visualChannels': {
					'colorField': {
						'name': False,
						'type': 'integer'
					},
					'colorScale': 'quantile',
					'strokeColorField': None,
					'strokeColorScale': 'quantile',
					'sizeField': None,
					'sizeScale': 'linear'
				}
			}, {
				'id': 'q00e0co',
				'type': 'arc',
				'config': {
					'dataId': 'data_1',
					'label': 'pickup -> dropoff arc',
					'color': [118, 255, 127],
					'highlightColor': [252, 242, 26, 255],
					'columns': {
						'lat0': 'pickup_latitude',
						'lng0': 'pickup_longitude',
						'lat1': 'dropoff_latitude',
						'lng1': 'dropoff_longitude'
					},
					'isVisible': False,
					'visConfig': {
						'opacity': 0.8,
						'thickness': .4,
						'colorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'sizeRange': [0, 10],
						'targetColor': [255, 255, 255]
					},
					'hidden': False,
					'textLabel': [{
						'field': None,
						'color': [255, 255, 255],
						'size': 18,
						'offset': [0, 0],
						'anchor': 'start',
						'alignment': 'center'
					}]
				},
				'visualChannels': {
					'colorField': None,
					'colorScale': 'quantile',
					'sizeField': None,
					'sizeScale': 'linear'
				}
			}, {
				'id': 'w0gcrw',
				'type': 'line',
				'config': {
					'dataId': 'data_1',
					'label': 'pickup -> dropoff line',
					'color': [136, 87, 44],
					'highlightColor': [252, 242, 26, 255],
					'columns': {
						'lat0': 'pickup_latitude',
						'lng0': 'pickup_longitude',
						'alt0': None,
						'lat1': 'dropoff_latitude',
						'lng1': 'dropoff_longitude',
						'alt1': None
					},
					'isVisible': False,
					'visConfig': {
						'opacity': 0.8,
						'thickness': 2,
						'colorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'sizeRange': [0, 10],
						'targetColor': None,
						'elevationScale': 1
					},
					'hidden': False,
					'textLabel': [{
						'field': None,
						'color': [255, 255, 255],
						'size': 18,
						'offset': [0, 0],
						'anchor': 'start',
						'alignment': 'center'
					}]
				},
				'visualChannels': {
					'colorField': None,
					'colorScale': 'quantile',
					'sizeField': None,
					'sizeScale': 'linear'
				}
			},{
				'id': 'hwkahn9',
				'type': 'cluster',
				'config': {
					'dataId': 'data_1',
					'label': 'grid',
					'color': [255, 153, 31],
					'highlightColor': [252, 242, 26, 255],
					'columns': {
						'lat': 'pickup_latitude',
						'lng': 'pickup_longitude',
						'altitude': None
					},
					'isVisible': False,
					'visConfig': {
						'opacity': 0.8,
						'strokeOpacity': 0.8,
						'thickness': 0.5,
						'strokeColor': None,
						'colorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'strokeColorRange': {
							'name': 'Global Warming',
							'type': 'sequential',
							'category': 'Uber',
							'colors': ['#5A1846', '#900C3F', '#C70039', '#E3611C', '#F1920E', '#FFC300']
						},
						'coverage': 0.9,
						'radius': 10,
						'gridSize': 100,
						'hexagonRadius': 0.1,
						'sizeRange': [0, 100],
						'radiusRange': [0, 50],
						'heightRange': [0, 500],
						'elevationScale': 10,
						'enableElevationZoomFactor': True,
						'stroked': False,
						'filled': True,
						'enable3d': False,
						'wireframe': False
					},
					'hidden': False,
					'textLabel': [{
						'field': None,
						'color': [255, 255, 255],
						'size': 18,
						'offset': [0, 0],
						'anchor': 'start',
						'alignment': 'center'
					}]
				},
				'visualChannels': {
					'colorField': None,
					'colorScale': 'quantile',
					'strokeColorField': None,
					'strokeColorScale': 'quantile',
					'sizeField': None,
					'sizeScale': 'linear',
					'heightField': None,
					'heightScale': 'linear',
					'radiusField': None,
					'radiusScale': 'linear'
				}
			}
			],
			'interactionConfig': {
				'tooltip': {
					'fieldsToShow': {
						'data_1': [{
							'name': 'fare_amount',
							'format': None
						}, {
							'name': 'pickup_year',
							'format': None
						}, {
							'name': 'pickup_week',
							'format': None
						}, {
							'name': 'pickup_day_week',
							'format': None
						}, {
							'name': 'pickup_hour',
							'format': None
						}]
					},
					'compareMode': False,
					'compareType': 'absolute',
					'enabled': True
				},
				'brush': {
					'size': 0.5,
					'enabled': False
				},
				'geocoder': {
					'enabled': False
				},
				'coordinate': {
					'enabled': False
				}
			},
			'layerBlending': 'normal',
			'splitMaps': [],
			'animationConfig': {
				'currentTime': None,
				'speed': 1
			}
		},
		'mapState': {
			'bearing': 0,
			'dragRotate': False,
			'latitude': 40.735455,
			'longitude': -73.992516,
			'pitch': 0,
			'zoom': 15,
			'isSplit': False
		},
		'mapStyle': {
			'styleType': 'dark',
			'topLayerGroups': {},
			'visibleLayerGroups': {
				'label': True,
				'road': True,
				'border': False,
				'building': True,
				'water': True,
				'land': True,
				'3d building': False
			},
			'threeDBuildingColor': [9.665468314072013, 17.18305478057247, 31.1442867897876],
			'mapStyles': {}
		}
	}
}