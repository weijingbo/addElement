import json

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from HelloWorld.experimentDetail import getRegion, getConstellation, getStationByExpId, getConstellationGroup, \
    getDeviceByNodeId
from TestModel import models
from django.core import serializers
from django.utils import timezone


@api_view(['GET'])
def getExperimentDetail(request, experiment_id):
    experiment = models.Experiment.objects.filter(id=experiment_id)
    data = json.loads(serializers.serialize("json", experiment))[0]["fields"]
    data["experimentId"] = experiment_id
    data["regionInfos"] = getRegion(experimentId=experiment_id)
    data["movingNodes"] = []
    data["tleOrbitSatellites"] = []
    data["constellationInfos"] = getConstellation(experiment_id)
    data["staticNodes"] = getStationByExpId(experiment_id)
    data["constellationGroupInfos"] = getConstellationGroup(experiment_id)
    data["externalIdBaseOfExperimentId"] = experiment_id << 32  # 实验ID偏移32位后的结果
    data["classicOrbitSatellites"] = []
    # data["constellationInfos"] = []
    # data["constellationGroupInfos"] = []
    # data["regionInfos"] =[]
    return_json = {
        "errorCode": 200,
        "errorMsg": "获取实验成功",
        "data": data

    }
    return JsonResponse(return_json, safe=False)
    # with open('D:\dev\DjangoTest\HelloWorld\HelloWorld\getConfig.json', encoding='utf-8') as f:
    #     settings = json.load(f)
    #     return JsonResponse(settings, safe=False)


@api_view(['GET'])
def getSpectrumConfig(request, experiment_id, cons_id):
    spectrumConfig = models.SpectrumConfig.objects.filter(experimentId=experiment_id, constellationId=cons_id)
    if len(spectrumConfig) != 0:
        result = json.loads(serializers.serialize("json", spectrumConfig))
        spectrum_temp = result[0]["fields"]
        spectrum_temp["fdbChCarries"] = eval(spectrum_temp["fdbChCarries"])
        spectrum_temp["fdbChPolar"] = eval(spectrum_temp["fdbChPolar"])
        spectrum_temp["fdbFec"] = eval(spectrum_temp["fdbFec"])
        spectrum_temp["fdbModcod"] = eval(spectrum_temp["fdbModcod"])
        spectrum_temp["fubChCarries"] = eval(spectrum_temp["fubChCarries"])
        spectrum_temp["fubChPolar"] = eval(spectrum_temp["fubChPolar"])
        spectrum_temp["fubFec"] = eval(spectrum_temp["fubFec"])
        spectrum_temp["fubModcod"] = eval(spectrum_temp["fubModcod"])
        spectrum_temp["udbChCarries"] = eval(spectrum_temp["udbChCarries"])
        spectrum_temp["udbChPolar"] = eval(spectrum_temp["udbChPolar"])
        spectrum_temp["udbFec"] = eval(spectrum_temp["udbFec"])
        spectrum_temp["udbModcod"] = eval(spectrum_temp["udbModcod"])
        spectrum_temp["uubChCarries"] = eval(spectrum_temp["uubChCarries"])
        spectrum_temp["uubChPolar"] = eval(spectrum_temp["uubChPolar"])
        spectrum_temp["uubFec"] = eval(spectrum_temp["uubFec"])
        spectrum_temp["uubModcod"] = eval(spectrum_temp["uubModcod"])
        dict = {
            "errorCode": 200,
            "data": {
                "spectrumConfig": spectrum_temp
            }
        }
        return JsonResponse(dict, safe=False)
    else:
        dict = {
            "errorCode": 0,
            "errorMsg": "频谱保存失败"
        }
        return JsonResponse(dict, safe=False)


