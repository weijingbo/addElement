# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework import serializers


class Area(models.Model):
    experiment_id = models.IntegerField()
    constellation_id = models.BigIntegerField()
    area_num = models.IntegerField()
    is_covered = models.IntegerField()
    area_height = models.IntegerField(blank=True, null=True)
    area_width = models.IntegerField(blank=True, null=True)
    netmask = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class CalcExperimentTopology(models.Model):
    experiment_id = models.IntegerField(primary_key=True)
    constellation_group_id = models.BigIntegerField()
    cur_time = models.BigIntegerField()
    top_type = models.IntegerField()
    topology = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_experiment_topology'
        unique_together = (('experiment_id', 'constellation_group_id', 'cur_time', 'top_type'),)


class CalcPointPosition(models.Model):
    point_key = models.IntegerField()
    experiment_id = models.IntegerField(primary_key=True)
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_point_position'
        unique_together = (('experiment_id', 'point_key'),)


class CalcSatellitePosition(models.Model):
    satellite_id = models.BigIntegerField(primary_key=True)
    experiment_id = models.IntegerField()
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    velocity = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_satellite_position'


class CalcSatelliteVisibility(models.Model):
    satellite_id = models.BigIntegerField(primary_key=True)
    node_key = models.BigIntegerField()
    node_type = models.IntegerField()
    experiment_id = models.IntegerField()
    constellation_group_id = models.BigIntegerField()
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    visibility = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calc_satellite_visibility'
        unique_together = (('satellite_id', 'node_key', 'node_type'),)


class ClientDeployment(models.Model):
    user_id = models.IntegerField()
    file_id = models.IntegerField()
    file_name = models.CharField(max_length=255)
    deploy_time = models.DateTimeField()
    hosts = models.TextField()
    log_file_name = models.CharField(max_length=255)
    experiment_id = models.IntegerField()
    is_running = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_deployment'


class ClientFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    file_name = models.CharField(max_length=255)
    upload_time = models.DateTimeField()
    size = models.IntegerField()
    deleted = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_file'


class CollectRecord(models.Model):
    collect_id = models.IntegerField()
    collect_time = models.DateTimeField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    attenuation = models.FloatField(blank=True, null=True)
    setup_time = models.BigIntegerField(blank=True, null=True)
    err = models.FloatField(blank=True, null=True)
    finished = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collect_record'


class Config(models.Model):
    experiment_id = models.IntegerField()
    entity_one_type = models.IntegerField()
    entity_one_id = models.BigIntegerField()
    entity_one_parent_id = models.BigIntegerField()
    entity_two_type = models.IntegerField()
    entity_two_id = models.BigIntegerField()
    entity_two_parent_id = models.BigIntegerField(blank=True, null=True)
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class Constellation(models.Model):
    id = models.BigIntegerField(db_column="id", primary_key=True)
    showName = models.CharField(db_column="name", max_length=100)
    nodeType = models.IntegerField(db_column="node_type")
    numberOfPlanes = models.IntegerField(db_column="orbit_count")
    numberOfSatsPerPlane = models.IntegerField(db_column="satellite_count")
    trueAnomalyInterval = models.FloatField(db_column="true_anomaly_interval")
    raanSpread = models.FloatField(db_column="raan_interval")
    _perigeeAltitude = models.FloatField(db_column="perigee_altitude", blank=True, null=True)
    _apogeeAltitude = models.FloatField(db_column="apogee_altitude", blank=True, null=True)
    inclination = models.FloatField(blank=True, null=True)
    raan = models.FloatField(blank=True, null=True)
    argOfPerigee = models.FloatField(db_column="argument_of_perigee", blank=True, null=True)
    trueAnomaly = models.FloatField(db_column="true_anomaly", blank=True, null=True)
    tle1 = models.CharField(max_length=100, blank=True, null=True)
    tle2 = models.CharField(max_length=100, blank=True, null=True)
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)
    experimentId = models.IntegerField(db_column="experiment_id")
    maxPlane = models.IntegerField(db_column="max_plane", blank=True, null=True)
    firstRow = models.CharField(db_column="first_row", max_length=2000, blank=True, null=True)
    zoningStatus = models.IntegerField(db_column="zoning_status")
    linkSwitchLatitude = models.FloatField(db_column="link_switch_latitude", blank=True, null=True)
    areaWidthNum = models.IntegerField(db_column="area_width_num", blank=True, null=True)
    areaHeightNum = models.IntegerField(db_column="area_height_num", blank=True, null=True)
    areaOffset = models.IntegerField(db_column="area_offset", blank=True, null=True)
    t1 = models.BigIntegerField(blank=True, null=True)
    t2 = models.FloatField(blank=True, null=True)
    t3 = models.FloatField(blank=True, null=True)
    t7 = models.FloatField(blank=True, null=True)
    satipDigit = models.IntegerField(db_column="satip_digit", blank=True, null=True)
    consIp = models.CharField(db_column="cons_ip", max_length=255, blank=True, null=True)
    consDigit = models.IntegerField(db_column="cons_digit", blank=True, null=True)
    constellationGroupId = models.BigIntegerField(db_column="constellation_group_id")
    constellationType = models.CharField(db_column="constellation_type", max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'constellation'


class ConstellationGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    experimentId = models.IntegerField(db_column="experiment_id")
    showName = models.CharField(db_column="name", max_length=200)
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)
    isHighOrbitConstellationGroup = models.IntegerField(db_column="is_high_orbit_constellation_group", blank=True,
                                                        null=True)

    class Meta:
        managed = False
        db_table = 'constellation_group'


