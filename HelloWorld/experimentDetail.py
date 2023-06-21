from TestModel import models
import json
from django.core import serializers
from django.db import connection
def getConstellationGroup(experimentId):
    constellation_group_select = models.ConstellationGroup.objects.filter(experimentId=experimentId)
    constellation_groups = json.loads(serializers.serialize("json", constellation_group_select))
    cons_list = []
    for cons in constellation_groups:
        cons_temp = cons["fields"]
        cons_temp["id"] = cons["pk"]
        cons_temp["regionInfos"] = getRegion(experimentId=experimentId, consId=cons["pk"])
        cons_temp["staticNodes"] = []
        cons_temp["classicOrbitSatellites"] = []
        cons_temp["movingNodes"] = []
        cons_temp["tleOrbitSatellites"] = []
        cons_temp["constellationInfos"] = getConstellation(experimentId=experimentId, consId=cons["pk"])
        # cons_temp["constellationInfos"] = []
        cons_list.append(cons_temp)
    return cons_list


def getRegion(experimentId, consId=0):
    regions_list = []
    with connection.cursor() as cursor:
        select = f"select region_id,region_info_list from ground_region where experiment_id={experimentId}"
        cursor.execute(select)
        result = cursor.fetchall()
        for res in result:
            regionId = res[0]
            region_temp = json.loads(res[1])
            region_consId = region_temp["constellationGroupId"]
            # 通过比较查询结果是否是该星座组下的区域
            if region_consId == consId:
                region_temp["terminals"] = getStationByExpId(experimentId, regionId, consId)
                regions_list.append(region_temp)

    return regions_list


def getConstellation(experimentId, consId=0):
    constellations_select = models.Constellation.objects.filter(experimentId=experimentId, constellationGroupId=consId)
    constellations = json.loads(serializers.serialize("json", constellations_select))
    constellationInfos = []
    # 处理每个星座的映射
    for con in constellations:
        temp = con['fields']
        temp["id"] = con['pk']
        temp['satellites'] = getSatsByconsId(experimentId=experimentId, consId=con['pk'], groupId=consId)
        temp["twoLineParam"] = {
            "tle1": temp.pop("tle1"),
            "tle2": temp.pop("tle2")
        }
        temp["sixNumbersParam"] = {
            "orientation": {
                "inclination": temp.pop("inclination"),
                "argOfPerigee": temp.pop("argOfPerigee"),
                "raan": temp.pop("raan"),
            },
            "shape": {
                "_apogeeAltitude": temp.pop("_apogeeAltitude"),
                "_perigeeAltitude": temp.pop("_perigeeAltitude"),
            },
            "trueAnomaly": temp.pop("trueAnomaly")
        }
        temp["polarOribit"] = False
        temp["interPlaneSpacing"] = 1.0
        constellationInfos.append(temp)
    return constellationInfos


def getSatsByconsId(experimentId, consId=0, groupId=0):
    satellite_select = models.Satellite.objects.filter(experimentId=experimentId, constellationId=consId,
                                                       constellationGroupId=groupId)
    satellite = json.loads(serializers.serialize("json", satellite_select))
    satellites = []
    # 处理每个卫星的映射
    for sat in satellite:
        sat_temp = sat['fields']
        sat_id = sat['pk']
        sat_temp["ipAddress"] = "--.--.--.--"

        sat_temp["communicationDevices"] = getDeviceByNodeId(sat_id)
        # 处理每个设备
        orientation = {
            "inclination": sat_temp.pop("inclination"),
            "argOfPerigee": sat_temp.pop("argOfPerigee"),
            "raan": sat_temp.pop("raan")
        }
        shape = {
            "_apogeeAltitude": sat_temp.pop("_apogeeAltitude"),
            "_perigeeAltitude": sat_temp.pop("_perigeeAltitude")
        },
        sat_temp["orientation"] = orientation
        sat_temp["shape"] = shape
        sat_temp["id"] = sat_id
        satellites.append(sat_temp)
    return satellites