@api_view(['POST'])
def saveSpectrumConfig(request):
    body = json.loads(request.body.decode('utf-8'))
    models.SpectrumConfig.objects.create(
        id=body["id"],
        name=body["name"],
        experimentId=body["experimentId"],
        constellationId=body["constellationId"],
        uubChBw=body["uubChBw"],
        uubChNum=body["uubChNum"],
        uubBwTot=body["uubBwTot"],
        uubChCarries=body["uubChCarries"],
        uubChK=body["uubChK"],
        uubChPolar=body["uubChPolar"],
        uubModcod=body["uubModcod"],
        uubRolloff=body["uubRolloff"],
        udbChBw=body["udbChBw"],
        udbChNum=body["udbChNum"],
        udbBwTot=body["udbBwTot"],
        udbChCarries=body["udbChCarries"],
        udbChK=body["udbChK"],
        udbChPolar=body["udbChPolar"],
        udbModcod=body["udbModcod"],
        udbRolloff=body["udbRolloff"],
        fubChBw=body["fubChBw"],
        fubChNum=body["fubChNum"],
        fubBwTot=body["fubBwTot"],
        fubChCarries=body["fubChCarries"],
        fubChK=body["fubChK"],
        fubChPolar=body["fubChPolar"],
        fubModcod=body["fubModcod"],
        fubRolloff=body["fubRolloff"],
        fdbChBw=body["fdbChBw"],
        fdbChNum=body["fdbChNum"],
        fdbBwTot=body["fdbBwTot"],
        fdbChCarries=body["fdbChCarries"],
        fdbChK=body["fdbChK"],
        fdbChPolar=body["fdbChPolar"],
        fdbModcod=body["fdbModcod"],
        fdbRolloff=body["fdbRolloff"],
        uubFec=body["uubFec"],
        udbFec=body["udbFec"],
        fubFec=body["fubFec"],
        fdbFec=body["fdbFec"],
        uubFrequencyPoint=body["uubFrequencyPoint"],
        udbFrequencyPoint=body["udbFrequencyPoint"],
        fubFrequencyPoint=body["fubFrequencyPoint"],
        fdbFrequencyPoint=body["fdbFrequencyPoint"],
    )
    models.Experiment.objects.filter(id=body["experimentId"]).update(internalIdMax=body["id"])
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


@api_view(['POST'])
def addConstellationGroup(request, experiment_id):
    body = json.loads(request.body.decode('utf-8'))
    experimentId = body["experimentId"]
    id = body["id"]
    showName = body["showName"]
    group = models.ConstellationGroup.objects.filter(id=id).first()
    if group:
        group.showName = showName
        group.save()
    else:
        models.ConstellationGroup.objects.create(experimentId=experimentId, showName=showName, id=id,
                                                 isHighOrbitConstellationGroup=0)
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


@api_view(['POST'])
def deleteConstellationGroupList(request):
    body = json.loads(request.body.decode('utf-8'))
    idList = body["idList"]
    for id in idList:
        # 这里需要把该星座组下的星座、区域、卫星、地面站等都要删除，暂时先只删除星座组
        models.ConstellationGroup.objects.filter(id=id).delete()
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