class Coverage(models.Model):
    experiment_id = models.IntegerField()
    coverage_data_list = models.JSONField(blank=True, null=True)
    grid_accuracy = models.IntegerField(blank=True, null=True)
    internal_id_max = models.BigIntegerField(blank=True, null=True)
    last_mod_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coverage'


class Device(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nodeId = models.BigIntegerField(db_column="node_id", blank=True, null=True)
    deviceName = models.CharField(db_column="name", max_length=100)
    devicePatternId = models.BigIntegerField(db_column="device_pattern_id")
    experimentId = models.IntegerField(db_column="experiment_id", blank=True, null=True)
    deviceType = models.IntegerField(db_column="type")
    deviceNumber = models.IntegerField(db_column="device_number", blank=True, null=True)
    areaDevice = models.IntegerField(db_column="area_device", blank=True, null=True)
    deviceIp = models.CharField(db_column="device_ip", max_length=255, blank=True, null=True)
    netmask = models.CharField(max_length=255, blank=True, null=True)
    routeId = models.BigIntegerField(db_column="route_id", blank=True, null=True)
    areaNum = models.IntegerField(db_column="area_num", blank=True, null=True)
    constellationId = models.BigIntegerField(db_column="constellation_id", blank=True, null=True)
    antennaType = models.IntegerField(db_column="antenna_type", blank=True, null=True)
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)
    pointingType = models.IntegerField(db_column="pointing_type", blank=True, null=True)
    azimuth = models.FloatField(blank=True, null=True)
    beamFov = models.FloatField(db_column="beam_fov", blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    minAzimuth = models.FloatField(db_column="min_azimuth", blank=True, null=True)
    maxAzimuth = models.FloatField(db_column="max_azimuth", blank=True, null=True)
    minElevation = models.FloatField(db_column="min_elevation", blank=True, null=True)
    maxElevation = models.FloatField(db_column="max_elevation", blank=True, null=True)
    maxRange = models.FloatField(db_column="max_range", blank=True, null=True)
    ubeamNum = models.IntegerField(db_column="ubeam_num", blank=True, null=True)
    halfAngleMinorAxis = models.FloatField(db_column="half_angle_minor_axis", blank=True, null=True)
    halfAngleMajorAxis = models.FloatField(db_column="half_angle_major_axis", blank=True, null=True)
    waveLength = models.FloatField(db_column="wave_length", blank=True, null=True)
    bandWidth = models.FloatField(db_column="band_width", blank=True, null=True)
    modulationMode = models.IntegerField(db_column="modulation_mode", blank=True, null=True)
    communication = models.IntegerField(blank=True, null=True)
    communicationSpeed = models.FloatField(db_column="communication_speed", blank=True, null=True)
    trPower = models.FloatField(db_column="tr_power", blank=True, null=True)
    diameter = models.FloatField(blank=True, null=True)
    trEfficiency = models.FloatField(db_column="tr_efficiency", blank=True, null=True)
    antennaTrGain = models.FloatField(db_column="antenna_tr_gain", blank=True, null=True)
    divergenceAngle = models.FloatField(db_column="divergence_angle", blank=True, null=True)
    otherTrGainLoss = models.FloatField(db_column="other_tr_gain_loss", blank=True, null=True)
    beamDistribution = models.IntegerField(db_column="beam_distribution", blank=True, null=True)
    polarizationMode = models.IntegerField(db_column="polarization_mode", blank=True, null=True)
    diffractionLimit = models.FloatField(db_column="diffraction_limit", blank=True, null=True)
    freq = models.FloatField(blank=True, null=True)
    backoff = models.FloatField(blank=True, null=True)
    contour = models.FloatField(blank=True, null=True)
    rolloff = models.FloatField(blank=True, null=True)
    bUtil = models.FloatField(db_column="b_util", blank=True, null=True)
    fec = models.IntegerField(blank=True, null=True)
    radiationModel = models.IntegerField(db_column="radiation_model", blank=True, null=True)
    reEfficiency = models.FloatField(db_column="re_efficiency", blank=True, null=True)
    antennaReGain = models.FloatField(db_column="antenna_re_gain", blank=True, null=True)
    otherReGainLoss = models.FloatField(db_column="other_re_gain_loss", blank=True, null=True)
    fNoiseTemperature = models.FloatField(db_column="f_noise_temperature", blank=True, null=True)
    receiveThreshold = models.FloatField(db_column="receive_threshold", blank=True, null=True)
    aptLoss = models.FloatField(db_column="apt_loss", blank=True, null=True)
    trackingError = models.IntegerField(db_column="tracking_error", blank=True, null=True)
    lnbGain = models.FloatField(db_column="lnb_gain", blank=True, null=True)
    maxDepoint = models.FloatField(db_column="max_depoint", blank=True, null=True)
    locationX = models.FloatField(db_column="locationx", blank=True, null=True)
    locationY = models.FloatField(db_column="locationy", blank=True, null=True)
    locationZ = models.FloatField(db_column="locationz", blank=True, null=True)
    dbeamNum = models.IntegerField(db_column="dbeam_num", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'


class DevicePattern(models.Model):
    id = models.BigIntegerField(primary_key=True)
    device_pattern_name = models.CharField(max_length=100)
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=100, blank=True, null=True)
    experiment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'device_pattern'


class Experiment(models.Model):
    startTimeStampMs = models.BigIntegerField(db_column="start_time")
    calculateStatus = models.IntegerField(db_column="calculate_status")
    groupId = models.IntegerField(db_column="group_id")
    start = models.IntegerField()
    h3Cr = models.IntegerField(db_column="h3_cr")
    internalIdMax = models.BigIntegerField(db_column="internal_id_max")
    endTimeStampMs = models.BigIntegerField(db_column="end_time")
    modified = models.IntegerField()
    createTimeStampMs = models.DateTimeField(db_column="create_time")
    step = models.IntegerField()
    experimentName = models.CharField(db_column="name", max_length=50)
    info = models.CharField(max_length=2000, blank=True, null=True)
    propLossType = models.CharField(db_column="prop_loss_type", max_length=200)
    topCalcType = models.IntegerField(db_column="top_calc_type")

    # open_time = models.BigIntegerField(blank=True, null=True)
    # top_sharding = models.IntegerField()
    # top_task_num = models.IntegerField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment'


class ExperimentStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    experiment_id = models.IntegerField()
    type = models.IntegerField()
    calculate_status = models.IntegerField()
    config_id = models.BigIntegerField(blank=True, null=True)
    config_status = models.IntegerField()
    running_status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment_status'


class Facility(models.Model):
    id = models.BigIntegerField(primary_key=True)
    showName = models.CharField(db_column="name", max_length=50)
    nodeType = models.IntegerField(db_column="node_type", blank=True, null=True)
    latitude = models.FloatField(db_column="prime_latitude")
    longitude = models.FloatField(db_column="prime_longitude")
    altitude = models.FloatField(db_column="prime_altitude")
    startTimeStampMs = models.BigIntegerField(db_column="start_time", blank=True, null=True)
    endTimeStampMs = models.BigIntegerField(db_column="end_time", blank=True, null=True)
    experimentId = models.IntegerField(db_column="experiment_id", blank=True, null=True)
    regionId = models.BigIntegerField(db_column="region_id", blank=True, null=True)
    nearStationId = models.BigIntegerField(db_column="near_station_id", blank=True, null=True)
    attitudeSeg = models.IntegerField(db_column="attitude_seg", blank=True, null=True)
    constraintOffset = models.FloatField(db_column="constraint_offset", blank=True, null=True)
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)
    routeId = models.BigIntegerField(db_column="route_id", blank=True, null=True)
    antennaNum = models.IntegerField(db_column="antenna_num", blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    accessConstellationList = models.TextField(db_column="access_constellation_list", blank=True, null=True)
    constellationGroupId = models.BigIntegerField(db_column="constellation_group_id")
    grade = models.CharField(max_length=200, blank=True, null=True)
    bwReq = models.IntegerField(db_column="bw_req", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility'


class GroundRegion(models.Model):
    regionId = models.BigIntegerField(db_column="region_id")
    experimentId = models.IntegerField(db_column="experiment_id")
    regionInfoList = models.JSONField(blank=True, null=True,db_column="region_info_list")
    internalIdMax = models.BigIntegerField(blank=True, null=True,db_column="internal_id_max")
    lastModTime = models.CharField(max_length=100, blank=True, null=True,db_column="last_mod_time")

    class Meta:
        managed = False
        db_table = 'ground_region'


class Position(models.Model):
    facility_id = models.BigIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    speed = models.FloatField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class RegionPairConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    experiment_id = models.IntegerField()
    region_first = models.BigIntegerField()
    region_second = models.BigIntegerField()
    terminal_pair_num = models.IntegerField()
    proto_type = models.IntegerField()
    intervals = models.IntegerField()
    package_size = models.IntegerField()
    show_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'region_pair_config'


class RouteDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    experiment_id = models.IntegerField()
    region_first = models.BigIntegerField(blank=True, null=True)
    region_second = models.BigIntegerField(blank=True, null=True)
    proto_type = models.IntegerField()
    intervals = models.IntegerField()
    package_size = models.IntegerField()
    source_node_id = models.BigIntegerField()
    source_node_name = models.CharField(max_length=50, blank=True, null=True)
    target_node_id = models.BigIntegerField()
    target_node_name = models.CharField(max_length=50, blank=True, null=True)
    target_node_route_id = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    color = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField()
    selected = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'route_detail'


class Satellite(models.Model):
    id = models.BigIntegerField(db_column="id", primary_key=True)
    showName = models.CharField(db_column="name", max_length=100)
    nodeType = models.IntegerField(db_column="node_type")
    _apogeeAltitude = models.FloatField(db_column="apogee_altitude", blank=True, null=True)
    _perigeeAltitude = models.FloatField(db_column="perigee_altitude", blank=True, null=True)
    inclination = models.FloatField(blank=True, null=True)
    argOfPerigee = models.FloatField(db_column="argument_of_perigee", blank=True, null=True)
    raan = models.FloatField(blank=True, null=True)
    trueAnomaly = models.FloatField(db_column="true_anomaly", blank=True, null=True)
    attitudeSeg = models.IntegerField(db_column="attitude_seg")
    constraintOffset = models.FloatField(db_column="constraint_offset")
    isMainSatellite = models.IntegerField(db_column="is_main_satellite")
    constellationId = models.BigIntegerField(db_column="constellation_id")
    planeIndex = models.IntegerField(db_column="plane_index", blank=True, null=True)
    interPlaneIndex = models.IntegerField(db_column="inter_plane_index", blank=True, null=True)
    deviceNumberLimit = models.IntegerField(db_column="device_number_limit")
    experimentId = models.IntegerField(db_column="experiment_id")
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)
    areaNum = models.IntegerField(db_column="area_num", blank=True, null=True)
    deviceId = models.CharField(db_column="device_id", max_length=255, blank=True, null=True)
    routeId = models.BigIntegerField(db_column="route_id", blank=True, null=True)
    constellationGroupId = models.BigIntegerField(db_column="constellation_group_id")
    tle1 = models.CharField(max_length=200, blank=True, null=True)
    tle2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'satellite'


class SceneConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    experiment_id = models.IntegerField(blank=True, null=True)
    primary_cons_paras = models.TextField(blank=True, null=True)
    primary_gateways = models.TextField(blank=True, null=True)
    primary_terminals = models.TextField(blank=True, null=True)
    secondary_cons_paras = models.TextField(blank=True, null=True)
    secondary_gateways = models.TextField(blank=True, null=True)
    secondary_terminals = models.TextField(blank=True, null=True)
    geo_satellite = models.TextField(blank=True, null=True)
    geo_gateways = models.TextField(blank=True, null=True)
    geo_terminals = models.TextField(blank=True, null=True)
    debris_set_name = models.CharField(max_length=255, blank=True, null=True)
    protected_set_name = models.TextField(blank=True, null=True)
    interference_type = models.IntegerField(blank=True, null=True)
    prop_loss_type = models.TextField(blank=True, null=True)
    track_strategy = models.IntegerField(blank=True, null=True)
    min_elevation = models.FloatField(blank=True, null=True)
    traffic_type = models.IntegerField(blank=True, null=True)
    resource_plan_algo = models.IntegerField(blank=True, null=True)
    geo_leo_protect_angle = models.FloatField(blank=True, null=True)
    sim_type = models.IntegerField(blank=True, null=True)
    sim_start = models.DateTimeField(blank=True, null=True)
    sim_end = models.DateTimeField(blank=True, null=True)
    sim_step = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scene_config'


class Sensor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    node_id = models.BigIntegerField()
    experiment_id = models.IntegerField()
    name = models.CharField(max_length=20)
    type = models.IntegerField()
    max_range = models.FloatField()
    half_angle = models.FloatField(blank=True, null=True)
    inner_half_angle = models.FloatField(blank=True, null=True)
    outer_half_angle = models.FloatField(blank=True, null=True)
    min_clock_angle = models.FloatField(blank=True, null=True)
    max_clock_angle = models.FloatField(blank=True, null=True)
    hori_half_angle = models.FloatField(blank=True, null=True)
    ver_half_angle = models.FloatField(blank=True, null=True)
    locationx = models.FloatField(blank=True, null=True)
    locationy = models.FloatField(blank=True, null=True)
    locationz = models.FloatField(blank=True, null=True)
    pointing_type = models.IntegerField()
    azimuth = models.FloatField()
    elevation = models.FloatField()
    boresight_type = models.IntegerField()
    min_azimuth = models.FloatField(blank=True, null=True)
    max_azimuth = models.FloatField(blank=True, null=True)
    min_elevation = models.FloatField(blank=True, null=True)
    max_elevation = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=30)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    remark = models.CharField(max_length=200, blank=True, null=True)
    sensor_target_list = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor'


class SpectrumConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    experimentId = models.IntegerField(db_column="experiment_id")
    constellationId = models.BigIntegerField(db_column="constellation_id")
    uubChBw = models.FloatField(db_column="uub_ch_bw", blank=True, null=True)
    uubChNum = models.IntegerField(db_column="uub_ch_num", blank=True, null=True)
    uubBwTot = models.FloatField(db_column="uub_bw_tot", blank=True, null=True)
    uubChCarries = models.TextField(db_column="uub_ch_carries", blank=True, null=True)
    uubChK = models.IntegerField(db_column="uub_ch_k", blank=True, null=True)
    uubChPolar = models.TextField(db_column="uub_ch_polar", blank=True, null=True)
    uubModcod = models.TextField(db_column="uub_mod_cod", blank=True, null=True)
    uubRolloff = models.FloatField(db_column="uub_roll_off", blank=True, null=True)
    udbChBw = models.FloatField(db_column="udb_ch_bw", blank=True, null=True)
    udbChNum = models.IntegerField(db_column="udb_ch_num", blank=True, null=True)
    udbBwTot = models.FloatField(db_column="udb_bw_tot", blank=True, null=True)
    udbChCarries = models.TextField(db_column="udb_ch_carries", blank=True, null=True)
    udbChK = models.IntegerField(db_column="udb_ch_k", blank=True, null=True)
    udbChPolar = models.TextField(db_column="udb_ch_polar", blank=True, null=True)
    udbModcod = models.TextField(db_column="udb_mod_cod", blank=True, null=True)
    udbRolloff = models.FloatField(db_column="udb_roll_off", blank=True, null=True)
    fubChBw = models.FloatField(db_column="fub_ch_bw", blank=True, null=True)
    fubChNum = models.IntegerField(db_column="fub_ch_num", blank=True, null=True)
    fubBwTot = models.FloatField(db_column="fub_bw_tot", blank=True, null=True)
    fubChCarries = models.TextField(db_column="fub_ch_carries", blank=True, null=True)
    fubChK = models.IntegerField(db_column="fub_ch_k", blank=True, null=True)
    fubChPolar = models.TextField(db_column="fub_ch_polar", blank=True, null=True)
    fubModcod = models.TextField(db_column="fub_mod_cod", blank=True, null=True)
    fubRolloff = models.FloatField(db_column="fub_roll_off", blank=True, null=True)
    fdbChBw = models.FloatField(db_column="fdb_ch_bw", blank=True, null=True)
    fdbChNum = models.IntegerField(db_column="fdb_ch_num", blank=True, null=True)
    fdbBwTot = models.FloatField(db_column="fdb_bw_tot", blank=True, null=True)
    fdbChCarries = models.TextField(db_column="fdb_ch_carries", blank=True, null=True)
    fdbChK = models.IntegerField(db_column="fdb_ch_k", blank=True, null=True)
    fdbChPolar = models.TextField(db_column="fdb_ch_polar", blank=True, null=True)
    fdbModcod = models.TextField(db_column="fdb_mod_cod", blank=True, null=True)
    fdbRolloff = models.FloatField(db_column="fdb_roll_off", blank=True, null=True)
    # create_time = models.DateTimeField(blank=True, null=True)
    # update_time = models.DateTimeField(blank=True, null=True)
    # remark = models.CharField(max_length=255, blank=True, null=True)
    uubFec = models.TextField(db_column="uub_fec", blank=True, null=True)
    udbFec = models.TextField(db_column="udb_fec", blank=True, null=True)
    fubFec = models.TextField(db_column="fub_fec", blank=True, null=True)
    fdbFec = models.TextField(db_column="fdb_fec", blank=True, null=True)
    uubFrequencyPoint = models.IntegerField(db_column="uub_frequency_point", )
    udbFrequencyPoint = models.IntegerField(db_column="udb_frequency_point", )
    fubFrequencyPoint = models.IntegerField(db_column="fub_frequency_point", )
    fdbFrequencyPoint = models.IntegerField(db_column="fdb_frequency_point", )

    class Meta:
        managed = False
        db_table = 'spectrum_config'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    loginTime = models.DateTimeField(db_column="login_time",blank=True, null=True)
    loginIp = models.CharField(db_column="login_ip",max_length=15, blank=True, null=True)
    status = models.IntegerField()
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroup(models.Model):
    name = models.CharField(max_length=50)
    userId = models.IntegerField(db_column="user_id")
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
    # remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'