def getDeviceByNodeId(nodeId):
    device_select = models.Device.objects.filter(nodeId=nodeId)
    devices = json.loads(serializers.serialize("json", device_select))
    devices_list = []
    for device in devices:
        device_temp = device["fields"]
        device_temp["id"] = device["pk"]
        device_temp["receiver"] = {
            "trackingError": device_temp.pop("trackingError"),
            "fNoiseTemperature": device_temp.pop("fNoiseTemperature"),
            "lnbGain": device_temp.pop("lnbGain"),
            "maxDepoint": device_temp.pop("maxDepoint"),
            "otherReGainLoss": device_temp.pop("otherReGainLoss"),
            "receiveThreshold": device_temp.pop("receiveThreshold"),
            "aptLoss": device_temp.pop("aptLoss"),
            "antennaReGain": device_temp.pop("antennaReGain"),
            "reEfficiency": device_temp.pop("reEfficiency"),
        }
        device_temp["deviceEquipConfig"] = {
            "elevation": device_temp.pop("elevation"),
            "pointingType": device_temp.pop("pointingType"),
            "minElevation": device_temp.pop("minElevation"),
            "halfAngleMinorAxis": device_temp.pop("halfAngleMinorAxis"),
            "dbeamNum": device_temp.pop("dbeamNum"),
            "azimuth": device_temp.pop("azimuth"),
            "maxRange": device_temp.pop("maxRange"),
            "minAzimuth": device_temp.pop("minAzimuth"),
            "ubeamNum": device_temp.pop("ubeamNum"),
            "halfAngleMajorAxis": device_temp.pop("halfAngleMajorAxis"),
            "maxAzimuth": device_temp.pop("maxAzimuth"),
            "beamFov": device_temp.pop("beamFov"),
            "maxElevation": device_temp.pop("maxElevation"),
        }
        device_temp["linkConfig"] = {
            "bandWidth": device_temp.pop("bandWidth"),
            "communicationSpeed": device_temp.pop("communicationSpeed"),
            "modulationMode": device_temp.pop("modulationMode"),
            "waveLength": device_temp.pop("waveLength"),
            "communication": device_temp.pop("communication"),
        }
        device_temp["transmitter"] = {
            "diffractionLimit": device_temp.pop("diffractionLimit"),
            "fec": device_temp.pop("fec"),
            "backoff": device_temp.pop("backoff"),
            "rolloff": device_temp.pop("rolloff"),
            "divergenceAngle": device_temp.pop("divergenceAngle"),
            "freq": device_temp.pop("freq"),
            "bUtil": device_temp.pop("bUtil"),
            "contour": device_temp.pop("contour"),
            "radiationModel": device_temp.pop("radiationModel"),
            "trPower": device_temp.pop("trPower"),
            "diameter": device_temp.pop("diameter"),
            "trEfficiency": device_temp.pop("trEfficiency"),
            "antennaTrGain": device_temp.pop("antennaTrGain"),
            "otherTrGainLoss": device_temp.pop("otherTrGainLoss"),
            "beamDistribution": device_temp.pop("beamDistribution"),
            "polarizationMode": device_temp.pop("polarizationMode"),
        }
        devices_list.append(device["fields"])
    return devices_list


def getStationByExpId(experimentId, regionId=0, consId=0):
    if regionId == 0:
        facility_select = models.Facility.objects.filter(experimentId=experimentId, regionId__isnull=True,
                                                         constellationGroupId=consId)
    else:
        facility_select = models.Facility.objects.filter(experimentId=experimentId, regionId=regionId,
                                                         constellationGroupId=consId)
    facilities = json.loads(serializers.serialize("json", facility_select))
    facility_list = []
    for facility in facilities:
        facility_temp = facility["fields"]
        facility_temp["id"] = facility["pk"]
        facility_temp["communicationDevices"] = getDeviceByNodeId(facility["pk"])
        facility_temp["position"] = {
            "altitude": facility_temp.pop("altitude"),
            "latitude": facility_temp.pop("latitude"),
            "longitude": facility_temp.pop("longitude"),
        }
        facility_list.append(facility_temp)
    return facility_list