@api_view(['POST'])
def addConstellation(request):
    body = json.loads(request.body.decode('utf-8'))
    experimentId = body["experimentId"]
    constellationInfo = body["constellationInfo"]
    internalIdMax = body["internalIdMax"]
    cons = models.Constellation.objects.create(
        id=constellationInfo["id"],
        showName=constellationInfo["showName"],
        nodeType=constellationInfo["nodeType"],
        numberOfPlanes=constellationInfo["numberOfPlanes"],
        numberOfSatsPerPlane=constellationInfo["numberOfSatsPerPlane"],
        trueAnomalyInterval=0,
        raanSpread=constellationInfo["raanSpread"],
        experimentId=experimentId,
        zoningStatus=0,
        constellationGroupId=constellationInfo["constellationGroupId"],
        _perigeeAltitude=constellationInfo["_perigeeAltitude"],
        _apogeeAltitude=constellationInfo["_apogeeAltitude"],
        inclination=constellationInfo["inclination"],
        raan=constellationInfo["raan"],
        constellationType=constellationInfo["constellationType"],
        argOfPerigee=constellationInfo["argOfPerigee"],
        trueAnomaly=constellationInfo["trueAnomaly"]
    )

    cons.save()
    sat_list = []
    for sat in constellationInfo["satellites"]:
        sat_list.append(models.Satellite(
            id=sat["id"],
            showName=sat["showName"],
            nodeType=sat["nodeType"],
            _apogeeAltitude=sat["_apogeeAltitude"],
            _perigeeAltitude=sat["_perigeeAltitude"],
            inclination=sat["inclination"],
            argOfPerigee=sat["argOfPerigee"],
            raan=sat["raan"],
            trueAnomaly=sat["trueAnomaly"],
            attitudeSeg=sat["attitudeSeg"],
            constraintOffset=sat["constraintOffset"],
            isMainSatellite=sat["isMainSatellite"],
            constellationId=sat["constellationId"],
            planeIndex=sat["planeIndex"],
            interPlaneIndex=sat["interPlaneIndex"],
            deviceNumberLimit=sat["deviceNumberLimit"],
            experimentId=experimentId,
            constellationGroupId=sat["constellationGroupId"],
            tle1=sat["tle1"],
            tle2=sat["tle2"]
        ))

    models.Satellite.objects.bulk_create(sat_list)
    models.Experiment.objects.filter(id=experimentId).update(internalIdMax=internalIdMax)
    result = {
        "errorCode": 200,
        "errorMsg": "插入成功"
    }
    return JsonResponse(result, safe=False)


def deleteConstellation(request):
    body = json.loads(request.body.decode('utf-8'))
    experimentId = body["experimentId"]
    id = body["id"]
    models.Constellation.objects.filter(id=id).first().delete()
    models.Satellite.objects.filter(constellationId=id).delete()
    models.Device.objects.filter(nodeId=id).delete()
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


def modifyConstellationName(request):
    body = json.loads(request.body.decode('utf-8'))
    showName = body["showName"]
    id = body["id"]
    models.Constellation.objects.filter(id=id).update(showName=showName)
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


def modifyNodeDeviceList(request):
    body = json.loads(request.body.decode('utf-8'))
    devices = body["devices"]
    targetId = body["targetId"]
    internalIdMax = body["internalIdMax"]
    experimentId = body["experimentId"]
    targetType = body["targetType"]
    if targetType == "constellation":
        targets = models.Satellite.objects.filter(constellationId=targetId)
    if targetType == "region":
        targets = models.Facility.objects.filter(regionId=targetId)
    for tr in targets:
        models.Device.objects.filter(devicePatternId=targetId).delete()
        device_list = []
        for device in devices.values():
            if device is not None:
                # ID 问题还需要处理
                deviceEquipConfig = device["deviceEquipConfig"]
                linkConfig = device["linkConfig"]
                receiver = device["receiver"]
                transmitter = device["transmitter"]
                device_temp = models.Device(
                    nodeId=tr.id,
                    id=internalIdMax,
                    devicePatternId=0,  # 后续可能还要修改
                    deviceName=device["deviceName"],
                    deviceType=device["deviceType"],
                    azimuth=deviceEquipConfig["azimuth"],
                    elevation=deviceEquipConfig["elevation"],
                    maxAzimuth=deviceEquipConfig["maxAzimuth"],
                    maxElevation=deviceEquipConfig["maxElevation"],
                    minAzimuth=deviceEquipConfig["minAzimuth"],
                    minElevation=deviceEquipConfig["minElevation"],
                    pointingType=deviceEquipConfig["pointingType"],
                    antennaReGain=receiver["antennaReGain"],
                    aptLoss=receiver["aptLoss"],
                    fNoiseTemperature=receiver["fNoiseTemperature"],
                    otherReGainLoss=receiver["otherReGainLoss"],
                    reEfficiency=receiver["reEfficiency"],
                    antennaTrGain=transmitter["antennaTrGain"],
                    beamDistribution=transmitter["antennaTrGain"],
                    diameter=transmitter["antennaTrGain"],
                    diffractionLimit=transmitter["antennaTrGain"],
                    divergenceAngle=transmitter["antennaTrGain"],
                    otherTrGainLoss=transmitter["antennaTrGain"],
                    trEfficiency=transmitter["antennaTrGain"],
                    trPower=transmitter["antennaTrGain"]
                )
                if device["deviceType"] == 1:
                    device_temp.maxRange = deviceEquipConfig["maxRange"]
                    device_temp.bandWidth = linkConfig["bandWidth"]
                    device_temp.communication = linkConfig["communication"]
                    device_temp.communicationSpeed = linkConfig["communicationSpeed"]
                    device_temp.modulationMode = linkConfig["modulationMode"]
                    device_temp.waveLength = linkConfig["waveLength"]
                    device_temp.receiveThreshold = receiver["receiveThreshold"]
                    device_temp.trackingError = receiver["trackingError"]
                else:
                    device_temp.beamFov = deviceEquipConfig["beamFov"]
                    device_temp.dbeamNum = deviceEquipConfig["azimuth"]
                    device_temp.halfAngleMajorAxis = deviceEquipConfig["halfAngleMajorAxis"]
                    device_temp.halfAngleMinorAxis = deviceEquipConfig["halfAngleMinorAxis"]
                    device_temp.modulationMode = linkConfig["modulationMode"]
                    device_temp.lnbGain = receiver["lnbGain"]
                    device_temp.maxDepoint = receiver["maxDepoint"]
                    device_temp.bUtil = transmitter["bUtil"]
                    device_temp.backoff = transmitter["backoff"]
                    device_temp.contour = transmitter["contour"]
                    device_temp.fec = transmitter["fec"]
                    device_temp.freq = transmitter["freq"]
                    device_temp.otherTrGainLoss = transmitter["otherTrGainLoss"]
                    device_temp.polarizationMode = transmitter["polarizationMode"]
                    device_temp.radiationModel = transmitter["radiationModel"]
                    device_temp.rolloff = transmitter["rolloff"]
                device_list.append(device_temp)
                internalIdMax += 1
        models.Device.objects.bulk_create(device_list)
        models.Experiment.objects.filter(id=experimentId).update(internalIdMax=internalIdMax)
    result = {
        "errorCode": 200,
        "data": {
            "internalIdMax": internalIdMax,
        }
    }
    return JsonResponse(result, safe=False)


# 分区
@api_view(['POST'])
def modifyGroundRegionAndTerminal(request):
    body = json.loads(request.body.decode('utf-8'))
    regionInfo = body['regionInfo']
    # d1 = timezone.now()
    # d2=timezone.localtime(d1)
    # d3=d2.strftime("%Y-%m-%d %H:%M:%S")
    # print(d3)

    terminals = regionInfo["terminals"],
    models.GroundRegion.objects.create(
        regionId=regionInfo["id"],
        experimentId=body["experimentId"],
        regionInfoList=body["regionInfo"],
        internalIdMax=body["internalIdMax"],
        lastModTime=timezone.now().strftime("%Y-%m-%d %H:%M:%S")  # 时间输出有问题
    )

    for facility in terminals:
        for terminals in facility:
            position = terminals["position"]
            models.Facility.objects.create(
                id=terminals["id"],
                showName=terminals["showName"],
                nodeType=terminals["nodeType"],
                latitude=position["latitude"],
                longitude=position["longitude"],
                altitude=position["altitude"],
                experimentId=body["experimentId"],
                constellationGroupId=terminals["constellationGroupId"],
                grade=terminals["grade"],
                bwReq=terminals["bwReq"],
                regionId=regionInfo["id"],
            )
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


def deleteGroundRegionAndTerminal(request):
    body = json.loads(request.body.decode('utf-8'))
    regionIdList = body["regionIdList"]
    for id in regionIdList:
        models.GroundRegion.objects.filter(regionId=id).delete()
        models.Facility.objects.filter(regionId=id).delete()
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


# 信关站\终端站
def modifyNode(request):
    body = json.loads(request.body.decode('utf-8'))
    data = body["data"]
    internalIdMax = body["internalIdMax"]
    experimentId = body["experimentId"]
    if data["nodeType"] == 1:
        models.Satellite.objects.create(
            id=data["id"],
            showName=data["showName"],
            nodeType=data["nodeType"],
            attitudeSeg=data["attitudeSeg"],
            constraintOffset=data["constraintOffset"],
            isMainSatellite=data["isMainSatellite"],
            constellationId=0,
            deviceNumberLimit=data["deviceNumberLimit"],
            experimentId=experimentId,
            constellationGroupId=data["parentId"],
            tle1=data["tle1"],
            tle2=data["tle2"]
        )
    elif data["nodeType"] == 2:
        # 后续开发
        print("小船")
    else:
        position = data["position"]
        models.Facility.objects.create(
            id=data["id"],
            showName=data["showName"],
            nodeType=data["nodeType"],
            latitude=position["latitude"],
            longitude=position["longitude"],
            altitude=position["altitude"],
            experimentId=body["experimentId"],
            attitudeSeg=data["attitudeSeg"],
            # deviceId=data["id"],
            accessConstellationList=data["accessConstellationList"],
            constellationGroupId=data["parentId"],
            grade=data["grade"],
            bwReq=data["bwReq"],
        )
    models.Experiment.objects.filter(id=experimentId).update(internalIdMax=internalIdMax)
    result = {
        "errorCode": 200
    }

    return JsonResponse(result, safe=False)


def deleteNodeList(request):
    body = json.loads(request.body.decode('utf-8'))
    nodeIdAndTypes = body["nodeIdAndTypes"]
    # experimentId=body["experimentId"]
    # print(body["nodeIdAndTypes"])
    for nodeIdList1 in nodeIdAndTypes:
        for key in nodeIdList1:
            datakey = 'nodeIds'
            if key == datakey:
                value = nodeIdList1[key]
                for id in value:
                    models.Facility.objects.filter(id=id).delete()
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


def login(request):
    result = {
        "errorCode": 200,
        "userId": "测试",
        "authToken": 1
    }
    return JsonResponse(result, safe=False)


@api_view(['GET'])
def getExperimentList(request):
    result = {
        "errorCode": 200,
        "userId": "测试",
        "authToken": 1
    }
    return JsonResponse(result, safe=False)


@api_view(['POST'])
def modifyDevicePattern(request):
    body = json.loads(request.body.decode('utf-8'))
    device_pattern_id = body["devicePattern"]["devicePatternId"]
    device_pattern_name = body["devicePattern"]["devicePatternName"]
    experiment_id = body["experimentId"]
    device = body["devicePattern"]["devices"][0]
    # deviceEquipConfig
    device_name = device["deviceName"]
    device_type = device["deviceType"]
    id = device["id"]  # 什么id
    azimuth = device["deviceEquipConfig"]["azimuth"]
    elevation = device["deviceEquipConfig"]["elevation"]
    max_azimuth = device["deviceEquipConfig"]["maxAzimuth"]
    max_elevation = device["deviceEquipConfig"]["maxElevation"]
    max_range = device["deviceEquipConfig"]["maxRange"]
    min_azimuth = device["deviceEquipConfig"]["minAzimuth"]
    min_elevation = device["deviceEquipConfig"]["minElevation"]
    pointing_type = device["deviceEquipConfig"]["pointingType"]
    print(pointing_type)
    # linkconfig
    band_width = device["linkConfig"]["bandWidth"]
    communication = device["linkConfig"]["communication"]
    communication_speed = device["linkConfig"]["communicationSpeed"]
    modulation_mode = device["linkConfig"]["modulationMode"]
    wave_length = device["linkConfig"]["waveLength"]
    print(wave_length)
    # receiver
    antenna_re_gain = device["receiver"]["antennaReGain"]
    apt_loss = device["receiver"]["aptLoss"]
    f_noise_temperature = device["receiver"]["fNoiseTemperature"]
    other_re_gain_loss = device["receiver"]["otherReGainLoss"]
    re_efficiency = device["receiver"]["reEfficiency"]
    receive_threshold = device["receiver"]["receiveThreshold"]
    tracking_error = device["receiver"]["trackingError"]
    print(f_noise_temperature)  # ceshi
    # transmitter
    beam_distribution = device["transmitter"]["beamDistribution"]
    diameter = device["transmitter"]["diameter"]
    diffraction_limit = device["transmitter"]["diffractionLimit"]
    divergence_angle = device["transmitter"]["divergenceAngle"]
    other_tr_gain_loss = device["transmitter"]["otherTrGainLoss"]
    tr_efficiency = device["transmitter"]["trEfficiency"]
    tr_power = device["transmitter"]["trPower"]
    print(diameter)  # ceshi
    internalIdMax = body["internalIdMax"]
    models.Device.objects.filter(id=id).delete()
    models.DevicePattern.objects.filter(id=device_pattern_id).delete()
    models.Device.objects.create(devicePatternId=device_pattern_id,
                                 experimentId=experiment_id,
                                 deviceName=device_name,
                                 deviceType=device_type,
                                 id=id,
                                 azimuth=azimuth,
                                 elevation=elevation,
                                 maxAzimuth=max_azimuth,
                                 maxElevation=max_elevation,
                                 maxRange=max_range,
                                 minAzimuth=min_azimuth,
                                 minElevation=min_elevation,
                                 pointingType=pointing_type,

                                 bandWidth=band_width,
                                 communication=communication,
                                 communicationSpeed=communication_speed,
                                 modulationMode=modulation_mode,
                                 waveLength=wave_length,

                                 antennaReGain=antenna_re_gain,
                                 aptLoss=apt_loss,
                                 fNoiseTemperature=f_noise_temperature,
                                 otherReGainLoss=other_re_gain_loss,
                                 reEfficiency=re_efficiency,
                                 receiveThreshold=receive_threshold,
                                 trackingError=tracking_error,

                                 beamDistribution=beam_distribution,
                                 diameter=diameter,
                                 diffractionLimit=diffraction_limit,
                                 divergenceAngle=divergence_angle,
                                 otherTrGainLoss=other_tr_gain_loss,
                                 trEfficiency=tr_efficiency,
                                 trPower=tr_power,
                                 )
    models.DevicePattern.objects.create(id=device_pattern_id,
                                        devicePatternName=device_pattern_name,
                                        experimentId=experiment_id,
                                        # create_time="2023-01-25 10:44:50",
                                        # update_time = "2023-01-25 10:44:50"
                                        )
    models.Experiment.objects.filter(id=experiment_id).update(internalIdMax=internalIdMax)
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


@api_view(['POST'])
def deleteDevicePattern(request):
    body = json.loads(request.body.decode('utf-8'))
    device_pattern_id = body["devicePatternIds"][0]
    experiment_id = body["experimentId"]
    # internalIdMax = body["internalIdMax"]
    models.Device.objects.filter(id=device_pattern_id).delete()
    models.DevicePattern.objects.filter(id=device_pattern_id).delete()
    # models.Experiment.objects.filter(id=experiment_id).update(internalIdMax=internalIdMax)
    result = {
        "errorCode": 200
    }
    return JsonResponse(result, safe=False)


@api_view(['GET'])
def getDevicePattern(request, experiment_id):
    id = request.GET.get('experiment_id')
    device_pattern = models.DevicePattern.objects.filter(experimentId=experiment_id)
    result = json.loads(serializers.serialize("json", device_pattern))
    device_pattern_list = []
    for res in result:
        device_pattern_temp = res["fields"]
        device_pattern_temp["devicePatternId"] = res["pk"]
        device_pattern_temp["devices"] = getDeviceByNodeId(res["pk"], 2)
        device_pattern_list.append(device_pattern_temp)
    dict = {
        "errorCode": 200,
        "data": {
            "devicePatterns": device_pattern_list
        }
    }
    # 这里出问题了，只打印了循环的最后一个，应该是把那个循环的所有结果保存在一个列表中，，放到list中了，但是不知道为啥还报错了
    # 列表里是所有实验id对应的设备模板，但前端还会执行说获取列表模板失败，那个语句是什么意思？数据格式不对？
    return JsonResponse(dict, safe=False)
